import itertools
from collections import defaultdict, Counter

# System health monitoring simulation with red herrings
def analyze_health_log(raw_logs):
    # Irrelevant preprocessing (distractor)
    normalized_data = [x.strip().lower() for x in raw_logs if x]
    filtered_entries = [entry for entry in normalized_data if 'error' not in entry]

    # Real data structures used later
    event_counts = defaultdict(int)
    severity_levels = []
    diagnostic_flags = [False, True, False]

    # Parsing actual metrics from logs
    for log in raw_logs:
        if 'temp' in log:
            try:
                temp_val = float(log.split('temp=')[1].split()[0])
                severity_levels.append(temp_val)
                event_counts['temperature_event'] += 1
            except:
                continue
        elif 'pressure' in log:
            try:
                p_val = float(log.split('pressure=')[1].split()[0])
                severity_levels.append(p_val * 0.75)  # Weighted contribution
                event_counts['pressure_anomaly'] += 1
            except:
                continue

    # Decoy statistical analysis (dead path)
    avg_severity = sum(severity_levels) / len(severity_levels) if severity_levels else 0
    peak = max(severity_levels) if severity_levels else 0
    noise_floor = [x for x in severity_levels if x > avg_severity]

    # Unused transformation chain (misleading)
    transformed = list(map(lambda x: x ** 2 - x, filter(lambda y: y > 30, severity_levels)))
    reshaped = list(itertools.chain.from_iterable([(t, t+1) for t in transformed[:3]])) if transformed else [0]

    # Core logic variables
    baseline_cycle = len([x for x in raw_logs if 'cycle' in x])
    cycle_count = baseline_cycle * 2  # Double count due to dual-phase logging

    # Bit manipulation decoy (irrelevant)
    encoded_flag = 0
    for flag in diagnostic_flags:
        encoded_flag = (encoded_flag << 1) | int(flag)
    encoded_flag ^= 255  # Obfuscation step (unused)

    # Real calculation components
    aggregate_score = sum(severity_levels) * 1.5
    anomaly_threshold = event_counts['temperature_event'] + event_counts['pressure_anomaly']
    correction_factor = len(filtered_entries) - len(raw_logs) + 5  # Net adjustment

    # Key distracting loop (no effect on final result)
    temp_debug = []
    for i in range(3):
        temp_debug.append({
            'iter': i,
            'value': (i * 113) % 7
        })
    metadata_snapshot = Counter(temp_debug)  # Dead use

    # Critical execution point
    final_diagnostic = aggregate_score + correction_factor * (cycle_count - anomaly_threshold)

    # Output requirement
    print(f"Result: {final_diagnostic}")

# Simulated sensor input log sequence (deterministic)
logs = [
    "[SYS] cycle start temp=45.2 pressure=60.1 nominal operation",
    "[DBG] checksum update complete",
    "[MON] cycle phase2 temp=52.8 detected spike",
    "[ERR] disk_queue_full retry=3",
    "[SYS] cycle end temp=48.9 pressure=58.3 post-stabilization",
    "[DBG] memory cleanup triggered",
    "[MON] cycle start temp=55.1 pressure=65.0 high load"
]

analyze_health_log(logs)