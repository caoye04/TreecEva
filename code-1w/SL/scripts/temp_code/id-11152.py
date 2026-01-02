import itertools

# Simulated system diagnostics with mixed relevance
def analyze_diagnostics(logs):
    error_count = sum(1 for log in logs if 'ERR' in log)
    warning_count = sum(1 for log in logs if 'WARN' in log)
    debug_count = sum(1 for log in logs if 'DEBUG' in log)  # Distractor
    return error_count, warning_count

# Irrelevant data transformation (dead path)
def transform_data(data):
    if not data:
        return []
    shifted = [(x >> 2) & 0xFF for x in data]
    filtered = [x for x in shifted if x % 3 == 0]
    return [x ^ 0xAA for x in filtered]  # Unused result

# Core calculation with red herrings
def compute_cycles(timestamps, threshold=50):
    valid_intervals = []
    temp_buffer = []
    decoy_sum = 0

    for i in range(1, len(timestamps)):
        diff = timestamps[i] - timestamps[i-1]
        if diff > threshold:
            valid_intervals.append(diff)
            temp_buffer.append(diff * 0.9)
        else:
            decoy_sum += diff ** 2  # Misleading accumulation

    # Real computation buried among distractions
    base_cycle = sum(valid_intervals) // len(valid_intervals) if valid_intervals else 0
    adjustment = len(temp_buffer) % 7
    return base_cycle + adjustment

# Secondary metric (partially relevant)
def calculate_efficiency(ratio_seq):
    avg_ratio = sum(ratio_seq) / len(ratio_seq)
    peak = max(ratio_seq)
    floor_val = min(ratio_seq)  # Slight distractor
    efficiency = (avg_ratio * 0.7) + (peak * 0.3) if peak > 0 else 0.0
    return round(efficiency, 4)

# Main evaluation logic with conditional expression and itertools
def evaluate_performance(results, factor):
    # Use of itertools to create distraction
    expanded = list(itertools.chain.from_iterable(
        [itertools.repeat(x, 2) for x in results if x % 2 == 1]
    ))
    
    # Conditional expression (required feature)
    scaling = factor if factor > 1.0 else (1.5 if sum(expanded) > 100 else 0.8)
    
    raw_total = sum(results)
    penalty = 0
    
    # Nested logic with multiple levels (3-4 deep)
    if raw_total > 200:
        for val in results:
            if val < 10:
                penalty += val * 0.5
            elif val < 50:
                for offset in [1, 2]:  # Extra nesting
                    penalty += (val // 10) * offset * 0.1
    else:
        penalty = raw_total * 0.1

    adjusted = raw_total - penalty
    final = int(adjusted * scaling)

    # Dead code: unreachable branch due to prior conditions
    if len(results) == 0:
        final = -999  # Never executed

    return final

# Global irrelevant constants
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 150
TEMP_THRESHOLD = 75  # Unused thermal parameter

# Input data generation (deterministic)
timestamp_log = [10, 68, 132, 145, 203, 270, 305]
metric_ratios = [12.5, 8.3, 45.1, 62.7, 9.4]
system_logs = [
    'INFO: Startup',
    'ERR: Disk full',
    'WARN: High latency',
    'DEBUG: Register state=0x3A',
    'ERR: Timeout'
]

# Unused data structure (distractor)
status_tree = {
    'root': {
        'node1': {'leafA': 100, 'leafB': 200},
        'node2': {
            'sub': {'deep': {'value': 42}}}  # Hidden but unused
    }
}

# Extract some values (only error/warning used)
errors, warnings = analyze_diagnostics(system_logs)
base_cycle_time = compute_cycles(timestamp_log)
efficiency_metric = calculate_efficiency(metric_ratios)

# Create input for target function
raw_results = [
    base_cycle_time + 5,
    (errors * 12) + 1,
    (warnings * 8) + 3,
    efficiency_metric // 1,
    42  # Magic number for checksum alignment
]

# Introduce a decoy transformation
transformed_raw = transform_data([int(x * 1.5) for x in raw_results])  # Not used

# Key statement
final_score = evaluate_performance(raw_results, efficiency_metric / 40)

print(f"Target result: {final_score}")