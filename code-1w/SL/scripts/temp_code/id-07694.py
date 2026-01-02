def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data if x['active']]
    offsets = [x % 7 for x in range(len(raw_values))]
    adjusted_values = []
    
    for i, val in enumerate(raw_values):
        temp_adjust = val + offsets[i] - 3
        if temp_adjust > 0:
            adjusted_values.append(temp_adjust)
    
    # Irrelevant distraction: noise computation
    noise_accumulator = 0
    for x in raw_values:
        noise_accumulator += (x ** 2) % 5
    noise_accumulator = (noise_accumulator * 0.1) // 1  # Unused in final logic
    
    # Core logic: windowed average and threshold filter
    window_size = 3
    filtered_scores = []
    for i in range(len(adjusted_values) - window_size + 1):
        window_avg = sum(adjusted_values[i:i+window_size]) / window_size
        if window_avg >= 5.0:
            filtered_scores.append(window_avg * 2)
    
    # Secondary distraction: tracking state that isn't used
    max_seen = -float('inf')
    stable_runs = 0
    for score in filtered_scores:
        if score > max_seen:
            max_seen = score
        if abs(score - max_seen) < 1e-5:
            stable_runs += 1
    
    # Final aggregation
    base_score = sum(filtered_scores) if filtered_scores else 0
    penalty = len(raw_values) - len(adjusted_values)  # Penalty for negative adjustments
    final_score = int(base_score - penalty * 2)
    
    return final_score

# Input data setup
benchmark_data = [
    {'metric': 4, 'active': True},
    {'metric': 2, 'active': True},
    {'metric': 6, 'active': True},
    {'metric': 8, 'active': False},  # Inactive, should be skipped
    {'metric': 5, 'active': True},
    {'metric': 3, 'active': True},
    {'metric': 7, 'active': True}
]

# Execution entry point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")