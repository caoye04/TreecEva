def calculate_performance(data):
    base_multiplier = 1.5
    adjustment_factor = 0.9
    temp_results = []
    cumulative_offset = 0
    
    for i, (value, weight) in enumerate(zip(data['metrics'], data['weights'])):
        if value < 0:
            continue
        
        # Irrelevant transformation (distractor)
        transformed = (value ** 0.5) * (i + 1)
        normalized = value * weight * base_multiplier
        
        # Only even-indexed values contribute to final score
        if i % 2 == 0:
            temp_results.append(normalized)
        else:
            cumulative_offset += value // 2
    
    # Distractor: unused computation
    avg_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    offset_correction = cumulative_offset * adjustment_factor
    
    # Actual logic: sum of valid normalized scores, adjusted by index-based bonus
    index_bonus = sum(0.1 * idx for idx, _ in enumerate(temp_results))
    raw_score = sum(temp_results)
    final_score = raw_score + index_bonus
    
    # Red herring: complex but unused expression
    theoretical_max = base_multiplier * sum(data['weights']) * max(data['metrics'])
    efficiency_ratio = raw_score / theoretical_max if theoretical_max else 0
    
    return final_score

# Input data
benchmark_data = {
    'metrics': [8, -3, 12, 7, 4],
    'weights': [0.2, 0.4, 0.6, 0.3, 0.5]
}

initial_state = {'status': 'active', 'version': '2.1'}
config_options = {'debug': False, 'strict_mode': True}

# Execution
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")