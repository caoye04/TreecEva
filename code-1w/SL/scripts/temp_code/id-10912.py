import itertools

def analyze_efficiency(log_entries):
    durations = []n    errors = []
    for entry in log_entries:
        parts = entry.split('|')
        if len(parts) < 3:
            continue
        duration_str = parts[1].strip()
        status = parts[2].strip()
        try:
            duration = float(duration_str)
            durations.append(duration)
            if 'ERROR' in status:
                errors.append(duration)
        except ValueError:
            pass
    avg_duration = sum(durations) / len(durations) if durations else 0
    error_rate = len(errors) / len(durations) if durations else 0
    return avg_duration, error_rate

def evaluate_reliability(timestamps):
    gaps = []
    sorted_timestamps = sorted([t for t in timestamps if t > 0])
    for i in range(1, len(sorted_timestamps)):
        gaps.append(sorted_timestamps[i] - sorted_timestamps[i-1])
    if not gaps:
        return 0.0
    return sum(gaps) / len(gaps)

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = sum(weights)
    normalized = [m / 100.0 for m in metrics]
    
    # Distractor: unused transformation
    inverted = [1.0 - n for n in normalized if n > 0.5]
    smoothed = []
    for i, val in enumerate(normalized):
        neighbor_avg = (normalized[i-1] + normalized[i] + normalized[(i+1) % len(normalized)]) / 3
        smoothed.append(neighbor_avg * 0.9 + val * 0.1)
    
    for i, (metric, weight) in enumerate(zip(normalized, weights)):
        if metric >= 0.8:
            weighted_sum += (metric * weight * 1.2)  # bonus for high performance
        elif metric < 0.5:
            weighted_sum += (metric * weight * 0.8)  # penalty for low
        else:
            weighted_sum += (metric * weight)
    
    final = (weighted_sum / total_weight) * 100
    return int(round(final))

# Simulated system telemetry
telemetry_logs = [
    'SYS| 2.34 | OK',
    'NET| 5.12 | ERROR: timeout',
    'DISK| 1.88 | OK',
    'MEM| 4.01 | ERROR: overflow',
    'CPU| 3.22 | OK'
]

timestamp_data = [100, 105, 112, 115, 125, 130]

# Extract primary metrics
avg_time, err_ratio = analyze_efficiency(telemetry_logs)
reliability_gap = evaluate_reliability(timestamp_data)

# Normalize into score components (scaled to 0-100)
speed_metric = max(0, 100 - (avg_time * 10))
error_metric = max(0, 100 - (err_ratio * 100))
gap_metric = 100 - min(100, reliability_gap)
consistency_metric = 85  # assumed from historical baseline

metrics = [speed_metric, error_metric, gap_metric, consistency_metric]
benchmark_weights = [0.3, 0.3, 0.2, 0.2]

# Irrelevant helper — distractor
def format_report(data):
    lines = []
    for idx, val in enumerate(data):
        prefix = f"Item-{idx+1}".rjust(8)
        bar = '*' * int(val // 5)
        lines.append(f"{prefix}: {val:6.2f} [{bar}]")
    return '\n'.join(lines)

report_str = format_report(metrics)  # dead end, not used later

# Auxiliary computation — semi-relevant but not critical
total_load = sum(len(seq) for seq in itertools.product([0,1], repeat=3))  # always 8
overhead = len(telemetry_logs) * total_load  # misleading complexity

# Key execution point
final_score = evaluate_performance(metrics, benchmark_weights)
print(f"Target result: {final_score}")