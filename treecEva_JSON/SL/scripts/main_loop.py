import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.execute_tasks import TaskExecutor
from scripts.generate_cot import CoTGenerator
from scripts.ai_evaluation import AIEvaluator
from scripts.generate_new_task import TaskGenerator

def run_execute_only():
    """只执行任务代码并生成答案"""
    print("=== Executing tasks only ===")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    print("✓ Task execution completed")

def run_cot_only():
    """只生成思维链(CoT)"""
    print("=== Generating chain of thought only ===")
    cot_generator = CoTGenerator()
    cot_generator.update_dataset_with_cot()
    print("✓ CoT generation completed")

def run_evaluation_only():
    """只评估AI模型正确性"""
    print("=== Running AI evaluation only ===")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()
    print("✓ AI evaluation completed")

def run_generate_task_only(num_tasks=1):
    """只生成新任务"""
    print(f"=== Generating {num_tasks} new task(s) only ===")
    
    successful_generations = 0
    task_generator = TaskGenerator()
    
    for i in range(num_tasks):
        print(f"\nGenerating task {i+1}/{num_tasks}...")
        try:
            new_task = task_generator.generate_and_validate_task()
            if new_task:
                successful_generations += 1
                print(f"✓ Task {i+1} generated successfully (ID: {new_task['id']})")
            else:
                print(f"✗ Task {i+1} generation failed")
        except Exception as e:
            print(f"✗ Task {i+1} generation failed with error: {e}")
    
    print(f"\n=== Generation Summary ===")
    print(f"Successfully generated: {successful_generations}/{num_tasks} tasks")
    return successful_generations > 0

def run_single_cycle():
    """运行一个完整的循环"""
    print("=== Starting new cycle ===")
    
    # 1. 执行任务
    print("\n1. Executing tasks...")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    
    # 2. 生成思维链
    print("\n2. Generating chain of thought...")
    cot_generator = CoTGenerator()
    cot_generator.update_dataset_with_cot()
    
    # 3. AI评估
    print("\n3. Running AI evaluation...")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()
    
    # 4. 生成新任务
    print("\n4. Generating new task...")
    task_generator = TaskGenerator()
    new_task = task_generator.generate_and_validate_task()
    
    print("\n=== Cycle completed ===")
    return new_task is not None

def run_multiple_cycles(num_cycles=5):
    """运行多个循环"""
    print(f"Starting {num_cycles} cycles of task generation and evaluation...")
    
    successful_cycles = 0
    for i in range(num_cycles):
        print(f"\n{'='*50}")
        print(f"CYCLE {i+1}/{num_cycles}")
        print(f"{'='*50}")
        
        try:
            success = run_single_cycle()
            if success:
                successful_cycles += 1
                print(f"✓ Cycle {i+1} completed successfully")
            else:
                print(f"✗ Cycle {i+1} failed")
        except Exception as e:
            print(f"✗ Cycle {i+1} failed with error: {e}")
    
    print(f"\n{'='*50}")
    print(f"SUMMARY: {successful_cycles}/{num_cycles} cycles completed successfully")
    print(f"{'='*50}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run the complete task generation and evaluation pipeline")
    
    # 单独执行选项
    parser.add_argument("--execute", action="store_true", help="Only execute tasks and generate answers")
    parser.add_argument("--cot", action="store_true", help="Only generate chain of thought")
    parser.add_argument("--evaluate", action="store_true", help="Only run AI evaluation")
    parser.add_argument("--generate", type=int, nargs='?', const=1, help="Only generate new tasks (specify number, default=1)")
    
    # 完整流程选项
    parser.add_argument("--single", action="store_true", help="Run a single complete cycle")
    parser.add_argument("--cycles", type=int, default=1, help="Number of cycles to run")
    
    args = parser.parse_args()
    
    try:
        # 单独执行选项（互斥）
        if args.execute:
            run_execute_only()
        elif args.cot:
            run_cot_only()
        elif args.evaluate:
            run_evaluation_only()
        elif args.generate is not None:
            run_generate_task_only(args.generate)
        elif args.single:
            run_single_cycle()
        else:
            # 默认行为：运行指定数量的完整循环
            run_multiple_cycles(args.cycles)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error occurred: {e}")
        sys.exit(1)