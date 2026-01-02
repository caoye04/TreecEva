from collections import defaultdict

# Simulated benchmark data across multiple test phases
test_phases = ['phase_a', 'phase_b', 'phase_c']
raw_data = [78, 92, 85, 67, 96, 88, 73]

# Misleading data structures (distractor)
stats_summary = defaultdict(int)
for val in raw_data:
    stats_summary['total'] += val
    if val > 80:
        stats_summary['high_count'] += 1

# Auxiliary processing with red herring calculations
adjusted_values = [x * 1.1 for x in raw_data if x < 90]
penalty_factor = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0

# Core logic embedded within noise
benchmark_results = []
counter = 0
for i, phase in enumerate(test_phases):
    phase_data = []
    for j in range(i + 1, i + 4):
        if j < len(raw_data):
            # Apply non-linear transformation
            transformed = (raw_data[j] ** 0.5) * (i + 1)
            phase_data.append(int(transformed))
    
    # Compute phase aggregate using conditional logic
    if len(phase_data) >= 2:
        mid_val = phase_data[len(phase_data)//2]
        max_val = max(phase_data)
        min_val = min(phase_data)
        # Weighted score with dummy weight variables
        weight_a = 0.4
        weight_b = 0.3
        weight_c = 0.3
        weighted_avg = weight_a * mid_val + weight_b * max_val + weight_c * min_val
        counter += 1
    else:
        weighted_avg = 0
    
    # Store structured result (only 'score' is used later)
    benchmark_results.append({
        'phase': phase,
        'data': phase_data,
        'score': int(weighted_avg),
        'outlier_flag': False  # unused field
    })

# Distractor: Unused function that looks important
def analyze_trend(data_list):
    trend_scores = []
    for entry in data_list:
        trend_scores.append(entry['score'] * 0.1)
    return sum(trend_scores)

# Real computation begins here — hidden among distractions
def calculate_performance(results):
    total = 0
    for item in results:
        score = item['score']
        # Boolean logic filter: only count scores passing multiple conditions
        condition_1 = (score & 1) == 0  # even numbers only
        condition_2 = score > 15
        condition_3 = (score % 3) != 0  # not divisible by 3
        
        if condition_1 and condition_2 and not condition_3:
            total += score
        elif condition_1 and condition_2:
            total += score // 2
        else:
            total -= score // 4  # small penalty
    return total + len(results)  # final adjustment

# Critical execution point
final_score = calculate_performance(benchmark_results)

# Print result as required
print(f"Result: {final_score}")