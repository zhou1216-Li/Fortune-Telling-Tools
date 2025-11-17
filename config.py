# 配置文件

# 数据库配置
import os
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "data", "fortune_telling.db")

# 数据文件路径
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZODIAC_DATA_PATH = os.path.join(BASE_DIR, "modules", "data", "zodiac_data.json")
MBTI_DATA_PATH = os.path.join(BASE_DIR, "modules", "data", "mbti_data.json")

# 界面配置
WINDOW_TITLE = "命理预测工具"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

# 运势类型
FORTUNE_TYPES = ["财运", "感情运", "事业运", "健康运"]

# 聊天助手配置
CHAT_API_KEY = ""  # API密钥（可在设置中配置，Android版本不需要）
CHAT_API_TYPE = "free_api"  # API类型: 'free_api'(免费，无需配置), 'openai', 'huggingface', 'mock'

