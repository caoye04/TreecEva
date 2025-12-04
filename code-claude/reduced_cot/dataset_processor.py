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
from ai_analyzer import AIAnalyzer, RegexTargetExtractor


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
        self.regex_extractor = RegexTargetExtractor()
        self.max_workers = max_workers
        
        # 确保必要目录存在
        self.temp_code_dir.mkdir(parents=True, exist_ok=True)
        
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
        return {'regex_failed': [], 'ai_failed': []}
    
    def _save_attention(self):
        """保存错误记录"""
        with open(self.attention_path, 'w', encoding='utf-8') as f:
            json.dump(self.attention_cases, f, ensure_ascii=False, indent=2)
    
    def analyze_target_with_retry(self, case, max_retries=3):
        """
        分析目标行和变量，支持重试
        使用正则表达式优先，失败后使用AI
        
        Args:
            case: 数据集中的case
            max_retries: AI分析的最大重试次数
            
        Returns:
            dict: 目标信息 {'target_line': int, 'target_var': str, 'method': str} 或 None
        """
        case_id = case['id']
        description = case['task']['description']
        code = case['task']['code']
        
        # 步骤1: 尝试正则表达式提取
        print(f"  [方法1] 正则表达式提取...")
        regex_result = self.regex_extractor.extract_target(description, code)
        
        if regex_result:
            # 验证正则结果
            if self.ai_analyzer.validate_target(
                code, 
                regex_result['target_line'], 
                regex_result['target_var']
            ):
                print(f"  ✓ 正则提取成功: line={regex_result['target_line']}, var={regex_result['target_var']}")
                return regex_result
            else:
                print(f"  ✗ 正则提取的结果验证失败")
                if 'regex_failed' not in self.attention_cases:
                    self.attention_cases['regex_failed'] = []
                if case_id not in self.attention_cases['regex_failed']:
                    self.attention_cases['regex_failed'].append(case_id)
        else:
            print(f"  ✗ 正则提取失败")
            if 'regex_failed' not in self.attention_cases:
                self.attention_cases['regex_failed'] = []
            if case_id not in self.attention_cases['regex_failed']:
                self.attention_cases['regex_failed'].append(case_id)
        
        # 步骤2: 使用AI分析（带重试）
        print(f"  [方法2] AI分析...")
        for attempt in range(1, max_retries + 1):
            print(f"    [AI尝试 {attempt}/{max_retries}]")
            
            # AI分析
            result = self.ai_analyzer.analyze_target(description, code, case_id)
            
            if result is None:
                print(f"    ✗ AI分析失败")
                if attempt < max_retries:
                    time.sleep(1)
                continue
            
            target_line = result['target_line']
            target_var = result['target_var']
            
            # 验证
            if not self.ai_analyzer.validate_target(code, target_line, target_var):
                print(f"    ✗ 验证失败: 目标信息不合理")
                if attempt < max_retries:
                    time.sleep(1)
                continue
            
            print(f"    ✓ AI分析成功: line={target_line}, var={target_var}")
            if result.get('reasoning'):
                print(f"      推理: {result['reasoning']}")
            return result
        
        # 所有尝试都失败
        print(f"  ✗ 所有方法都失败")
        if 'ai_failed' not in self.attention_cases:
            self.attention_cases['ai_failed'] = []
        if case_id not in self.attention_cases['ai_failed']:
            self.attention_cases['ai_failed'].append(case_id)
        
        return None
    
    def extract_all_targets(self, force=False):
        """
        批量提取所有cases的目标信息
        
        Args:
            force: 是否强制重新提取（即使已存在）
        """
        print(f"\n{'='*60}")
        print(f"批量提取目标信息")
        print(f"{'='*60}\n")
        
        cases_to_extract = []
        for case in self.dataset:
            case_id = case['id']
            if not force and case_id in self.all_target_info:
                continue
            cases_to_extract.append(case)
        
        if not cases_to_extract:
            print("所有cases都已有目标信息！")
            return
        
        print(f"需要提取: {len(cases_to_extract)} cases\n")
        
        success_count = 0
        failure_count = 0
        regex_success = 0
        ai_success = 0
        
        for case in tqdm(cases_to_extract, desc="提取目标信息"):
            case_id = case['id']
            print(f"\n处理 {case_id}...")
            
            target_info = self.analyze_target_with_retry(case)
            
            if target_info:
                self.all_target_info[case_id] = {
                    'target_line': target_info['target_line'],
                    'target_var': target_info['target_var']
                }
                success_count += 1
                
                # 统计方法
                if target_info.get('method') == 'regex':
                    regex_success += 1
                elif target_info.get('method') == 'ai':
                    ai_success += 1
                
                # 定期保存
                if success_count % 10 == 0:
                    self._save_all_target_info()
                    self._save_attention()
            else:
                failure_count += 1
        
        # 最终保存
        self._save_all_target_info()
        self._save_attention()
        
        print(f"\n{'='*60}")
        print(f"目标信息提取完成")
        print(f"成功: {success_count} cases")
        print(f"  - 正则提取: {regex_success} cases")
        print(f"  - AI分析: {ai_success} cases")
        print(f"失败: {failure_count} cases")
        print(f"总计: {len(self.all_target_info)} cases 有目标信息")
        print(f"{'='*60}\n")
        
        # 打印错误统计
        if self.attention_cases.get('regex_failed'):
            print(f"正则提取失败: {len(self.attention_cases['regex_failed'])} cases")
        if self.attention_cases.get('ai_failed'):
            print(f"AI分析失败: {len(self.attention_cases['ai_failed'])} cases")
            print(f"  {', '.join(self.attention_cases['ai_failed'][:10])}{'...' if len(self.attention_cases['ai_failed']) > 10 else ''}")
    
    def write_code_files(self, force=False):
        """
        将所有cases的代码写入临时文件
        
        Args:
            force: 是否强制重写（即使文件已存在）
        """
        print(f"\n{'='*60}")
        print(f"写入代码文件")
        print(f"{'='*60}\n")
        
        written_count = 0
        skipped_count = 0
        
        for case in tqdm(self.dataset, desc="写入代码文件"):
            case_id = case['id']
            code = case['task']['code']
            code_file = self.temp_code_dir / f"{case_id}.py"
            
            if code_file.exists() and not force:
                skipped_count += 1
                continue
            
            with open(code_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            written_count += 1
        
        print(f"\n写入: {written_count} 个文件")
        print(f"跳过: {skipped_count} 个文件")
        print(f"总计: {len(self.dataset)} 个文件")
        print(f"{'='*60}\n")
    
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
        
        # 检查代码文件
        code_file = self.temp_code_dir / f"{case_id}.py"
        if not code_file.exists():
            # 尝试写入代码文件
            try:
                with open(code_file, 'w', encoding='utf-8') as f:
                    f.write(case['task']['code'])
                print(f"  ✓ 创建代码文件")
            except Exception as e:
                print(f"  ✗ 错误: 无法创建代码文件: {e}")
                return False
        
        # 步骤1: 获取目标信息
        if case_id not in self.all_target_info:
            print(f"  [步骤1/5] 分析目标...")
            target_info = self.analyze_target_with_retry(case)
            
            if target_info is None:
                print(f"  ✗ 失败: 无法确定目标")
                return False
            
            # 保存到统一的all-target-info.json
            self.all_target_info[case_id] = {
                'target_line': target_info['target_line'],
                'target_var': target_info['target_var']
            }
            self._save_all_target_info()
            self._save_attention()
        else:
            print(f"  [步骤1/5] 使用已有的目标信息")
            target_info = self.all_target_info[case_id]
        
        target_line = target_info['target_line']
        target_var = target_info['target_var']
        print(f"    目标: line={target_line}, var={target_var}")
        
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
        
        # 打印错误统计
        if self.attention_cases.get('regex_failed'):
            print(f"正则提取失败: {len(self.attention_cases['regex_failed'])} cases")
        if self.attention_cases.get('ai_failed'):
            print(f"AI分析失败: {len(self.attention_cases['ai_failed'])} cases")
            print(f"  {', '.join(self.attention_cases['ai_failed'][:10])}{'...' if len(self.attention_cases['ai_failed']) > 10 else ''}")
    
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