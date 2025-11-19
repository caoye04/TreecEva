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