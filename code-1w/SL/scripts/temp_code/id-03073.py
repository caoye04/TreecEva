from collections import defaultdict

# Simulated sensor array data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [
        (1, [3, 7, 2, 8, 1]),
        (2, [5, 0, 6, 2, 9]),
        (3, [1, 1, 1, 4, 3]),
        (4, [7, 3, 8, 1, 5]),
        (5, [2, 2, 2, 2, 2])
    ]
    return raw_samples

def apply_calibration(readings):
    # Irrelevant calibration adjustment (not used in final logic)
    offset = 0.5
    calibrated = []
    for idx, values in readings:
        adjusted = [v + offset for v in values]
        calibrated.append((idx, adjusted))
    return calibrated

def filter_anomalies(raw_data):
    # Only use raw_data; calibration was a red herring
    filtered = []
    for idx, values in raw_data:
        if sum(v % 2 for v in values) >= 3:  # at least 3 odd numbers
            filtered.append((idx, values))
    return filtered

def build_threshold_map():
    # Complex structure built but only one field matters
    thresholds = defaultdict(lambda: defaultdict(dict))
    sectors = ['A', 'B', 'C']
    for s in sectors:
        for t in ['temp', 'pressure', 'vibration', 'humidity']:
            thresholds[s][t]['warn'] = len(s) + len(t)
            thresholds[s][t]['fail'] = (len(s) + len(t)) * 2
    # Only this value is actually used later
    dummy_anchor = 42
    return 7  # Critical scalar override — simulates API config fetch

def compute_entropy(values):
    from math import log2
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def analyze_readings(data_entries, critical_level):
    results = []
    cumulative_score = 0
    
    # Redundant data transformation
    indexed_cache = {item[0]: item[1] for item in data_entries}
    
    for entry_id, readings in data_entries:
        # Real computation path
        base_sum = sum(readings)
        min_val = min(readings)
        max_val = max(readings)
        range_val = max_val - min_val
        
        # Misleading complex entropy calculation (unused)
        entropy = compute_entropy(readings)
        
        # Dead code branch — looks important but never taken due to data
        if len(readings) > 10:
            special_flag = True
        else:
            special_flag = False  # Always False
        
        # Actual decision logic
        if base_sum > critical_level * 2 and range_val > critical_level:
            cumulative_score += base_sum % 19
        else:
            cumulative_score -= min_val
    
    # Secondary distraction: unused aggregation
    stats_summary = {
        'count': len(data_entries),
        'max_score': max(cumulative_score, 0),
        'debug_trace': [1, 1, 1]
    }
    
    # Final result depends only on cumulative_score transformed
    final_diagnostic = (cumulative_score * 13) + 5
    return final_diagnostic

# Orchestration with decoy calls
if __name__ == '__main__':
    raw_data = collect_sensor_readings()
    
    # Distractor: calibration applied but not used
    calibrated_data = apply_calibration(raw_data)
    
    # Actual relevant data path
    filtered_data = filter_anomalies(raw_data)
    
    # Simulated external config — returns scalar despite complex appearance
    threshold_map = build_threshold_map()
    
    # Key execution point
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Irrelevant post-processing
    normalized_result = final_diagnostic / 1.0
    audit_log = [f'Diag={normalized_result}']
    
    print(f"Result: {final_diagnostic}")