import requests
import json

# 你的API配置（直接替换，无需修改其他部分）
CONFIG = {
    "base_url": "https://api.ezai88.com",
    "api_key": "sk-gq8qRNNiNIjS0x8tzfMl8F9bscL4wopT7oA2qD2FU8xKTrnp",
    "model": "claude-3-7-sonnet-20250219"
}

def test_ai_api():
    print("=== 简洁AI API测试 ===\n")
    print(f"测试配置：{json.dumps(CONFIG, indent=2)}\n")

    # 1. 构建请求参数（适配Claude类API格式）
    url = f"{CONFIG['base_url']}/v1/chat/completions"  # 常见Claude API路径，若不同可修改
    headers = {
        "Authorization": f"Bearer {CONFIG['api_key']}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": CONFIG["model"],
        "messages": [{"role": "user", "content": "返回'测试成功'即可，无需额外内容"}],
        "max_tokens": 10
    }

    try:
        # 2. 发送请求
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()  # 非200状态码抛异常

        # 3. 解析并验证响应
        result = response.json()
        print("✅ 请求成功！")
        print(f"响应状态码：{response.status_code}")
        print(f"API返回结果：{result['choices'][0]['message']['content'].strip()}")

    except requests.exceptions.Timeout:
        print("❌ 测试失败：请求超时（20秒）")
    except requests.exceptions.ConnectionError:
        print("❌ 测试失败：无法连接API（地址错误/网络问题）")
    except requests.exceptions.HTTPError as e:
        print(f"❌ 测试失败：HTTP错误 - {e}")
        print(f"API错误详情：{response.text}")  # 关键错误信息（密钥/配额/模型问题）
    except json.JSONDecodeError:
        print("❌ 测试失败：API返回非JSON格式")
        print(f"原始响应：{response.text}")
    except Exception as e:
        print(f"❌ 测试失败：未知错误 - {str(e)}")

if __name__ == "__main__":
    test_ai_api()