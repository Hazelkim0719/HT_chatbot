1. Data source: API call from news website 
2. process the data
3. Use chatbot to translate into US slang 
4. create a service that outputs few news recap tailored to customers 

# 실행 방법  
## 1. docker 설치
## 2. 이미지 빌드  
```sudo docker build -t ht-project .```
## 3. 컨테이너 실행
```sudo docker run -it -v $(pwd):/app -e TZ=Asia/Seoul --name ht-project ht-project```
## 4. 파일 실행
```python src/gen_data/main.py```  
&nbsp;
&nbsp;
# 카카오톡 인증  
## 1. kakao developer에 팀원 초대하기
[링크](https://developers.kakao.com/console/app/1185992/config/member)에서 팀원 초대
## 2. 카카오 로그인 후 앱 가입 및 약관 동의
```https://kauth.kakao.com/oauth/authorize?client_id=f9cbbdc855a78e7329fe5b21345cabcb&redirect_uri=https://example.com/oauth&response_type=code&scope=profile_nickname,friends,talk_message```  
위 링크를 통해 사용자가 로그인한 후 약관 동의
## 3. tokens 발급
2번까지 해도 사용자 추가가 되지만 혹시 안되면 KakaoLoginMng클래스의 load_tokens 함수를 참고하여 tokens 발급해보기

# requirements 
```python==3.13
openai==1.59.6
python-dotenv==0.20.0
Flask==2.0.3
beautifulsoup4==4.12.3
schedule==1.1.0
requests==2.32.3
```
