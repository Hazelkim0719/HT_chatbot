from datagenerator import DataGenerator

if __name__ == '__main__':
    data_generator = DataGenerator()
    data_generator.load_news()
    data = data_generator.load_gpt()
    data_generator.write_data(data)
    data_generator.rewrite_gpt_data()
    
