from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 105, 130, 90, 115, 140, 95]
    processed = defaultdict(int)
    temp_buffer = [x * 0.8 for x in raw_data]  # Normalize readings

    for idx, val in enumerate(temp_buffer):
        if idx % 2 == 0:
            processed['even_index_sum'] += val
        else:
            processed['odd_index_sum'] += val

    # Distractor computation: irrelevant average
    fake_avg = sum(temp_buffer) / len(temp_buffer) * 0.95
    scaling_factor = 1.1  # Unused distraction

    return dict(processed)

def calculate_baseline(data):
    # Irrelevant baseline calculation (not used in final logic)
    base = 0
    for k, v in data.items():
        base += len(k) % 3
    return base * 2.5

def apply_correction(values):
    # Corrective scaling based on empirical factors
    correction_map = {0: 1.0, 1: 0.98, 2: 1.02, 3: 0.99, 4: 1.01}
    corrected = []
    for i, v in enumerate(values):
        key = i % 5
        corrected.append(v * correction_map[key])
    return corrected

def compute_weighted_parts(even_sum, odd_sum):
    # Real computation branch
    part_a = even_sum * 1.2
    part_b = odd_sum * 0.85
    
    # Distractor: unused path
    if part_a > 1000:
        buffer_overflow_sim = part_a / 100

    return part_a, part_b

def evaluate_performance(metrics, weights):
    # Extract relevant metrics
    even_sum = metrics.get('even_index_sum', 0)
    odd_sum = metrics.get('odd_index_sum', 0)
    
    # Apply weighting
    w1, w2 = weights[0], weights[1]
    weighted_even = even_sum * w1
    weighted_odd = odd_sum * w2
    
    # Intermediate distractor variables
    temp_result = (weighted_even + weighted_odd) / 2
    debug_flag = False
    log_entry = f"Intermediate: {temp_result:.2f}"
    
    # Final composition
    raw_score = weighted_even + weighted_odd
    adjustment = abs(weighted_even - weighted_odd) * 0.1
    final_score = raw_score - adjustment
    
    # Red herring: conditional that never triggers
    if debug_flag and log_entry:
        print("Debug mode active")
        
    return final_score

# Main execution flow
data_metrics = collect_metrics()
_ = calculate_baseline(data_metrics)  # Call with no assignment

# Transform the sums into a list for correction
sums_list = [data_metrics['even_index_sum'], data_metrics['odd_index_sum']]
corrected_sums = apply_correction(sums_list)

# Weights determined empirically
weights_config = [1.2, 0.85]

# Key statement
final_score = evaluate_performance({
    'even_index_sum': corrected_sums[0],
    'odd_index_sum': corrected_sums[1]
}, weights_config)

print(f"Result: {final_score}")