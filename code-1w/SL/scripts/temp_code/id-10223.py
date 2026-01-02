from collections import defaultdict, Counter
import math

# Simulated telemetry data from distributed sensors
telemetry_streams = [
    [1.2, 0.9, 1.5, 2.1, 1.8, 0.7],
    [0.8, 1.1, 1.0, 1.3, 0.9, 1.4],
    [2.5, 1.7, 2.2, 1.9, 2.4, 2.0],
    [0.5, 0.3, 0.6, 0.4, 0.7, 0.5]
]

# Irrelevant baseline thresholds (distractor)
baseline_thresholds = {"A": 0.45, "B": 0.62, "C": 0.38, "D": 0.71}

# System health mapping (only partially used)
health_map = defaultdict(lambda: 'unknown')
for i, label in enumerate(['sensor_0', 'sensor_1', 'sensor_2', 'sensor_3']):
    health_map[label] = 'critical' if i % 3 == 0 else 'stable'

# Decoy function – appears important but unused in final calculation
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Auxiliary transformation with red herring output
def transform_readings(streams):
    transformed = []
    aggregate_stats = []
    for stream in streams:
        normalized = [x * math.log(x + 1e-5) for x in stream]  # distorts values
        filtered = [x for x in normalized if x > -5]  # noop practically
        transformed.append(filtered)
        aggregate_stats.append(sum(filtered))
    
    # Misleading intermediate result
    avg_magnitude = sum(aggregate_stats) / len(aggregate_stats) if aggregate_stats else 0
    spike_count = sum(1 for s in streams for val in s if val > 1.5)
    return transformed, avg_magnitude, spike_count

# Hidden pattern detector (used indirectly via side-channel logic)
def detect_pattern(sequence):
    if len(sequence) < 4:
        return False
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return any(diffs[i] == diffs[i+1] == diffs[i+2] for i in range(len(diffs)-2))

# Core processing pipeline
log_data = {
    'events': [
        {'type': 'read', 'src': 0, 'val': 1.2},
        {'type': 'read', 'src': 1, 'val': 0.9},
        {'type': 'read', 'src': 0, 'val': 1.5},
        {'type': 'read', 'src': 2, 'val': 2.5},
        {'type': 'read', 'src': 1, 'val': 1.1},
    ],
    'timestamps': [1678886400, 1678886401, 1678886402, 1678886403, 1678886404]
}

system_state = {
    'active_sensors': {0, 1, 2},
    'calibration_mode': False,
    'last_reset': 1678886300,
    'version': 'v2.3.1'
}

# Dead code path — simulates fallback mechanism never triggered
def fallback_recalibrate(state):
    state['calibration_mode'] = True
    adjustment = sum([len(s) for s in telemetry_streams])
    return adjustment * 0.01

# Real-time anomaly scoring with conditional expressions and set ops
anomaly_flags = set()
critical_bounds = defaultdict(int)

for idx, stream in enumerate(telemetry_streams):
    mean_val = sum(stream) / len(stream)
    variance = sum((x - mean_val) ** 2 for x in stream) / len(stream)
    critical_bounds[idx] = 2 * math.sqrt(variance) if variance > 0.1 else 0.5
    
    # Conditional expression used as control gate
    status = 'alert' if mean_val > 1.6 else ('watch' if mean_val > 0.8 else 'normal')
    
    if status == 'alert' and idx in system_state['active_sensors']:
        anomaly_flags.add(idx)

# Simulate historical comparison (unused in final logic)
historical_averages = [1.1, 0.95, 2.05, 0.48]
variance_drift = [
    abs((sum(telemetry_streams[i]) / len(telemetry_streams[i])) - historical_averages[i])
    for i in range(len(telemetry_streams))
]

def process_metrics(logs, state):
    src_counter = Counter(event['src'] for event in logs['events'])
    total_reads = sum(src_counter.values())
    
    # Key branching logic based on sensor activity and patterns
    primary_sources = {src for src, cnt in src_counter.items() if cnt >= 1}
    active_match = len(primary_sources & state['active_sensors'])
    
    # Hidden dependency: only sensor 0 has repeating diff pattern
    pattern_detected = detect_pattern(telemetry_streams[0])
    
    # Compute base metric
    base_metric = 0
    for event in logs['events']:
        if event['src'] == 0:
            base_metric += event['val'] * 10
        elif event['src'] == 1:
            base_metric += event['val'] * 5

    # Conditional amplification
    multiplier = 3 if pattern_detected and active_match >= 2 else 1
    
    # Final diagnostic depends on subtle interaction between pattern and source count
    intermediate_result = base_metric * multiplier
    
    # Additional obfuscation: irrelevant min/max usage
    max_val = max(event['val'] for event in logs['events'])
    min_val = min(event['val'] for event in logs['events'])
    range_penalty = (max_val - min_val) * 2 if max_val > 2.0 else 0
    
    # Distractor: this looks like it affects output but doesn't due to order
    decoy_adjustment = fallback_recalibrate(state)  # returns small float, not applied
    
    # Actual final computation
    result = int(intermediate_result - range_penalty)  # integer conversion hides trail
    
    # Critical assignment point
    final_diagnostic = result + 17  # offset applied deterministically
    
    return final_diagnostic

# Execution point of interest
transformed_data, meta_score, spikes = transform_readings(telemetry_streams)

# Key statement
final_diagnostic = process_metrics(log_data, system_state)

print(f"Result: {final_diagnostic}")