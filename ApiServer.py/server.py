import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import re
from flask import Flask, jsonify
from flask_cors import CORS
from generateData.gen_data.utils import FileLoader

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    f = FileLoader()
    d = f.load_json('../generateData/data/dataset.json')
    d = iter_parse_abstract(d)
    d = iter_parse_annotation(d)
    
    return jsonify(d)

def parse_abstract(text):
    return [
        text[:text.find("2.")-1],
        text[text.find("2."):text.find("3.")-1],
        text[text.find("3."):]
    ]

def iter_parse_abstract(data):
    for i in range(len(data)):
        data[i]['gpt']['gpt_abstract'] = parse_abstract(data[i]['gpt']['gpt_abstract'])
    return data

def iter_parse_annotation(data):
    for i in range(len(data)):
        data[i]['gpt']['gpt_annotation'] = parse_annotation(data[i]['gpt']['gpt_annotation'])
    return data

def parse_annotation(annotation_text):
    # 숫자와 마침표 뒤의 내용을 찾는 정규 표현식
    pattern = r'(\d+\.)\s*([^0-9]+)'
    
    # 정규식으로 매칭된 결과를 리스트로 반환
    result = re.findall(pattern, annotation_text)
    print(result)
    # 매칭된 부분을 "숫자. 내용" 형식으로 다시 합쳐서 반환
    return [f"{match[1].strip()}" for match in result]

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

