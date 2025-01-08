import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, naver_url):
        self.naver_url = naver_url
        self.news_links = []
        self.news = []
        self.news_ids = []
        self.data_load()

    def get_news(self):
        return self.news
    
    def data_load(self):
        self.get_news_links(self.naver_url)
        self.get_news_ids(self.news_links)
        self.crawl_news(self.news_ids)

    def get_news_links(self, naver_fin_home):
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
        for id in news_ids:
            response = requests.get(f'https://n.news.naver.com/mnews/article/{id['office_id']}/{id['article_id']}')
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h2',"media_end_head_headline").find('span').get_text()
            article = soup.find('article', 'go_trans _article_content').get_text().replace("\n","")
            date = soup.find('span', 'media_end_head_info_datestamp_time _ARTICLE_DATE_TIME').attrs['data-date-time']

            self.news.append({'title':title,'article':article,'date':date})