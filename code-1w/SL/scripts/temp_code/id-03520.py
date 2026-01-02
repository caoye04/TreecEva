def analyze_productivity(logs):
    total_entries = len(logs)
    valid_entries = [entry for entry in logs if entry['status'] == 'success']
    failed_entries = [entry for entry in logs if entry['status'] == 'failed']
    
    # Distractor: count characters in error messages (not used later)
    error_chars = sum(len(entry.get('error', '')) for entry in failed_entries)
    temp_diagnostic = error_chars * 0.1
    
    success_rate = len(valid_entries) / total_entries if total_entries > 0 else 0
    avg_latency = sum(entry['latency'] for entry in valid_entries) / len(valid_entries) if valid_entries else 0
    
    return success_rate, avg_latency, len(failed_entries)

logs_data = [
    {'status': 'success', 'latency': 120, 'timestamp': '2023-05-01T10:00:00'},
    {'status': 'success', 'latency': 80, 'timestamp': '2023-05-01T10:01:00'},
    {'status': 'failed', 'error': 'timeout', 'timestamp': '2023-05-01T10:02:00'},
    {'status': 'success', 'latency': 150, 'timestamp': '2023-05-01T10:03:00'},
    {'status': 'failed', 'error': 'auth', 'timestamp': '2023-05-01T10:04:00'},
    {'status': 'success', 'latency': 90, 'timestamp': '2023-05-01T10:05:00'}
]

# Extract metrics
efficiency, response_time, fault_count = analyze_productivity(logs_data)

# Auxiliary distractor computation: simulate load factor (not directly used)
load_factor = len(logs_data) * 0.75
peak_load_metric = load_factor ** 2

# Character frequency analysis on timestamps (irrelevant but plausible)
timestamp_chars = ''.join([log['timestamp'] for log in logs_data])
char_frequency = {}
for c in timestamp_chars:
    char_frequency[c] = char_frequency.get(c, 0) + 1
rare_char_penalty = sum(1 for freq in char_frequency.values() if freq < 2)

# Real evaluation logic using lambda for dynamic threshold
adjustment_factor = lambda x: 0.9 if x > 100 else 1.1
penalty_ratio = fault_count / len(logs_data) if logs_data else 0
adjusted_efficiency = efficiency * adjustment_factor(response_time)

# Final scoring with weighted components
base_score = adjusted_efficiency * 100
error_penalty = penalty_ratio * 20
response_penalty = (response_time / 200) * 15

final_score = base_score - error_penalty - response_penalty

# Irrelevant set operation (distractor)
unique_timestamps = set(timestamp_chars)
unused_entropy = len(unique_timestamps) / len(timestamp_chars)

Result: {final_score}