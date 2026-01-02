def filter_anomalous(logs):
    # Irrelevant transformation
    timestamps = [entry['ts'] for entry in logs if 'ts' in entry]
    avg_time = sum(timestamps) / len(timestamps) if timestamps else 0
    
    # Distractor: complex but unused filtering logic
    critical_ids = {i for i, e in enumerate(logs) if e.get('priority') == 'high'}
    redundant_data = {str(x): x * 2 for x in range(len(logs))}  # Dead code

    # Actual relevant filtering: remove readings with negative values
    filtered = [e['reading'] for e in logs if e['reading'] >= 0]
    return filtered


def rolling_window_avg(data, window=3):
    # Unused helper function - distractor
    if len(data) < window:
        return []
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]


def analyze_readings(readings):
    # Track state across iterations
    trend_states = []
    cumulative_shift = 0
    
    for i in range(1, len(readings)):
        diff = readings[i] - readings[i-1]
        cumulative_shift += diff
        if diff > 5:
            trend_states.append('spike')
        elif diff < -5:
            trend_states.append('drop')
        else:
            trend_states.append('stable')
    
    # Distractor: string analysis on fake labels
    state_labels = ''.join([t[0] for t in trend_states]).upper()
    label_checksum = sum(ord(c) for c in state_labels) % 100  # Misleading intermediate
    
    # Relevant logic: count stable trends and apply multiplier
    stability_count = trend_states.count('stable')
    volatility_index = trend_states.count('spike') + trend_states.count('drop')
    
    # Core computation
    base_score = stability_count * 7
    penalty = volatility_index * 3
    
    # Additional distractor: bit manipulation with no real impact
    masked_score = base_score ^ 0b1010
    temp_result = (penalty << 2) | 7
    
    # Final diagnostic depends only on net shift and adjusted score
    adjustment = abs(cumulative_shift) // 10 if cumulative_shift != 0 else 1
    final_diagnostic = (base_score - penalty) // adjustment
    
    # Print to ensure visibility
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated system logs with mixed content
system_logs = [
    {'ts': 1001, 'reading': 23.5, 'sensor': 'A', 'priority': 'low'},
    {'ts': 1002, 'reading': 25.1, 'sensor': 'B', 'priority': 'high'},
    {'ts': 1003, 'reading': 19.8, 'sensor': 'A', 'priority': 'low'},
    {'ts': 1004, 'reading': 20.0, 'sensor': 'C', 'priority': 'medium'},
    {'ts': 1005, 'reading': 27.3, 'sensor': 'B', 'priority': 'high'},
    {'ts': 1006, 'reading': -1.5, 'sensor': 'D', 'priority': 'low'},  # filtered out
    {'ts': 1007, 'reading': 35.0, 'sensor': 'A', 'priority': 'low'},
    {'ts': 1008, 'reading': 33.0, 'sensor': 'B', 'priority': 'medium'},
    {'ts': 1009, 'reading': 33.1, 'sensor': 'C', 'priority': 'low'}
]

# Unused auxiliary data structures
aux_metadata = {
    'version': '2.1-alpha',
    'calibration': [0.99, 1.01, 0.98],
    'history': set(),
    'flags': {f'flag_{i}': False for i in range(5)}
}

# Key execution point
final_diagnostic = analyze_readings(filter_anomalous(system_logs))