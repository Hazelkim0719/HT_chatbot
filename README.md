# project overview
1. Data source: API call from news website 
2. process the data
3. Use chatbot to translate into US slang 
4. create a service that outputs few news recap tailored to customers 

# Result🎉
![image](https://github.com/user-attachments/assets/48c5fe38-73fe-447f-84b4-aa08f472de3d)
![image](https://github.com/user-attachments/assets/18706a9d-3013-4de0-a802-c0e9a5deb2a4)
![image](https://github.com/user-attachments/assets/f610e406-d569-42cc-ab5d-8c55811673fa)
![제목 없음](https://github.com/user-attachments/assets/1f2bbe86-0f06-4112-844f-d9292f490466)


# kakao server(gen_Server) 실행 방법  
## - 파일 실행 -
### 1. docker 설치
### 2. 이미지 빌드  
```sudo docker build -t ht-project .```
### 3. 컨테이너 실행
```sudo docker run -it -v $(pwd):/app -e TZ=Asia/Seoul --name ht-project ht-project```
### 4. 파일 실행
```python src/gen_data/main.py```  
&nbsp;
&nbsp;
&nbsp;
## - 카카오톡 인증 -
### 1. kakao developer에 팀원 초대하기
[링크](https://developers.kakao.com/console/app/1185992/config/member)에서 팀원 초대
### 2. 카카오 로그인 후 앱 가입 및 약관 동의
```https://kauth.kakao.com/oauth/authorize?client_id=f9cbbdc855a78e7329fe5b21345cabcb&redirect_uri=https://example.com/oauth&response_type=code&scope=profile_nickname,friends,talk_message```  
위 링크를 통해 사용자가 로그인한 후 약관 동의
### 3. tokens 발급
2번까지 해도 사용자 추가가 되지만 혹시 안되면 KakaoLoginMng클래스의 load_tokens 함수를 참고하여 tokens 발급해보기
&nbsp;
&nbsp;
&nbsp;
## - requirements -
```python==3.13
openai==1.59.6
python-dotenv==0.20.0
Flask==2.0.3
Flask-Cors=5.0.0
beautifulsoup4==4.12.3
schedule==1.1.0
requests==2.32.3
```
---
# api server 실행 방법  
## - 파일 실행 -
### 1. docker 설치
### 2. 이미지 빌드(/HTPROJECT/ApiServer 폴더에서 실행)
```sudo docker build -t ht-project-api-server .```
### 3. 컨테이너 실행(/HTPROJECT 폴더에서 실행)
```sudo docker run -it -v $(pwd):/workspace -p 5000:5000 --name ht-project-api-server ht-project-api-server```
### 4. 파일 실행
```python ApiServer/app.py``` 

## - requirements -
```
Flask==3.1.0
Flask-Cors==5.0.0
```

--- 
# Frontend 실행 방법
### ※ API server와 같은 네트워크 내에서 작동
## - 파일 실행 -
### 1. npm 설치
### 2. node_modules 설치
```npm install```
### 3. api 가져오기 위한 라이브러리 설치
```npm install axios```
### 4. react 실행
```npm run dev```

## - requirements -
```
react=18.3.1
react-dom=18.3.1
axios=1.7.9
```
