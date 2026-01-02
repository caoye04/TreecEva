from collections import defaultdict
import math

# Simulate sensor benchmark data with noise and metadata
def generate_test_bench():
    raw_readings = [12, 15, 22, 8, 33, 40, 25, 18]
    timestamps = [100, 105, 110, 115, 120, 125, 130, 135]
    modes = ['active', 'idle', 'active', 'sleep', 'active', 'active', 'idle', 'active']
    
    benchmark_data = []
    for i in range(len(raw_readings)):
        benchmark_data.append({
            'value': raw_readings[i],
            'ts': timestamps[i],
            'mode': modes[i],
            'delta': raw_readings[i] - (raw_readings[i-1] if i > 0 else 0)
        })
    return benchmark_data

# Auxiliary function to compute signal variance (not directly used in final score)
def compute_variance(signal_list):
    n = len(signal_list)
    if n == 0:
        return 0.0
    mean_val = sum(signal_list) / n
    squared_diffs = [(x - mean_val) ** 2 for x in signal_list]
    return sum(squared_diffs) / n

# Misleading preprocessing step that calculates but doesn't use frequency map
def preprocess_signals(data):
    freq_map = defaultdict(int)
    active_values = []
    time_gaps = []
    
    for i, entry in enumerate(data):
        freq_map[entry['value']] += 1
        if entry['mode'] == 'active':
            active_values.append(entry['value'])
        if i > 0:
            gap = entry['ts'] - data[i-1]['ts']
            time_gaps.append(gap)
    
    # Distractor: compute statistical measures not used later
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0
    gap_variance = compute_variance(time_gaps)
    
    # This filtering is actually irrelevant to final result
    filtered_active = [v for v in active_values if v > 15]
    
    return active_values  # Only this part matters, rest is distraction

# Core logic with nested conditions and accumulation
def calculate_performance(data):
    processed = preprocess_signals(data)
    
    # Key intermediate values
    base_accum = 0
    penalty_adjustment = 0
    peak_count = 0
    
    # Real logic begins here — detect peaks and apply scoring rules
    for i in range(1, len(processed) - 1):
        prev_val, curr_val, next_val = processed[i-1], processed[i], processed[i+1]
        
        # Define a local peak in active mode sequence
        if curr_val > prev_val and curr_val >= next_val:
            peak_count += 1
            base_accum += curr_val
        elif curr_val < prev_val and curr_val <= next_val:
            penalty_adjustment -= 1  # minor penalty for valleys
    
    # Additional distractor computation (unused)
    ideal_peak_ratio = peak_count / len(processed) if processed else 0
    stability_metric = math.exp(-abs(penalty_adjustment) * 0.1)
    
    # Final score depends only on base_accum and peak_count
    final_component = base_accum + (peak_count * 10) + penalty_adjustment
    
    # More red herring: unused normalization
    if base_accum != 0:
        normalized_score = final_component / base_accum
    
    return int(final_component)

# Main execution flow
test_data = generate_test_bench()

# Irrelevant transformation: creates shadow copy with extra field
decorated_data = [
    {**item, 'checksum': item['value'] ^ item['ts']} 
    for item in test_data
]

# Unused aggregation across all modes (distractor)
all_deltas = [entry['delta'] for entry in test_data]
total_drift = sum(all_deltas)

# Another dead-end path: hypothetical prediction model
predictive_factor = sum([d['value'] for d in test_data if d['mode'] != 'sleep']) * 0.05

# Critical statement
final_score = calculate_performance(test_data)

print(f"Result: {final_score}")