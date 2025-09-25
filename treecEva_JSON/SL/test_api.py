import openai
from config import AI_APIS

def test_all_apis():
    """测试所有API连接"""
    for api_name, api_config in AI_APIS.items():
        print(f"\nTesting {api_name} ({api_config['model']})...")
        
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        try:
            response = client.chat.completions.create(
                model=api_config['model'],
                messages=[{"role": "user", "content": "Hello, can you respond with just the number 42?"}],
                max_tokens=10
            )
            
            result = response.choices[0].message.content
            print(f"✓ {api_name}: {result}")
            
        except Exception as e:
            print(f"✗ {api_name}: Error - {str(e)}")

if __name__ == "__main__":
    test_all_apis()