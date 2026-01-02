def evaluate_performance(results, multiplier):
    score = 0
    penalty = 0
    bonus_applied = False

    temp_length_sum = 0  # Distractor: accumulates string lengths but not used in final logic
    for entry in results:
        temp_length_sum += len(entry['name'])

    for i, task in enumerate(results):
        name = task['name']
        status = task['status']
        complexity = task['complexity']

        base_points = len(name) * complexity
        if 'critical' in name.lower():
            base_points *= 2

        if status == 'completed':
            score += base_points
            if complexity >= 3:
                score += 5  # Bonus for high-complexity completion
                bonus_applied = True
        elif status == 'failed':
            penalty += complexity * 10

        # Irrelevant conditional branch (distractor)
        if i % 2 == 0 and len(name) > 6:
            temp_value = complexity ** 2
            temp_value -= 1  # Dead computation

    # Misleading intermediate calculation
    avg_length = temp_length_sum / len(results) if results else 0
    adjustment = int(avg_length) if avg_length > 5 else 0

    final_score = (score - penalty) * multiplier + adjustment

    # Additional red herring: tracking unused stats
    success_count = sum(1 for t in results if t['status'] == 'completed')
    if success_count >= 3:
        final_score += 10  # Real effect, but subtly integrated

    return final_score


def main():
    # Input data with meaningful structure
    task_results = [
        {'name': 'DataProcessor', 'status': 'completed', 'complexity': 4},
        {'name': 'ImageClassifier', 'status': 'failed', 'complexity': 5},
        {'name': 'critical_updater', 'status': 'completed', 'complexity': 3},
        {'name': 'Logger', 'status': 'completed', 'complexity': 2},
        {'name': 'Authenticator', 'status': 'failed', 'complexity': 4}
    ]

    base_multiplier = 1.5
    debug_mode = False  # Unused flag (distractor)

    # Simulate auxiliary pre-processing (irrelevant to final result)
    processed_names = [t['name'].upper().replace('_', '') for t in task_results]
    filtered_names = [n for n in processed_names if 'AUTH' not in n]

    final_score = evaluate_performance(task_results, base_multiplier)

    # Print result as required
    print(f"Target result: {final_score}")

if __name__ == '__main__':
    main()