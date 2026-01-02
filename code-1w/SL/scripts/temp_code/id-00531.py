def analyze_efficiency(values):
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg, variance

# Simulate system performance metrics
task_load = [12, 15, 18, 20, 14, 16]
response_times = [95, 102, 88, 110, 97, 105]
error_rates = [0.02, 0.01, 0.03, 0.02, 0.01, 0.04]

baseline, variation = analyze_efficiency(response_times)
threshold = int(baseline // 10 * 1.5)

efficiency_map = {}
for i, load in enumerate(task_load):
    key = f'load_{load}'
    efficiency_map[key] = baseline / (load + 1) if i % 2 == 0 else baseline / (load + 2)

# Prepare metrics dictionary with various stats
metrics = {
    'avg_response': baseline,
    'stability': 100 - variation,
    'peak_load': max(task_load),
    'total_tasks': sum(task_load),
    'error_trend': sum(1 for e in error_rates if e > 0.02),
    'efficiency_lookup': efficiency_map
}

# Misleading intermediate calculations
phantom_score = 0
for rt in response_times:
    if rt < threshold * 8:
        phantom_score += 1
phantom_score *= threshold

# Auxiliary function to compute final score
def process_performance(data, limit):
    score = 0
    score += int(data['avg_response'] // 5)
    
    high_load_bonus = 10 if data['peak_load'] > 15 else 5
    score += high_load_bonus
    
    # Use string method to extract digits from keys
    valid_keys = [k for k in data['efficiency_lookup'].keys() if 'load_' in k]
    load_numbers = [int(k.replace('load_', '')) for k in valid_keys]
    total_filtered_load = sum(l for l in load_numbers if l >= limit)
    
    # Accumulate based on filtered load
    accumulation = 0
    for num in sorted(load_numbers):
        if num >= limit:
            accumulation += num // 3
    
    # Apply combinatorics: number of ways to pick 2 tasks from error trend
    errors_above_threshold = data['error_trend']
    combinations = (errors_above_threshold * (errors_above_threshold - 1)) // 2 if errors_above_threshold >= 2 else 0
    
    # Final computation
    score += accumulation
    score -= combinations  # penalty for too many errors
    
    # Dead code - never executed but looks relevant
    # if limit < 0:
    #     score = 0
    
    return score

# Execute main logic
final_score = process_performance(metrics, threshold)

# Print result as required
print(f"Target result: {final_score}")