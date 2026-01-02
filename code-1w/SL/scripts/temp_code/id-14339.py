def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    adjustment = 0.0
    total_points = 0
    performance_log = []
    intermediate_results = []

    for i, (test_id, score, category) in enumerate(data):
        normalized_score = score / 100.0
        category_weight = 1.1 if category == 'critical' else 0.9
        
        # Irrelevant logging computation
        log_entry = f"Test {test_id}: Raw={score}, Norm={normalized_score:.2f}"
        performance_log.append(log_entry)

        # Main scoring logic
        weighted_score = normalized_score * category_weight * base_multiplier
        
        # Distractor: unused conditional path
        if score < 0:
            raise ValueError("Invalid score")  # Never triggered
        
        # Simulate environmental interference (distractor)
        env_noise = (i % 3) * 0.01
        adjusted_score = weighted_score - env_noise
        
        # Actual contribution to result
        total_points += adjusted_score
        
        # Dead code: stored but not used
        intermediate_results.append((test_id, adjusted_score, env_noise))

        # Conditional bonus (only applies to high performers)
        if score > bonus_threshold:
            adjustment += 0.05

    # Secondary distraction: complex but irrelevant combinatorics
    n = len(data)
    max_possible_pairs = n * (n - 1) // 2 if n > 1 else 0
    pair_analysis = [0] * max_possible_pairs if max_possible_pairs > 0 else []

    # Core final calculation
    raw_performance = total_points * 100
    applied_adjustment = raw_performance * (1 + adjustment)
    final_score = int(applied_adjustment + 0.5)  # Round to nearest integer

    # Additional red herring: bitwise manipulation with no effect
    mask = 0xFF
    masked_result = final_score & mask
    dummy_check = (masked_result ^ 0xAA) | 0x55

    return final_score

# Simulated benchmark dataset
benchmark_data = [
    (101, 92, 'critical'),
    (102, 76, 'standard'),
    (103, 89, 'critical'),
    (104, 81, 'standard'),
    (105, 94, 'critical')
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")