import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
from options import LARGE_CATEGORIES, JS_TS_COMMON_OPTIONS, JS_TS_MAKESHOP_OPTIONS, PHP_OPTIONS, DB_OPTIONS
from chatgpt import get_openai_response
from naming_conventions import naming_conventions

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수에서 Discord 봇 토큰을 가져옵니다.
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='/', intents=intents)

conversation_active = False
selected_language = ""
selected_convention = ""
selected_type = ""
wanted_definition = ""
response_list = []
response_list_index = 0

@bot.event
async def on_ready():
    logging.info(f'[{bot.user.name}]를 실행합니다 - {bot.user.id}')
    logging.info('------')

# 봇이 준비되었을 때 동작할 코드를 정의합니다.
@bot.command(name='작명시작')
async def start_conversation(ctx):
    selected_convention_view = SelectedConventionView()
    await ctx.send("안녕하세요! 네이밍 상담소입니다 (‾◡◝) 어떤 언어로 작업하시고 계신가요?", view=selected_convention_view)

@bot.event
async def on_message(message):
    global conversation_active, selected_language, selected_convention, selected_type, wanted_definition, response_list_index
    double_check_buttons_view = DoubleCheckButtonsView()
    
    # 봇이 보낸 메시지는 무시합니다.
    if message.author.bot:
        return

    # 사용자가 작명 종료를 요청하면 대화를 종료합니다.
    if message.content == '/작명종료':
        conversation_active = False
        await message.channel.send('필요하실 때 또 찾아주세요!\n\n------ 작명 상담소를 종료합니다 ------')
        return
    
    # 사용자가 보낸 메시지를 로깅합니다.
    if message.guild is None:
        logging.info(f'[{message.author}]가 보낸 메시지: {message.content}')
    else:
        logging.info(f'[{message.channel}] 채널에서 [{message.author}]가 보낸 채널 메시지: {message.content}')
    
    # 대화가 진행 중(conversation_active == True)이라면 사용자가 원하는 정의를 가져옵니다.
    if conversation_active:
        wanted_definition = message.content
        await message.channel.send(f'[{selected_language}]에서 [{selected_convention}] 네이밍 컨벤션을 따르는 [{selected_type}]이/가 [{wanted_definition}]를 함축한 의미의 이름이 필요하신거죠?', view=double_check_buttons_view)
    
    else:
        await bot.process_commands(message)
        

class UXHandlerButtonsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.select_value = None
        
    @discord.ui.button(label='다른 결과도 보여줄래?🤔', style=discord.ButtonStyle.primary)
    async def get_diff_result_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        global response_list_index
        
        self.select_value = True
        ux_handler_buttons_view = UXHandlerButtonsView()
        
        if response_list_index >= len(response_list):
            response_list_index = 0
            await interaction.response.defer()
            await interaction.followup.send(f'앗, 준비된 결과는 여기까지랍니다!\n\n만약 처음 결과를 다시 보고 싶으시다면 [다른 결과도 보여줄래?🤔] 버튼을 클릭해주세요!', view=ux_handler_buttons_view)
        else :    
            await interaction.response.defer()
            await interaction.followup.send(f'네! 다른 결과도 보여드릴게요~(∩^o^)⊃━☆ \n {response_list[response_list_index]}', view=ux_handler_buttons_view)
            response_list_index += 1  # 다음 인덱스로 이동
        
    @discord.ui.button(label='다른 이름 지어볼까?😄', style=discord.ButtonStyle.success)
    async def make_new_naming_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.select_value = False
        selected_convention_view = SelectedConventionView()
        await interaction.response.defer()
        await interaction.followup.send('좋아요! 다시 시작해볼까요?(｡･∀･)ﾉﾞ', view=selected_convention_view)
        
    @discord.ui.button(label='충분해!😉', style=discord.ButtonStyle.danger)
    async def off_chatbot_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        global conversation_active
        conversation_active = False
        
        await interaction.response.defer()
        await interaction.followup.send('네! 다음에 또 불러주세요~♪(´▽｀)\n\n ------ 작명 상담소를 종료합니다 ------')
        return    
    
    
class DoubleCheckButtonsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.select_value = None
    
    @discord.ui.button(label='응, 맞아 ⭕', style=discord.ButtonStyle.success)
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.select_value = True
        await interaction.response.defer()
        await interaction.followup.send(f'좋아요! 입력하신 정보를 기반으로 이름을 지어볼게요!\n\n -------------- 잠시만 기다려주세요( •̀ ω •́ )✧ --------------')
        
        global conversation_active, selected_language, selected_convention, selected_type, wanted_definition, response_list, response_list_index
        uXHandlerButtonsView = UXHandlerButtonsView()
        
        messages = [
            {"role": "system", "content": f"너는 code convention에 매우 엄격한 개발자야. 네이밍을 할 때, 네가 선택한 '{selected_language}'기술 사용시 '{selected_convention}' 컨벤션에 맞게 '{selected_type}'의 이름을 지어야 해."},
            {"role": "system", "content": "naming을 할 때, 서비스/기능 이름이나 성격 등을 직관적으로 설명할 수 있는 단어, 사용자가 이해하기 쉬운 단어 위주로 사용해야 해."},
            {"role": "system", "content": "이름의 전체 길이가 최대 20자를 넘지 않도록 작성해줘."},
            {"role": "system", "content": f"선택한 naming convention의 상세한 규칙은 다음과 같아:\n {naming_conventions[selected_language][selected_convention][selected_type]}"},
            {"role": "system", "content": f"다음 규칙에 맞게 '{wanted_definition}'의 의미를 담은 이름을 3가지를 가장 naming convention에 적합한 순서대로 추천해줘."},
            {"role": "system", "content": "각 추천된 이름을 구성하는 영어 단어의 의미도 함께 전달해줘."},
        ]
        
        # OpenAI API를 통해 사용자가 원하는 이름을 추천받습니다.
        response_list = await get_openai_response(messages)

        if len(response_list) > 0:
            await interaction.followup.send(f'{response_list[response_list_index]}', view=uXHandlerButtonsView)
            response_list_index += 1  # 다음 인덱스로 이동
        
    @discord.ui.button(label='아니, 다시! ❌', style=discord.ButtonStyle.danger)
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.select_value = False
        selectedConventionView = SelectedConventionView()
        await interaction.response.send_message('앗, 그렇다면 다시 차례대로 입력해볼까요?', view=selectedConventionView)
    
     
class SelectedConventionView(discord.ui.View):
    def __init__(self):
        super().__init__()

        languages = [
            ("JS/TS", "JS/TS"),
            ("PHP", "PHP"),
            ("DB", "DB")
        ]

        self.select = discord.ui.Select(
            placeholder="작업하고 계신 프로젝트에서 어떤 기술을 사용하시나요?",
            options=[
                discord.SelectOption(label=label, description=LARGE_CATEGORIES[label], emoji=None, default=False)
                for label, _ in languages
            ]
        )

        self.select.callback = self.select_convention_callback
        self.add_item(self.select)
        
    # 사용자가 선택한 값을 변수에 저장하고 다음 질문을 띄웁니다.
    async def select_convention_callback(self, interaction: discord.Interaction):
        global selected_language
        selected_language = self.select.values[0]  # 사용자가 선택한 값을 변수에 저장
        self.select.placeholder = "어떤 네이밍 컨벤션을 사용하시고 싶으신가요?"
        
        conventions = []
        if selected_language == "JS/TS":
            conventions = [
                ("공통규칙", "전반적인 JS/TS 사용 프로젝트의 보편적인 네이밍 컨벤션"),
                ("메이크샵", "사내 Notion>MAKE#CRM 내 기재된 React.js/Next.js 네이밍 규칙 문서 기반의 네이밍 컨벤션")
            ]
        elif selected_language == "PHP":
            conventions = [
                ("공통규칙", "전반적인 PHP 사용 프로젝트의 보편적인 네이밍 컨벤션"),
                ("메이크샵", "사내 Notion>개발본부>메이크샵 신입교육자료에 기재된 메이크샵 내 프로젝트를 위한 네이밍 컨벤션")
            ]
        elif selected_language == "DB":
            conventions = [
                ("공통규칙", "MySQL, PostgreSQL 등 RDBMS에서 사용되는 보편적인 테이블/컬럼 네이밍 컨벤션"),
                ("메이크샵", "사내 Notion>NMP 내 기재된 데이터베이스 네이밍 규칙 문서 기반의 네이밍 컨벤션")
            ]

        self.select.options = [
            discord.SelectOption(label=label, description=description, emoji=None, default=False)
            for label, description in conventions
        ]

        self.select.callback = self.select_type_callback
        await interaction.response.send_message(f'[{selected_language}]를 사용하시는군요! 좀 더 좋은 이름을 짓기 위하여 원하시는 네이밍 컨벤션을 선택해주세요.', view=self)
        
        
    async def select_type_callback(self, interaction: discord.Interaction):
        global selected_language, selected_convention, conversation_active
        selected_convention = self.select.values[0]  # 사용자가 선택한 값을 변수에 저장

        options = []
        if selected_language == "JS/TS":
            if selected_convention == "공통규칙":
                self.select.placeholder = "전반적인 JS/TS 사용 프로젝트의 보편적인 네이밍 컨벤션입니다."
                options = JS_TS_COMMON_OPTIONS
            elif selected_convention == "메이크샵":
                self.select.placeholder = "메이크샵 내 공통 프론트엔드 프레임워크는 React.js/Next.js입니다. 사내 Notion>MAKE#CRM 내 기재된 React.js/Next.js 네이밍 규칙 문서 기반의 네이밍 컨벤션입니다."
                options = JS_TS_MAKESHOP_OPTIONS
        elif selected_language == "PHP":
            if selected_convention == "공통규칙":
                self.select.placeholder = "전반적인 PHP 사용 프로젝트의 보편적인 네이밍 컨벤션입니다."
            elif selected_convention == "메이크샵":
                self.select.placeholder = "사내 Notion>개발본부>메이크샵 신입교육자료에 기재된 메이크샵 내 프로젝트를 위한 네이밍 컨벤션입니다."
            options = PHP_OPTIONS
        elif selected_language == "DB":
            if selected_convention == "공통규칙":
                self.select.placeholder = "MySQL, PostgreSQL 등 RDBMS에서 사용되는 보편적인 테이블/컬럼 네이밍 컨벤션입니다."
            elif selected_convention == "메이크샵":
                self.select.placeholder = "사내 Notion>NMP 내 기재된 데이터베이스 네이밍 규칙 문서 기반의 네이밍 컨벤션입니다."
            options = DB_OPTIONS

        self.select.options = [
            discord.SelectOption(label=option)
            for option in options
        ]

        self.select.callback = self.select_element_callback
        await interaction.response.send_message(f'[{selected_convention}] 네이밍 컨벤션을 선택하셨네요! 어떤 요소의 이름을 짓고 싶으신가요?', view=self)
 
    async def select_element_callback(self, interaction: discord.Interaction):
        global selected_type, selected_convention, conversation_active
        selected_type = self.select.values[0]  # 사용자가 선택한 값을 변수에 저장
        
        # 사용자로부터 원하는 정의 입력 받기
        await interaction.response.send_message(f'만들고자하는 [{selected_type}]이/가 어떤 기능을 하는지 간단히 설명해주실래요?')
        conversation_active = True        
 
bot.run(discord_bot_token)