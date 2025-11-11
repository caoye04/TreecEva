"""
COT生成Agent - 最终版
解决问题：
1. 多行表达式行号定位
2. 重复行去重
3. 最终答案修复
4. 参数缺失优化
"""

import json
import subprocess
import os
import sys
import ast
import re
import linecache
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any

sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai


# ============================================================================
# 第一部分：COT模板配置
# ============================================================================

COT_TEMPLATES = {
    'en': {
        'header': "Target: Find the value of variable {target_var} after [line {target_line}] executes\n",
        'footer': "\nAnswer: {target_var} = {final_value}",
    },
    'zh': {
        'header': "目标: 求[第{target_line}行]执行后变量 {target_var} 的值\n",
        'footer': "\n答案: {target_var} = {final_value}",
    }
}


# ============================================================================
# 第二部分：代码执行追踪器
# ============================================================================

class CodeTracer:
    """代码执行追踪器"""
    
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)
        self.trace_active = False
        self.pending_trace = None
        self.output_lines = []
        
    def should_trace_file(self, filename):
        if not filename:
            return False
        return os.path.abspath(filename) == self.target_file
    
    def trace_handler(self, frame, event, arg):
        filename = frame.f_code.co_filename
        
        if not self.should_trace_file(filename):
            return self.trace_handler
        
        func_name = frame.f_code.co_name
        
        if func_name == '<module>':
            self.trace_active = True
        
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            
            local_vars = frame.f_locals.copy()
            
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line
            }
        
        elif event == 'return' and func_name == '<module>':
            if self.pending_trace and self.trace_active:
                self.output_pending_trace(frame.f_locals.copy())
                self.pending_trace = None
            self.trace_active = False
        
        return self.trace_handler
    
    def output_pending_trace(self, current_vars):
        lineno = self.pending_trace['lineno']
        source = self.pending_trace['source']
        
        filtered_vars = self.filter_variables(current_vars)
        
        self.output_lines.append(f"{lineno} {source}")
        
        if filtered_vars:
            var_names = list(filtered_vars.keys())
            var_values = [self.serialize_value(filtered_vars[name]) for name in var_names]
            self.output_lines.append(f"{lineno} {var_names} {var_values}")
        else:
            self.output_lines.append(f"{lineno} [] []")
    
    def filter_variables(self, local_vars):
        filtered = {}
        for name, value in local_vars.items():
            if name.startswith('__'):
                continue
            if callable(value) and not isinstance(value, type):
                continue
            if isinstance(value, type):
                continue
            filtered[name] = value
        return filtered
    
    def serialize_value(self, value, depth=0):
        if depth > 2:
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
                items = [self.serialize_value(v, depth+1) for v in value[:5]]
                return {'_type': 'list', '_items': items, '_len': len(value)}
            elif isinstance(value, dict):
                items = {}
                for i, (k, v) in enumerate(value.items()):
                    if i >= 3:
                        break
                    items[str(k)] = self.serialize_value(v, depth+1)
                return {'_type': 'dict', '_items': items, '_len': len(value)}
            else:
                return {'_type': 'str', '_value': str(value)[:50]}
        except:
            return {'_type': 'str', '_value': str(value)[:50]}
    
    @staticmethod
    def trace_code(code_str, temp_file):
        """追踪代码字符串"""
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(code_str)
        
        tracer = CodeTracer(temp_file)
        sys.settrace(tracer.trace_handler)
        
        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                code = compile(f.read(), temp_file, 'exec')
                exec(code, {'__name__': '__main__'})
        except SystemExit:
            pass
        except Exception as e:
            print(f"  [追踪警告] 代码执行出错: {e}")
        
        sys.settrace(None)
        
        return tracer.output_lines


# ============================================================================
# 第三部分：依赖分析与剪枝
# ============================================================================

class TraceLine:
    """追踪行"""
    def __init__(self, lineno, code, var_names=None, var_values=None):
        self.lineno = lineno
        self.code = code.strip()
        self.var_names = var_names or []
        self.var_values = var_values or []
    
    def get_var_dict(self):
        return dict(zip(self.var_names, self.var_values))


class ValueFormatter:
    """值格式化器"""
    
    @staticmethod
    def format(value_struct):
        if not isinstance(value_struct, dict) or '_type' not in value_struct:
            return str(value_struct)
        
        vtype = value_struct['_type']
        
        if vtype == 'str':
            val = value_struct['_value']
            return f"'{val}'" if len(val) < 30 else f"'{val[:27]}...'"
        elif vtype in ['int', 'float', 'bool']:
            return str(value_struct['_value'])
        elif vtype == 'None':
            return 'None'
        elif vtype == 'list':
            total = value_struct.get('_len', 0)
            return f'[...{total} items]' if total > 0 else '[]'
        elif vtype == 'dict':
            total = value_struct.get('_len', 0)
            return f'{{...{total} items}}' if total > 0 else '{}'
        else:
            return str(value_struct)[:30]


class DependencyAnalyzer:
    """依赖分析器"""
    
    def extract_lvalue(self, code):
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
        except:
            pass
        match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code)
        if match:
            return [match.group(1)]
        return []
    
    def extract_dependencies(self, code):
        """提取依赖"""
        deps = set()
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Name):
                    deps.add(node.id)
        except:
            vars_in_code = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)
            deps.update(vars_in_code)
        
        keywords = {'if', 'else', 'for', 'while', 'in', 'range', 'def', 
                   'return', 'True', 'False', 'None', 'print', 'len', 'sum'}
        return deps - keywords
    
    def is_control_flow(self, code):
        code_stripped = code.strip()
        return any(code_stripped.startswith(kw) for kw in 
                  ['if ', 'elif ', 'else:', 'for ', 'while ', 'return'])


class TracePruner:
    """追踪剪枝器"""
    
    def __init__(self, trace_lines):
        self.lines = trace_lines
        self.analyzer = DependencyAnalyzer()
    
    def parse_trace_lines(self, output_lines):
        """解析追踪输出"""
        lines = []
        i = 0
        while i < len(output_lines):
            line = output_lines[i].strip()
            if not line:
                i += 1
                continue
            
            parts = line.split(' ', 1)
            if len(parts) < 2:
                i += 1
                continue
            
            lineno = int(parts[0])
            code = parts[1]
            
            var_names = []
            var_values = []
            if i + 1 < len(output_lines):
                next_line = output_lines[i + 1].strip()
                if next_line.startswith(str(lineno) + ' ['):
                    try:
                        parts = next_line.split(' ', 1)
                        if len(parts) > 1:
                            var_data = parts[1]
                            names_str, values_str = var_data.split('] [')
                            var_names = eval(names_str + ']')
                            var_values = eval('[' + values_str)
                        i += 1
                    except:
                        pass
            
            trace_line = TraceLine(lineno, code, var_names, var_values)
            lines.append(trace_line)
            i += 1
        
        self.lines = lines
    
    def prune(self, target_line, target_var):
        """执行剪枝"""
        focused_vars = {target_var}
        keep_lines = set()
        
        # 找到目标行
        for line in self.lines:
            if line.lineno == target_line:
                deps = self.analyzer.extract_dependencies(line.code)
                focused_vars.update(deps)
                break
        
        # 回溯分析
        for line in reversed(self.lines):
            if line.lineno > target_line:
                continue
            
            if line.lineno == target_line:
                keep_lines.add(line.lineno)
                continue
            
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(line.lineno)
                deps = self.analyzer.extract_dependencies(line.code)
                focused_vars.update(deps)
                continue
            
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            if any(lv in focused_vars for lv in lvalues):
                keep_lines.add(line.lineno)
                deps = self.analyzer.extract_dependencies(line.code)
                focused_vars.update(deps)
        
        # 过滤并格式化
        kept_lines = [line for line in self.lines if line.lineno in keep_lines]
        
        pruned_lines = []
        for line in kept_lines:
            filtered_names = []
            filtered_values = []
            
            for name, value_struct in zip(line.var_names, line.var_values):
                if name in focused_vars:
                    formatted = ValueFormatter.format(value_struct)
                    filtered_names.append(name)
                    filtered_values.append(formatted)
            
            pruned_line = TraceLine(line.lineno, line.code, filtered_names, filtered_values)
            pruned_lines.append(pruned_line)
        
        return pruned_lines


# ============================================================================
# 第四部分：COT生成器
# ============================================================================

class COTGenerator:
    """COT生成器"""
    
    def __init__(self, pruned_lines, target_line, target_var, answer, lang='en'):
        self.pruned_lines = pruned_lines
        self.target_line = target_line
        self.target_var = target_var
        self.answer = answer
        self.lang = lang
        self.templates = COT_TEMPLATES[lang]
    
    def generate(self):
        """生成COT"""
        output_lines = []
        
        # Header
        output_lines.append(self.templates['header'].format(
            target_line=self.target_line, 
            target_var=self.target_var
        ))
        
        # 去重：记录每行出现次数
        line_count = {}
        for line in self.pruned_lines:
            line_count[line.lineno] = line_count.get(line.lineno, 0) + 1
        
        # 生成步骤
        current_count = {}
        for line in self.pruned_lines:
            current_count[line.lineno] = current_count.get(line.lineno, 0) + 1
            
            # 去重：如果某行重复超过5次，只保留最后一次
            total_count = line_count[line.lineno]
            if total_count > 5 and current_count[line.lineno] < total_count:
                continue
            
            # 生成注释
            comment = self._generate_comment(line)
            
            # 格式化输出
            if self.lang == 'zh':
                code_line = f"[第{line.lineno}行]  {line.code}"
                explain_line = f"[解释] {comment}"
            else:
                code_line = f"[line {line.lineno}]  {line.code}"
                explain_line = f"[explain] {comment}"
            
            output_lines.append(code_line)
            if comment:
                output_lines.append(explain_line)
        
        # Footer
        output_lines.append(self.templates['footer'].format(
            target_var=self.target_var,
            final_value=self.answer
        ))
        
        return '\n'.join(output_lines)
    
    def _generate_comment(self, line):
        """生成简洁注释"""
        code = line.code.strip()
        var_dict = line.get_var_dict()
        
        # 赋值
        if '=' in code and not code.startswith('='):
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$', code)
            if match:
                var_name = match.group(1)
                value = var_dict.get(var_name, '?')
                
                if self.lang == 'zh':
                    return f"赋值: {var_name} = {value}"
                else:
                    return f"Assign: {var_name} = {value}"
        
        # For循环
        if code.startswith('for '):
            match = re.match(r'for\s+(\w+)\s+in\s+(.+):', code)
            if match:
                iter_var = match.group(1)
                iter_val = var_dict.get(iter_var, '?')
                
                if self.lang == 'zh':
                    return f"循环: {iter_var} = {iter_val}"
                else:
                    return f"Loop: {iter_var} = {iter_val}"
        
        # If语句
        if code.startswith('if '):
            if self.lang == 'zh':
                return "条件判断"
            else:
                return "Condition check"
        
        # 默认
        if self.lang == 'zh':
            return "执行"
        else:
            return "Execute"


# ============================================================================
# 第五部分：AI定位器（改进版）
# ============================================================================

class TargetLocator:
    """目标变量和行号定位器 - 改进版（处理多行表达式）"""
    
    @staticmethod
    def find_assignment_end_line(code, var_name):
        """找到变量赋值的结束行号（处理多行表达式）"""
        try:
            tree = ast.parse(code)
            
            assignments = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == var_name:
                            # 使用end_lineno获取多行语句的结束行
                            end_line = getattr(node, 'end_lineno', node.lineno)
                            assignments.append(end_line)
            
            return max(assignments) if assignments else None
                    
        except Exception as e:
            return None
    
    @staticmethod
    def find_print_variable(code):
        """从print语句中提取变量名"""
        lines = code.split('\n')
        
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i].strip()
            
            if line.startswith('print('):
                # f-string中的变量
                match = re.search(r'\{(\w+)\}', line)
                if match:
                    return match.group(1), i + 1
                
                # 逗号分隔
                match = re.search(r'print\([^,]+,\s*(\w+)\)', line)
                if match:
                    return match.group(1), i + 1
                
                # 直接打印
                match = re.search(r'print\((\w+)\)', line)
                if match:
                    return match.group(1), i + 1
        
        return None, None
    
    @staticmethod
    def locate_target(description, code):
        """改进的定位逻辑"""
        # 步骤1: 从print找变量
        target_var, print_line = TargetLocator.find_print_variable(code)
        
        if not target_var:
            print("  ✗ 无法从print语句中找到目标变量")
            return None, None, "No target variable"
        
        print(f"  ✓ 识别目标变量: {target_var}")
        
        # 步骤2: 用AST找赋值结束行
        target_line = TargetLocator.find_assignment_end_line(code, target_var)
        
        if target_line:
            print(f"  ✓ AST定位赋值结束行: {target_line}")
            return target_var, target_line, "AST located"
        
        # Fallback: print的前一个非空行
        lines = code.split('\n')
        for i in range(print_line - 2, -1, -1):
            if lines[i].strip() and not lines[i].strip().startswith('#'):
                target_line = i + 1
                print(f"  ⚠ 使用fallback行号: {target_line}")
                return target_var, target_line, "Fallback"
        
        return None, None, "Failed"


# ============================================================================
# 第六部分：主COT生成类
# ============================================================================

class CoTGenerator:
    """COT生成主类"""
    
    def __init__(self):
        self.dataset = None
        self.temp_dir = "temp_code"
        self.log_dir = "data/cot_logs"
        
        os.makedirs(self.temp_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
        
    def load_data(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def has_valid_cot(self, task_data):
        """检查是否已有有效的COT"""
        if "task" not in task_data:
            return False
            
        cot = task_data["task"].get("cot", "")
        
        if not cot or not cot.strip():
            return False
            
        if "API Error:" in cot or "Missing param" in cot:
            return False
            
        if len(cot.strip()) < 20:
            return False
            
        return True
    
    def generate_cot_for_task(self, task_data):
        """为单个任务生成COT"""
        task_id = task_data["id"]
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        answer = task_data["task"]["answer"]
        
        print(f"\n{'='*60}")
        print(f"生成COT: {task_id}")
        print(f"{'='*60}")
        
        # 步骤1: 定位目标
        print("\n[步骤1/4] 定位目标变量和行号...")
        target_var, target_line, reasoning = TargetLocator.locate_target(description, code)
        
        if not target_var or not target_line:
            print(f"  ✗ 定位失败")
            return None, None
        
        print(f"  ✓ 目标变量: {target_var}")
        print(f"  ✓ 目标行号: {target_line}")
        print(f"  ✓ 正确答案: {answer}")
        
        # 步骤2: 代码追踪
        print("\n[步骤2/4] 代码执行追踪...")
        temp_file = os.path.join(self.temp_dir, f"{task_id}.py")
        
        try:
            trace_output = CodeTracer.trace_code(code, temp_file)
            print(f"  ✓ 追踪完成，共 {len(trace_output)} 行")
        except Exception as e:
            print(f"  ✗ 追踪失败: {e}")
            return None, None
        
        # 步骤3: 智能剪枝
        print("\n[步骤3/4] 智能剪枝...")
        pruner = TracePruner(trace_output)
        pruner.parse_trace_lines(trace_output)
        
        try:
            pruned_lines = pruner.prune(target_line, target_var)
            print(f"  ✓ 剪枝完成，保留 {len(pruned_lines)} 行")
        except Exception as e:
            print(f"  ✗ 剪枝失败: {e}")
            return None, None
        
        # 步骤4: 生成COT
        print("\n[步骤4/4] 生成COT...")
        
        cot_gen_en = COTGenerator(pruned_lines, target_line, target_var, answer, lang='en')
        cot_en = cot_gen_en.generate()
        print(f"  ✓ 英文COT生成完成")
        
        cot_gen_zh = COTGenerator(pruned_lines, target_line, target_var, answer, lang='zh')
        cot_zh = cot_gen_zh.generate()
        print(f"  ✓ 中文COT生成完成")
        
        # 保存日志
        log_file = os.path.join(self.log_dir, f"{task_id}_cot.txt")
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"Task ID: {task_id}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("Chinese COT:\n")
            f.write("-" * 60 + "\n")
            f.write(cot_zh)
            f.write("\n\n")
            
            f.write("English COT:\n")
            f.write("-" * 60 + "\n")
            f.write(cot_en)
            f.write("\n")
        
        print(f"  ✓ 日志已保存: {log_file}")
        
        return cot_en, cot_zh
    
    def update_dataset_with_cot(self):
        """更新数据集"""
        self.load_data()
        
        generated_count = 0
        skipped_count = 0
        failed_count = 0
        
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            
            if "task" not in task:
                continue
                
            task_id = task["id"]
            
            if self.has_valid_cot(task):
                print(f"⏭ Task {task_id}: COT已存在，跳过")
                skipped_count += 1
                continue
            
            cot_en, cot_zh = self.generate_cot_for_task(task)
            
            if cot_en:
                self.dataset[i]["task"]["cot"] = cot_en
                print(f"✓ Task {task_id}: COT生成成功")
                generated_count += 1
            else:
                print(f"✗ Task {task_id}: COT生成失败")
                failed_count += 1
        
        # 保存数据集
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*60}")
        print("COT生成完成!")
        print(f"{'='*60}")
        print(f"  生成成功: {generated_count}")
        print(f"  跳过: {skipped_count}")
        print(f"  失败: {failed_count}")
        print(f"  数据集已更新: {DATASET_PATH}")
        print(f"  日志目录: {self.log_dir}/")


if __name__ == "__main__":
    generator = CoTGenerator()
    generator.update_dataset_with_cot()