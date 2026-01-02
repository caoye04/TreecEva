from collections import defaultdict

def main():
    # Simulate employee performance evaluation
    base_score = 74
    extra_tasks = 3
    penalty = 10

    # Calculate bonus points using dictionary aggregation
    task_weights = {'debugging': 2, 'review': 1, 'deployment': 3}
    task_log = ['debugging', 'debugging', 'review', 'deployment']
    
    task_counter = defaultdict(int)
    for task in task_log:
        task_counter[task] += 1

    bonus_points = 0
    for task, count in task_counter.items():
        bonus_points += count * task_weights[task]

    # Additional irrelevant tracking (minor interference)
    status_flags = {k: (v > 1) for k, v in task_counter.items()}
    total_tasks_completed = sum(task_counter.values())

    def calculate_performance(bp):
        raw = base_score + bp * 2
        if raw >= 90:
            return raw + 5
        elif raw >= 80:
            return raw + 2
        else:
            return raw - penalty

    final_score = calculate_performance(bonus_points)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()