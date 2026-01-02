import math

# Simulated sensor data processing pipeline with performance scoring
def analyze_response_time(latency_ms):
    if latency_ms < 50:
        return 9
    elif latency_ms < 100:
        return 7
    elif latency_ms < 200:
        return 5
    else:
        return 3

def compute_stability_factor(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return max(0, 10 - math.sqrt(variance) / 5)

def evaluate_consistency(log_entries):
    transitions = 0
    for i in range(1, len(log_entries)):
        if log_entries[i] != log_entries[i-1]:
            transitions += 1
    return 10 if transitions == 0 else max(1, 10 - transitions // 2)

def dummy_analysis(data):  # Dead function - irrelevant
    return sum(x * 0.1 for x in data if x > 50)

def legacy_calibration(values):  # Unused legacy code
    adjusted = [v * 0.95 for v in values]
    return adjusted

# Irrelevant utility functions (distractors)
toggle_bit = lambda x, bit: x ^ (1 << bit)
shift_and_mask = lambda val, shift: (val << shift) & 0xFF

# Sensor input data (simulated)
response_times = [45, 67, 89, 52, 78]
raw_sensor_readings = [102, 105, 98, 103, 101, 104, 100]
operation_log = ['STABLE', 'STABLE', 'STABLE', 'ERROR', 'RECOVERED', 'STABLE']

# Misleading intermediate computations
noise_floor = sum(math.sin(r/10) for r in raw_sensor_readings)
dummy_metric_a = noise_floor * 1.5
dummy_metric_b = toggle_bit(len(operation_log), 3)
dummy_list_transform = [shift_and_mask(x, 2) for x in raw_sensor_readings]

# Real metrics computation
metric_latency = analyze_response_time(sum(response_times) / len(response_times))
metric_stability = compute_stability_factor(raw_sensor_readings)
metric_consistency = evaluate_consistency(operation_log)

# Additional red herring variables
phantom_score = metric_latency * 0.7 + 15
shadow_weight = 0.0  # Never used
placeholder_array = [0] * 10

# Weights for aggregation (some are decoys)
weights = {
    'latency': 0.4,
    'stability': 0.35,
    'consistency': 0.25,
    'fictional': 0.0  # Invalid weight - distractor
}

# Metrics dictionary with extra irrelevant entries
metrics = {
    'latency': metric_latency,
    'stability': metric_stability,
    'consistency': metric_consistency,
    'dummy': dummy_metric_a,
    'buffer_overflow_count': 7,  # Fake metric
    'last_reset_code': 0xDEAD  # Hex distraction
}

# Core aggregation logic
aggregate_performance = lambda m, w: (
    m['latency'] * w['latency'] + 
    m['stability'] * w['stability'] + 
    m['consistency'] * w['consistency']
)

# Final score calculation
final_score = aggregate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")