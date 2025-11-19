你好！我正在做一个处理代码推理数据集cot的框架。

我现在发现了一个比较严重的问题，即我在智能回溯与剪枝这一步，不太能很好的处理函数关系，导致最终cot的太长了

我似乎只会在主流程做智能剪枝，而函数不做任何剪枝全部进入了

我认为我需要对函数这种做合适的剪枝处理。

我们关心函数的输出，因此回溯整个函数，再做适当的剪枝，类似于主流程的思路，您觉得怎么样呢。

帮我实现一下这个逻辑吧！感恩

### 背景介绍

该框架构用于处理数据集“TreecEva_data_reduced_formated_cot.json”，其中一共有2025个数据，该框架由于在其中产生cot。

具体流程如下：

1. 目前分析case n
2. 调用AI，构建合适的提示词，并提供json中的description信息和code信息，让AI分析这个case的目标行和目标变量。并将所有case的target信息存在`all-target-info.json`中，和数据集json位于同一文件夹。
3. 分析第二步的目标行和目标变量是否分析与定位正确，如果不对则重新分析，最多分析三次。并将错误1、2、3次的case编号，存在attention.json中，和数据集json位于同一文件夹。（如：1：case1、case2；2：case7……）
4. 利用相关组件，对每个case进行分析，一样产出：trace_test.txt（完整追踪）、trimmed_trace_test.txt （剪枝后的追踪）、final_cot_test.txt（最终COT英文版）这三个文件。并将结果存储在`/temp_code/SL-MIX-Sn`中。
5. 将该case的cot信息整合进`TreecEva_data_reduced_formated_cot.json`中
6. 继续处理下一个case
7. 主函数有以下运行方式：a. 直接分析全部case，但跳过存在cot的 b. 直接分析某一个case 

### 处理思路流程

#### 步骤1: 代码执行追踪

**输入**: Python代码文件名(如 `test.py`)

**处理**: 使用 `auto_trace` 工具对代码进行插桩和执行追踪

**输出**: `trace_原文件名.txt`,格式为:

```json
{行号} {代码内容}
{行号} [{变量名列表}] [{变量值列表}]
```

每行代码执行后都会记录当前所有变量的状态,包括循环展开后的每次迭代。

---

#### 步骤2: 智能回溯与剪枝

**核心算法**: 从目标行号开始向上回溯,构建依赖图并剪除无关代码

**核心原则**: 每一行的变量列表必须包含**下一行计算所需的所有变量**,确保推理链的连续性和可计算性。

**剪枝规则**:

1. **依赖追踪与传播**:
   - 维护一个"关注变量集合",初始只包含目标变量
   - 遇到赋值语句 `a = b + c`,如果 `a` 在关注集合中,则将 `b` 和 `c` 加入集合
   - **关键**: 变量一旦进入关注集合,就要在所有后续行中保留其值,直到该变量被重新赋值或最终不再需要
   - 不在关注集合中的赋值语句直接删除
2. **控制流保留**:
   - 所有 `if`、`elif`、`else`、`for`、`while` 等控制流语句必须保留
   - 保留 `break`、`continue`、`return` 等流程控制语句
   - 保留函数定义和类定义(如果目标变量涉及)
3. **变量列表精简**:
   - 每行的变量列表只保留"当前关注变量集合"中的变量及其值
   - 保持变量名和值的对应关系
   - 确保下一行所需的所有变量都在当前行的变量列表中
4. **特殊情况处理**:
   - 函数调用: 如 `result = func(a, b)`,需追踪 `func` 和参数 `a, b`
   - 对象属性: 如 `obj.attr = value`,需追踪 `obj` 和 `value`
   - 多重赋值: 如 `a, b = 1, 2`,正确拆分依赖关系
   - 增强赋值: 如 `a += b`,等价于 `a = a + b`
   - 切片操作: 如 `lst[1:3]`,需追踪 `lst`
   - 推导式: 如 `[x*2 for x in lst]`,需追踪 `lst`

**输出**: `trimed_trace_原文件名.txt`,格式为:

```asciidoc
{目标行号}
{目标变量名}
---
{精简后的追踪记录}
```

---

#### 步骤3: 模板化COT生成

**输入**: `trimed_trace_原文件名.txt`

**处理**: 基于代码AST类型和变量值,使用预定义模板生成COT注释

**核心方法**: 模板匹配与参数填充(无需AI调用)

### 项目结构

```
项目目录/ 
├── config.py           	   					# 配置和模板
├── tracer.py          		   					# 代码追踪
├── pruner.py                  					# 依赖分析和剪枝
├── cot_generator.py           					# COT生成
├── main.py                    					# 主流程
├── TreecEva_data_reduced_formated_cot.json     # 数据集
├── all-target-info.json                     # 所有case的目标信息
├── attention.json                           # 错误重试记录
└── temp_code/                 # 数据集中可执行代码存储位置
    ├── SL-MIX-S0001.py
    ├── SL-MIX-S0001/
    │   ├── trace_SL-MIX-S0001.txt         # 完整追踪
    │   ├── trimmed_trace_SL-MIX-S0001.txt # 剪枝后的追踪
    │   └── final_cot_SL-MIX-S0001.txt     # 最终COT
    ├── SL-MIX-S0002.py
    ├── ...
    ├── SL-MIX-S2024.py
    └── SL-MIX-S2025.py
```

### 代码细节

#### ai_analyzer.py

```py
"""
AI分析器 - 用于自动识别目标行和目标变量
"""

import json
import re
import time
from openai import OpenAI
import httpx


class AIAnalyzer:
    """AI分析器，用于识别代码的目标行和目标变量"""
    
    def __init__(self, api_config, timeout=60, max_retries=3):
        """
        初始化AI分析器
        
        Args:
            api_config: API配置字典，包含 base_url, api_key, model
            timeout: 请求超时时间（秒）
            max_retries: 最大重试次数
        """
        http_client = httpx.Client(
            timeout=timeout,
            verify=False,
            follow_redirects=True
        )
        
        self.client = OpenAI(
            base_url=api_config['base_url'],
            api_key=api_config['api_key'],
            http_client=http_client
        )
        self.model = api_config['model']
        self.max_retries = max_retries
    
    def analyze_target(self, description, code, case_id):
        """
        分析代码的目标行和目标变量
        
        Args:
            description: 问题描述
            code: Python代码
            case_id: case的ID
            
        Returns:
            dict: {'target_line': int, 'target_var': str, 'confidence': str}
        """
        prompt = self._build_analysis_prompt(description, code)
        
        for retry in range(self.max_retries):
            try:
                print(f"    [API调用] 尝试 {retry + 1}/{self.max_retries}...")
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are an expert Python code analyzer. Your task is to identify the EXACT target line and target variable based on the problem description."
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    temperature=0.1,
                    max_tokens=500
                )
                
                result = response.choices[0].message.content.strip()
                print(f"    [API响应] 成功获取")
                return self._parse_ai_response(result, case_id, code)
                
            except Exception as e:
                error_msg = str(e)
                print(f"    [API错误] {error_msg}")
                
                if retry < self.max_retries - 1:
                    wait_time = 2 ** retry
                    print(f"    [等待] {wait_time}秒后重试...")
                    time.sleep(wait_time)
                else:
                    print(f"    [AI分析错误] Case {case_id}: {error_msg}")
                    return None
        
        return None
    
    def _build_analysis_prompt(self, description, code):
        """构建分析提示词"""
        # 给代码添加行号
        lines = code.split('\n')
        numbered_code = '\n'.join([f"{i+1:3d} | {line}" for i, line in enumerate(lines)])
        
        prompt = f"""Given the following problem description and Python code, identify:
1. The EXACT target line number (the line that computes or assigns the final answer)
2. The target variable name (the variable we need to track)

Problem Description:
{description}

Python Code with Line Numbers:
{numbered_code}

IMPORTANT RULES:
1. The target variable is usually explicitly mentioned in the description (like "value of variable 'result_value'")
2. The target line is the line where this variable gets its FINAL VALUE (last assignment)
3. If the description mentions a specific variable name, that MUST be the target variable
4. The target line should be BEFORE the print statement (if any)
5. Look for the LAST assignment to the target variable
6. Count line numbers EXACTLY as shown in the numbered code above

Example:
If description says "value of variable 'result_value'" and line 29 is "result_value = total_variance ^ product_count"
Then target_line should be 29 and target_var should be "result_value"

Please respond in the following JSON format ONLY (no other text):
{{
    "target_line": <exact_line_number>,
    "target_var": "<exact_variable_name>",
    "reasoning": "<brief explanation of why you chose this line and variable>"
}}
"""
        return prompt
    
    def _parse_ai_response(self, response, case_id, code):
        """解析AI响应"""
        try:
            # 尝试提取JSON
            json_match = re.search(r'\{[^{}]*\}', response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                
                # 验证必需字段
                if 'target_line' in result and 'target_var' in result:
                    target_line = int(result['target_line'])
                    target_var = str(result['target_var'])
                    
                    # 基本验证
                    if not self._quick_validate(code, target_line, target_var):
                        print(f"    [解析警告] AI响应未通过验证")
                        print(f"    [AI建议] Line {target_line}, Var '{target_var}'")
                        
                        # 尝试自动修正
                        corrected = self._try_auto_correct(code, target_var)
                        if corrected:
                            print(f"    [自动修正] Line {corrected['target_line']}, Var '{corrected['target_var']}'")
                            return corrected
                        
                        return None
                    
                    return {
                        'target_line': target_line,
                        'target_var': target_var,
                        'reasoning': result.get('reasoning', ''),
                        'confidence': 'high'
                    }
            
            print(f"    [解析警告] Case {case_id}: 无法解析AI响应")
            print(f"    [响应内容] {response[:200]}...")
            return None
            
        except Exception as e:
            print(f"    [解析错误] Case {case_id}: {e}")
            print(f"    [响应内容] {response[:200]}...")
            return None
    
    def _quick_validate(self, code, target_line, target_var):
        """快速验证目标信息"""
        lines = code.split('\n')
        
        # 检查行号范围
        if target_line < 1 or target_line > len(lines):
            return False
        
        # 检查变量是否在代码中
        if target_var not in code:
            return False
        
        # 检查目标行是否包含该变量的赋值
        target_line_code = lines[target_line - 1].strip()
        if not target_line_code or target_line_code.startswith('#'):
            return False
        
        # 检查该行是否对目标变量进行赋值
        if not re.search(rf'\b{re.escape(target_var)}\s*=', target_line_code):
            return False
        
        return True
    
    def _try_auto_correct(self, code, target_var):
        """尝试自动修正目标行"""
        lines = code.split('\n')
        
        # 查找所有对目标变量的赋值
        assignment_lines = []
        for i, line in enumerate(lines, 1):
            if re.search(rf'\b{re.escape(target_var)}\s*=', line):
                assignment_lines.append(i)
        
        if not assignment_lines:
            return None
        
        # 选择最后一个赋值行（在print之前）
        for line_num in reversed(assignment_lines):
            line_code = lines[line_num - 1].strip()
            # 确保不是在循环或条件语句的深层嵌套中
            if not line_code.startswith('print'):
                return {
                    'target_line': line_num,
                    'target_var': target_var,
                    'reasoning': 'Auto-corrected to last assignment before print',
                    'confidence': 'medium'
                }
        
        # 如果找不到，返回最后一个赋值
        return {
            'target_line': assignment_lines[-1],
            'target_var': target_var,
            'reasoning': 'Auto-corrected to last assignment',
            'confidence': 'low'
        }
    
    def validate_target(self, code, target_line, target_var):
        """
        验证目标行和变量是否合理
        
        Args:
            code: Python代码
            target_line: 目标行号
            target_var: 目标变量
            
        Returns:
            bool: 是否有效
        """
        return self._quick_validate(code, target_line, target_var)


class TargetValidator:
    """目标信息验证器"""
    
    @staticmethod
    def validate_by_execution(code_file, target_line, target_var):
        """通过执行代码验证目标信息"""
        try:
            import importlib.util
            import sys
            from io import StringIO
            
            spec = importlib.util.spec_from_file_location("test_module", code_file)
            module = importlib.util.module_from_spec(spec)
            
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            try:
                spec.loader.exec_module(module)
                
                if hasattr(module, target_var):
                    return True
                
            finally:
                sys.stdout = old_stdout
            
            return False
            
        except Exception as e:
            print(f"    [验证错误] 执行验证失败: {e}")
            return False
```

#### dataset_processor.py

```py
"""
数据集处理器 - 处理TreecEva数据集的COT生成
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time

from tracer import PythonTracer
from pruner import TracePruner
from cot_generator import COTGenerator
from ai_analyzer import AIAnalyzer, TargetValidator


class DatasetProcessor:
    """数据集处理器"""
    
    def __init__(self, dataset_path, api_config, max_workers=4):
        """
        初始化数据集处理器
        
        Args:
            dataset_path: 数据集JSON文件路径
            api_config: AI API配置
            max_workers: 最大并行工作数
        """
        self.dataset_path = Path(dataset_path)
        self.dataset_dir = self.dataset_path.parent
        self.temp_code_dir = self.dataset_dir / 'temp_code'
        
        self.all_target_info_path = self.dataset_dir / 'all-target-info.json'
        self.attention_path = self.dataset_dir / 'attention.json'
        
        self.ai_analyzer = AIAnalyzer(api_config)
        self.max_workers = max_workers
        
        # 加载数据集
        self.raw_dataset = self._load_dataset()
        self.dataset = self._extract_cases()
        
        # 加载已有的目标信息和错误记录
        self.all_target_info = self._load_all_target_info()
        self.attention_cases = self._load_attention()
    
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
        for i, item in enumerate(self.raw_dataset):
            if isinstance(item, dict) and 'id' in item:
                case_id = item['id']
                for case in self.dataset:
                    if case['id'] == case_id:
                        self.raw_dataset[i] = case
                        break
        
        with open(self.dataset_path, 'w', encoding='utf-8') as f:
            json.dump(self.raw_dataset, f, ensure_ascii=False, indent=2)
    
    def _load_all_target_info(self):
        """加载所有目标信息"""
        if self.all_target_info_path.exists():
            with open(self.all_target_info_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_all_target_info(self):
        """保存所有目标信息"""
        with open(self.all_target_info_path, 'w', encoding='utf-8') as f:
            json.dump(self.all_target_info, f, ensure_ascii=False, indent=2)
    
    def _load_attention(self):
        """加载错误记录"""
        if self.attention_path.exists():
            with open(self.attention_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'1': [], '2': [], '3': []}
    
    def _save_attention(self):
        """保存错误记录"""
        with open(self.attention_path, 'w', encoding='utf-8') as f:
            json.dump(self.attention_cases, f, ensure_ascii=False, indent=2)
    
    def analyze_target_with_retry(self, case, max_retries=3):
        """
        分析目标行和变量，支持重试
        
        Args:
            case: 数据集中的case
            max_retries: 最大重试次数
            
        Returns:
            dict: 目标信息 {'target_line': int, 'target_var': str}
        """
        case_id = case['id']
        description = case['task']['description']
        code = case['task']['code']
        
        for attempt in range(1, max_retries + 1):
            print(f"  [尝试 {attempt}/{max_retries}] 分析目标...")
            
            # AI分析
            result = self.ai_analyzer.analyze_target(description, code, case_id)
            
            if result is None:
                print(f"  ✗ AI分析失败")
                if attempt < max_retries:
                    time.sleep(1)
                continue
            
            target_line = result['target_line']
            target_var = result['target_var']
            
            # 验证
            if not self.ai_analyzer.validate_target(code, target_line, target_var):
                print(f"  ✗ 验证失败: 目标信息不合理")
                if attempt < max_retries:
                    time.sleep(1)
                    if str(attempt) not in self.attention_cases:
                        self.attention_cases[str(attempt)] = []
                    if case_id not in self.attention_cases[str(attempt)]:
                        self.attention_cases[str(attempt)].append(case_id)
                continue
            
            print(f"  ✓ 分析成功: line={target_line}, var={target_var}")
            print(f"    推理: {result.get('reasoning', '')}")
            return result
        
        # 所有尝试都失败
        print(f"  ✗ 所有尝试都失败")
        if str(max_retries) not in self.attention_cases:
            self.attention_cases[str(max_retries)] = []
        if case_id not in self.attention_cases[str(max_retries)]:
            self.attention_cases[str(max_retries)].append(case_id)
        
        return None
    
    def process_single_case(self, case):
        """
        处理单个case
        
        Args:
            case: 数据集中的case
            
        Returns:
            bool: 是否成功
        """
        case_id = case['id']
        print(f"\n{'='*60}")
        print(f"处理 Case: {case_id}")
        print(f"{'='*60}")
        
        # 检查是否已有COT
        if case['task'].get('cot') and case['task']['cot'].strip():
            print(f"  ⊙ 跳过: 已有COT")
            return True
        
        # 创建case目录
        case_dir = self.temp_code_dir / case_id
        case_dir.mkdir(parents=True, exist_ok=True)
        
        code_file = self.temp_code_dir / f"{case_id}.py"
        if not code_file.exists():
            print(f"  ✗ 错误: 代码文件不存在 {code_file}")
            return False
        
        # 步骤1: 分析目标（从统一的all-target-info.json读取或分析）
        if case_id in self.all_target_info:
            print(f"  ⊙ 使用已有的目标信息")
            target_info = self.all_target_info[case_id]
        else:
            print(f"  [步骤1/5] AI分析目标...")
            target_info = self.analyze_target_with_retry(case)
            
            if target_info is None:
                print(f"  ✗ 失败: 无法确定目标")
                return False
            
            # 保存到统一的all-target-info.json
            self.all_target_info[case_id] = target_info
            self._save_all_target_info()
            self._save_attention()
        
        target_line = target_info['target_line']
        target_var = target_info['target_var']
        
        # 步骤2: 代码追踪
        print(f"  [步骤2/5] 代码追踪...")
        trace_file = case_dir / f"trace_{case_id}.txt"
        try:
            PythonTracer.trace_file(str(code_file), str(trace_file))
            print(f"    ✓ 追踪完成")
        except Exception as e:
            print(f"    ✗ 追踪失败: {e}")
            return False
        
        # 步骤3: 智能剪枝
        print(f"  [步骤3/5] 智能剪枝...")
        pruned_file = case_dir / f"trimmed_trace_{case_id}.txt"
        try:
            TracePruner.prune_trace(
                str(trace_file),
                target_line,
                target_var,
                str(pruned_file),
                source_file=str(code_file)
            )
            print(f"    ✓ 剪枝完成")
        except Exception as e:
            print(f"    ✗ 剪枝失败: {e}")
            return False
        
        # 步骤4: 生成COT
        print(f"  [步骤4/5] 生成COT...")
        cot_file = case_dir / f"final_cot_{case_id}.txt"
        try:
            COTGenerator.generate_cot(str(pruned_file), str(cot_file), lang='en')
            print(f"    ✓ COT生成完成")
        except Exception as e:
            print(f"    ✗ COT生成失败: {e}")
            return False
        
        # 步骤5: 读取并整合COT到数据集
        print(f"  [步骤5/5] 整合COT到数据集...")
        try:
            with open(cot_file, 'r', encoding='utf-8') as f:
                cot_content = f.read()
            
            case['task']['cot'] = cot_content
            self._save_dataset()
            print(f"    ✓ 已整合到数据集")
        except Exception as e:
            print(f"    ✗ 整合失败: {e}")
            return False
        
        print(f"  ✓ Case {case_id} 处理完成")
        return True
    
    def process_all_cases(self, skip_existing=True):
        """处理所有cases"""
        print(f"\n{'='*60}")
        print(f"开始批量处理数据集")
        print(f"总数: {len(self.dataset)} cases")
        print(f"并行数: {self.max_workers}")
        print(f"{'='*60}\n")
        
        cases_to_process = []
        for case in self.dataset:
            if skip_existing and case['task'].get('cot') and case['task']['cot'].strip():
                continue
            cases_to_process.append(case)
        
        print(f"需要处理: {len(cases_to_process)} cases\n")
        
        if not cases_to_process:
            print("所有cases都已处理完成！")
            return
        
        success_count = 0
        failure_count = 0
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_case = {
                executor.submit(self.process_single_case, case): case
                for case in cases_to_process
            }
            
            with tqdm(total=len(cases_to_process), desc="处理进度") as pbar:
                for future in as_completed(future_to_case):
                    case = future_to_case[future]
                    try:
                        success = future.result()
                        if success:
                            success_count += 1
                        else:
                            failure_count += 1
                    except Exception as e:
                        print(f"\n处理异常 {case['id']}: {e}")
                        failure_count += 1
                    
                    pbar.update(1)
                    pbar.set_postfix({
                        '成功': success_count,
                        '失败': failure_count
                    })
        
        self._save_dataset()
        self._save_all_target_info()
        self._save_attention()
        
        print(f"\n{'='*60}")
        print(f"批量处理完成")
        print(f"成功: {success_count} cases")
        print(f"失败: {failure_count} cases")
        print(f"{'='*60}\n")
        
        if self.attention_cases and any(self.attention_cases.values()):
            print("错误重试统计:")
            for attempt, cases in self.attention_cases.items():
                if cases:
                    print(f"  第{attempt}次失败: {len(cases)} cases")
                    print(f"    {', '.join(cases[:10])}{'...' if len(cases) > 10 else ''}")
    
    def process_case_by_id(self, case_id):
        """处理指定ID的case"""
        for case in self.dataset:
            if case['id'] == case_id:
                success = self.process_single_case(case)
                if success:
                    self._save_dataset()
                    self._save_all_target_info()
                    self._save_attention()
                return
        
        print(f"✗ Case {case_id} 不存在")
        print(f"可用的cases: {', '.join([c['id'] for c in self.dataset[:10]])}...")
```

#### attribute_analyzer.py

```py
"""
属性访问分析器
用于识别代码中的属性访问模式，并指导对象的精简显示
"""

import ast
from typing import Set, Dict, List
import textwrap


class AttributePathCollector(ast.NodeVisitor):
    """收集代码中所有的属性访问路径"""
    
    def __init__(self):
        self.paths = set()  # 完整的属性路径，如 'student.score.math'
    
    def visit_Attribute(self, node):
        path = self._build_path(node)
        if path:
            self.paths.add(path)
            # 同时添加所有父路径
            parts = path.split('.')
            for i in range(1, len(parts)):
                parent_path = '.'.join(parts[:i])
                self.paths.add(parent_path)
        self.generic_visit(node)
    
    def _build_path(self, node):
        """构建属性访问路径"""
        parts = []
        current = node
        
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        
        if isinstance(current, ast.Name):
            parts.append(current.id)
            return '.'.join(reversed(parts))
        
        return None


def analyze_file_for_attribute_usage(filename):
    """分析整个文件，返回每个变量的属性使用映射
    
    Returns:
        {变量名: {使用的属性路径集合}}
        例如: {'student': {'student.score', 'student.score.math'}}
    """
    var_attr_map = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        
        tree = ast.parse(code)
        collector = AttributePathCollector()
        collector.visit(tree)
        
        # 组织成按变量分组的映射
        for path in collector.paths:
            root_var = path.split('.')[0]
            if root_var not in var_attr_map:
                var_attr_map[root_var] = set()
            var_attr_map[root_var].add(path)
        
    except Exception as e:
        print(f"[属性分析警告] 分析文件时出错: {e}")
    
    return var_attr_map


def analyze_lines_for_attribute_usage(filename, start_line, end_line=None):
    """分析指定行范围内的属性使用情况
    
    Args:
        filename: 源文件名
        start_line: 起始行号（包含）
        end_line: 结束行号（包含），None表示到文件末尾
    
    Returns:
        {变量名: {使用的属性路径集合}}
    """
    var_attr_map = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 提取指定范围的代码
        if end_line is None:
            end_line = len(lines)
        
        # 注意：行号从1开始，列表索引从0开始
        relevant_lines = lines[start_line - 1:end_line]
        code_segment = ''.join(relevant_lines)
        
        if not code_segment.strip():
            return var_attr_map
        
        # 去除缩进，使代码可以被解析
        code_segment = textwrap.dedent(code_segment)
        
        # 解析代码段
        tree = ast.parse(code_segment)
        collector = AttributePathCollector()
        collector.visit(tree)
        
        # 组织成按变量分组的映射
        for path in collector.paths:
            root_var = path.split('.')[0]
            if root_var not in var_attr_map:
                var_attr_map[root_var] = set()
            var_attr_map[root_var].add(path)
        
    except Exception as e:
        # 静默失败，不影响主流程
        pass
    
    return var_attr_map


def get_required_attributes_for_var(var_name, attr_paths):
    """提取变量需要显示的属性
    
    Args:
        var_name: 变量名
        attr_paths: 该变量相关的所有属性路径
    
    Returns:
        需要显示的直接属性集合，例如 {'age', 'company'}
    """
    required = set()
    
    for path in attr_paths:
        parts = path.split('.')
        if parts[0] != var_name:
            continue
        
        if len(parts) > 1:
            # 第一级属性
            required.add(parts[1])
    
    return required


class SmartObjectFormatter:
    """智能对象格式化器 - 只显示用到的属性"""
    
    def __init__(self, var_name, used_paths, depth_limit=3):
        """
        Args:
            var_name: 变量名
            used_paths: 该变量的属性使用路径集合
            depth_limit: 深度限制
        """
        self.var_name = var_name
        self.used_paths = used_paths or set()
        self.depth_limit = depth_limit
        
        # 解析出需要显示的属性结构
        self.required_attrs = self._parse_required_attrs()
    
    def _parse_required_attrs(self):
        """解析需要显示的属性结构
        
        Returns:
            {属性名: 子属性字典}
        """
        attrs = {}
        
        for path in self.used_paths:
            parts = path.split('.')
            if parts[0] != self.var_name:
                continue
            
            if len(parts) == 1:
                # 只是变量本身，不是属性访问
                continue
            
            # 构建树结构
            current = attrs
            for part in parts[1:]:
                if part not in current:
                    current[part] = {}
                current = current[part]
        
        return attrs
    
    def format(self, obj, depth=0):
        """格式化对象"""
        if depth > self.depth_limit:
            return "..."
        
        # 基础类型直接返回
        if isinstance(obj, str):
            return f"'{obj}'"
        elif isinstance(obj, (int, float, bool)):
            return str(obj)
        elif obj is None:
            return "None"
        elif isinstance(obj, (list, tuple)):
            return self._format_sequence(obj, depth)
        elif isinstance(obj, dict):
            return self._format_dict(obj, depth)
        elif hasattr(obj, '__dict__'):
            # 自定义对象
            return self._format_custom_object(obj, depth)
        else:
            return str(obj)
    
    def _format_custom_object(self, obj, depth):
        """格式化自定义对象"""
        class_name = type(obj).__name__
        
        if not self.required_attrs:
            # 没有属性被使用，显示简化形式
            return f"{class_name}(...)"
        
        # 只显示需要的属性
        parts = []
        for attr_name in sorted(self.required_attrs.keys()):  # 排序以保证稳定输出
            if hasattr(obj, attr_name):
                attr_value = getattr(obj, attr_name)
                
                # 递归格式化属性值
                sub_required = self.required_attrs[attr_name]
                if sub_required and hasattr(attr_value, '__dict__'):
                    # 子对象也需要精简
                    sub_formatter = SmartObjectFormatter(
                        attr_name, 
                        self._get_sub_paths(attr_name),
                        self.depth_limit
                    )
                    formatted_value = sub_formatter.format(attr_value, depth + 1)
                else:
                    formatted_value = self._basic_format(attr_value, depth + 1)
                
                parts.append(f"{attr_name}={formatted_value}")
        
        if not parts:
            return f"{class_name}(...)"
        
        return f"{class_name}({', '.join(parts)})"
    
    def _get_sub_paths(self, attr_name):
        """获取子属性的路径集合"""
        sub_paths = set()
        prefix = f"{self.var_name}.{attr_name}."
        
        for path in self.used_paths:
            if path.startswith(prefix):
                # 转换为相对路径
                sub_path = attr_name + path[len(self.var_name + '.' + attr_name):]
                sub_paths.add(sub_path)
        
        return sub_paths
    
    def _basic_format(self, value, depth):
        """基础格式化"""
        if depth > self.depth_limit:
            return "..."
        
        if isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, (int, float, bool)):
            return str(value)
        elif isinstance(value, list):
            if not value or depth >= self.depth_limit - 1:
                return f"[...{len(value)} items]" if value else "[]"
            items = [self._basic_format(v, depth + 1) for v in value[:3]]
            suffix = ", ..." if len(value) > 3 else ""
            return f"[{', '.join(items)}{suffix}]"
        elif isinstance(value, dict):
            if not value or depth >= self.depth_limit - 1:
                return f"{{...{len(value)} items}}" if value else "{}"
            return "{...}"
        elif hasattr(value, '__dict__'):
            return f"{type(value).__name__}(...)"
        else:
            return str(value)
    
    def _format_sequence(self, seq, depth):
        """格式化序列"""
        if not seq:
            return "[]" if isinstance(seq, list) else "()"
        
        if depth >= self.depth_limit - 1:
            bracket = ("[", "]") if isinstance(seq, list) else ("(", ")")
            return f"{bracket[0]}...{len(seq)} items{bracket[1]}"
        
        items = [self._basic_format(item, depth + 1) for item in seq[:5]]
        if len(seq) > 5:
            items.append("...")
        
        if isinstance(seq, list):
            return f"[{', '.join(items)}]"
        else:
            return f"({', '.join(items)})"
    
    def _format_dict(self, d, depth):
        """格式化字典"""
        if not d:
            return "{}"
        
        if depth >= self.depth_limit - 1:
            return f"{{...{len(d)} items}}"
        
        items = []
        for i, (k, v) in enumerate(d.items()):
            if i >= 3:
                items.append("...")
                break
            items.append(f"{self._basic_format(k, depth+1)}: {self._basic_format(v, depth+1)}")
        
        return f"{{{', '.join(items)}}}"
```

#### config.py

```py
"""
配置文件和COT模板定义 - 增强版行内注释 (中英双语) + 函数调用支持
"""

# -----------------------------------------------------------------
# 英文COT模板 (EN)
# -----------------------------------------------------------------

HEADER_TEMPLATES_EN = "Target: Find the value of variable {target_var} after [line {target_line}] executes\n"
FOOTER_TEMPLATES_EN = "\nAnswer: {target_var} = {final_value} (last updated on {source_info})"
VAR_SOURCE_TEMPLATES_EN = "defined at [line {def_line}]"
VAR_SOURCE_UNKNOWN_EN = "an unknown source"

INLINE_COT_TEMPLATES_EN = {
    'assign_constant': {
        'template': "  # Assign: {var} = {value}",
    },
    'assign_expr': {
        'template': "  # Compute: {expr_detail} = {result}",
    },
    'aug_assign': {
        'template': "  ## Update: {var} changed from {old_val} (defined at {def_line}) to {old_val}{op}{operand} = {result}",
    },
    'for_start': {
        'template': "  # Loop Start: {iter_var} takes its first value {iter_val}",
    },
    'for_continue': {
        'template': "  # Loop Iteration: {iter_var} is now {iter_val} (iteration {iter_count})",
    },
    'for_end': {
        'template': "  # Loop End: Iteration finished",
    },
    'while_start': {
        'template': "  # while Loop Start: Condition is true",
    },
    'while_continue': {
        'template': "  # while Loop Iteration: Condition is still true",
    },
    'while_end': {
        'template': "  # while Loop End: Condition is false",
    },
    'if_true': {
        'template': "  # Condition: True, entering 'if' block",
    },
    'if_false': {
        'template': "  # Condition: False, skipping 'if' block",
    },
    'else': {
        'template': "  # Entering 'else' block",
    },
    'elif_true': {
        'template': "  # 'elif' Condition: True, entering block",
    },
    'elif_false': {
        'template': "  # 'elif' Condition: False, checking next",
    },
    'return': {
        'template': "  # Return: {value}",
    },
    'function_def': {
        'template': "  # Define function: {func_name}",
    },
    'function_call': {
        'template': "  # Call function {func_name}({params})",
    },
    'function_enter': {
        'template': "  # Enter function {func_name}: {params}",
    },
    'function_return': {
        'template': "  # Function {func_name} returns {value}",
    },
    'print_statement': {
        'template': "  # Output: {print_content}",
    },
}

# -----------------------------------------------------------------
# 中文COT模板 (ZH)
# -----------------------------------------------------------------

HEADER_TEMPLATES_ZH = "目标: 求[第{target_line}行]执行后变量 {target_var} 的值\n"
FOOTER_TEMPLATES_ZH = "\n答案: {target_var} = {final_value} (最后在{source_info}更新)"
VAR_SOURCE_TEMPLATES_ZH = "[第{def_line}行]"
VAR_SOURCE_UNKNOWN_ZH = "未知来源"

INLINE_COT_TEMPLATES_ZH = {
    'assign_constant': {
        'template': "  # 赋值: {var} = {value}",
    },
    'assign_expr': {
        'template': "  # 计算: {expr_detail} = {result}",
    },
    'aug_assign': {
        'template': "  # 更新: {var} 从{def_line}的 {old_val} 变为 {old_val}{op}{operand} = {result}",
    },
    'for_start': {
        'template': "  # 开始循环: {iter_var} 取第一个值 {iter_val}",
    },
    'for_continue': {
        'template': "  # 继续循环: {iter_var} 取下一个值 {iter_val} (第{iter_count}次)",
    },
    'for_end': {
        'template': "  # 循环结束: 已遍历完所有元素",
    },
    'while_start': {
        'template': "  # while循环开始: 条件为真",
    },
    'while_continue': {
        'template': "  # while循环继续: 条件仍为真",
    },
    'while_end': {
        'template': "  # while循环结束: 条件为假",
    },
    'if_true': {
        'template': "  # 条件判断: 为真，进入if分支",
    },
    'if_false': {
        'template': "  # 条件判断: 为假，跳过if分支",
    },
    'else': {
        'template': "  # 进入else分支",
    },
    'elif_true': {
        'template': "  # elif条件: 为真,进入该分支",
    },
    'elif_false': {
        'template': "  # elif条件: 为假，继续检查",
    },
    'return': {
        'template': "  # 返回: {value}",
    },
    'function_def': {
        'template': "  # 定义函数: {func_name}",
    },
    'function_call': {
        'template': "  # 调用函数 {func_name}({params})",
    },
    'function_enter': {
        'template': "  # 进入函数 {func_name}: {params}",
    },
    'function_return': {
        'template': "  # 函数 {func_name} 返回 {value}",
    },
    'print_statement': {
        'template': "  # 输出: {print_content}",
    },
}

# -----------------------------------------------------------------
# 模板选择器
# -----------------------------------------------------------------

TEMPLATES = {
    'en': {
        'header': HEADER_TEMPLATES_EN,
        'footer': FOOTER_TEMPLATES_EN,
        'var_source': VAR_SOURCE_TEMPLATES_EN,
        'var_unknown': VAR_SOURCE_UNKNOWN_EN,
        'inline': INLINE_COT_TEMPLATES_EN,
    },
    'zh': {
        'header': HEADER_TEMPLATES_ZH,
        'footer': FOOTER_TEMPLATES_ZH,
        'var_source': VAR_SOURCE_TEMPLATES_ZH,
        'var_unknown': VAR_SOURCE_UNKNOWN_ZH,
        'inline': INLINE_COT_TEMPLATES_ZH,
    }
}
```

#### cot_generator.py

```py
"""
基于行内注释的COT生成器 - 增强函数调用支持（完整修复版）
"""

import ast
import re
from config import TEMPLATES


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}
        self.loop_body_lines = {}
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        if line.is_function_enter:
            return 'function_enter'
        if line.is_function_return:
            return 'function_return'
        
        code = line.code.strip()
        lineno = line.lineno
        
        if code.startswith('print('):
            return 'print_statement'
        
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                self.loop_body_lines[lineno] = set()
                if next_line and not next_line.is_function_enter and not next_line.is_function_return and next_line.lineno > lineno:
                    self.loop_body_lines[lineno].add(next_line.lineno)
                return 'for_start'
            else:
                self.loop_counters[lineno] += 1
                
                if next_line and not next_line.is_function_enter and not next_line.is_function_return:
                    next_lineno = next_line.lineno
                    if next_lineno in self.loop_body_lines.get(lineno, set()):
                        return 'for_continue'
                    else:
                        return 'for_end'
                else:
                    return 'for_end'
        
        if prev_line and not prev_line.is_function_enter and not prev_line.is_function_return and prev_line.code.strip().startswith('for '):
            prev_lineno = prev_line.lineno
            if prev_lineno in self.loop_body_lines and lineno > prev_lineno:
                self.loop_body_lines[prev_lineno].add(lineno)
        
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and not next_line.is_function_enter and not next_line.is_function_return and next_line.lineno > lineno:
                    return 'while_continue'
                else:
                    return 'while_end'
        
        if code.startswith('if '):
            return 'if_true'
        if code.startswith('elif '):
            return 'elif_true'
        if code.startswith('else:'):
            return 'else'
        if code.startswith('return'):
            return 'return'
        if code.startswith('def '):
            return 'function_def'
        
        if '=' in code and not code.startswith('='):
            if re.search(r'\w+\s*\+=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*-=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*\*=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*/=\s*', code):
                return 'aug_assign'
            
            match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$', code)
            if match:
                return 'aug_assign'
            
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        if isinstance(node.value, ast.Call):
                            return 'function_call'
                        if isinstance(node.value, (ast.Constant, ast.Num, ast.Str)):
                            return 'assign_constant'
                        else:
                            return 'assign_expr'
            except:
                if re.match(r'^\s*\w+\s*=\s*[\d\'"]+\s*$', code):
                    return 'assign_constant'
                else:
                    return 'assign_expr'
        
        return 'unknown'


class VariableTracker:
    """变量来源追踪器 - 支持函数上下文"""
    
    def __init__(self, lang='en'):
        self.var_definitions = {}  # {var_name: lineno}
        self.var_history = {}
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.function_contexts = []  # 函数调用栈
        self.param_sources = {}  # 参数来源映射 {param_name: {'actual_var': xxx, 'def_line': xxx}}
    
    def enter_function(self, func_name, param_mapping):
        """进入函数，建立参数映射"""
        context = {
            'func_name': func_name,
            'param_mapping': param_mapping.copy(),
            'local_vars': {}
        }
        self.function_contexts.append(context)
        
        # 更新参数来源
        for param, info in param_mapping.items():
            actual_var = info.get('actual_var', param)
            # 查找实参的定义行
            def_line = self.var_definitions.get(actual_var)
            self.param_sources[param] = {
                'actual_var': actual_var,
                'def_line': def_line
            }
    
    def exit_function(self):
        """退出函数"""
        if self.function_contexts:
            self.function_contexts.pop()
        
        # 清理参数来源，恢复上层函数的参数
        self.param_sources = {}
        if self.function_contexts:
            current_context = self.function_contexts[-1]
            for param, info in current_context.get('param_mapping', {}).items():
                actual_var = info.get('actual_var', param)
                def_line = self.var_definitions.get(actual_var)
                self.param_sources[param] = {
                    'actual_var': actual_var,
                    'def_line': def_line
                }
    
    def update_var(self, var_name, lineno, value):
        """更新变量定义"""
        self.var_definitions[var_name] = lineno
        if var_name not in self.var_history:
            self.var_history[var_name] = []
        self.var_history[var_name].append((lineno, value))
        
        # 如果在函数内，也记录到函数上下文
        if self.function_contexts:
            self.function_contexts[-1]['local_vars'][var_name] = lineno
    
    def get_def_line(self, var_name):
        """获取变量最后定义的行号"""
        return self.var_definitions.get(var_name)
    
    def get_var_source_info(self, var_name):
        """获取变量来源信息"""
        # 检查是否是函数参数
        if var_name in self.param_sources:
            param_info = self.param_sources[var_name]
            actual_var = param_info.get('actual_var', var_name)
            def_line = param_info.get('def_line')
            
            if def_line:
                if self.lang == 'en':
                    return f"parameter {var_name} defined at [line {def_line}]"
                else:
                    return f"参数 {var_name} 定义于 [第{def_line}行]"
            else:
                if self.lang == 'en':
                    return f"parameter {var_name}"
                else:
                    return f"参数 {var_name}"
        
        # 普通变量
        def_line = self.var_definitions.get(var_name)
        if def_line:
            return self.templates['var_source'].format(def_line=def_line)
        return self.templates['var_unknown']


class ParameterExtractor:
    """参数提取器"""
    
    def __init__(self, var_tracker, lang='en'):
        self.var_tracker = var_tracker
        self.lang = lang
    
    def extract(self, line, line_type, classifier, prev_var_dict=None, call_line_info=None):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip() if not line.is_function_enter and not line.is_function_return else '',
        }
        
        var_dict = line.get_var_dict()
        
        # 函数进入
        if line_type == 'function_enter':
            params['func_name'] = line.func_name
            param_strs = []
            
            # 使用参数映射来显示来源
            if line.param_mapping:
                for param_name in line.var_names:
                    # 格式化参数值
                    idx = line.var_names.index(param_name)
                    if idx < len(line.var_values):
                        param_value_raw = line.var_values[idx]
                        # 格式化值
                        from pruner import ValueFormatter
                        param_value = ValueFormatter.format(param_value_raw)
                    else:
                        param_value = '?'
                    
                    if param_name in line.param_mapping:
                        mapping_info = line.param_mapping[param_name]
                        actual_var = mapping_info.get('actual_var', param_name)
                        
                        # 查找实参的定义行
                        def_line = self.var_tracker.get_def_line(actual_var)
                        if def_line:
                            if self.lang == 'en':
                                source_info = f"defined at [line {def_line}]"  # 修改此行
                                param_strs.append(f"{param_name}={param_value} ({actual_var} {source_info})")  # 修改格式
                            else:
                                source_info = f"[第{def_line}行]"
                                param_strs.append(f"{param_name}={param_value} (来自{actual_var}在{source_info})")
                        else:
                            param_strs.append(f"{param_name}={param_value}")
                    else:
                        param_strs.append(f"{param_name}={param_value}")
            else:
                # 无映射信息，只显示格式化的值
                for name in line.var_names:
                    idx = line.var_names.index(name)
                    if idx < len(line.var_values):
                        from pruner import ValueFormatter
                        value = ValueFormatter.format(line.var_values[idx])
                    else:
                        value = '?'
                    param_strs.append(f"{name}={value}")
            
            params['params'] = ', '.join(param_strs) if param_strs else 'no parameters'
            return params
        
        # 函数返回
        if line_type == 'function_return':
            params['func_name'] = line.func_name
            from pruner import ValueFormatter
            params['value'] = ValueFormatter.format(line.return_value)
            return params
        
        # Print语句
        if line_type == 'print_statement':
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                if print_arg in var_dict:
                    source = self.var_tracker.get_var_source_info(print_arg)
                    params['print_content'] = f"{print_arg}={var_dict[print_arg]} ({source})"
                else:
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign', 'function_call']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 函数调用赋值
        if line_type == 'function_call':
            match = re.match(r'\s*(\w+)\s*=\s*(\w+)\((.*)\)', line.code)
            if match:
                var_name = match.group(1)
                func_name = match.group(2)
                args_str = match.group(3)
                
                params['var'] = var_name
                params['func_name'] = func_name
                params['value'] = var_dict.get(var_name, '?')
                params['result'] = params['value']
                
                # 解析参数
                arg_details = []
                if args_str:
                    args = [a.strip() for a in args_str.split(',')]
                    for arg in args:
                        if arg in var_dict or (prev_var_dict and arg in prev_var_dict):
                            val = var_dict.get(arg) or prev_var_dict.get(arg)
                            source = self.var_tracker.get_var_source_info(arg)
                            arg_details.append(f"{arg}={val} ({source})")
                        else:
                            arg_details.append(arg)
                
                params['params'] = ', '.join(arg_details) if arg_details else ''
                
                self.var_tracker.update_var(var_name, line.lineno, params['value'])
        
        # 表达式展开
        if line_type == 'assign_expr':
            params['expr_detail'] = self._expand_expression_with_source(
                line.code, var_dict, prev_var_dict
            )
            if 'var' in params and params['value'] == '?':
                parts = line.code.split('=', 1)
                if len(parts) == 2:
                    expr = parts[1].strip()
                    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', expr):
                        if expr in var_dict:
                            params['value'] = var_dict[expr]
                            params['result'] = params['value']
                        elif prev_var_dict and expr in prev_var_dict:
                            params['value'] = prev_var_dict[expr]
                            params['result'] = params['value']
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 常量赋值
        if line_type == 'assign_constant':
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params.get('var')
            
            if '+=' in line.code:
                params['op'] = '+'
                parts = line.code.split('+=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '-=' in line.code:
                params['op'] = '-'
                parts = line.code.split('-=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '*=' in line.code:
                params['op'] = '*'
                parts = line.code.split('*=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '/=' in line.code:
                params['op'] = '/'
                parts = line.code.split('/=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            else:
                match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(.+)$', line.code)
                if match:
                    params['op'] = match.group(2)
                    operand_expr = match.group(3).strip()
                else:
                    params['op'] = '?'
                    operand_expr = '?'
            
            params['operand'] = operand_expr
            
            if var and prev_var_dict:
                params['old_val'] = prev_var_dict.get(var, '?')
                params['def_line'] = self.var_tracker.get_var_source_info(var)
            else:
                params['old_val'] = '?'
                params['def_line'] = '?'
            
            if var:
                self.var_tracker.update_var(var, line.lineno, params['value'])
        
        # For循环
        if line_type.startswith('for'):
            match = re.match(r'for\s+(\w+)\s+in\s+(.+):', line.code)
            if match:
                iter_var = match.group(1)
                iter_source = match.group(2).strip()
                params['iter_var'] = iter_var
                params['iter_val'] = var_dict.get(iter_var, '?')
                params['iter_count'] = classifier.loop_counters.get(line.lineno, 1)
                params['iter_source'] = iter_source

                if iter_var in var_dict:
                    self.var_tracker.update_var(iter_var, line.lineno, var_dict[iter_var])
        
        # While循环
        if line_type.startswith('while'):
            params['condition'] = line.code.replace('while', '').replace(':', '').strip()
        
        # Return语句
        if line_type == 'return':
            return_val = line.code.replace('return', '').strip()
            if return_val in var_dict:
                source = self.var_tracker.get_var_source_info(return_val)
                params['value'] = f"{return_val}={var_dict[return_val]} ({source})"
            else:
                params['value'] = return_val
        
        # 函数定义
        if line_type == 'function_def':
            match = re.match(r'def\s+(\w+)', line.code)
            if match:
                params['func_name'] = match.group(1)
        
        return params
    
    def _extract_lvalue(self, code):
        """提取左值"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    targets = []
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            targets.append(target.id)
                    return targets
                elif isinstance(node, ast.AugAssign):
                    if isinstance(node.target, ast.Name):
                        return [node.target.id]
        except:
            pass
        
        match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]=', code)
        if match:
            return [match.group(1)]
        
        return []
    
    def _expand_expression_with_source(self, code, var_dict, prev_var_dict=None):
        """展开表达式，显示每个变量的值和来源"""
        parts = code.split('=', 1)
        if len(parts) < 2:
            return code
        
        left_part = parts[0].strip()
        expr = parts[1].strip()
        
        lvalues = self._extract_lvalue(code)
        lvalue_set = set(lvalues)
        
        var_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        variables = re.findall(var_pattern, expr)
        
        var_details = []
        unique_vars = set()
        
        for var in variables:
            if var in ['range', 'len', 'sum', 'max', 'min', 'int', 'str', 'list', 'dict', 'True', 'False', 'None'] or var in unique_vars:
                continue
            unique_vars.add(var)
            
            if var in lvalue_set:
                if prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
            else:
                if var in var_dict:
                    val = var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
                elif prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
        
        if var_details:
            detail_str = f", where {', '.join(var_details)}" if self.lang == 'en' else f", 其中 {', '.join(var_details)}"
            return f"{expr}{detail_str}"
        else:
            return expr


class COTGenerator:
    """行内注释式COT生成器 - 支持函数调用"""
    
    def __init__(self, pruned_file, lang='en'):
        self.pruned_file = pruned_file
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.target_line = None
        self.target_var = None
        self.lines = []
        self.var_tracker = VariableTracker(lang=self.lang)
        self.return_values = {}  # 记录函数返回值 {func_call_line: return_value}
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        from pruner import TraceLine
        i = 3
        param_mapping = {}
        current_call_line = None  # 记录当前函数调用所在行
        
        while i < len(content):
            line = content[i].strip()
            if not line:
                i += 1
                continue
            
            # 读取参数映射（应该在FUNCTION_ENTER之前）
            if line.startswith('PARAM_MAPPING'):
                parts = line.split(' ', 1)
                if len(parts) >= 2:
                    try:
                        param_mapping = eval(parts[1])
                    except:
                        param_mapping = {}
                i += 1
                continue
            
            # 函数进入
            if line.startswith('FUNCTION_ENTER'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    code = parts[3]
                    
                    var_names = []
                    var_values = []
                    if i + 1 < len(content):
                        next_line = content[i + 1].strip()
                        if next_line.startswith(str(lineno) + ' ['):
                            try:
                                parts = next_line.split(' ', 1)
                                if len(parts) > 1:
                                    var_data = parts[1]
                                    var_names, var_values = self._parse_var_lists(var_data)
                                i += 1
                            except:
                                pass
                    
                    trace_line = TraceLine(lineno, code, var_names, var_values,
                                         is_function_enter=True, func_name=func_name,
                                         param_mapping=param_mapping.copy())
                    self.lines.append(trace_line)
                    param_mapping = {}
                    i += 1
                    continue
            
            # 函数返回
            if line.startswith('FUNCTION_RETURN'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    return_value_str = parts[3]
                    try:
                        return_value = eval(return_value_str)
                    except:
                        return_value = return_value_str
                    
                    # 记录返回值（关联到调用行）
                    if current_call_line:
                        from pruner import ValueFormatter
                        self.return_values[current_call_line] = ValueFormatter.format(return_value)
                        current_call_line = None
                    
                    trace_line = TraceLine(lineno, '', [], [],
                                         is_function_return=True,
                                         func_name=func_name,
                                         return_value=return_value)
                    self.lines.append(trace_line)
                    i += 1
                    continue
            
            parts = line.split(' ', 1)
            if len(parts) < 2:
                i += 1
                continue
            
            lineno = int(parts[0])
            code = parts[1]
            
            # 检查是否是函数调用行
            if '=' in code and '(' in code:
                try:
                    tree = ast.parse(code)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                            current_call_line = lineno
                            break
                except:
                    pass
            
            var_names = []
            var_values = []
            if i + 1 < len(content):
                next_line = content[i + 1].strip()
                if next_line.startswith(str(lineno) + ' ['):
                    try:
                        parts = next_line.split(' ', 1)
                        if len(parts) > 1:
                            var_data = parts[1]
                            var_names, var_values = self._parse_var_lists(var_data)
                        i += 1
                    except:
                        pass
            
            trace_line = TraceLine(lineno, code, var_names, var_values)
            self.lines.append(trace_line)
            i += 1
    
    def _parse_var_lists(self, var_data):
        """解析变量列表"""
        try:
            parts = var_data.split('] [')
            if len(parts) == 2:
                names_str = parts[0] + ']'
                values_str = '[' + parts[1]
                names = eval(names_str)
                values = eval(values_str)
                return names, values
        except:
            pass
        return [], []
    
    def generate(self):
        """生成行内注释式COT（支持函数调用）"""
        
        # 预计算循环总数
        total_counts = {}
        dry_classifier = CodeClassifier()
        prev_line = None
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            dry_classifier.classify(line, prev_line, next_line)
            prev_line = line
        total_counts = dry_classifier.loop_counters

        # 实际生成
        classifier = CodeClassifier()
        extractor = ParameterExtractor(self.var_tracker, lang=self.lang)
        
        output_lines = []
        header_template = self.templates['header']
        footer_template = self.templates['footer']
        inline_templates = self.templates['inline']
        
        output_lines.append(header_template.format(
            target_line=self.target_line, 
            target_var=self.target_var
        ))
        
        prev_var_dict = {}
        prev_line_obj = None
        
        current_loop_header = None
        loop_skip_state = {}
        function_depth = 0

        LOOP_SUMMARY_THRESHOLD = 5
        SKIP_AFTER_ITER = 2
        RESUME_BEFORE_ITER = 2
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            line_type = classifier.classify(line, prev_line_obj, next_line)
            
            # 处理函数进入
            if line_type == 'function_enter':
                function_depth += 1
                indent = "  " * (function_depth - 1)
                
                # 建立参数映射到变量追踪器
                self.var_tracker.enter_function(line.func_name, line.param_mapping)
                
                params = extractor.extract(line, line_type, classifier, prev_var_dict)
                template_info = inline_templates.get(line_type)
                
                if template_info:
                    comment_text = template_info['template'].format(**params)
                    comment_text = comment_text.lstrip().lstrip('#').lstrip()
                    
                    if self.lang == 'zh':
                        code_line = f"{indent}[第{line.lineno}行]  {line.code}"
                        explain_line = f"{indent}{comment_text}"
                    else:
                        code_line = f"{indent}[line {line.lineno}]  {line.code}"
                        explain_line = f"{indent}{comment_text}"

                    output_lines.append(code_line)
                    if comment_text:
                        output_lines.append(explain_line)
                
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # 处理函数返回
            if line_type == 'function_return':
                indent = "  " * (function_depth - 1)
                
                params = extractor.extract(line, line_type, classifier, prev_var_dict)
                template_info = inline_templates.get(line_type)
                
                if template_info:
                    comment_text = template_info['template'].format(**params)
                    comment_text = comment_text.lstrip().lstrip('#').lstrip()
                    
                    if self.lang == 'zh':
                        explain_line = f"{indent}{comment_text}"
                    else:
                        explain_line = f"{indent}{comment_text}"
                    
                    output_lines.append(explain_line)
                
                # 退出函数上下文
                self.var_tracker.exit_function()
                
                function_depth = max(0, function_depth - 1)
                prev_line_obj = line
                continue
            
            # 循环总结逻辑
            if line_type in ('for_start', 'while_start'):
                current_loop_header = line.lineno
                loop_skip_state[current_loop_header] = False
            
            if current_loop_header:
                total_iter = total_counts.get(current_loop_header, 0)
                current_iter = classifier.loop_counters.get(current_loop_header, 0)
                
                START_SKIP_ITER = SKIP_AFTER_ITER + 1
                RESUME_ITER = total_iter - RESUME_BEFORE_ITER + 1

                is_summarizable = total_iter > LOOP_SUMMARY_THRESHOLD
                
                if is_summarizable:
                    if current_iter == START_SKIP_ITER:
                        num_skipped = total_iter - SKIP_AFTER_ITER - RESUME_BEFORE_ITER
                        summary_template = {
                            'en': f"\n... [Line {current_loop_header}] repeats {num_skipped} more times ...\n",
                            'zh': f"\n... [第{current_loop_header}行] 额外循环了 {num_skipped} 次 ...\n"
                        }
                        output_lines.append(summary_template[self.lang].strip()) 
                        loop_skip_state[current_loop_header] = True
                    
                    elif current_iter == RESUME_ITER:
                        loop_skip_state[current_loop_header] = False
                
                if loop_skip_state.get(current_loop_header, False):
                    prev_var_dict = line.get_var_dict()
                    prev_line_obj = line
                    if line_type in ('for_end', 'while_end'):
                        current_loop_header = None
                    continue

            if line_type == 'unknown':
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # 提取参数 - 在这里提前更新var_tracker（针对主流程变量）
            params = extractor.extract(line, line_type, classifier, prev_var_dict)
            
            template_info = inline_templates.get(line_type)
            if not template_info:
                # 即使没有模板，也要更新变量定义
                if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
                    lvalues = extractor._extract_lvalue(line.code)
                    if lvalues:
                        var_name = lvalues[0]
                        var_value = line.get_var_dict().get(var_name, '?')
                        self.var_tracker.update_var(var_name, line.lineno, var_value)
                
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            indent = "  " * function_depth
            
            comment_text = ""
            try:
                comment_with_prefix = template_info['template'].format(**params)
                comment_text = comment_with_prefix.lstrip().lstrip('#').lstrip()
            except KeyError as e:
                comment_text = f"(Missing param: {e})"

            if self.lang == 'zh':
                code_line = f"{indent}[第{line.lineno}行]  {line.code}"
                explain_line = f"{indent}{comment_text}"
            else:
                code_line = f"{indent}[line {line.lineno}]  {line.code}"
                explain_line = f"{indent}{comment_text}"        
            
            output_lines.append(code_line)
            if comment_text:
                output_lines.append(explain_line)
            
            prev_var_dict = line.get_var_dict()
            prev_line_obj = line
            
            if line_type in ('for_end', 'while_end'):
                current_loop_header = None
        
        # 最终答案 - 增强查找逻辑
        final_value = '?'
        
        # 首先检查返回值字典
        if self.target_line in self.return_values:
            final_value = self.return_values[self.target_line]
        else:
            # 从最后一行开始查找
            for line in reversed(self.lines):
                if not line.is_function_enter and not line.is_function_return:
                    var_dict = line.get_var_dict()
                    if self.target_var in var_dict:
                        final_value = var_dict[self.target_var]
                        break
        
        source_info = self.var_tracker.get_var_source_info(self.target_var)
        
        output_lines.append(footer_template.format(
            target_var=self.target_var,
            final_value=final_value,
            source_info=source_info
        ))
        
        return '\n'.join(output_lines)
    
    def save_cot(self, output_file):
        """保存COT"""
        cot_text = self.generate()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cot_text)
        return output_file
    
    @staticmethod
    def generate_cot(pruned_file, output_file, lang='en'):
        """静态方法：生成COT"""
        generator = COTGenerator(pruned_file, lang=lang)
        generator.load_pruned_trace()
        return generator.save_cot(output_file)
```

#### main.py

```py
"""
COT生成框架主流程 - 重构版
支持数据集批量处理
"""

import argparse
from pathlib import Path
from dataset_processor import DatasetProcessor


# AI API配置
API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"
BASE_URL = "https://llmapi.paratera.com/v1"

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
}


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='COT Generation Framework for TreecEva Dataset',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 处理所有cases（跳过已有COT的）
  python main.py --all
  
  # 处理所有cases（包括已有COT的）
  python main.py --all --no-skip
  
  # 处理单个case
  python main.py --case SL-MIX-S0001
  
  # 使用不同的AI模型
  python main.py --all --model qwen3_coder
  
  # 调整并行数
  python main.py --all --workers 8
        """
    )
    
    parser.add_argument(
        '--dataset',
        default='TreecEva_data_reduced_formated_cot.json',
        help='数据集JSON文件路径（默认: TreecEva_data_reduced_formated_cot.json）'
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
        '--model',
        choices=['qwen3_235b', 'qwen3_coder'],
        default='qwen3_235b',
        help='使用的AI模型（默认: qwen3_235b）'
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
    
    # 检查数据集文件
    dataset_path = Path(args.dataset)
    if not dataset_path.exists():
        print(f"错误: 数据集文件不存在: {dataset_path}")
        return
    
    # 获取API配置
    api_config = AI_APIS[args.model]
    
    print(f"{'='*60}")
    print(f"COT Generation Framework - Dataset Mode")
    print(f"{'='*60}")
    print(f"数据集: {dataset_path}")
    print(f"AI模型: {args.model}")
    print(f"并行数: {args.workers}")
    print(f"{'='*60}\n")
    
    # 创建处理器
    processor = DatasetProcessor(
        str(dataset_path),
        api_config,
        max_workers=args.workers
    )
    
    # 执行处理
    if args.all:
        processor.process_all_cases(skip_existing=not args.no_skip)
    elif args.case:
        processor.process_case_by_id(args.case)


if __name__ == '__main__':
    main()
```

#### pruner.py

```py
"""
依赖分析和智能剪枝模块 - 增强函数调用支持
"""

import ast
import re
import json
from typing import Set, Dict, List, Tuple
from attribute_analyzer import (
    analyze_file_for_attribute_usage, 
    analyze_lines_for_attribute_usage,
    SmartObjectFormatter
)


class TraceLine:
    """表示追踪文件中的一行"""
    def __init__(self, lineno, code, var_names=None, var_values=None, depth=0, 
                 is_function_enter=False, is_function_return=False, func_name=None, 
                 return_value=None, param_mapping=None):
        self.lineno = lineno
        self.code = code.strip()
        self.var_names = var_names or []
        self.var_values = var_values or []
        self.depth = depth
        self.is_function_enter = is_function_enter
        self.is_function_return = is_function_return
        self.func_name = func_name
        self.return_value = return_value
        self.param_mapping = param_mapping or {}  # 参数映射 {形参: {'actual_var': 实参名, 'value': 值}}
    
    def get_var_dict(self):
        """获取变量字典"""
        return dict(zip(self.var_names, self.var_values))
    
    def __repr__(self):
        if self.is_function_enter:
            return f"TraceLine(ENTER {self.func_name} at {self.lineno})"
        elif self.is_function_return:
            return f"TraceLine(RETURN {self.func_name} at {self.lineno})"
        return f"TraceLine({self.lineno}, {self.code[:30]}..., depth={self.depth})"


class ValueFormatter:
    """值格式化器"""
    
    @staticmethod
    def format(value_struct, var_name='', required_attrs=None, depth=0):
        """格式化结构化值"""
        if depth > 3:
            return "..."
        
        if not isinstance(value_struct, dict) or '_type' not in value_struct:
            return str(value_struct)
        
        vtype = value_struct['_type']
        
        if vtype == 'str':
            return f"'{value_struct['_value']}'"
        elif vtype in ['int', 'float', 'bool']:
            return str(value_struct['_value'])
        elif vtype == 'None':
            return 'None'
        elif vtype == 'list':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return '[]'
            if depth >= 2:
                return f'[...{total} items]'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"[{', '.join(formatted)}]"
        elif vtype == 'tuple':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return '()'
            if depth >= 2:
                return f'(...{total} items)'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"({', '.join(formatted)})"
        elif vtype == 'namedtuple':
            class_name = value_struct.get('_class', 'namedtuple')
            attrs = value_struct.get('_attrs', {})
            if not attrs or depth >= 2:
                return f"{class_name}(...)"
            parts = []
            for k, v in list(attrs.items())[:5]:
                formatted = ValueFormatter.format(v, f"{var_name}.{k}", None, depth+1)
                parts.append(f"{k}={formatted}")
            return f"{class_name}({', '.join(parts)})"
        elif vtype == 'dict':
            items = value_struct.get('_items', {})
            total = value_struct.get('_len', len(items))
            if not items:
                return '{}'
            if depth >= 2:
                return f'{{...{total} items}}'
            parts = []
            for k, v in list(items.items())[:3]:
                formatted_v = ValueFormatter.format(v, '', None, depth+1)
                parts.append(f"{k}: {formatted_v}")
            if total > len(parts):
                parts.append('...')
            return f"{{{', '.join(parts)}}}"
        elif vtype == 'set':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return 'set()'
            if depth >= 2:
                return f'{{...{total} items}}'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"{{{', '.join(formatted)}}}"
        elif vtype == 'object':
            class_name = value_struct.get('_class', 'object')
            all_attrs = value_struct.get('_attrs', {})
            
            if not all_attrs:
                return f"{class_name}(...)"
            
            if required_attrs:
                parts = []
                for attr in sorted(required_attrs):
                    if attr in all_attrs:
                        attr_value = all_attrs[attr]
                        sub_required = {a.split('.', 1)[1] for a in required_attrs 
                                      if a.startswith(attr + '.') and '.' in a.split(attr + '.', 1)[1]}
                        formatted = ValueFormatter.format(
                            attr_value, 
                            f"{var_name}.{attr}",
                            sub_required if sub_required else None,
                            depth + 1
                        )
                        parts.append(f"{attr}={formatted}")
                
                if not parts:
                    return f"{class_name}(...)"
                return f"{class_name}({', '.join(parts)})"
            else:
                if depth >= 2:
                    return f"{class_name}(...)"
                parts = []
                for k, v in list(all_attrs.items())[:5]:
                    formatted = ValueFormatter.format(v, f"{var_name}.{k}", None, depth+1)
                    parts.append(f"{k}={formatted}")
                if len(all_attrs) > 5:
                    parts.append('...')
                return f"{class_name}({', '.join(parts)})"
        else:
            return value_struct.get('_repr', str(value_struct))


class AttributeAccessAnalyzer:
    """属性访问分析器"""
    
    @staticmethod
    def analyze_code(code):
        """分析代码中的属性访问"""
        attr_paths = set()
        simple_vars = set()
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute):
                    path = AttributeAccessAnalyzer._build_path(node)
                    if path:
                        attr_paths.add(path)
                        root = path.split('.')[0]
                        simple_vars.add(root)
                elif isinstance(node, ast.Name):
                    simple_vars.add(node.id)
        except:
            pass
        
        return attr_paths, simple_vars
    
    @staticmethod
    def _build_path(node):
        """构建属性访问路径"""
        parts = []
        current = node
        
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        
        if isinstance(current, ast.Name):
            parts.append(current.id)
            return '.'.join(reversed(parts))
        
        return None


class DependencyAnalyzer:
    """依赖分析器"""
    
    def __init__(self):
        self.focused_vars = set()
        self.var_first_use = {}
    
    def extract_lvalue(self, code):
        """提取赋值语句左值"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    targets = []
                    for target in node.targets:
                        targets.extend(self._extract_names(target, include_attrs=True))
                    return targets
                elif isinstance(node, ast.AugAssign):
                    return self._extract_names(node.target, include_attrs=True)
        except:
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_.]*)\s*[=+\-*/]=', code)
            if match:
                return [match.group(1)]
        return []
    
    def _extract_names(self, node, include_attrs=False):
        """从AST节点提取变量名"""
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Attribute):
            if include_attrs:
                path = self._build_attr_path(node)
                return [path] if path else []
            else:
                return self._extract_names(node.value, include_attrs)
        elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
            names = []
            for elt in node.elts:
                names.extend(self._extract_names(elt, include_attrs))
            return names
        elif isinstance(node, ast.Subscript):
            return self._extract_names(node.value, include_attrs)
        return []
    
    def _build_attr_path(self, node):
        """构建属性访问路径"""
        parts = []
        current = node
        
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        
        if isinstance(current, ast.Name):
            parts.append(current.id)
            return '.'.join(reversed(parts))
        
        return None
    
    def extract_dependencies(self, code):
        """提取代码行的变量依赖"""
        deps = set()
        
        try:
            attr_accesses, simple_vars = AttributeAccessAnalyzer.analyze_code(code)
            deps.update(attr_accesses)
            
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    right_attrs, right_simple = AttributeAccessAnalyzer.analyze_code(
                        ast.unparse(node.value) if hasattr(ast, 'unparse') else ''
                    )
                    deps.update(right_attrs)
                    deps.update(right_simple)
                    return deps
                elif isinstance(node, ast.AugAssign):
                    left_name = self._extract_names(node.target, include_attrs=True)
                    deps.update(left_name)
                    
                    right_attrs, right_simple = AttributeAccessAnalyzer.analyze_code(
                        ast.unparse(node.value) if hasattr(ast, 'unparse') else ''
                    )
                    deps.update(right_attrs)
                    deps.update(right_simple)
                    return deps
            
            deps.update(simple_vars)
            
        except:
            if '=' in code:
                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '&=', '|=', '^=', '>>=', '<<=']:
                    if op in code:
                        parts = code.split(op, 1)
                        if len(parts) == 2:
                            left_var = parts[0].strip()
                            right_expr = parts[1].strip()
                            deps.add(left_var)
                            vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', right_expr)
                            deps.update(vars_in_right)
                        break
                else:
                    parts = code.split('=', 1)
                    if len(parts) == 2:
                        right_expr = parts[1]
                        vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', right_expr)
                        deps.update(vars_in_right)
            else:
                vars_in_code = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', code)
                deps.update(vars_in_code)
            
            keywords = {'if', 'else', 'elif', 'for', 'while', 'in', 'range', 
                       'def', 'class', 'return', 'True', 'False', 'None', 'print',
                       'and', 'or', 'not', 'is', 'with', 'as', 'try', 'except',
                       'finally', 'raise', 'break', 'continue', 'pass', 'lambda',
                       'yield', 'import', 'from', 'global', 'nonlocal'}
            deps = deps - keywords
        
        return deps
    
    def is_control_flow(self, code):
        """判断是否为控制流语句"""
        code_stripped = code.strip()
        control_keywords = ['if ', 'elif ', 'else:', 'for ', 'while ', 
                           'def ', 'class ', 'try:', 'except:', 'finally:', 
                           'with ', 'return', 'break', 'continue']
        return any(code_stripped.startswith(kw) for kw in control_keywords)
    
    def is_print_statement(self, code):
        """判断是否为print语句"""
        code_stripped = code.strip()
        return code_stripped.startswith('print(')
    
    def is_function_call(self, code):
        """判断是否为函数调用"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    return True
        except:
            pass
        return False
    
    def get_root_var(self, var_name):
        """获取属性路径的根变量"""
        return var_name.split('.')[0]
    
    def is_related_var(self, var1, var2):
        """判断两个变量是否相关"""
        if var1 == var2:
            return True
        if var1.startswith(var2 + '.') or var2.startswith(var1 + '.'):
            return True
        return False


class TracePruner:
    """追踪记录剪枝器 - 支持函数调用"""
    
    def __init__(self, trace_file, source_file=None):
        self.trace_file = trace_file
        self.source_file = source_file
        self.lines = []
        self.analyzer = DependencyAnalyzer()
        self.target_line = None
    
    def load_trace(self):
        """加载追踪文件 - 支持函数调用和参数映射"""
        with open(self.trace_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        i = 0
        param_mapping = {}  # 临时存储最近的参数映射
        
        while i < len(content):
            line = content[i].strip()
            if not line:
                i += 1
                continue
            
            # 检查参数映射
            if line.startswith('PARAM_MAPPING'):
                parts = line.split(' ', 2)
                if len(parts) >= 3:
                    func_name = parts[1]
                    mapping_str = parts[2]
                    try:
                        param_mapping = eval(mapping_str)
                    except:
                        param_mapping = {}
                i += 1
                continue
            
            # 检查函数进入
            if line.startswith('FUNCTION_ENTER'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    code = parts[3]
                    
                    var_names = []
                    var_values = []
                    if i + 1 < len(content):
                        next_line = content[i + 1].strip()
                        if next_line.startswith(str(lineno) + ' ['):
                            try:
                                parts = next_line.split(' ', 1)
                                if len(parts) > 1:
                                    var_data = parts[1]
                                    var_names, var_values = self._parse_var_lists(var_data)
                                i += 1
                            except:
                                pass
                    
                    trace_line = TraceLine(lineno, code, var_names, var_values, 
                                         is_function_enter=True, func_name=func_name,
                                         param_mapping=param_mapping.copy())
                    self.lines.append(trace_line)
                    param_mapping = {}  # 清空映射
                    i += 1
                    continue
            
            # 检查函数返回
            if line.startswith('FUNCTION_RETURN'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    return_value_str = parts[3]
                    try:
                        return_value = eval(return_value_str)
                    except:
                        return_value = return_value_str
                    
                    trace_line = TraceLine(lineno, '', [], [], 
                                         is_function_return=True, 
                                         func_name=func_name,
                                         return_value=return_value)
                    self.lines.append(trace_line)
                    i += 1
                    continue
            
            # 检查深度标记
            depth = 0
            if line.startswith('DEPTH_'):
                match = re.match(r'DEPTH_(\d+)\s+(.+)', line)
                if match:
                    depth = int(match.group(1))
                    line = match.group(2)
            
            parts = line.split(' ', 1)
            if len(parts) < 2:
                i += 1
                continue
            
            lineno = int(parts[0])
            code = parts[1]
            
            var_names = []
            var_values = []
            if i + 1 < len(content):
                next_line = content[i + 1].strip()
                if next_line.startswith(str(lineno) + ' ['):
                    try:
                        parts = next_line.split(' ', 1)
                        if len(parts) > 1:
                            var_data = parts[1]
                            var_names, var_values = self._parse_var_lists(var_data)
                        i += 1
                    except:
                        pass
            
            trace_line = TraceLine(lineno, code, var_names, var_values, depth=depth)
            self.lines.append(trace_line)
            i += 1
    
    def _parse_var_lists(self, var_data):
        """解析变量列表"""
        try:
            parts = var_data.split('] [')
            if len(parts) == 2:
                names_str = parts[0] + ']'
                values_str = '[' + parts[1]
                
                names = eval(names_str)
                values = eval(values_str)
                return names, values
        except Exception as e:
            print(f"解析变量列表失败: {e}")
        return [], []
    
    def prune(self, target_line, target_var):
        """执行剪枝"""
        self.target_line = target_line
        
        print(f"\n===== 剪枝分析（支持函数调用） =====")
        print(f"目标行: {target_line}, 目标变量: {target_var}")
        
        focused_vars = {target_var}
        keep_lines = set()
        var_enter_line = {}
        
        target_line_obj = None
        for idx, line in enumerate(self.lines):
            if line.lineno == target_line and not line.is_function_enter and not line.is_function_return:
                target_line_obj = line
                target_idx = idx
        
        if target_line_obj:
            deps = self.analyzer.extract_dependencies(target_line_obj.code)
            print(f"\n目标行代码: {target_line_obj.code}")
            print(f"目标行依赖: {deps}")
            focused_vars.update(deps)
            for dep in deps:
                var_enter_line[dep] = target_line
        
        print(f"初始关注变量集合: {focused_vars}\n")
        
        # 从目标行向上回溯
        for idx in range(len(self.lines) - 1, -1, -1):
            line = self.lines[idx]
            
            if not line.is_function_enter and not line.is_function_return and line.lineno > target_line:
                continue
            
            # 函数返回
            if line.is_function_return:
                keep_lines.add(idx)
                print(f"函数返回 {line.func_name} at line {line.lineno}")
                continue
            
            # 函数进入
            if line.is_function_enter:
                keep_lines.add(idx)
                for var_name in line.var_names:
                    focused_vars.add(var_name)
                print(f"函数进入 {line.func_name} at line {line.lineno}, 参数: {line.var_names}")
                continue
            
            if line.lineno == target_line:
                keep_lines.add(idx)
                continue
            
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(idx)
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                if new_deps:
                    print(f"第{line.lineno}行(控制流): {line.code.strip()}")
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
                continue
            
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(self.analyzer.is_related_var(dep, fv) for dep in deps for fv in focused_vars):
                    keep_lines.add(idx)
                    print(f"第{line.lineno}行(print): {line.code.strip()}")
                continue
            
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            if any(self.analyzer.is_related_var(lv, fv) for lv in lvalues for fv in focused_vars):
                keep_lines.add(idx)
                
                print(f"第{line.lineno}行(赋值): {line.code.strip()}")
                print(f"  定义了关注变量: {set(lvalues)}")
                
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                
                if new_deps:
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
        
        print(f"\n最终关注变量集合: {focused_vars}")
        print(f"保留的行索引: {sorted(keep_lines)}\n")
        
        # 第二遍：格式化保留的行
        kept_lines = [self.lines[idx] for idx in sorted(keep_lines)]
        
        print("===== 格式化输出 =====")
        
        pruned_lines = []
        
        for i, line in enumerate(kept_lines):
            if line.is_function_enter or line.is_function_return:
                pruned_lines.append(line)
                continue
            
            current_attr_usage = {}
            if self.source_file:
                current_attr_usage = analyze_lines_for_attribute_usage(
                    self.source_file, 
                    line.lineno,
                    line.lineno
                )
            
            future_uses = set()
            for j in range(i + 1, len(kept_lines)):
                future_line = kept_lines[j]
                if not future_line.is_function_enter and not future_line.is_function_return:
                    uses = self.analyzer.extract_dependencies(future_line.code)
                    future_uses.update(uses & focused_vars)
            
            current_defines = set(self.analyzer.extract_lvalue(line.code))
            current_uses = self.analyzer.extract_dependencies(line.code)
            
            vars_to_keep = (current_uses & focused_vars) | \
                          (current_defines & focused_vars) | \
                          (future_uses & focused_vars)
            
            print(f"第{line.lineno}行: {line.code.strip()}")
            
            filtered_names = []
            filtered_values = []
            
            for name, value_struct in zip(line.var_names, line.var_values):
                root_var = self.analyzer.get_root_var(name)
                
                if any(self.analyzer.is_related_var(name, vk) for vk in vars_to_keep):
                    if root_var in current_attr_usage:
                        paths = current_attr_usage[root_var]
                        required = set()
                        for path in paths:
                            parts = path.split('.')
                            if parts[0] == root_var and len(parts) > 1:
                                required.add(parts[1])
                        
                        formatted = ValueFormatter.format(
                            value_struct, 
                            root_var,
                            required if required else None
                        )
                    else:
                        if root_var in current_defines:
                            formatted = ValueFormatter.format(value_struct, root_var, None)
                        else:
                            if isinstance(value_struct, dict) and value_struct.get('_type') == 'object':
                                class_name = value_struct.get('_class', 'object')
                                formatted = f"{class_name}(...)"
                            else:
                                formatted = ValueFormatter.format(value_struct, root_var, None)
                    
                    filtered_names.append(name)
                    filtered_values.append(formatted)
            
            pruned_line = TraceLine(line.lineno, line.code, 
                                   filtered_names, filtered_values, 
                                   depth=line.depth)
            pruned_lines.append(pruned_line)
            print()
        
        return pruned_lines, focused_vars
    
    def save_pruned(self, pruned_lines, target_line, target_var, output_file):
        """保存剪枝结果"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{target_line}\n")
            f.write(f"{target_var}\n")
            f.write("---\n")
            
            for line in pruned_lines:
                if line.is_function_enter:
                    # 先保存参数映射（在FUNCTION_ENTER之前）
                    if line.param_mapping:
                        f.write(f"PARAM_MAPPING {line.param_mapping}\n")
                    f.write(f"FUNCTION_ENTER {line.lineno} {line.func_name} {line.code}\n")
                    f.write(f"{line.lineno} {line.var_names} {line.var_values}\n")
                elif line.is_function_return:
                    f.write(f"FUNCTION_RETURN {line.lineno} {line.func_name} {line.return_value}\n")
                else:
                    f.write(f"{line.lineno} {line.code}\n")
                    f.write(f"{line.lineno} {line.var_names} {line.var_values}\n")
    
    @staticmethod
    def prune_trace(trace_file, target_line, target_var, output_file, source_file=None):
        """静态方法：执行剪枝"""
        pruner = TracePruner(trace_file, source_file)
        pruner.load_trace()
        pruned_lines, focused_vars = pruner.prune(target_line, target_var)
        pruner.save_pruned(pruned_lines, target_line, target_var, output_file)
        return output_file, pruned_lines
```

#### tracer.py

```py
"""
Python代码执行追踪器 - 支持函数调用追踪（增强版）
增加函数调用参数映射追踪
"""

import sys
import linecache
import os
import ast
import re


class PythonTracer:
    """Python代码执行追踪器"""
    
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)
        self.trace_active = False
        self.has_main_function = False
        self.module_started = False
        self.pending_trace = None
        self.output_lines = []
        self.call_stack = []
        self.user_functions = set()
        self.in_user_function = 0
        self.function_signatures = {}  # 存储函数签名
        
    def analyze_function_signatures(self, filename):
        """分析文件中的函数签名"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
                
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    params = [arg.arg for arg in node.args.args]
                    self.function_signatures[node.name] = params
        except:
            pass
    
    def extract_call_arguments(self, source_line):
        """从调用语句中提取实参名称"""
        try:
            # 匹配 var = func(arg1, arg2, ...)
            match = re.match(r'\s*\w+\s*=\s*(\w+)\((.*)\)', source_line)
            if match:
                args_str = match.group(2).strip()
                if not args_str:
                    return []
                args = [arg.strip() for arg in args_str.split(',')]
                return args
        except:
            pass
        return []
    
    def check_for_main(self, filename):
        """检查文件中是否定义了main函数"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return 'def main(' in content or 'def main():' in content
        except:
            return False
    
    def should_trace_file(self, filename):
        """判断是否应该追踪该文件"""
        if not filename:
            return False
        abs_filename = os.path.abspath(filename)
        return abs_filename == self.target_file
    
    def trace_handler(self, frame, event, arg):
        """追踪处理函数"""
        filename = frame.f_code.co_filename
        
        if not self.should_trace_file(filename):
            return self.trace_handler
        
        func_name = frame.f_code.co_name
        
        special_names = ['<module>', 'main', '<listcomp>', '<dictcomp>', '<setcomp>', '<genexpr>']
        is_special = func_name in special_names
        
        # 处理call事件
        if event == 'call':
            if func_name == 'main':
                self.has_main_function = True
                self.trace_active = True
                self.call_stack.append(('main', frame.f_lineno))
                return self.trace_handler
            elif not is_special:
                self.user_functions.add(func_name)
                if self.trace_active:
                    # 输出挂起的调用行（主流程）
                    if self.pending_trace:
                        caller_frame = frame.f_back
                        if caller_frame:
                            caller_vars = caller_frame.f_locals.copy()
                            self.output_pending_trace(caller_vars)
                            
                            # 提取调用行的实参
                            call_line = self.pending_trace['source']
                            actual_args = self.extract_call_arguments(call_line)
                            
                            # 输出参数映射信息
                            if actual_args and func_name in self.function_signatures:
                                formal_params = self.function_signatures[func_name]
                                param_mapping = {}
                                for i, (formal, actual) in enumerate(zip(formal_params, actual_args)):
                                    param_mapping[formal] = {
                                        'actual_var': actual,
                                        'value': caller_vars.get(actual, actual)
                                    }
                                
                                # 添加映射信息到输出
                                self.output_lines.append(f"PARAM_MAPPING {func_name} {param_mapping}")
                            
                            self.pending_trace = None
                    
                    # 进入函数
                    self.in_user_function += 1
                    self.call_stack.append((func_name, frame.f_back.f_lineno if frame.f_back else 0))
                    
                    # 输出函数进入信息
                    lineno = frame.f_lineno
                    source_line = linecache.getline(filename, lineno).rstrip()
                    
                    self.output_lines.append(f"FUNCTION_ENTER {lineno} {func_name} {source_line}")
                    
                    # 输出函数参数
                    local_vars = frame.f_locals.copy()
                    filtered_vars = self.filter_variables(local_vars)
                    if filtered_vars:
                        var_names = list(filtered_vars.keys())
                        var_values = [self.serialize_value(filtered_vars[name]) for name in var_names]
                        self.output_lines.append(f"{lineno} {var_names} {var_values}")
                    
                return self.trace_handler
        
        # 模块级别代码
        if not self.has_main_function and func_name == '<module>':
            if not self.module_started:
                self.module_started = True
                self.call_stack.append(('<module>', 0))
            self.trace_active = True
        
        if self.has_main_function and not self.trace_active:
            return self.trace_handler
        
        # 处理line事件
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            
            if source_line.strip().startswith(('class ', 'def ')) and not source_line.strip().startswith('def main'):
                return self.trace_handler
            
            local_vars = frame.f_locals.copy()
            
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            depth = self.in_user_function + 1
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line,
                'depth': depth
            }
        
        # 处理return事件
        elif event == 'return':
            if self.trace_active:
                if self.pending_trace:
                    self.output_pending_trace(frame.f_locals.copy())
                    self.pending_trace = None
                
                if func_name in self.user_functions:
                    lineno = frame.f_lineno
                    return_value = arg
                    
                    self.output_lines.append(f"FUNCTION_RETURN {lineno} {func_name} {self.serialize_value(return_value)}")
                    
                    if self.call_stack and self.call_stack[-1][0] == func_name:
                        self.call_stack.pop()
                    
                    self.in_user_function = max(0, self.in_user_function - 1)
                
                if func_name == 'main':
                    self.trace_active = False
                    if self.call_stack and self.call_stack[-1][0] == 'main':
                        self.call_stack.pop()
                elif func_name == '<module>' and self.module_started:
                    self.trace_active = False
                    if self.call_stack and self.call_stack[-1][0] == '<module>':
                        self.call_stack.pop()
        
        return self.trace_handler
    
    def output_pending_trace(self, current_vars, is_function_enter=False):
        """输出待输出的追踪行"""
        lineno = self.pending_trace['lineno']
        source = self.pending_trace['source']
        depth = self.pending_trace.get('depth', 0)
        
        filtered_vars = self.filter_variables(current_vars)
        
        prefix = f"DEPTH_{depth} " if depth > 1 else ""
        self.output_lines.append(f"{prefix}{lineno} {source}")
        
        if filtered_vars:
            var_names = list(filtered_vars.keys())
            var_values = [self.serialize_value(filtered_vars[name]) for name in var_names]
            self.output_lines.append(f"{lineno} {var_names} {var_values}")
        else:
            self.output_lines.append(f"{lineno} [] []")
    
    def filter_variables(self, local_vars):
        """过滤变量，只保留数据变量"""
        filtered = {}
        for name, value in local_vars.items():
            if name.startswith('__'):
                continue
            if callable(value) and not isinstance(value, type):
                continue
            if isinstance(value, type):
                continue
            if str(type(value)).startswith("<class 'module"):
                continue
            if hasattr(value, '__bases__') and tuple in getattr(value, '__bases__', []):
                continue
            
            filtered[name] = value
        return filtered
    
    def serialize_value(self, value, depth=0):
        """序列化值为结构化数据"""
        if depth > 3:
            return "..."
        
        try:
            if isinstance(value, str):
                return {'_type': 'str', '_value': value}
            elif isinstance(value, bool):
                return {'_type': 'bool', '_value': value}
            elif isinstance(value, int):
                return {'_type': 'int', '_value': value}
            elif isinstance(value, float):
                return {'_type': 'float', '_value': value}
            elif value is None:
                return {'_type': 'None'}
            elif isinstance(value, list):
                items = [self.serialize_value(v, depth+1) for v in value[:10]]
                return {'_type': 'list', '_items': items, '_len': len(value)}
            elif isinstance(value, tuple):
                if hasattr(value, '_fields'):
                    attrs = {}
                    for k in value._fields:
                        attrs[k] = self.serialize_value(getattr(value, k), depth+1)
                    return {
                        '_type': 'namedtuple',
                        '_class': type(value).__name__,
                        '_attrs': attrs
                    }
                else:
                    items = [self.serialize_value(v, depth+1) for v in value[:10]]
                    return {'_type': 'tuple', '_items': items, '_len': len(value)}
            elif isinstance(value, dict):
                items = {}
                for i, (k, v) in enumerate(value.items()):
                    if i >= 5:
                        break
                    items[str(k)] = self.serialize_value(v, depth+1)
                return {'_type': 'dict', '_items': items, '_len': len(value)}
            elif isinstance(value, set):
                items = [self.serialize_value(v, depth+1) for v in list(value)[:10]]
                return {'_type': 'set', '_items': items, '_len': len(value)}
            elif hasattr(value, '__dict__'):
                attrs = {}
                for k, v in value.__dict__.items():
                    if not k.startswith('_'):
                        attrs[k] = self.serialize_value(v, depth+1)
                return {
                    '_type': 'object',
                    '_class': type(value).__name__,
                    '_attrs': attrs
                }
            else:
                return {'_type': 'unknown', '_repr': str(value)}
        except Exception as e:
            return {'_type': 'error', '_msg': str(e)}
    
    def save_output(self, output_file):
        """保存输出到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))
    
    @staticmethod
    def trace_file(script_file, output_file='trace_output.txt'):
        """追踪Python文件的执行"""
        tracer = PythonTracer(script_file)
        tracer.has_main_function = tracer.check_for_main(script_file)
        tracer.analyze_function_signatures(script_file)
        
        sys.settrace(tracer.trace_handler)
        
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                code = compile(f.read(), script_file, 'exec')
                exec(code, {'__name__': '__main__'})
        except SystemExit:
            pass
        
        sys.settrace(None)
        
        tracer.save_output(output_file)
        
        return output_file
```

#### TreecEva_data_reduced_formated_cot.json

```json
[
  {
    "background": "I am developing a comprehensive evaluation benchmark for large language models in the code reasoning domain. This benchmark specifically focuses on assessing statement-level reasoning capabilities of LLMs across multiple computational paradigms: (1) Arithmetic Operations - including basic arithmetic (addition, subtraction, multiplication, division), advanced mathematical operations (exponentiation, logarithms, trigonometric functions), bitwise operations (AND, OR, XOR, shift operations), and composite calculations combining multiple operation types; (2) Boolean Logic - encompassing comparison operations (equality, inequality, relational comparisons), logical operations (AND, OR, NOT), and short-circuit evaluation patterns; (3) API/Function Calls - covering built-in function invocations, mathematical library usage, string manipulation functions, and container/data structure operations; (4) Variable Assignment - including simple assignments, multiple simultaneous assignments, tuple unpacking, and destructuring assignments; (5) Complex Mixed Scenarios - integrating multiple reasoning types in sophisticated logical chains.",
    "requirements": "Generate additional examples following the provided template format with these specific criteria: (1) Create significantly more complex code samples with extended logical reasoning chains requiring multiple inference steps; (2) Ensure each example has a unique, deterministic answer that can be computed through step-by-step execution; (3) Maintain strict format consistency across all generated examples, matching the exact structure and field organization of the provided samples; (4) Incorporate diverse programming languages and paradigms while maintaining code complexity at an advanced level suitable for challenging LLM reasoning capabilities."
  },
  {
    "id": "SL-MIX-S0001",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 5
    },
    "task": {
      "description": "A data analyst is processing a sales matrix where each row represents a product and each column represents a region. They need to: (1) find products with total sales above 100, (2) calculate the variance of sales for these products, (3) apply a transformation where variance is XORed with the product count. What is the value of variable 'result_value' after all transformations?",
      "code": "# Sales matrix: rows are products, columns are regions\nsales_matrix = [\n    [25, 30, 28, 35],\n    [15, 20, 18, 22],\n    [40, 35, 38, 42],\n    [12, 15, 10, 14]\n]\n\n# Step 1: Find products with total sales > 100\nhigh_sales_products = []\nfor product_sales in sales_matrix:\n    total_sales = sum(product_sales)\n    if total_sales > 100:\n        high_sales_products.append(product_sales)\n\n# Step 2: Calculate variance for each high-sales product\nvariances = []\nfor product_sales in high_sales_products:\n    mean = sum(product_sales) / len(product_sales)\n    squared_diffs = [(x - mean) ** 2 for x in product_sales]\n    variance = sum(squared_diffs) / len(squared_diffs)\n    variances.append(int(variance))\n\n# Step 3: XOR operation\nproduct_count = len(high_sales_products)\ntotal_variance = sum(variances)\nresult_value = total_variance ^ product_count\n\nprint(f\"Result: {result_value}\")",
      "answer": 17,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S0002",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 4,
      "intervention": 6
    },
    "task": {
      "description": "A password strength analyzer processes a password through multiple validation steps: (1) counts character types (uppercase, lowercase, digits), (2) calculates a base score using specific weights, (3) applies penalties for common patterns, (4) uses bitwise operations to encode the final strength level. What is the value of variable 'strength_code' after analyzing the password?",
      "code": "password = \"SecurePass2024\"\n\n# Step 1: Count character types\nuppercase_count = sum(1 for c in password if c.isupper())\nlowercase_count = sum(1 for c in password if c.islower())\ndigit_count = sum(1 for c in password if c.isdigit())\n\n# Step 2: Calculate base score with weights\nbase_score = uppercase_count * 3 + lowercase_count * 2 + digit_count * 4\n\n# Step 3: Check for common patterns and apply penalty\nhas_consecutive = False\nfor i in range(len(password) - 1):\n    if ord(password[i+1]) - ord(password[i]) == 1:\n        has_consecutive = True\n        break\n\npenalty = 5 if has_consecutive else 0\nadjusted_score = base_score - penalty\n\n# Step 4: Encode strength using bitwise operations\nstrength_level = adjusted_score // 10\nstrength_code = (strength_level << 2) | (digit_count & 0x3)\n\nprint(f\"Result: {strength_code}\")",
      "answer": 12,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S0003",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 4,
      "intervention": 8
    },
    "task": {
      "description": "A text processing pipeline analyzes document metadata to classify sensitivity levels. The system uses pattern matching, logical conditions, and string transformations to determine access permissions. What is the value of variable 'access_level' at the end of execution?",
      "code": "import re\n\ndef sanitize_metadata(doc_meta):\n    return re.sub(r'[^a-zA-Z0-9_\\- ]', '', doc_meta).strip()\n\ndef evaluate_clearance(doc_meta):\n    sanitized = sanitize_metadata(doc_meta)\n    is_internal = 'INTERNAL' in sanitized\n    is_confidential = 'CONFIDENTIAL' in sanitized\n    is_public = 'PUBLIC' in sanitized\n    \n    # Short-circuit evaluation with logical operations\n    if is_public and not (is_internal or is_confidential):\n        return 1\n    elif is_internal and not is_confidential:\n        return 2\n    elif is_confidential or (is_internal and 'RESTRICTED' in sanitized):\n        return 3\n    else:\n        return 0\n\ndocuments_metadata = [\n    'PUBLIC DOCUMENT',\n    'INTERNAL USE ONLY - CONFIDENTIAL',\n    'CONFIDENTIAL - RESTRICTED ACCESS',\n    'PUBLIC RELEASE - INTERNAL REVIEW',\n    'RESTRICTED CONFIDENTIAL DOCUMENT'\n]\n\n# List comprehension with generator expression\nprocessed_levels = [evaluate_clearance(meta) for meta in documents_metadata if len(meta) > 10]\n\n# Pattern matching for final classification\naccess_level = 0\nmatch sum(processed_levels):\n    case n if n > 10:\n        access_level = 5\n    case n if n > 7:\n        access_level = 4\n    case n if n > 4:\n        access_level = 3\n    case n if n > 1:\n        access_level = 2\n    case _:\n        access_level = 1\n\nprint(f'Result: {access_level}')",
      "answer": 5,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S0004",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 3,
      "intervention": 6
    },
    "task": {
      "description": "A route planner calculates the shortest path cost in a simple graph. The graph is represented as an adjacency matrix. Starting from node 0, the algorithm finds all paths to node 3 within 2 hops, calculates their costs, and applies a discount based on the number of valid paths found. What is the value of variable 'final_cost' after optimization?",
      "code": "# Adjacency matrix: graph[i][j] = cost from node i to j (0 means no edge)\ngraph = [\n    [0, 10, 15, 0],\n    [0, 0, 0, 12],\n    [0, 8, 0, 14],\n    [0, 0, 0, 0]\n]\n\nstart_node = 0\ntarget_node = 3\nmax_hops = 2\n\n# Find all paths within max_hops\nvalid_paths = []\nfor intermediate in range(len(graph)):\n    # Direct path (1 hop)\n    if graph[start_node][intermediate] > 0 and graph[intermediate][target_node] > 0:\n        cost = graph[start_node][intermediate] + graph[intermediate][target_node]\n        valid_paths.append(cost)\n\n# Calculate minimum cost\nif valid_paths:\n    min_cost = min(valid_paths)\n    num_paths = len(valid_paths)\n    \n    # Apply discount based on number of paths\n    discount_rate = num_paths * 2\n    discount = min_cost * discount_rate // 100\n    final_cost = min_cost - discount\nelse:\n    final_cost = 0\n\nprint(f\"Result: {final_cost}\")",
      "answer": 22,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S0005",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervent
```
