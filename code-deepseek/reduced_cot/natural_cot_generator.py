"""
Natural COT Generator - 使用AI生成自然语言COT
读取剪枝后的追踪文件，结合问题描述和代码，让AI生成自然语言的推理过程
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time
from openai import OpenAI


class NaturalCOTGenerator:
    """自然语言COT生成器 - 使用AI"""
    
    def __init__(self, dataset_path, api_config, max_workers=4):
        """
        初始化生成器
        
        Args:
            dataset_path: 数据集JSON文件路径
            api_config: AI API配置 {'base_url': ..., 'api_key': ..., 'model': ...}
            max_workers: 最大并行工作数
        """
        self.dataset_path = Path(dataset_path)
        self.dataset_dir = self.dataset_path.parent
        self.temp_code_dir = self.dataset_dir / 'temp_code'
        
        # 初始化AI客户端 - 修改这里，参考 ai_analyzer.py
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
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _extract_cases(self):
        """从原始数据集中提取实际的cases（跳过background等元数据）"""
        cases = []
        for item in self.raw_dataset:
            if isinstance(item, dict) and 'id' in item:
                cases.append(item)
        
        print(f"[数据集] 加载了 {len(cases)} 个有效cases")
        return cases
    
    def _save_dataset(self):
        """保存数据集（保持原始结构）"""
        # 更新原始数据集中的cases
        for i, item in enumerate(self.raw_dataset):
            if isinstance(item, dict) and 'id' in item:
                case_id = item['id']
                # 查找对应的case
                for case in self.dataset:
                    if case['id'] == case_id:
                        self.raw_dataset[i] = case
                        break
        
        # 保存到文件
        with open(self.dataset_path, 'w', encoding='utf-8') as f:
            json.dump(self.raw_dataset, f, ensure_ascii=False, indent=2)
        
        print(f"  💾 已保存到 {self.dataset_path}")
    
    def _read_trimmed_trace(self, case_id):
        """
        读取剪枝后的追踪文件
        
        Args:
            case_id: Case ID (如: SL-MIX-S0001)
            
        Returns:
            str: 追踪文件内容，如果文件不存在则返回None
        """
        case_dir = self.temp_code_dir / case_id
        trimmed_file = case_dir / f"trimmed_trace_{case_id}.txt"
        
        if not trimmed_file.exists():
            return None
        
        with open(trimmed_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _generate_prompt(self, description, code, trimmed_trace):
        """
        生成AI提示词
        
        Args:
            description: 问题描述
            code: 源代码
            trimmed_trace: 剪枝后的追踪记录
            
        Returns:
            str: 完整的提示词
        """
        prompt = f"""You are an expert in code reasoning and execution tracing. Your task is to generate a clear, natural Chain-of-Thought (COT) explanation for a code analysis question.

**Question:**
{description}

**Source Code:**
```python
{code}
```

**Execution Trace (Pruned - showing only relevant steps):**
```
{trimmed_trace}
```

**Instructions:**
1. Analyze the question to understand what value is being asked for
2. Walk through the execution trace step by step
3. Explain how variables are initialized and updated
4. Track the computation flow, especially for loops and conditionals
5. Clearly state the final answer

**Output Requirements:**
- Write in clear, natural language (not just code comments)
- Explain the logic behind each important step
- Show intermediate values when helpful
- Make it educational - as if teaching a student
- End with a clear statement of the final answer

Generate the COT explanation below:"""

        return prompt

    def _call_ai(self, prompt, max_retries=3):
        """
        调用AI API生成COT
        
        Args:
            prompt: 提示词
            max_retries: 最大重试次数
            
        Returns:
            str: 生成的COT，失败则返回None
        """
        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful code analysis assistant that explains program execution step by step in natural language."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3,  # 较低的temperature以获得更一致的输出
                    max_tokens=2000
                )
                
                cot = response.choices[0].message.content.strip()
                return cot
                
            except Exception as e:
                print(f"    ✗ AI调用失败 (尝试 {attempt}/{max_retries}): {e}")
                if attempt < max_retries:
                    time.sleep(2)  # 等待2秒后重试
        
        return None

    def process_single_case(self, case):
        """
        处理单个case，生成natural COT
        
        Args:
            case: 数据集中的单个case
            
        Returns:
            bool: 是否成功
        """
        case_id = case['id']
        print(f"\n{'='*60}")
        print(f"处理 Case: {case_id}")
        print(f"{'='*60}")
        
        # 检查是否已有COT
        if case['task'].get('cot') and case['task']['cot'].strip():
            print(f"  ⊙ 跳过: 已有COT (长度: {len(case['task']['cot'])} 字符)")
            self.stats['skipped'] += 1
            return True
        
        # 提取必要信息
        description = case['task']['description']
        code = case['task']['code']
        
        # 读取剪枝后的追踪文件
        print(f"  [步骤1/3] 读取剪枝后的追踪文件...")
        trimmed_trace = self._read_trimmed_trace(case_id)
        
        if not trimmed_trace:
            print(f"  ✗ 错误: 未找到剪枝后的追踪文件")
            print(f"    预期位置: temp_code/{case_id}/trimmed_trace_{case_id}.txt")
            self.stats['failure'] += 1
            return False
        
        print(f"    ✓ 已读取 (长度: {len(trimmed_trace)} 字符)")
        
        # 生成prompt
        print(f"  [步骤2/3] 生成AI提示词...")
        prompt = self._generate_prompt(description, code, trimmed_trace)
        print(f"    ✓ 提示词长度: {len(prompt)} 字符")
        
        # 调用AI生成COT
        print(f"  [步骤3/3] 调用AI生成Natural COT...")
        cot = self._call_ai(prompt)
        
        if not cot:
            print(f"  ✗ 失败: AI生成COT失败")
            self.stats['failure'] += 1
            return False
        
        # 更新数据集
        case['task']['cot'] = cot
        self.stats['success'] += 1
        
        print(f"  ✓ 成功生成COT")
        print(f"    长度: {len(cot)} 字符")
        print(f"    预览: {cot[:100]}...")
        
        return True

    def process_all_cases(self, skip_existing=True):
        """
        批量处理所有cases
        
        Args:
            skip_existing: 是否跳过已有COT的cases
        """
        print(f"\n{'='*60}")
        print(f"开始批量生成Natural COT")
        print(f"总数: {len(self.dataset)} cases")
        print(f"并行数: {self.max_workers}")
        print(f"跳过已存在: {skip_existing}")
        print(f"{'='*60}\n")
        
        # 筛选需要处理的cases
        cases_to_process = []
        for case in self.dataset:
            if skip_existing and case['task'].get('cot') and case['task']['cot'].strip():
                continue
            cases_to_process.append(case)
        
        self.stats['total'] = len(cases_to_process)
        
        print(f"需要处理: {len(cases_to_process)} cases\n")
        
        if not cases_to_process:
            print("所有cases都已处理完成！")
            return
        
        # 并行处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            future_to_case = {
                executor.submit(self.process_single_case, case): case
                for case in cases_to_process
            }
            
            # 使用进度条显示处理进度
            with tqdm(total=len(cases_to_process), desc="总体进度") as pbar:
                for future in as_completed(future_to_case):
                    case = future_to_case[future]
                    try:
                        success = future.result()
                    except Exception as e:
                        print(f"\n处理异常 {case['id']}: {e}")
                        self.stats['failure'] += 1
                    
                    # 更新进度条
                    pbar.update(1)
                    pbar.set_postfix({
                        '成功': self.stats['success'],
                        '失败': self.stats['failure']
                    })
                    
                    # 定期保存（每10个case保存一次）
                    if (self.stats['success'] + self.stats['failure']) % 10 == 0:
                        self._save_dataset()
        
        # 最终保存
        self._save_dataset()
        
        # 打印统计信息
        print(f"\n{'='*60}")
        print(f"批量处理完成")
        print(f"{'='*60}")
        print(f"总计: {self.stats['total']} cases")
        print(f"成功: {self.stats['success']} cases")
        print(f"失败: {self.stats['failure']} cases")
        print(f"跳过: {self.stats['skipped']} cases")
        print(f"成功率: {self.stats['success']/max(self.stats['total'],1)*100:.1f}%")
        print(f"{'='*60}\n")

    def process_case_by_id(self, case_id):
        """
        处理指定ID的case
        
        Args:
            case_id: Case ID (如: SL-MIX-S0001)
        """
        for case in self.dataset:
            if case['id'] == case_id:
                success = self.process_single_case(case)
                if success:
                    self._save_dataset()
                return
        
        print(f"✗ Case {case_id} 不存在")
        print(f"可用的cases: {', '.join([c['id'] for c in self.dataset[:10]])}...")

def main():
    """主函数 - 示例用法"""
    import argparse
    parser = argparse.ArgumentParser(
        description='Natural COT Generator - 使用AI生成自然语言推理过程',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        示例用法:

        处理所有cases（跳过已有COT的）
        python natural_cot_generator.py --all

        处理所有cases（包括已有COT的）
        python natural_cot_generator.py --all --no-skip

        处理单个case
        python natural_cot_generator.py --case SL-MIX-S0001

        调整并行数
        python natural_cot_generator.py --all --workers 8

        使用不同的数据集文件
        python natural_cot_generator.py --dataset custom_data.json --all
        """
        )
    parser.add_argument(
        '--dataset',
        default='TreecEva_data_reduced_natural_cot.json',
        help='数据集JSON文件路径（默认: TreecEva_data_reduced_natural_cot.json）'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='处理所有cases'
    )

    parser.add_argument(
        '--case',
        type=str,
        help='处理指定的case ID（如: SL-MIX-S0001）'
    )

    parser.add_argument(
        '--no-skip',
        action='store_true',
        help='不跳过已有COT的cases（默认会跳过）'
    )

    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        help='并行处理的worker数量（默认: 4）'
    )

    args = parser.parse_args()

    # 检查参数
    if not args.all and not args.case:
        parser.print_help()
        print("\n错误: 必须指定 --all 或 --case")
        return

    # API配置 - 与 ai_analyzer.py 保持一致
    API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"
    BASE_URL = "https://llmapi.paratera.com/v1"

    api_config = {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3.2-Exp"
    }

    print(f"{'='*60}")
    print(f"Natural COT Generator")
    print(f"{'='*60}")
    print(f"数据集: {args.dataset}")
    print(f"AI模型: {api_config['model']}")
    print(f"并行数: {args.workers}")
    print(f"{'='*60}\n")

    # 创建生成器
    generator = NaturalCOTGenerator(
        args.dataset,
        api_config=api_config,
        max_workers=args.workers
    )

    # 执行处理
    if args.all:
        generator.process_all_cases(skip_existing=not args.no_skip)
    elif args.case:
        generator.process_case_by_id(args.case)

if __name__ == '__main__':
    main()