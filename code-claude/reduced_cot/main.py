"""
COT生成框架主流程 - 重构版
支持数据集批量处理
"""

import argparse
from pathlib import Path
from dataset_processor import DatasetProcessor

# API配置
API_KEY = "sk-gq8qRNNiNIjS0x8tzfMl8F9bscL4wopT7oA2qD2FU8xKTrnp"
BASE_URL = "https://api.ezai88.com/v1"

AI_APIS = {
    "claude-3-7-sonnet-20250219": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "claude-3-7-sonnet-20250219"
    }
}


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='COT Generation Framework for TreecEva Dataset',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 批量提取所有目标信息
  python main.py --extract-targets
  
  # 写入所有代码文件
  python main.py --write-code
  
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
  
  # 完整流程：提取目标 -> 写入代码 -> 处理所有
  python main.py --extract-targets --write-code --all
        """
    )
    
    parser.add_argument(
        '--dataset',
        default='TreecEva_data_reduced_formated_cot.json',
        help='数据集JSON文件路径（默认: TreecEva_data_reduced_formated_cot.json）'
    )
    
    parser.add_argument(
        '--extract-targets',
        action='store_true',
        help='批量提取所有cases的目标信息到all-target-info.json'
    )
    
    parser.add_argument(
        '--write-code',
        action='store_true',
        help='将所有cases的代码写入temp_code目录'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='处理所有cases生成COT'
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
        '--force',
        action='store_true',
        help='强制重新处理（用于--extract-targets和--write-code）'
    )
    
    parser.add_argument(
        '--model',
        default='claude-3-7-sonnet-20250219',
        choices=list(AI_APIS.keys()),
        help='使用的AI模型'
    )
    
    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        help='并行处理的worker数量（默认: 4）'
    )
    
    args = parser.parse_args()
    
    # 检查参数
    if not any([args.extract_targets, args.write_code, args.all, args.case]):
        parser.print_help()
        print("\n错误: 必须指定至少一个操作: --extract-targets, --write-code, --all, 或 --case")
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
        api_config=api_config,
        max_workers=args.workers
    )
    
    # 执行操作
    if args.extract_targets:
        processor.extract_all_targets(force=args.force)
    
    if args.write_code:
        processor.write_code_files(force=args.force)
    
    if args.all:
        processor.process_all_cases(skip_existing=not args.no_skip)
    elif args.case:
        processor.process_case_by_id(args.case)


if __name__ == '__main__':
    main()


#     # 完整流程
# python main.py --extract-targets --write-code --all

# # 只提取目标
# python main.py --extract-targets

# # 处理单个case
# python main.py --case SL-MIX-S0001

# # 使用不同模型
# python main.py --all --model qwen3_coder