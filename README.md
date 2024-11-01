# discord-naming-bot
특정 기술에 대하여 보편적인 네이밍 컨벤션, 메이크샵 사내 네이밍 컨벤션에 따른 요소명을 지어주는 AI Discord Chatbot입니다!

# 1. 실행 방법
## 1) .env.sample 파일 
 - .sample을 지운 뒤 해당 파일에 정의된 개인 OPENAI_API_KEY, DISCORD_BOT_TOKEN 를 채워주세요.
 - 디스코드 봇 생성 및 OpenAI 계정 생성 후 발급된 토큰과 API Key를 입력해주시면 됩니다.

## 2) python bot.py
 - discord, openai 라이브러리를 설치해주세요!
 - main 실행 파일은 bot.py입니다. 터미널에 python.py를 실행하면 추가한 봇이 online 상태로 변경됩니다.
 - 정상적으로 실행되면 터미널에다음과 같이 로그가 찍힙니다.
   - INFO:root:[작명소]를 실행합니다 - 1297808820734787634
   - INFO:root:------
