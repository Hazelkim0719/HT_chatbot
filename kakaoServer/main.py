import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from generateData.gen_data import DataGenerator
from generateData.gen_data.utils import Logging, FileLoader
from kakao import KakaoSendMng
import schedule
import time

class schedule_gen_server:
    def __init__(self):
        self.log = Logging()
        self.send_msg_cnt = 5
        self.load_gpt_cnt = 15
        self.data_path = '../generateData/data/dataset.json'

    def gen_data(self, cnt):
        data_generator = DataGenerator()
        f = FileLoader()
        data_generator.load_news()
        data = data_generator.load_gpt(cnt)
        data_generator.write_data(data)
        data_generator.rewrite_gpt_data()
        f.cleanup_file(self.data_path)

    def send_kakaotalk(self, cnt):
        k = KakaoSendMng()
        k.multi_send(cnt)

    def send_kakao_schedule(self):
        self.gen_data(self.send_msg_cnt)
        self.send_kakaotalk(self.send_msg_cnt)

    def load_gen_data(self):
        self.gen_data(self.load_gpt_cnt)

if __name__ == '__main__':
    sgs = schedule_gen_server()

    kakao_time_table = ["08:00", "15:00"]
    load_time_table = ["09:30","11:00","13:30", "16:30", "18:00", "19:30", "21:00"]

    for t in kakao_time_table:
            sgs.log.log(f"register schedule send kakao({t})")
            schedule.every().day.at(t).do(sgs.send_kakao_schedule)

    for t in load_time_table:
            sgs.log.log(f"register schedule load gpt data({t})")
            schedule.every().day.at(t).do(sgs.load_gen_data)


    while True:
        schedule.run_pending()
        time.sleep(1)  # CPU 점유율을 낮추기 위해 짧은 대기 추가