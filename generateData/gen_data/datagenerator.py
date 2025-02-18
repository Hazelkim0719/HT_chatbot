import os
import time
import json

from dotenv import load_dotenv
from .crawl import Crawler
from .chatgpt import GPTLoader
from .utils import Logging, FileLoader

class DataGenerator:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.environ.get('GPT_KEY')
        self.url = os.environ.get('NAVER_URL')
        self.gpt = GPTLoader(self.API_KEY)

        self.news = ""
        self.data_filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "dataset.json")
        
        self.crawler = Crawler(self.url, self.data_filename)
        self.file_loader = FileLoader()
        self.log = Logging()

    def load_news(self):
        """crwaler를 통해 naver 뉴스를 모두 가져오는 함수\n
        Args:
            None
        Returns:
            None
        """
        self.crawler.data_load()
        self.news = self.crawler.get_news()

    def load_gpt(self, cnt):
        """네이버 뉴스를 gpt에 입력하고 네이버 뉴스의 원본 데이터와 gpt 결과를 병합하여 반환하는 함수\n
        Args:
            cnt (int) : cnt <= 15, gpt에 입력할 데이터 개수
        Returns:
            data (dict) : 네이버 뉴스와 gpt 결과를 병합된 변수
        """
        data = []
        for i in range(cnt):
            if i < len(self.news):
                self.log.log(f"call gpt({i+1})..")
                result = {"origin" : self.news[i]}
                if i != 0 and i % 3 == 0:
                    self.log.log("Wait 80 seconds due to token limitation..")
                    time.sleep(80)
                result['gpt'] = self.gpt.run_gpt(self.news[i])
                data.append(result)
        return data

    def write_data(self, data):
        """data를 json파일로 저장하는 함수\n
        Args:
            data (dict) : load_gpt()에서 반환된 변수
        Returns:
            None
        """
        self.log.log("file save..")
        if os.path.isfile(self.data_filename):
            self.file_loader.append_json(self.data_filename, data)
        else:
            self.file_loader.write_json(self.data_filename, data)

    def rewrite_gpt_data(self):
        """str -> dict으로 변환 후 json파일로 저장하는 함수, gpt 결과를 write_data()한 후 다시 불러올 때 str로 인식할 경우 사용\n
        Args:
            data (dict) : load_gpt()에서 반환된 변수
        Returns:
            None
        """
        json_data = self.file_loader.load_json(self.data_filename)
        for i in range(len(json_data)):
            if type(json_data[i]['gpt']) is str:
                json_gpt = json.loads(json_data[i]['gpt'])
                json_data[i]['gpt'] = json_gpt

        self.file_loader.write_json(self.data_filename, json_data)