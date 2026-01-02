def analyze_log_stream(raw_data):
    # Parse timestamp and size from log entries
    entries = []
    for line in raw_data.splitlines():
        if not line.strip() or 'ERROR' in line:
            continue
        parts = line.split('|')
        timestamp = parts[0].strip()
        size_str = parts[2].strip()
        size_kb = float(size_str.replace('KB', ''))
        entries.append((timestamp, size_kb))

    return entries


def filter_noisy_signals(data, min_val, max_val):
    # This function is unused but included as distraction
    return [x for x in data if min_val < x < max_val]


def calculate_remaining_capacity(log_entries, threshold):
    total_bandwidth = 100000.0  # KB
    usage_log = []
    temp_shadow = []

    for _, size in log_entries:
        if size > threshold:
            usage_log.append(size * 0.9)  # Adjusted for compression
        else:
            usage_log.append(size)

    # Simulate time-windowed slicing: last 7 entries
    recent_usage = usage_log[-7:] if len(usage_log) >= 7 else usage_log[:]

    # Misleading intermediate computation (not used in final result)
    avg_usage = sum(usage_log) / len(usage_log) if usage_log else 0
    peak_usage = max(usage_log) if usage_log else 0
    projected_next = avg_usage * 1.2

    # Actual capacity calculation
    cumulative_used = sum(recent_usage)
    efficiency_factor = 0.95
    adjusted_used = cumulative_used * efficiency_factor

    remaining = total_bandwidth - adjusted_used

    # Dead code branch - never executed due to fixed threshold
    if threshold > 1000:
        fallback = total_bandwidth * 0.8
        return fallback

    # Key variable assignment
    final_capacity = int(remaining)

    # Extraneous list manipulation
    temp_shadow.extend([1] * len(recent_usage))
    slice_offset = temp_shadow[::2]  # Unused slicing operation

    return final_capacity

# Simulated log input
log_input = '''
2023-06-01T08:00:01 | INFO  | 45.2KB |
2023-06-01T08:05:12 | INFO  | 103.5KB |
2023-06-01T08:10:23 | WARN  | 76.8KB |
2023-06-01T08:15:34 | INFO  | 201.3KB |
2023-06-01T08:20:45 | INFO  | 54.9KB |
2023-06-01T08:25:56 | INFO  | 88.1KB |
2023-06-01T08:30:07 | INFO  | 156.7KB |
2023-06-01T08:35:18 | INFO  | 67.4KB |
2023-06-01T08:40:29 | INFO  | 92.3KB |
2023-06-01T08:45:40 | INFO  | 134.6KB |
'''

# Irrelevant preprocessing step
processed_lines = log_input.strip().split('\n')
line_count = len(processed_lines)
dummy_stats = {"lines": line_count, "ignored": 2}

# Main execution flow
parsed_entries = analyze_log_stream(log_input)
threshold = 100.0

# Key statement
final_capacity = calculate_remaining_capacity(parsed_entries, threshold)

# Print result
print(f"Result: {final_capacity}")