import json
import re
from datetime import datetime

class FileLoader:
    def __init__(self):
        pass

    def load_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
            return data

    def load_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    
    def write_json(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f)

    def convert_str_to_json(data):
        return json.loads(data)

    def append_json(self, filename, data):
        result = []
        with open(filename, 'r') as f:
            result = json.load(f)
        for d in data:
            result.append(d)
        self.write_json(filename, result)

    def cleanup_file(self, filename):
        data = self.load_json(filename)
        unique_data = {item['origin']['id']: item for item in data}.values()
        sorted_data = sorted(
            unique_data,
            key=lambda x: datetime.strptime(x['origin']['date'], "%Y-%m-%d %H:%M:%S")
        )
        parsed_anntation_data = self.iter_parse_annotation(sorted_data)
        parse_abstract_data = self.iter_parse_abstract(parsed_anntation_data)
        self.write_json(filename, parse_abstract_data)

    def parse_abstract(self, text):
        if type(text) is str:
            return [
                text[:text.find("2.")-1],
                text[text.find("2."):text.find("3.")-1],
                text[text.find("3."):]
            ]
        elif type(text) is dict:
            return list(text.values())
        else:
            return text
            
    def iter_parse_abstract(self, data):
        for i in range(len(data)):
            data[i]['gpt']['gpt_abstract'] = self.parse_abstract(data[i]['gpt']['gpt_abstract'])
        return data
    def iter_parse_annotation(self, data):
        for i in range(len(data)):
            data[i]['gpt']['gpt_annotation'] = self.parse_annotation(data[i]['gpt']['gpt_annotation'])
        return data

    def parse_annotation(self, annotation_text):
        if type(annotation_text) is str:
            # 숫자와 마침표 뒤의 내용을 찾는 정규 표현식
            pattern = r'(\d+\.)\s*([^0-9]+)'
            
            # 정규식으로 매칭된 결과를 리스트로 반환
            result = re.findall(pattern, annotation_text)
            # 매칭된 부분을 "숫자. 내용" 형식으로 다시 합쳐서 반환
            return [f"{match[1].strip()}" for match in result]
        elif type(annotation_text) is dict:
            return list(annotation_text.values())
        else:
            return annotation_text