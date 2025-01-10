import requests
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'f9cbbdc855a78e7329fe5b21345cabcb'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'yFCHHDSWoasA-K7xBYa14iwt98Zr2sZQTlRrArx5GbHSRAPuKFE0tgAAAAQKPXLrAAABlFCWe8HdCc_9be4aqQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open("./data/kakaoToken.json","w") as fp:
    json.dump(tokens, fp)