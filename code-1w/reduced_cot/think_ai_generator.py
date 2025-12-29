"""
Reasoning Model Dataset Converter
将普通训练数据集转换为推理模型训练格式
- 将 cot 改为 think
- 生成简洁的 response（目的、思路、结果）
"""

import json
import os
from pathlib import Path
from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time
from openai import OpenAI


class ReasoningDatasetConverter:
    """推理模型数据集转换器"""
    
    def __init__(self, input_path, output_path, api_config, max_workers=4):
        """
        初始化转换器
        
        Args:
            input_path: 输入数据集路径
            output_path: 输出数据集路径
            api_config: AI API配置
            max_workers: 最大并行数
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        
        # 初始化AI客户端
        self.client = OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        self.model = api_config['model']
        self.max_workers = max_workers
        
        # 加载数据集
        self.raw_dataset = self._load_dataset()
        self.dataset = self._extract_cases()
        
        # 统计信息
        self.stats = {
            'total': 0,
            'success': 0,
            'failure': 0,
            'skipped': 0
        }
    
    def _load_dataset(self):
        """加载原始数据集"""
        with open(self.input_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _extract_cases(self):
        """提取有效的cases"""
        cases = []
        for item in self.raw_dataset:
            if isinstance(item, dict) and 'id' in item:
                cases.append(item)
        
        print(f"[数据集] 加载了 {len(cases)} 个有效cases")
        return cases
    
    def _save_dataset(self, dataset_to_save):
        """保存转换后的数据集"""
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(dataset_to_save, f, ensure_ascii=False, indent=2)
        
        print(f"  💾 已保存到 {self.output_path}")
    
    def _generate_response_prompt(self, description, code, answer, think):
        """
        生成用于创建response的提示词
        
        Args:
            description: 问题描述
            code: 源代码
            answer: 最终答案
            think: 推理过程（原cot）
            
        Returns:
            str: 提示词
        """
        prompt = f"""You are an expert code reasoning assistant. Based on the given information, generate a concise and clear response that explains the solution.

**Question:**
{description}

**Code:**
```python
{code}
```

**Final Answer:**
{answer}

**Detailed Reasoning Process (Think):**
{think}

**Your Task:**
Generate a **concise response**  that includes:

Purpose: Briefly state what the question is asking for
Approach: Summarize the key computation steps or logic
Result: Clearly state the final answer

**Requirements:**

Be concise and direct (total response should be 3-5 sentences)
Use clear, natural language
Focus on the high-level logic, not every detail
End with a clear statement of the final answer
Example Response Format:
"This question asks us to find the value of variable X after executing a specific statement. The code first [brief key step 1], then [brief key step 2], and finally [brief key step 3]. Through these calculations, the final value of X is [answer]."

Generate the response below (ONLY the response text, no extra formatting):"""

        return prompt

    def _call_ai_for_response(self, prompt, max_retries=3):
        """
        调用AI生成response
        
        Args:
            prompt: 提示词
            max_retries: 最大重试次数
            
        Returns:
            str: 生成的response，失败则返回None
        """
        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that generates concise, clear explanations for code reasoning problems."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3,
                    max_tokens=500  # response应该简短
                )
                
                response_text = response.choices[0].message.content.strip()
                return response_text
                
            except Exception as e:
                print(f"    ✗ AI调用失败 (尝试 {attempt}/{max_retries}): {e}")
                if attempt < max_retries:
                    time.sleep(2)
        
        return None

    def process_single_case(self, case):
        """
        处理单个case，转换为推理模型格式
        
        Args:
            case: 数据集中的单个case
            
        Returns:
            dict: 转换后的case，失败则返回None
        """
        case_id = case['id']
        print(f"\n{'='*60}")
        print(f"处理 Case: {case_id}")
        print(f"{'='*60}")
        
        try:
            # 复制case结构
            new_case = {
                'id': case['id'],
                'metadata': case['metadata'].copy(),
                'task': {}
            }
            
            # 获取原始数据
            description = case['task']['description']
            code = case['task']['code']
            answer = case['task']['answer']
            cot = case['task'].get('cot', '')
            
            if not cot or not cot.strip():
                print(f"  ✗ 错误: Case缺少COT，跳过")
                self.stats['skipped'] += 1
                return None
            
            # Step 1: 将cot改为think
            print(f"  [步骤1/2] 转换 cot -> think")
            new_case['task']['description'] = description
            new_case['task']['code'] = code
            new_case['task']['answer'] = answer
            new_case['task']['think'] = cot
            print(f"    ✓ Think 长度: {len(cot)} 字符")
            
            # Step 2: 生成response
            print(f"  [步骤2/2] 调用AI生成Response...")
            prompt = self._generate_response_prompt(description, code, answer, cot)
            response_text = self._call_ai_for_response(prompt)
            
            if not response_text:
                print(f"  ✗ 失败: AI生成Response失败")
                self.stats['failure'] += 1
                return None
            
            new_case['task']['response'] = response_text
            
            print(f"  ✓ 成功生成Response")
            print(f"    长度: {len(response_text)} 字符")
            print(f"    预览: {response_text[:150]}...")
            
            self.stats['success'] += 1
            return new_case
            
        except Exception as e:
            print(f"  ✗ 处理异常: {e}")
            self.stats['failure'] += 1
            return None

    def convert_all_cases(self):
        """批量转换所有cases"""
        print(f"\n{'='*60}")
        print(f"开始转换数据集为推理模型格式")
        print(f"总数: {len(self.dataset)} cases")
        print(f"并行数: {self.max_workers}")
        print(f"{'='*60}\n")
        
        self.stats['total'] = len(self.dataset)
        
        converted_cases = []
        
        # 并行处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            future_to_case = {
                executor.submit(self.process_single_case, case): case
                for case in self.dataset
            }
            
            # 使用进度条显示处理进度
            with tqdm(total=len(self.dataset), desc="转换进度") as pbar:
                for future in as_completed(future_to_case):
                    case = future_to_case[future]
                    try:
                        new_case = future.result()
                        if new_case:
                            converted_cases.append(new_case)
                    except Exception as e:
                        print(f"\n处理异常 {case['id']}: {e}")
                        self.stats['failure'] += 1
                    
                    # 更新进度条
                    pbar.update(1)
                    pbar.set_postfix({
                        '成功': self.stats['success'],
                        '失败': self.stats['failure'],
                        '跳过': self.stats['skipped']
                    })
        
        # 保留原数据集中的background等元数据
        output_dataset = []
        for item in self.raw_dataset:
            if isinstance(item, dict) and 'background' in item:
                output_dataset.append(item)
        
        # 添加转换后的cases
        output_dataset.extend(converted_cases)
        
        # 保存转换后的数据集
        self._save_dataset(output_dataset)
        
        # 打印统计信息
        print(f"\n{'='*60}")
        print(f"转换完成")
        print(f"{'='*60}")
        print(f"总计: {self.stats['total']} cases")
        print(f"成功: {self.stats['success']} cases")
        print(f"失败: {self.stats['failure']} cases")
        print(f"跳过: {self.stats['skipped']} cases")
        print(f"成功率: {self.stats['success']/max(self.stats['total'],1)*100:.1f}%")
        print(f"{'='*60}\n")
        
        return output_dataset

    def convert_case_by_id(self, case_id):
        """转换指定ID的case（用于测试）"""
        for case in self.dataset:
            if case['id'] == case_id:
                new_case = self.process_single_case(case)
                if new_case:
                    print(f"\n转换后的格式预览:")
                    print(json.dumps(new_case, ensure_ascii=False, indent=2)[:500])
                    print("...")
                return new_case
        
        print(f"✗ Case {case_id} 不存在")
        return None

def main():
    """主函数"""
    import argparse
    parser = argparse.ArgumentParser(
        description='Reasoning Model Dataset Converter - 转换为推理模型训练格式',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            示例用法:

            转换整个数据集
            python think_ai_generator.py --input TreecEva_data_reduced_natural_cot.json --output TreecEva_reasoning_format.json

            测试单个case的转换
            python think_ai_generator.py --input TreecEva_data_reduced_natural_cot.json --case SL-MIX-S0001

            调整并行数
            python think_ai_generator.py --input data.json --output output.json --workers 8

            python think_ai_generator.py --input TreecEva_data_reduced_natural_cot.json --output Think_TreecEva_data_reduced_natural_aigenerate_cot.json --workers 8
            """
        )
    parser.add_argument(
        '--input',
        required=True,
        help='输入数据集JSON文件路径'
    )

    parser.add_argument(
        '--output',
        default='TreecEva_reasoning_format.json',
        help='输出数据集JSON文件路径（默认: TreecEva_reasoning_format.json）'
    )

    parser.add_argument(
        '--case',
        type=str,
        help='仅转换指定的case ID（用于测试）'
    )

    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        help='并行处理的worker数量（默认: 4）'
    )

    args = parser.parse_args()

    # API配置
    API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"
    BASE_URL = "https://llmapi.paratera.com/v1"

    api_config = {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3.2-Exp"
    }

    print(f"{'='*60}")
    print(f"Reasoning Model Dataset Converter")
    print(f"{'='*60}")
    print(f"输入: {args.input}")
    print(f"输出: {args.output}")
    print(f"AI模型: {api_config['model']}")
    print(f"并行数: {args.workers}")
    print(f"{'='*60}\n")

    # 创建转换器
    converter = ReasoningDatasetConverter(
        input_path=args.input,
        output_path=args.output,
        api_config=api_config,
        max_workers=args.workers
    )

    # 执行转换
    if args.case:
        # 测试单个case
        converter.convert_case_by_id(args.case)
    else:
        # 转换所有cases
        converter.convert_all_cases()

if __name__ == '__main__':
    main()  