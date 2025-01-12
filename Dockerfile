# 베이스 이미지: Python 3.13.0
FROM python:3.13-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 업데이트 및 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 필요한 Python 패키지 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Flask 애플리케이션 실행
CMD ["bash"]