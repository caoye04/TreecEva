from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_data = [
    {'sensor': 'temp', 'value': 45, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013, 'status': 'ok'},
    {'sensor': 'temp', 'value': 52, 'status': 'overheat'},
    {'sensor': 'humidity', 'value': 67, 'status': 'ok'},
    {'sensor': 'temp', 'value': 49, 'status': 'ok'}
]

# Irrelevant helper function for dead path
def analyze_network(latency_log):
    total = sum(latency_log)
    avg = total / len(latency_log) if latency_log else 0
    return [x for x in latency_log if x > avg]

# Unused data structure (distractor)
network_trace = [12, 45, 67, 23, 89, 34, 56]
high_latency_events = analyze_network(network_trace)

# Sensor aggregation logic
def collect_sensor_metrics(data):
    aggregated = defaultdict(list)
    status_count = Counter()
    
    for entry in data:
        sensor = entry['sensor']
        value = entry['value']
        status = entry['status']
        
        aggregated[sensor].append(value)
        status_count[status] += 1
    
    averages = {k: sum(v)/len(v) for k, v in aggregated.items()}
    return averages, status_count

# Baseline thresholds (some are misleading)
baseline = {
    'temp': 50.0,
    'pressure': 1010.0,
    'humidity': 60.0,
    'vibration': 15.0  # irrelevant - no such sensor
}

# Complex evaluation with red herrings
def evaluate_performance(metrics, baseline):
    score = 0
    penalty_adjustment = 0.0
    temp_deviation = abs(metrics.get('temp', 0) - baseline['temp'])
    pressure_deviation = abs(metrics.get('pressure', 0) - baseline['pressure'])
    humidity_deviation = abs(metrics.get('humidity', 0) - baseline['humidity'])
    
    # Real scoring logic begins
    if temp_deviation <= 5:
        score += 40
    elif temp_deviation < 10:
        score += 25
    else:
        score += 10
    
    if pressure_deviation < 5:
        score += 30
    elif pressure_deviation < 15:
        score += 20
    else:
        score += 5

    if humidity_deviation <= 10:
        score += 25
    else:
        score += 15
    
    # Distractor: unused conditional branch based on non-existent sensor
    if metrics.get('vibration', 0) > baseline['vibration']:
        penalty_adjustment -= 10  # never executed
    
    # Bitwise obfuscation of an irrelevant calculation
    debug_flag = 0b1010 ^ 0b1100  # result is 0b0110 = 6, unused
    mask_result = debug_flag & 0b0101  # 6 & 5 = 4, also unused
    
    # Early termination red herring (not taken)
    if score > 100:
        return -1  # dead code
    
    # Final adjustment using only relevant components
    consistency_bonus = 1 if temp_deviation < 8 and pressure_deviation < 10 else 0
    score += consistency_bonus * 5
    
    # Critical statement
    final_score = int(score)
    
    # Dead code path with misleading print
    if False:
        print(f'Debug: applying vibration correction {mask_result}')
    
    return final_score

# Data processing flow
averages, counts = collect_sensor_metrics(telemetry_data)
system_health_summary = {"metrics": averages, "issues": dict(counts)}

# Triggering key computation
final_score = evaluate_performance(averages, baseline)

# Output result
print(f"Result: {final_score}")