import os

# 文件路径配置
DATASET_PATH = "data/Statement-Level-MIX.json"
ANSWER_PATH = "data/answer.json"
TEMP_CODE_DIR = "temp_code"

# API配置
API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"

# 请根据你的实际API提供商调整
BASE_URL = "https://llmapi.paratera.com/v1"

# 选择5个不同的模型进行评估
AI_APIS = {
    "qwen3_235b": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "Qwen3-235B-A22B-Instruct-2507"
    },
    "qwen3_coder": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "Qwen3-Coder-480B-A35B-Instruct"
    },
    "minimax_text": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "MiniMax-Text-01"
    },
    "glm4_plus": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "GLM-4-Plus"
    },
    "deepseek_v3": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3-250324"
    }
}

# 确保目录存在
os.makedirs(TEMP_CODE_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)