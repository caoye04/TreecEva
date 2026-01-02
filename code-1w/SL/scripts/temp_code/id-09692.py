from collections import defaultdict, Counter

# Simulated system health monitoring with extensive irrelevant computations
def analyze_components(log_data):
    stats = defaultdict(int)
    temp_history = []
    for entry in log_data:
        if 'error' in entry:
            stats['errors'] += 1
        elif 'warning' in entry:
            stats['warnings'] += 1
        else:
            stats['normal'] += 1
        temp_history.append(len(entry))

    avg_temp = sum(temp_history) / len(temp_history) if temp_history else 0
    return dict(stats), avg_temp

def compute_checksum(data):
    # Irrelevant cryptographic checksum (red herring)
    chk = 0
    for item in data:
        for c in item:
            chk ^= ord(c) << (len(item) % 4)
    return chk % 1000

def transform_sequence(seq):
    # Complex but irrelevant transformation
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append((val ** 2) + 3)
        else:
            result.append((val // 2) - 1)
    return [x for x in result if x > 0][::-1]

def generate_baseline_profile(history_window=5):
    # Generates baseline with fake metrics (distractor)
    profile = {}
    for i in range(history_window):
        key = f"metric_{i}"
        profile[key] = (i * 17 + 23) % 89
    return profile

def filter_outliers(data, threshold=2):
    # Unused outlier detection (dead code path)
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def evaluate_performance(metrics, base):
    score = 0
    weight_map = {k: (ord(k[-1]) % 7) + 1 for k in metrics.keys()}
    
    # Core logic embedded in noise
    for k in metrics:
        if k in base:
            diff = abs(metrics[k] - base[k])
            if diff < 5:
                score += 10 * weight_map[k]
            elif diff < 10:
                score += 5 * weight_map[k]
            else:
                score -= 2 * weight_map[k]
    
    # Secondary adjustment based on character patterns in keys
    key_chars = ''.join(metrics.keys())
    char_count = Counter(key_chars)
    dominant_char_value = ord(max(char_count, key=lambda x: char_count[x]))
    
    if dominant_char_value % 2 == 0:
        score += 7
    else:
        score -= 3
    
    # Slice-based interference
    slices = [key_chars[i:i+2] for i in range(0, len(key_chars)-1, 3)]
    slice_score = sum(len(s) for s in slices if s[0] != s[-1])
    score += slice_score  # Minor contribution to actual answer
    
    return score

# Main execution flow
if __name__ == "__main__":
    # Real input data
    system_logs = [
        "node_1_ok", "node_2_error", "node_3_warning",
        "node_4_ok", "node_5_error", "heartbeat_active"
    ]
    
    # Irrelevant data transformations
    raw_sequence = [4, 7, 2, 9, 1, 8, 3]
    transformed_seq = transform_sequence(raw_sequence)
    checksum = compute_checksum(system_logs)
    
    # Extract meaningful metrics from logs
    log_stats, average_length = analyze_components(system_logs)
    
    # Map log stats to numeric metrics (actual relevant path)
    extracted_metrics = {
        'errors': log_stats.get('errors', 0) * 10,
        'warnings': log_stats.get('warnings', 0) * 5,
        'normal': log_stats.get('normal', 0) * 2,
        'length_avg': int(average_length)
    }
    
    # Baseline generation (some values will match, others won't)
    baseline = generate_baseline_profile(5)
    # Override with known fixed baseline for deterministic outcome
    baseline = {
        'errors': 20, 'warnings': 15, 'normal': 30, 'length_avg': 12
    }
    
    # Critical statement
    final_score = evaluate_performance(extracted_metrics, baseline)
    
    # Dead code branches (never executed)
    if False:
        filtered = filter_outliers(transformed_seq)
        final_score = max(filtered) - min(filtered)
    
    # Output result as required
    print(f"Result: {final_score}")