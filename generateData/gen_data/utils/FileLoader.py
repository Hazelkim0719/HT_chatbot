import json
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
        self.write_json(filename, sorted_data)