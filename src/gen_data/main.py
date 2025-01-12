from datagenerator import DataGenerator
from kakao import KakaoSendMng
from utils import Logging, FileLoader
import schedule
import time

def gen_data():
    data_generator = DataGenerator()
    data_generator.load_news()
    data = data_generator.load_gpt(9)
    data_generator.write_data(data)
    data_generator.rewrite_gpt_data()

def send_kakaotalk():
    k = KakaoSendMng()
    k.multi_send(9)

def schedule_fun():
    gen_data()
    send_kakaotalk()

if __name__ == '__main__':
    f = FileLoader()
    f.cleanup_file()
    schedule.every().day.at("00:00").do(f.cleanup_file)

    time_table = ["08:00", "15:00"]
    log = Logging()
    for t in time_table:
        log.log(f"register schedule {t}")
        schedule.every().day.at(t).do(schedule_fun)

    while True:
        schedule.run_pending()
        time.sleep(1)  # CPU 점유율을 낮추기 위해 짧은 대기 추가