from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta 

# load .env
load_dotenv()
API_KEY = os.environ.get('NYT_KEY')
search_date = (datetime.now() -timedelta(days=2)).strftime("%Y%m%d")
res = requests.get(f'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:("Business") &begin_date={search_date}&api-key={API_KEY}')
data = res.json()

if data["status"] == "OK":
    results = data["response"]["docs"]
    for result in results:
        print(result["abstract"])
        print(result["section_name"])
        print(result["news_desk"])
        print(result["web_url"])
        print("\n")                

