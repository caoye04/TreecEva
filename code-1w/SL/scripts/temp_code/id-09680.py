from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant pattern analysis (distractor)
    flat_streaks = 0
    current_flat = 0
    for t in trend:
        if t == 0:
            current_flat += 1
        else:
            if current_flat > 2:
                flat_streaks += 1
            current_flat = 0

    # Real logic: count increasing pairs
    increasing_pairs = 0
    for a, b in combinations(sequence, 2):
        if b > a:
            increasing_pairs += 1

    return increasing_pairs

def validate_string_format(s):
    # Distractor function: checks format but not used in final score
    if not isinstance(s, str):
        return False
    if s.count('.') != 1:
        return False
    parts = s.split('.')
    return parts[0].isdigit() and parts[1].isdigit()

def calculate_performance(data):
    base_score = 0
    adjustment = 0.0
    temp_result = []
    
    for record in data:
        # Extract numeric values from string-encoded records
        raw_values = record['values']
        parsed = [float(x.strip()) for x in raw_values.split(',')]
        
        # Real contribution to score
        avg = sum(parsed) / len(parsed)
        base_score += int(avg)
        
        # Use of string method (required feature)
        tag = record['tag'].strip().upper()
        
        # Conditional branch based on tag (real logic)
        if 'CRITICAL' in tag:
            adjustment += 0.5
        elif 'MONITOR' in tag:
            adjustment -= 0.2
        
        # Dead code path (distractor)
        if 'DEBUG' in tag:
            temp_result.append('Skipped')
            continue  # early skip that never triggers due to data
        
        # Accumulate valid contributions
        temp_result.append(len(parsed))
    
    # Set operation (suggested paradigm)
    unique_lengths = len(set(temp_result))
    
    # Red herring calculation with no impact
    outlier_count = 0
    all_vals = []
    for r in data:
        all_vals.extend([float(x.strip()) for x in r['values'].split(',')])
    mean_all = sum(all_vals) / len(all_vals)
    for v in all_vals:
        if abs(v - mean_all) > 2 * (sum((x - mean_all)**2 for x in all_vals) / len(all_vals))**0.5:
            outlier_count += 1

    # Final score depends only on base_score, adjustment, and unique_lengths
    final_score = base_score + int(adjustment * 10) + unique_lengths
    return final_score

# Simulated benchmark dataset
benchmark_data = [
    {'values': '10.0, 12.5, 8.3, 15.7', 'tag': 'critical-v1'},
    {'values': '7.2, 9.1, 6.4', 'tag': 'MONITOR_FAST'},
    {'values': '20.0, 22.1, 19.8, 25.3, 21.0', 'tag': 'CRITICAL_FINAL'}
]

# Call the function
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")