import requests

# Base URL
BASE_URL = "http://localhost:5000"

def test_home():
    response = requests.get(BASE_URL)
    print(response.text)

if __name__ == "__main__":
    print("Testing Flask App...\n")
    test_home()