import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 가져오기
api_key = os.getenv('OPENAI_API_KEY')

# print(f"Loaded API Key: {api_key}")
