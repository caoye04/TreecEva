import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.execute_tasks import TaskExecutor
from scripts.generate_cot import CoTGenerator
from scripts.ai_evaluation import AIEvaluator
from scripts.generate_new_task import TaskGenerator

def run_execute_only():
    """只执行任务代码并生成答案"""
    print("\n" + "="*70)
    print("EXECUTING TASKS ONLY")
    print("="*70)
    executor = TaskExecutor()
    executor.execute_all_tasks()
    print("✓ Task execution completed\n")

def run_cot_only(api_name="qwen3_coder", skip_existing=True, specific_tasks=None):
    """只生成思维链(CoT)"""
    print("\n" + "="*70)
    print("GENERATING CHAIN OF THOUGHT ONLY")
    print("="*70)
    cot_generator = CoTGenerator()
    
    if specific_tasks:
        # 重新生成特定任务
        cot_generator.regenerate_specific_tasks(specific_tasks, api_name=api_name)
    else:
        # 生成所有任务的CoT
        result = cot_generator.update_dataset_with_cot(
            api_name=api_name,
            skip_existing=skip_existing
        )
        print(f"✓ CoT generation completed: {result['successful']} successful, "
              f"{result['failed']} failed, {result['skipped']} skipped\n")

def run_evaluation_only(evaluate_mode="unrated"):
    """
    只评估AI模型正确性
    
    Args:
        evaluate_mode: 评估模式
            - "all": 评估所有任务
            - "unrated": 只评估难度为-1的未评估任务（默认）
    """
    print("\n" + "="*70)
    print(f"RUNNING AI EVALUATION ONLY (Mode: {evaluate_mode.upper()})")
    print("="*70)
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks(evaluate_mode=evaluate_mode)
    print("✓ AI evaluation completed\n")

def run_generate_task_only(num_tasks=1):
    """只生成新任务"""
    print("\n" + "="*70)
    print(f"GENERATING {num_tasks} NEW TASK(S) ONLY")
    print("="*70)
    
    successful_generations = 0
    task_generator = TaskGenerator()
    
    for i in range(num_tasks):
        print(f"\n[Task {i+1}/{num_tasks}]")
        try:
            new_task = task_generator.generate_and_validate_task()
            if new_task:
                successful_generations += 1
                print(f"✓ Task {i+1} generated successfully (ID: {new_task['id']})")
            else:
                print(f"✗ Task {i+1} generation failed")
        except Exception as e:
            print(f"✗ Task {i+1} generation failed with error: {e}")
    
    print(f"\n{'='*70}")
    print(f"GENERATION SUMMARY: {successful_generations}/{num_tasks} tasks generated")
    print(f"{'='*70}\n")
    return successful_generations > 0

def run_single_cycle(cot_api="qwen3_coder", cot_skip_existing=True, 
                     eval_mode="unrated"):
    """
    运行一个完整的循环
    
    Args:
        cot_api: CoT生成使用的API
        cot_skip_existing: 是否跳过已存在的CoT
        eval_mode: 评估模式 ("all" 或 "unrated")
    """
    print("\n" + "="*70)
    print("STARTING NEW COMPLETE CYCLE")
    print("="*70)
    
    # 1. 执行任务
    print("\n[1/4] Executing tasks...")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    
    # 2. 生成思维链
    print("\n[2/4] Generating chain of thought...")
    cot_generator = CoTGenerator()
    cot_result = cot_generator.update_dataset_with_cot(
        api_name=cot_api,
        skip_existing=cot_skip_existing
    )
    print(f"CoT: {cot_result['successful']} successful, "
          f"{cot_result['failed']} failed, {cot_result['skipped']} skipped")
    
    # 3. AI评估
    print(f"\n[3/4] Running AI evaluation (mode: {eval_mode})...")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks(evaluate_mode=eval_mode)
    
    # 4. 生成新任务
    print("\n[4/4] Generating new task...")
    task_generator = TaskGenerator()
    new_task = task_generator.generate_and_validate_task()
    
    print("\n" + "="*70)
    print("CYCLE COMPLETED")
    print("="*70 + "\n")
    return new_task is not None

def run_multiple_cycles(num_cycles=5, cot_api="qwen3_coder", 
                       cot_skip_existing=True, eval_mode="unrated"):
    """
    运行多个循环
    
    Args:
        num_cycles: 循环次数
        cot_api: CoT生成使用的API
        cot_skip_existing: 是否跳过已存在的CoT
        eval_mode: 评估模式 ("all" 或 "unrated")
    """
    print(f"\n{'='*70}")
    print(f"STARTING {num_cycles} COMPLETE CYCLES")
    print(f"{'='*70}\n")
    
    successful_cycles = 0
    for i in range(num_cycles):
        print(f"\n{'#'*70}")
        print(f"# CYCLE {i+1}/{num_cycles}")
        print(f"{'#'*70}")
        
        try:
            success = run_single_cycle(
                cot_api=cot_api,
                cot_skip_existing=cot_skip_existing,
                eval_mode=eval_mode
            )
            if success:
                successful_cycles += 1
                print(f"✓ Cycle {i+1} completed successfully")
            else:
                print(f"✗ Cycle {i+1} failed")
        except Exception as e:
            print(f"✗ Cycle {i+1} failed with error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"ALL CYCLES COMPLETED")
    print(f"{'='*70}")
    print(f"Success Rate: {successful_cycles}/{num_cycles} cycles")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run the complete task generation and evaluation pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 运行单个完整循环（只评估未评估的任务）
  python main_loop.py --single
  
  # 运行单个循环并评估所有任务
  python main_loop.py --single --eval-all
  
  # 运行5个循环
  python main_loop.py --cycles 5
  
  # 只执行代码
  python main_loop.py --execute
  
  # 只生成CoT（使用特定API）
  python main_loop.py --cot --cot-api qwen3_235b
  
  # 重新生成所有CoT（包括已存在的）
  python main_loop.py --cot --no-skip-cot
  
  # 重新生成特定任务的CoT
  python main_loop.py --cot --cot-tasks SL-MIX-S001 SL-MIX-S002
  
  # 只评估未评估的任务（默认）
  python main_loop.py --evaluate
  
  # 评估所有任务
  python main_loop.py --evaluate --eval-all
  
  # 只生成10个新任务
  python main_loop.py --generate 10
        """
    )
    
    # 单独执行选项
    parser.add_argument("--execute", action="store_true", 
                       help="Only execute tasks and generate answers")
    parser.add_argument("--cot", action="store_true", 
                       help="Only generate chain of thought")
    parser.add_argument("--evaluate", action="store_true", 
                       help="Only run AI evaluation")
    parser.add_argument("--generate", type=int, nargs='?', const=1, metavar='N',
                       help="Only generate N new tasks (default=1)")
    
    # CoT相关参数
    parser.add_argument("--cot-api", type=str, default="qwen3_coder",
                       help="API to use for CoT generation (default: qwen3_coder)")
    parser.add_argument("--no-skip-cot", action="store_true",
                       help="Regenerate CoT even if it already exists")
    parser.add_argument("--cot-tasks", nargs='+', metavar='TASK_ID',
                       help="Specific task IDs to regenerate CoT for")
    
    # 评估相关参数（新增）
    parser.add_argument("--eval-all", action="store_true",
                       help="Evaluate ALL tasks (default: only unrated tasks with difficulty=-1)")
    
    # 完整流程选项
    parser.add_argument("--single", action="store_true", 
                       help="Run a single complete cycle")
    parser.add_argument("--cycles", type=int, default=1, metavar='N',
                       help="Number of complete cycles to run (default=1)")
    
    args = parser.parse_args()
    
    # 确定评估模式
    eval_mode = "all" if args.eval_all else "unrated"
    
    try:
        # 单独执行选项（互斥）
        if args.execute:
            run_execute_only()
        elif args.cot:
            run_cot_only(
                api_name=args.cot_api,
                skip_existing=not args.no_skip_cot,
                specific_tasks=args.cot_tasks
            )
        elif args.evaluate:
            run_evaluation_only(evaluate_mode=eval_mode)
        elif args.generate is not None:
            run_generate_task_only(args.generate)
        elif args.single:
            run_single_cycle(
                cot_api=args.cot_api,
                cot_skip_existing=not args.no_skip_cot,
                eval_mode=eval_mode
            )
        else:
            # 默认行为：运行指定数量的完整循环
            run_multiple_cycles(
                num_cycles=args.cycles,
                cot_api=args.cot_api,
                cot_skip_existing=not args.no_skip_cot,
                eval_mode=eval_mode
            )
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)