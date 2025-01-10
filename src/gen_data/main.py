from datagenerator import DataGenerator
import schedule
import time
from kakaoServer import KakaoMng

def gen_data():
    data_generator = DataGenerator()
    data_generator.load_news()
    data = data_generator.load_gpt(10)
    data_generator.write_data(data)
    data_generator.rewrite_gpt_data()

def send_kakaotalk():
    k = KakaoMng()
    k.multi_send(10)

def schedule_fun():
    print("schedule function start!")
    gen_data()
    send_kakaotalk()

if __name__ == '__main__':
    print("schedule start..")
    schedule.every().day.at("08:00").do(schedule_fun)
    schedule.every().day.at("15:00").do(schedule_fun)
    while True:
        schedule.run_pending()
        time.sleep(1)  # CPU 점유율을 낮추기 위해 짧은 대기 추가