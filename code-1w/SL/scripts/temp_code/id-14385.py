from collections import defaultdict, Counter
import math

# Simulated system telemetry data
def collect_telemetry():
    signals = [1.2, 0.9, 1.5, 2.1, 1.8, 0.7, 1.3, 1.6]
    timestamps = [162345, 162346, 162348, 162350, 162355, 162356, 162358, 162360]
    modes = ['active', 'idle', 'active', 'overload', 'overload', 'idle', 'active', 'active']
    return list(zip(signals, timestamps, modes))

def analyze_phase_shift(data):
    total_shift = 0.0
    for sig, ts, mode in data:
        if mode == 'overload':
            total_shift += math.sin(sig) * 0.5
        elif mode == 'idle':
            total_shift -= math.cos(sig) * 0.3
    return total_shift

def compute_heartbeat_intervals(timestamps):
    intervals = []
    for i in range(1, len(timestamps)):
        intervals.append(timestamps[i] - timestamps[i-1])
    avg_interval = sum(intervals) / len(intervals)
    return [intv for intv in intervals if intv <= avg_interval + 1]

def generate_fault_patterns(signal_vals):
    pattern_count = defaultdict(int)
    for val in signal_vals:
        rounded = round(val, 1)
        if rounded > 1.0:
            pattern_count['high'] += 1
        elif rounded < 1.0:
            pattern_count['low'] += 1
        else:
            pattern_count['nominal'] += 1
    return dict(pattern_count)

def evaluate_stability_index(phases, intervals):
    # Irrelevant computation path (dead logic)
    temp_analysis = [x * 1.05 for x in intervals if x > 3]
    if len(temp_analysis) > 5:
        return sum(temp_analysis) / 100
    else:
        return abs(phases) * 10

def filter_noisy_readings(raw_data):
    clean_data = []
    for sig, ts, mode in raw_data:
        if sig < 0.6 or sig > 2.5:
            continue
        if 'diag' in mode:  # never occurs
            break
        clean_data.append((sig, ts, mode))
    return clean_data

def accumulate_diagnostics(cleaned):
    stats = {'count': 0, 'sum_signal': 0.0, 'modes': []}
    for sig, ts, mode in cleaned:
        stats['count'] += 1
        stats['sum_signal'] += sig
        stats['modes'].append(mode)
    
    # Distractor: complex unused structure
    summary_blob = {
        'meta': {'version': '2.1', 'valid': True},
        'data': [math.log(s + 1) for s in [1, 2, 3]],
        'checksum': sum([1, 1, 1])
    }
    
    return stats

def aggregate_metrics(log_entry, diag_set):
    base_score = log_entry.get('base', 0)
    offset = len(diag_set.get('modes', [])) * 0.25
    penalty = 0
    
    # Real calculation path
    if diag_set['count'] > 5:
        penalty -= 1.5
    if diag_set['sum_signal'] > 8.0:
        penalty -= 0.8
    
    # Misleading manipulation
    temp_value = base_score
    for i in range(3):
        temp_value = (temp_value + 0.1) * 0.95  # converges but unused
    
    final = base_score + offset + penalty
    return round(final, 4)

# Main execution flow
telemetry = collect_telemetry()

# Extract components
signals_only = [item[0] for item in telemetry]
timestamps_only = [item[1] for item in telemetry]

# Perform phase analysis
phase_result = analyze_phase_shift(telemetry)

# Compute heartbeat intervals
intervals_filtered = compute_heartbeat_intervals(timestamps_only)

# Generate fault distribution
fault_profile = generate_fault_patterns(signals_only)

# Evaluate system stability (result not used in final answer)
stability_metric = evaluate_stability_index(phase_result, intervals_filtered)

# Filter out invalid readings
filtered_data = filter_noisy_readings(telemetry)

# Accumulate diagnostic statistics
diag_stats = accumulate_diagnostics(filtered_data)

# Build timing log structure (only 'base' matters)
timing_log = {
    'base': len(intervals_filtered) * 1.3,
    'origin': 'primary',
    'sequence': [x * 0.7 for x in intervals_filtered]
}

# Create auxiliary diagnostics map
diagnostics = {
    'modes': [mode for _, _, mode in filtered_data],
    'count': diag_stats['count'],
    'sum_signal': diag_stats['sum_signal']
}

# Key statement: compute final diagnostic score
final_diagnostic = aggregate_metrics(timing_log, diagnostics)

# Output result
print(f"Result: {final_diagnostic}")