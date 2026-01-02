def analyze_system_health(usage_logs):
    # Irrelevant health metrics (distractor)
    cpu_peaks = [x['cpu'] for x in usage_logs if x['cpu'] > 85]
    memory_spikes = sum(1 for x in usage_logs if x['mem'] > 90)
    disk_io_avg = sum(x['io'] for x in usage_logs) / len(usage_logs)

    # Red herring computation
    anomaly_score = len(cpu_peaks) * 2 + memory_spikes
    if anomaly_score > 10:
        status = 'DEGRADED'
    else:
        status = 'STABLE'

    # Unused function (dead code path)
    def calculate_network_latency():
        return sum(i * 0.05 for i in range(len(usage_logs)))

    # Distracting transformation
    timestamps = [log['ts'] for log in usage_logs]
    time_gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0

    # Meaningless aggregation
    weighted_load = 0
    for entry in usage_logs:
        weighted_load += entry['cpu'] * 0.7 + entry['mem'] * 0.3

    return {'status': status, 'anomaly': anomaly_score}


def preprocess_logs(raw_data):
    # Parse and filter logs (partially relevant)
    parsed = []
    for line in raw_data:
        parts = line.split(',')
        if len(parts) < 4:
            continue
        try:
            parsed.append({
                'ts': int(parts[0]),
                'cpu': float(parts[1]),
                'mem': float(parts[2]),
                'io': float(parts[3])
            })
        except ValueError:
            continue

    # Sorting is unnecessary but looks important
    parsed.sort(key=lambda x: x['ts'])

    # Extra filtering with no impact downstream
    filtered = [p for p in parsed if p['cpu'] >= 0 and p['mem'] <= 100]

    # Decoy statistic
    duration = parsed[-1]['ts'] - parsed[0]['ts'] if parsed else 0

    return parsed  # Only this matters


def compute_efficiency_index(data):
    # Real calculation buried in noise
    total_cpu = sum(d['cpu'] for d in data)
    total_mem = sum(d['mem'] for d in data)
    efficiency = (total_cpu * 0.6 + total_mem * 0.4) / len(data) if data else 0

    # Fake normalization
    if efficiency > 75:
        level = 'HIGH'
    elif efficiency > 50:
        level = 'MEDIUM'
    else:
        level = 'LOW'

    # Unused derived values
    peak_utilization = max(max(d['cpu'], d['mem']) for d in data) if data else 0
    utilization_variance = sum((d['cpu'] + d['mem'] - efficiency*2)**2 for d in data) / len(data) if data else 0

    return efficiency  # Only this used later


def evaluate_performance(log_entries, baseline_metrics):
    # Core logic mixed with distractions
    base_efficiency = baseline_metrics.get('efficiency', 60)
    current_efficiency = compute_efficiency_index(log_entries)

    # Bit manipulation decoy (looks cryptic but irrelevant)
    magic_flag = (int(current_efficiency) ^ 0xFF) & 0x0F
    if magic_flag % 3 == 0:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95

    # Real scoring logic
    raw_score = current_efficiency - base_efficiency
    adjusted_score = raw_score * adjustment_factor

    # Multiple layers of conditional logic (some irrelevant)
    if current_efficiency > base_efficiency:
        bonus = 10 * (current_efficiency - base_efficiency) / base_efficiency
    else:
        bonus = -5

    # Final formula
    final_score = int(adjusted_score + bonus + 5)  # Key result

    # Fake logging (distractor output)
    debug_info = {
        'raw': raw_score,
        'adj': adjusted_score,
        'bonus_applied': bonus,
        'magic': magic_flag,
        'flag_state': bin(magic_flag)
    }

    return final_score

# Simulated input data
raw_log_input = [
    "1000,78.2,65.4,23.1",
    "1001,82.1,70.0,25.5",
    "1002,75.3,68.2,20.0",
    "1003,88.0,72.1,30.2",
    "1004,80.5,66.3,24.8"
]

baseline_metrics = {
    'efficiency': 68.5,
    'threshold': 85,
    'version': '2.1'
}

# Execution chain
parsed_logs = preprocess_logs(raw_log_input)
health_report = analyze_system_health(parsed_logs)
system_efficiency = compute_efficiency_index(parsed_logs)
final_score = evaluate_performance(parsed_logs, baseline_metrics)

print(f"Result: {final_score}")