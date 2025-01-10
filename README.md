1. Data source: API call from news website 
2. process the data
3. Use chatbot to translate into US slang 
4. create a service that outputs few news recap tailored to customers 

## install  
```pip install openai```  
```pip install python-dotenv```  
```pip install flask```
```pipinstall schedule```
  
## 카카오톡 인증
1. ```https://kauth.kakao.com/oauth/authorize?client_id=[본인 api id]&redirect_uri=https://example.com/oauth&response_type=code&scope=profile_nickname,friends,talk_message``` 접속 후 가입  
2. URL의 code=뒷부분을 복사 후 src/loadAccessToken.py의 authorize_code에 기입
3. 코드 실행 후 저장된 access_token을 api의 token으로 사용
4. 다른 사용자도 위와 같은 방법으로 인증 후 서버에서 메시지 수신 가능

