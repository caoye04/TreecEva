def analyze_performance(records):
    total_entries = len(records)
    valid_count = sum(1 for r in records if r['status'] == 'active')
    inactive_count = total_entries - valid_count
    
    # Irrelevant distraction: calculate average latency (not used later)
    latencies = [r['response_time'] for r in records if 'response_time' in r]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    
    # Distraction: simulate debug flag check
    debug_mode = False
    if debug_mode:
        print(f'Debug: Found {valid_count} active entries')

    # Semi-relevant transformation
    weights = [0.1, 0.2, 0.3, 0.4]
    weighted_valid = valid_count * sum(w ** 2 for w in weights)  # Minor effect

    return valid_count, total_entries


def compute_baseline(n):
    # Dead function with no real impact
    base = 1
    for i in range(2, n + 1):
        base += i % 3
    return base

# Main data processing chain
data_log = [
    {'id': 1, 'status': 'active', 'response_time': 120},
    {'id': 2, 'status': 'inactive'},
    {'id': 3, 'status': 'active', 'response_time': 95},
    {'id': 4, 'status': 'active', 'response_time': 200},
    {'id': 5, 'status': 'inactive'},
    {'id': 6, 'status': 'active', 'response_time': 150},
    {'id': 7, 'status': 'active'}
]

threshold = 0.4

# Secondary distraction: unused statistical calculation
mean_response = sum(r.get('response_time', 0) for r in data_log) / len(data_log)
std_dev_sq = sum((r.get('response_time', 0) - mean_response) ** 2 for r in data_log) / len(data_log)

# Core logic with key nesting and conditionals
def process_metrics(log, thresh):
    active, total = analyze_performance(log)
    ratio = active / total
    
    # Nested conditional with red herring
    if ratio > thresh:
        adjustment_factor = 1.2
        if total > 5:
            adjustment_factor *= 0.9  # slight reduction
        else:
            adjustment_factor *= 1.1
        
        # Bitwise distraction (has minimal impact)
        flag_mask = 0b1010
        adjustment_factor ^= (flag_mask & active) / 100
        
        # Real computation path
        raw_score = active * 10 + (total - active) * (-5)
        efficiency_score = raw_score * adjustment_factor
        
        # Additional irrelevant state tracking
        history = [{'step': 'init', 'val': raw_score}]
        for i in range(1, 3):
            history.append({'step': f'adj_{i}', 'val': efficiency_score})
    else:
        efficiency_score = 50
    
    # More distraction: unused set operation
    unique_ids = {item['id'] for item in log}
    overflow_flag = len(unique_ids) & 1  # never used

    return int(efficiency_score), efficiency_score  # return both int and float

final_output = process_metrics(data_log, threshold)
efficiency_score = final_output[1]

Result: {efficiency_score}