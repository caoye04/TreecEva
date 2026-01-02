from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (0.45, 'sensor_A', 'init'),
    (1.23, 'sensor_B', 'init'),
    (0.67, 'sensor_A', 'read'),
    (2.89, 'sensor_C', 'init'),
    (0.74, 'sensor_A', 'read'),
    (1.15, 'sensor_B', 'read'),
    (3.01, 'sensor_C', 'read'),
    (0.88, 'sensor_A', 'read'),
    (1.32, 'sensor_B', 'read')
]

system_flags = [True, False, True, True, False]
device_status = {'sensor_A': 1, 'sensor_B': 1, 'sensor_C': 0, 'sensor_D': 1}
redundancy_pool = ['backup_X', 'backup_Y']

def analyze_response_times(log):
    sensor_times = defaultdict(list)
    for entry in log:
        duration, sensor, op = entry
        if op == 'read':
            sensor_times[sensor].append(duration)
    averages = {}
    for sensor, times in sensor_times.items():
        averages[sensor] = sum(times) / len(times)
    return averages

def count_operations(log):
    op_counter = Counter(op for _, _, op in log)
    return dict(op_counter)

def calculate_entropy(flags):
    total = len(flags)
    true_count = sum(flags)
    false_count = total - true_count
    if true_count == 0 or false_count == 0:
        return 0.0
    p_true = true_count / total
    p_false = false_count / total
    return - (p_true * math.log2(p_true) + p_false * math.log2(p_false))

def validate_sensors(status):
    active = [k for k, v in status.items() if v == 1]
    inactive = [k for k, v in status.items() if v == 0]
    return active, inactive

def generate_diagnostics(sensor_data, entropy_val, operations):
    base_score = entropy_val * 100
    adjustment = len(sensor_data.get('sensor_A', [])) * 5
    # Irrelevant transformation
    temp_offset = sum([len(x) for x in redundancy_pool]) * 0.5
    base_score += adjustment
    # Dead code path - never used
    def deprecated_calib():
        return sum([ord(c) for c in 'calib']) % 7
    return round(base_score, 4)

def filter_abnormal_reads(log):
    # Extract only readings above threshold (distraction logic)
    outliers = []
    for entry in log:
        duration, sensor, op = entry
        if op == 'read' and duration > 2.0:
            outliers.append((duration, sensor))
    return outliers

def compute_system_health(log, flags):
    avg_response = sum([t for t, s, o in log if o == 'read']) / len([t for t, s, o in log if o == 'read'])
    entropy = calculate_entropy(flags)
    health_index = (1 / avg_response) * (entropy + 1) * 10
    return round(health_index, 3)

def aggregate_metrics(log, flags):
    # Core calculation path
    response_averages = analyze_response_times(log)
    operation_counts = count_operations(log)
    entropy_value = calculate_entropy(flags)
    health_metric = compute_system_health(log, flags)
    
    # Distractor variables
    unused_analysis = filter_abnormal_reads(log)
    temp_snapshot = {s: len(times) for s, times in response_averages.items()}
    calibration_sequence = [x for x in range(5) if x % 2 == 0]
    alignment_factor = math.sin(math.pi / 4)  # Unused constant
    
    # Meaningful but indirect contribution
    diagnostic_base = generate_diagnostics(response_averages, entropy_value, operation_counts)
    
    # Critical computation with distractors embedded
    final_component = 0
    for i, flag in enumerate(flags):
        if flag:
            final_component += (i + 1) * 100
        else:
            final_component -= 50
    
    # Key interference: multiple contributing factors, but only one determines answer
    scaling_factor = len(response_averages.get('sensor_A', []))
    decoy_result = scaling_factor * health_metric * diagnostic_base  # Not used
    final_diagnostic = int(diagnostic_base + final_component)
    
    # Red herring: modifying unrelated state
    device_status['sensor_D'] = 0  # No effect on result
    
    return final_diagnostic

# Execution flow
initial_stats = count_operations(timing_log)
entropy_measure = calculate_entropy(system_flags)
active_sensors, _ = validate_sensors(device_status)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output result
print(f"Result: {final_diagnostic}")