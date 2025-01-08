from dotenv import load_dotenv
import os
import time
from crawl import Crawler
from chatgpt import GPTLoader
class DataGenerator:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.environ.get('GPT_KEY')
        self.gpt = GPTLoader(self.API_KEY)

        self.url = os.environ.get('NAVER_URL')
        self.crawler = Crawler(self.url)
        self.news = self.crawler.get_news()

    def write_data(self):
        data = []
        for i in range(2):
            result = {"origin" : self.news[i]}
            if i != 0 and i % 3 == 0:
                time.sleep(70000)
            else:
                result['gpt'] = self.gpt.run_gpt(self.news[i])
            data.append(result)

        with open('./database.txt','w', encoding='utf-8') as f:
            f.write(str(data))