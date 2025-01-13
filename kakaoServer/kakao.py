import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from generateData.gen_data.utils import Logging, FileLoader
from dotenv import load_dotenv, set_key, find_dotenv
import requests
import json
from datetime import datetime


class KakaoLoginMng():
    def __init__(self):
        load_dotenv()
        self.dotenv_path = find_dotenv()
        self.rest_api_key = os.environ.get('KAKAO_API_KEY') 
        self.refresh_token = os.environ.get('KAKAO_REFRESH_TOKEN') 
        self.access_token = os.environ.get('KAKAO_ACCESS_TOKEN') 

        self.url = 'https://kauth.kakao.com/oauth/token'
        self.check_token_url = "https://kapi.kakao.com/v1/user/access_token_info"
        self.redirect_uri = 'https://example.com/oauth'

    def is_expire_access_token(self):
        """access token이 만료되었는지 함수\n
        Args:
            None
        Returns:
            is_expire (Bool) : 만료 되었으면 True, 아니면 False
        """
        header = {"Authorization": 'Bearer ' + self.access_token}
        res_code = requests.get(self.check_token_url, headers=header).status_code
        if res_code == 200:
            return False
        else:
            return True

    def load_tokens(self, code):
        """refresh token, access token 모두 발급 받는 함수\n
        Args:
            code (str) : 노션에 정리되어 있는 URL에서 카카오 로그인 후 리다이렉트 되는 URL의 code 부분
        Returns:
            tokens (dict) : 새로 발급 받은 토큰들
        """
        data = {
            'grant_type':'authorization_code',
            'client_id':self.rest_api_key,
            'redirect_uri':self.redirect_uri,
            'code': code
            }
        
        response = requests.post(self.url, data=data)
        
        tokens = response.json()
        print(tokens)
        """
        set_key(self.dotenv_path,'KAKAO_REFRESH_TOKEN',tokens["refresh_token"])
        set_key(self.dotenv_path,'KAKAO_ACCESS_TOKEN',tokens["access_token"])
        return {
            'access_token' : tokens["access_token"],
            'refresh_token' : tokens["refresh_token"]
            }
        """

    def load_access_token(self):
        """access token을 발급 받는 함수\n
        Args:
            None
        Returns:
            access_token (str) : 새로 발급된 access 토큰
        """
        data = {
            'grant_type':'refresh_token',
            'client_id':self.rest_api_key,
            'refresh_token': self.refresh_token
            }
        response = requests.post(self.url, data=data)
        
        tokens = response.json()
        set_key(self.dotenv_path,'KAKAO_ACCESS_TOKEN',tokens["access_token"])
        return tokens["access_token"]


class KakaoSendMng():
    def __init__(self):
        load_dotenv()
        self.f = FileLoader()
        self.log = Logging()
        self.klm = KakaoLoginMng()

        self.send_me_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        self.send_friend_url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
        self.load_friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
        self.token = os.environ.get('KAKAO_ACCESS_TOKEN')
        self.text = self.f.load_json('../generateData/data/dataset.json')
        self.header = {"Authorization": 'Bearer ' + self.token}
        self.friend_cnt = 0
        self.friend_list = self.load_friend()

    def multi_send(self, cnt):
        #self.send_multi_greeting()
        for i in range(1,cnt+1):
            self.send_msg(i,'me')
            #self.send_msg(i,'friend')

    def send_multi_greeting(self):
        self.send_greeting_text(0, 'me')
        
        for i in range(len(self.friend_list)):
            self.send_greeting_text(i, 'friend') 
        

    def send_msg(self, i, who):
        data = self.make_data(self.gen_text(-i), self.gen_link(self.text[-i]["origin"]["url"]), "기사 확인")

        if who == "friend":
            self.log.log(f"send to {who}s({i})")
            data['receiver_uuids'] = json.dumps(self.split_uuid(self.friend_list))
            response = requests.post(self.send_friend_url,data=data,headers=self.header)
        elif who == "me":
            self.log.log(f"send to {who}({i})")
            response = requests.post(self.send_me_url,data=data,headers=self.header)

    def send_greeting_text(self, i, who):
        formatted_time = datetime.now().strftime("%Y년 %m월 %d일 %H시")
        
        text = f"좋은 하루에요 {self.friend_list[i]["name"]}님!\n {formatted_time} 주요 뉴스 알려드리겠습니다!"
        link_url = "https://finance.naver.com/news/mainnews.naver"
        data = self.make_data(text, self.gen_link(link_url),"주요 기사 확인")

        if who == "friend":
            self.log.log(f"send greeting msg to {self.friend_list[i]["uuid"]}")
            data['receiver_uuids'] = json.dumps([self.friend_list[i]["uuid"]])
            response = requests.post(self.send_friend_url,data=data,headers=self.header)
        elif who == "me":
            self.log.log(f"send greeting msg to {who}")
            response = requests.post(self.send_me_url,data=data,headers=self.header)

    def load_friend(self): 
        try:
            result = []
            # 토큰 만료 시 토큰 발급 후 다시 요청
            if self.klm.is_expire_access_token():
                self.log.log("load access token")
                self.token = self.klm.load_access_token()
                self.header = {"Authorization": 'Bearer ' + self.token}

            res = json.loads(requests.get(self.load_friend_url, headers=self.header).text)
            for i in range(res['total_count']):
                uuid = res['elements'][i]['uuid']
                name = res['elements'][i]['profile_nickname']
                result.append({"uuid": uuid, "name": name})
            self.log.log("load friend list")
            return result
        except:
            self.log.log("force load friend list")
            self.friend_cnt = 2
            return [
                {'uuid': 'BT0ENAc-CT4SJhQjFSAQKQU0BT0IMQg6ew', 'name': '우리아빠'}, 
                {'uuid': 'BTQENw4_DjYALBgqEyoeLhwwATAIPQQ9D0Y', 'name': '우리엄마'}]

    def split_uuid(self, friend_data):
        result = []
        for data in friend_data:
            result.append(data['uuid'])
        return result

    def gen_link(self, url):
        return {
                "web_url": url,
                "mobile_web_url": url
        }

    def make_data(self, text, link, btn_title):
        return {
            "template_object": json.dumps({
                "object_type":"text",
                "text": text,
                "link": link,
                "button_title": btn_title
            })
        }

    def gen_text(self, i):
        return f"""제목: {self.text[i]["gpt"]["gpt_title"]}\n\
날짜: {self.text[i]["origin"]["date"]}\n\
주제: {self.text[i]["gpt"]["gpt_section"]}\n\
{'\n'.join(self.text[i]["gpt"]["gpt_abstract"][:3])}"""
