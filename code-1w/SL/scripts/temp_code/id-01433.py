def evaluate_performance(feedbacks, benchmarks):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Irrelevant data processing (distractor)
    temp_analysis = [len(str(x)) for x in benchmarks if x > 0]
    avg_length = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    feedback_set = set(feedbacks)
    benchmark_data = {i: val for i, val in enumerate(benchmarks)}
    
    # Real logic begins
    for idx, value in enumerate(benchmarks):
        if value in feedback_set:
            base_score += value // 3
        if idx % 2 == 0 and value < 50:
            penalty_adjustment -= 2
    
    # Use of zip and enumerate together (python idiom)
    for i, (k, v) in enumerate(zip(benchmark_data.keys(), benchmark_data.values())):
        if i + v > 75:
            bonus_tracker.append(i * 1.5)
    
    # Misleading complex-looking but unused calculation
    phantom_score = sum([x ** 0.5 for x in benchmarks if x % 4 == 0]) * 0.1
    shadow_buffer = [x for x in feedbacks if str(x).endswith('5')]
    
    # Actual contribution to final result
    valid_bonuses = len([b for b in bonus_tracker if b > 5])
    final_score = base_score + penalty_adjustment + valid_bonuses
    
    # Print required at the end
    print(f"Result: {final_score}")
    return final_score

# Input data
feedbacks = [12, 18, 27, 36, 45]
benchmarks = [9, 18, 25, 36, 44, 50]
evaluate_performance(feedbacks, benchmarks)