from collections import defaultdict, Counter
import itertools

# Simulated system telemetry processing with diagnostic analysis
def analyze_response_times(events):
    timing_log = defaultdict(list)
    temp_cache = []
    for event in events:
        service, duration, status = event['svc'], event['dur'], event['sts']
        if status == 'OK':
            timing_log[service].append(duration)
        else:
            # Dead path: error handling not used in final calculation
            temp_cache.append(duration * 1.5)
    return timing_log

def evaluate_consistency(logs):
    consistency_score = 0
    for svc, times in logs.items():
        if len(times) > 1:
            variance = sum((a - b) ** 2 for a, b in itertools.combinations(times, 2))
            consistency_score += variance / len(times)
    return consistency_score

def detect_anomalies(data):
    anomalies = []
    flat_data = [val for sublist in data.values() for val in sublist]
    threshold = sum(flat_data) / len(flat_data) + (max(flat_data) - min(flat_data)) * 0.25
    for svc, readings in data.items():
        for r in readings:
            if r > threshold:
                anomalies.append((svc, r))
    # Irrelevant but plausible decoy computation
    anomaly_summary = Counter([a[0] for a in anomalies])
    return anomaly_summary  # Not used later

def compute_efficiency_metric(logs):
    efficiency_pairs = []
    for service, timings in logs.items():
        avg_time = sum(timings) / len(timings)
        peak = max(timings)
        efficiency_pairs.append((avg_time, peak))
    
    weighted_sum = 0.0
    for i, (avg, peak) in enumerate(efficiency_pairs):
        weighted_sum += avg * (1.0 if i % 2 == 0 else 0.85) + (peak * 0.1)
    return weighted_sum

def generate_system_flags(raw_timings):
    flag_set = set()
    total_calls = 0
    outlier_count = 0
    for svc_data in raw_timings.values():
        total_calls += len(svc_data)
        for t in svc_data:
            if t > 90:
                outlier_count += 1
    if total_calls > 10:
        flag_set.add('HIGH_VOLUME')
    if outlier_count / total_calls > 0.3:
        flag_set.add('OUTLIER_RISK')
    if total_calls % 7 == 0:  # Misleading condition, never true in this case
        flag_set.add('CYCLIC_PATTERN')
    return flag_set

def aggregate_metrics(logs, flags):
    base_score = compute_efficiency_metric(logs)
    adjustment_factor = 1.0
    if 'HIGH_VOLUME' in flags:
        adjustment_factor *= 0.9
    if 'OUTLIER_RISK' in flags:
        adjustment_factor *= 1.1
    
    # Core calculation path
    raw_values = [t for ts in logs.values() for t in ts]
    median_val = sorted(raw_values)[len(raw_values)//2]
    mode_val = Counter(raw_values).most_common(1)[0][0]
    
    # Final diagnostic integrates multiple reasoning paths
    final_diagnostic = int(base_score * adjustment_factor + (median_val ^ mode_val))
    return final_diagnostic

# Simulated input data - fixed and deterministic
system_events = [
    {'svc': 'auth', 'dur': 45, 'sts': 'OK'},
    {'svc': 'api', 'dur': 60, 'sts': 'OK'},
    {'svc': 'db', 'dur': 75, 'sts': 'OK'},
    {'svc': 'auth', 'dur': 45, 'sts': 'OK'},
    {'svc': 'api', 'dur': 60, 'sts': 'OK'},
    {'svc': 'db', 'dur': 75, 'sts': 'OK'},
    {'svc': 'auth', 'dur': 45, 'sts': 'OK'},
    {'svc': 'api', 'dur': 95, 'sts': 'OK'},
    {'svc': 'db', 'dur': 75, 'sts': 'OK'},
    {'svc': 'auth', 'dur': 45, 'sts': 'OK'},
    {'svc': 'api', 'dur': 60, 'sts': 'OK'},
    {'svc': 'db', 'dur': 75, 'sts': 'OK'}
]

timing_log = analyze_response_times(system_events)
evaluate_consistency(timing_log)  # Dead call: result ignored
detect_anomalies(timing_log)       # Dead call: result unused
event_flags = generate_system_flags(timing_log)
final_diagnostic = aggregate_metrics(timing_log, event_flags)
print(f"Target result: {final_diagnostic}")