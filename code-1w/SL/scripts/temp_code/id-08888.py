def evaluate_performance(results, weights):
    # Normalize weights to ensure they sum to 1.0
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    # Extract performance metrics
    success_count = sum(1 for r in results if r['status'] == 'success')
    failure_count = len(results) - success_count
    completion_rate = success_count / len(results)

    # Compute weighted score based on task difficulty and outcome
    raw_scores = []
    for i, res in enumerate(results):
        base_score = 10 if res['status'] == 'success' else -5
        difficulty_bonus = res['difficulty'] * 2
        time_penalty = 0
        if res['elapsed_time'] > res['time_limit']:
            time_penalty = 3
        
        # Irrelevant computation: tracking phase contributions (not used in final score)
        phase_contribution = f"Phase-{res['phase']}: {base_score + difficulty_bonus - time_penalty}"
        raw_scores.append(base_score + difficulty_bonus - time_penalty)

    # Distractor: unused aggregation methods
    median_score = sorted(raw_scores)[len(raw_scores)//2]
    max_possible = max(raw_scores)
    min_possible = min(raw_scores)
    average_raw = sum(raw_scores) / len(raw_scores)

    # Actual scoring uses weighted average of raw scores
    weighted_sum = sum(raw_scores[i] * normalized_weights[i] for i in range(len(raw_scores)))

    # Additional distraction: string processing for log (not affecting result)
    log_tag = "PERF-REPORT"
    tag_suffix = log_tag.lower().replace('-', '_')[4:]
    metadata_str = f"{log_tag}_{tag_suffix.upper()}_{len(results)}"
    padding_length = 20 - len(metadata_str)
    padded_metadata = metadata_str + '*' * padding_length

    # Final adjustment: bonus if completion rate > threshold
    bonus_applied = False
    if completion_rate >= 0.75:
        weighted_sum += 8
        bonus_applied = True

    # Dead code path: never executed due to logic above
    if bonus_applied and weighted_sum > 100:
        weighted_sum = 100  # Capping (unreachable in this case)

    return int(weighted_sum)

# Main execution block
if __name__ == '__main__':
    # Simulated task results from system workflow
    task_results = [
        {'status': 'success', 'difficulty': 3, 'elapsed_time': 120, 'time_limit': 150, 'phase': 'alpha'},
        {'status': 'success', 'difficulty': 5, 'elapsed_time': 180, 'time_limit': 180, 'phase': 'beta'},
        {'status': 'failure', 'difficulty': 4, 'elapsed_time': 200, 'time_limit': 160, 'phase': 'beta'},
        {'status': 'success', 'difficulty': 2, 'elapsed_time': 90, 'time_limit': 100, 'phase': 'gamma'},
        {'status': 'success', 'difficulty': 5, 'elapsed_time': 220, 'time_limit': 250, 'phase': 'gamma'}
    ]

    # Base importance weights for each task (arbitrary but fixed)
    base_weights = [1, 2, 1, 2, 3]

    # Tracking auxiliary stats (distractors)
    total_tasks = len(task_results)
    unique_phases = set(r['phase'] for r in task_results)
    phase_count = len(unique_phases)

    # Key statement
    final_score = evaluate_performance(task_results, base_weights)
    
    # Print result as required
    print(f"Result: {final_score}")