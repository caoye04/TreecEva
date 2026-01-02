from collections import defaultdict, Counter

# Simulated health monitoring system with data processing and diagnostics

def analyze_readings(readings):
    stats = defaultdict(float)
    total = 0
    count = 0
    high_alerts = 0
    
    for val in readings:
        if val > 100:
            high_alerts += 1
        total += val
        count += 1
    
    stats['average'] = total / count if count else 0
    stats['alerts'] = high_alerts
    stats['normalized'] = stats['average'] / (high_alerts + 1)
    
    # Irrelevant transformation
    temp_str = "data_point_" + str(int(stats['average']))
    reversed_name = temp_str[::-1].upper()
    
    return stats

def validate_signal(signal_list):
    # Distractor function: processes signal but not used in final result
    valid_count = 0
    for s in signal_list:
        if isinstance(s, str) and 'OK' in s:
            valid_count += 1
    return valid_count

def compute_stability_index(entries):
    # Another red herring: computes stability but not directly used
    if not entries:
        return 0
    squared_sum = sum([x**2 for x in entries])
    linear_sum = sum(entries)
    index = squared_sum / (linear_sum + 1)
    return round(index, 3)

def extract_flags(metadata):
    # Unrelated flag extraction
    flags = []
    for key, value in metadata.items():
        if 'flag' in key:
            flags.append(value)
    return ''.join(flags).lower()

def process_metrics(data, thresholds):
    # Core logic embedded within distractions
    result_map = defaultdict(int)
    
    # Key intermediate values
    baseline = data.get('baseline', 50)
    readings = data.get('readings', [])
    
    analysis = analyze_readings(readings)
    avg = analysis['average']
    
    # Real computation path begins here
    deviation = abs(avg - baseline)
    tolerance = thresholds.get('tolerance', 10)
    severity = 0
    
    if deviation > 2 * tolerance:
        severity = 3
    elif deviation > tolerance:
        severity = 2
    elif deviation > 0:
        severity = 1
    
    # Bitwise encoding of state (mixed paradigm)
    encoded_state = (severity << 2) | (analysis['alerts'] & 0b11)
    
    # Additional irrelevant counters
    counter_obj = Counter(readings)
    rare_values = [k for k, v in counter_obj.items() if v == 1]
    
    # String manipulation distraction
    tag_sequence = "_X_".join([str(r) for r in rare_values[:3]])
    checksum = sum([len(tag_sequence), len(rare_values)]) % 7
    
    # Final diagnostic depends only on encoded_state and checksum in a non-obvious way
    adjustment = 5 if len(rare_values) % 2 == 1 else -2
    final_diagnostic = encoded_state * 3 + checksum + adjustment
    
    # Dead code branch - never executed due to above logic
    if final_diagnostic < 0:
        fallback = compute_stability_index(readings)
        final_diagnostic = int(fallback)
    
    return final_diagnostic

# Main execution context
if __name__ == "__main__":
    # Input data setup
    health_data = {
        'baseline': 48,
        'readings': [45, 52, 98, 103, 47, 50, 106, 49],
        'device_id': 'HMX-9021',
        'version': 'v2.3',
        'flag_critical': 'N',
        'flag_monitor': 'Y'
    }
    
    threshold_map = {
        'tolerance': 12,
        'window': 5,
        'flag_threshold': 75
    }
    
    # Unused variables - distractors
    signal_health = ['OK', 'OK', 'FAULT', 'OK']
    metadata_trace = {"user": "admin", "mode": "diagnostic"}
    temp_result = validate_signal(signal_health)
    stability_score = compute_stability_index(health_data['readings'])
    flags_active = extract_flags(health_data)
    
    # Critical execution point
    final_diagnostic = process_metrics(health_data, threshold_map)
    
    # Output the target result
    print(f"Target result: {final_diagnostic}")