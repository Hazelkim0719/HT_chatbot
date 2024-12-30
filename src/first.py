from dotenv import load_dotenv
import os
import requests

# load .env
load_dotenv()
API_KEY = os.environ.get('NYT_KEY')
res = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:("Business") &begin_date=20241227&api-key='+API_KEY)
data = res.json()

if data["status"] == "OK":
    results = data["response"]["docs"]
    for result in results:
        cnt += 1
        print(result["abstract"])
        print(result["section_name"])
        print(result["news_desk"])
        print("\n")                

