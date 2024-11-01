import os
import re
import logging
import openai
from dotenv import load_dotenv

# 환경 변수를 .env 파일에서 로딩
load_dotenv()

# 환경 변수에서 OpenAI API 키를 가져옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=openai_api_key)

response_openai = ""
response_list = []
response_list_index = 0

logging.basicConfig(level=logging.INFO)

# OpenAI API를 호출하는 함수
async def get_openai_response(messages):
    global response_openai, response_list, response_list_index
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.5,
        ) 
        
        response_openai = response.choices[0].message.content
        sections = re.split(r'\n(?=\d+\.)', response_openai.strip())
        response_list = [section.strip() for section in sections]
        
        return response_list
        
    except openai.RateLimitError as e:
        logging.warning("OpenAI 사용량이 초과되었습니다. 작업을 진행할 수 없습니다.")
        return "OpenAI 사용량이 초과되었습니다. OpenAI 홈페이지 내 Dashboard에서 사용량을 확인해주세요."