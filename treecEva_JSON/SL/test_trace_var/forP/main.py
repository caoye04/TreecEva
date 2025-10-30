"""
COT生成框架主流程
"""

import os
import argparse
from tracer import PythonTracer
from pruner import TracePruner
from cot_generator import COTGenerator


class COTFramework:
    """COT生成框架主类"""
    
    def __init__(self, source_file, target_line, target_var):
        self.source_file = source_file
        self.target_line = target_line
        self.target_var = target_var
        
        # 生成文件名和目录
        base_name = os.path.splitext(os.path.basename(source_file))[0]
        self.data_dir = f"data_{base_name}"
        
        # 创建数据目录
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 生成文件路径（存放在data目录中）
        self.trace_file = os.path.join(self.data_dir, f"trace_{base_name}.txt")
        self.pruned_file = os.path.join(self.data_dir, f"trimmed_trace_{base_name}.txt")
        self.cot_file = os.path.join(self.data_dir, f"final_cot_{base_name}.txt")
    
    def run(self):
        """执行完整流程"""
        print("=" * 60)
        print("COT生成框架")
        print("=" * 60)
        
        # 步骤1: 代码执行追踪
        print("\n[步骤1/4] 代码执行追踪...")
        print(f"  源文件: {self.source_file}")
        print(f"  数据目录: {self.data_dir}/")
        PythonTracer.trace_file(self.source_file, self.trace_file)
        print(f"  ✓ 追踪完成，输出: {self.trace_file}")
        
        # 步骤2: 目标定位
        print("\n[步骤2/4] 目标定位...")
        print(f"  目标行号: {self.target_line}")
        print(f"  目标变量: {self.target_var}")
        print(f"  ✓ 目标已确定")
        
        # 步骤3: 智能回溯与剪枝
        print("\n[步骤3/4] 智能回溯与剪枝...")
        TracePruner.prune_trace(self.trace_file, self.target_line, 
                               self.target_var, self.pruned_file)
        print(f"  ✓ 剪枝完成，输出: {self.pruned_file}")
        
        # 步骤4: 模板化COT生成
        print("\n[步骤4/4] 模板化COT生成...")
        COTGenerator.generate_cot(self.pruned_file, self.cot_file)
        print(f"  ✓ COT生成完成，输出: {self.cot_file}")
        
        # 显示结果
        print("\n" + "=" * 60)
        print("生成完成！")
        print("=" * 60)
        print(f"\n数据目录: {self.data_dir}/")
        print(f"  ├── {os.path.basename(self.trace_file)}")
        print(f"  ├── {os.path.basename(self.pruned_file)}")
        print(f"  └── {os.path.basename(self.cot_file)}")
        
        # 显示COT内容
        print("\n" + "-" * 60)
        print("COT内容预览:")
        print("-" * 60)
        with open(self.cot_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        return self.cot_file


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='COT生成框架')
    parser.add_argument('source_file', help='Python源代码文件')
    parser.add_argument('target_line', type=int, help='目标行号')
    parser.add_argument('target_var', help='目标变量名')
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.source_file):
        print(f"错误: 文件 '{args.source_file}' 不存在")
        return
    
    # 运行框架
    framework = COTFramework(args.source_file, args.target_line, args.target_var)
    framework.run()


if __name__ == '__main__':
    # 示例用法（无参数时）
    import sys
    if len(sys.argv) == 1:
        print("示例用法:")
        print("  python main.py test.py 7 d")
        print("\n正在运行示例...")
        
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
        
        framework = COTFramework('test.py', 7, 'd')
        framework.run()
    else:
        main()