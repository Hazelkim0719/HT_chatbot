import requests
from bs4 import BeautifulSoup
from utils import Logging, FileLoader

class Crawler:
    def __init__(self, naver_url):
        self.log = Logging()
        self.f = FileLoader()
        self.naver_url = naver_url
        self.news_links = []
        self.news = []
        self.news_ids = []

    def get_news(self):
        return self.news
    
    def data_load(self):
        self.get_news_links(self.naver_url)
        self.get_news_ids(self.news_links)
        self.crawl_news(self.news_ids)

    def get_news_links(self, naver_fin_home):
        self.log.log("crawl naver fin home")
        response = requests.get(naver_fin_home)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_list = soup.find('ul','newsList')
        news_blocks = news_list.find_all('li','block1')
        
        for block in news_blocks:
            self.news_links.append(block.find('dt','thumb').find('a')['href'])

    def get_news_ids(self, news_links):
        for link in news_links:
            article_id_idx = link.find('article_id')
            office_id_idx = link.find('office_id')

            article_id = link[article_id_idx+11:article_id_idx+21]
            office_id = link[office_id_idx+10:office_id_idx+13]

            self.news_ids.append({'article_id':article_id,'office_id':office_id})

    def crawl_news(self, news_ids):
        data = self.f.load_json('../data/dataset.json') 
        for id in news_ids:
            formatted_id = f"{id['office_id']}_{id['article_id']}"
            if any(item['origin']['id'] == formatted_id for item in data):
                self.log.log(f"duplication news({id['article_id']})")
            else:   
                self.log.log(f"crawl news!({id['article_id']})")
                response = requests.get(f'https://n.news.naver.com/mnews/article/{id["office_id"] }/{id["article_id"]}')
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('h2',"media_end_head_headline").find('span').get_text()
                article = soup.find('article', 'go_trans _article_content').get_text().replace("\n","")
                date = soup.find('span', 'media_end_head_info_datestamp_time _ARTICLE_DATE_TIME').attrs['data-date-time']

                self.news.append({
                    'id': formatted_id,
                    'title': title,
                    'article': article,
                    'date': date, 
                    'url': f'https://n.news.naver.com/mnews/article/{ id["office_id"] }/{id["article_id"]}'
                })