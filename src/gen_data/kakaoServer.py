import requests
import json
import fileloader as fl
from dotenv import load_dotenv
import os
from datetime import datetime

class KakaoMng():
    def __init__(self):
        f = fl.FileLoader()
        load_dotenv()

        self.me_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        self.friend_url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
        self.token = os.environ.get('KAKAO_TOKEN')
        self.text = f.load_json('../data/dataset.json')
        self.header = {"Authorization": 'Bearer ' + self.token}
        self.friend_cnt = 0
        self.friend_list = self.load_friend()

    def multi_send(self, cnt):
        self.send_multi_greeting(self)
        for i in range(1,cnt+1):
            print(f'[{i}] send msg to KaKaoTalk')
            self.send_me(i)
            self.send_friend(i)

    def send_me(self, i):
        data = {
            "template_object": json.dumps({
                "object_type":"text",
                "text": self.gen_text(i),
                "link":{
                    "web_url": self.text[0]["origin"]["url"],
                    "mobile_web_url": self.text[0]["origin"]["url"]
                },
                "button_title": "기사 확인"
            })
        }
        response = requests.post(self.me_url,data=data,headers=self.header)

    def send_friend(self, i):
        data={
            'receiver_uuids': json.dumps(self.split_uuid(self.friend_list)),
            "template_object": json.dumps({
                "object_type":"text",
                "text": self.gen_text(i),
                "link":{
                    "web_url": self.text[0]["origin"]["url"],
                    "mobile_web_url": self.text[0]["origin"]["url"]
                },
                "button_title": "기사 확인"
            })
        }
        response = requests.post(self.friend_url,data=data,headers=self.header)

    def load_friend(self):
        result = []
        url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
        res = json.loads(requests.get(url, headers=self.header).text)
        self.friend_cnt = int(res['total_count'])
        for i in range(res['total_count']):
            uuid = res['elements'][i]['uuid']
            name = res['elements'][i]['profile_nickname']
            result.append({"uuid": uuid, "name": name})
        return result

    def split_uuid(self, friend_data):
        result = []
        for data in friend_data:
            result.append(data['uuid'])
        return result
    
    def gen_text(self, i):
        return f"""제목: {self.text[i]["gpt"]["gpt_title"]}\n\
날짜: {self.text[i]["origin"]["date"]}\n\
주제: {self.text[i]["gpt"]["gpt_section"]}\n\
{self.split_abstarct(self.text[i]["gpt"]["gpt_abstract"])}"""

    def split_abstarct(self, text):
        text = text[:text.find("2.")-1] + "\n" + text[text.find("2."):text.find("3.")-1] + '\n' + text[text.find("3."):]
        return text

    def send_greeting_text(self, i):
        now = datetime.now()
        formatted_time = now.strftime("%Y년 %m월 %d일 %H시")

        data={
            'receiver_uuids': json.dumps([self.friend_list[i]["uuid"]]),
            "template_object": json.dumps({
                "object_type":"text",
                "text": f"좋은 하루에요 {self.friend_list[i]["name"]}님!\n {formatted_time} 주요 뉴스 알려드리겠습니다!",
                "link":{
                    "web_url": "https://finance.naver.com/news/mainnews.naver",
                    "mobile_web_url": "https://finance.naver.com/news/mainnews.naver"
                },
                "button_title": "주요 기사 확인"
            })
        }
        response = requests.post(self.friend_url,data=data,headers=self.header)
        print(response)
        return 

    def send_multi_greeting(self):
        for i in range(self.friend_cnt):
            self.send_greeting_text(i)