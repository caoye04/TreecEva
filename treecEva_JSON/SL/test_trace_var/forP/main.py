"""
COT生成框架主流程
"""

import os
import argparse
from tracer import PythonTracer
from pruner import TracePruner
from cot_generator import COTGenerator
# from reverse_cot_generator import ReverseCOTGenerator # 注释掉了


class COTFramework:
    """COT生成框架主类"""
    
    def __init__(self, source_file, target_line, target_var, generate_zh=False):
        self.source_file = source_file
        self.target_line = target_line
        self.target_var = target_var
        self.generate_zh = generate_zh # 新增
        
        # 生成文件名和目录
        base_name = os.path.splitext(os.path.basename(source_file))[0]
        self.data_dir = f"data_{base_name}"
        
        # 创建数据目录
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 生成文件路径（存放在data目录中）
        self.trace_file = os.path.join(self.data_dir, f"trace_{base_name}.txt")
        self.pruned_file = os.path.join(self.data_dir, f"trimmed_trace_{base_name}.txt")
        # 默认英文COT文件
        self.cot_file = os.path.join(self.data_dir, f"final_cot_{base_name}.txt") 
        # 新增：中文COT文件路径
        self.cot_file_zh = os.path.join(self.data_dir, f"final_zh_cot_{base_name}.txt")
        # self.reverse_cot_file = os.path.join(self.data_dir, f"reverse_cot_{base_name}.txt")
    
    def run(self):
        """执行完整流程"""
        print("=" * 60)
        print("COT Generation Framework")
        print("=" * 60)
        
        # 步骤1: 代码执行追踪
        print("\n[Step 1/4] Code Execution Tracing...")
        print(f"  Source File: {self.source_file}")
        print(f"  Data Directory: {self.data_dir}/")
        PythonTracer.trace_file(self.source_file, self.trace_file)
        print(f"  ✓ Trace complete, output: {self.trace_file}")
        
        # 步骤2: 目标定位
        print("\n[Step 2/4] Target Localization...")
        print(f"  Target Line: {self.target_line}")
        print(f"  Target Variable: {self.target_var}")
        print(f"  ✓ Target locked")
        
        # 步骤3: 智能回溯与剪枝
        print("\n[Step 3/4] Smart Backtracking & Pruning...")
        TracePruner.prune_trace(
            self.trace_file, 
            self.target_line, 
            self.target_var, 
            self.pruned_file,
            source_file=self.source_file
        )
        print(f"  ✓ Pruning complete, output: {self.pruned_file}")
        
        # 步骤4: 模板化COT生成 (English - 默认)
        print("\n[Step 4/4] Generating COT (English)...")
        COTGenerator.generate_cot(self.pruned_file, self.cot_file, lang='en')
        print(f"  ✓ English COT generated: {self.cot_file}")
        
        # [新增] 步骤5: 模板化COT生成 (Chinese - 可选)
        if self.generate_zh:
            print("\n[Bonus Step] Generating COT (Chinese)...")
            COTGenerator.generate_cot(self.pruned_file, self.cot_file_zh, lang='zh')
            print(f"  ✓ Chinese COT generated: {self.cot_file_zh}")
        
        # 显示结果
        print("\n" + "=" * 60)
        print("Generation Complete!")
        print("=" * 60)
        print(f"\nData Directory: {self.data_dir}/")
        print(f"  ├── {os.path.basename(self.trace_file)}")
        print(f"  ├── {os.path.basename(self.pruned_file)}")
        print(f"  ├── {os.path.basename(self.cot_file)} (English)")
        if self.generate_zh:
            print(f"  └── {os.path.basename(self.cot_file_zh)} (Chinese)")
        
        # 显示英文COT内容
        print("\n" + "-" * 60)
        print("English COT Preview:")
        print("-" * 60)
        with open(self.cot_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        # 显示中文COT内容
        if self.generate_zh:
            print("\n" + "-" * 60)
            print("Chinese COT Preview:")
            print("-" * 60)
            with open(self.cot_file_zh, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        
        return self.cot_file


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='COT Generation Framework')
    parser.add_argument('source_file', help='Python source code file')
    parser.add_argument('target_line', type=int, help='Target line number')
    parser.add_argument('target_var', help='Target variable name')
    # 新增 --zh 参数
    parser.add_argument('--zh', action='store_true', help='Generate an additional Chinese (zh) COT file')
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.source_file):
        print(f"Error: File '{args.source_file}' not found.")
        return
    
    # 运行框架
    framework = COTFramework(
        args.source_file, 
        args.target_line, 
        args.target_var, 
        generate_zh=args.zh  # 传递参数
    )
    framework.run()


if __name__ == '__main__':
    # 示例用法（无参数时）
    import sys
    if len(sys.argv) == 1:
        print("Example Usage:")
        print("  python main.py test.py 7 d")
        print("  python main.py test.py 7 d --zh  (To generate Chinese version too)")
        print("\nRunning example...")
        
        # 创建示例文件
        with open('test.py', 'w', encoding='utf-8') as f:
            f.write("""a = 1
b = 2
c = a + b
d = 1
for i in range(2):
    d = d + 1
d = d + a
""")
        
        # 运行不带 --zh 的示例
        print("\n--- Running EN-only example ---")
        framework_en = COTFramework('test.py', 7, 'd', generate_zh=False)
        framework_en.run()
        
        # 运行带 --zh 的示例
        print("\n--- Running EN + ZH example ---")
        framework_zh = COTFramework('test.py', 7, 'd', generate_zh=True)
        framework_zh.run()
    else:
        main()