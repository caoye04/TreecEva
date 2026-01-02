def monitor_subsystem_performance(sensor_data, thresholds):
    performance_score = 0
    for i, reading in enumerate(sensor_data):
        if i % 3 == 0:
            performance_score += reading // 2
        elif reading > thresholds.get(i % 5, 100):
            performance_score -= 1
    return performance_score


def compute_data_integrity_check(data_stream):
    seen = set()
    duplicates = 0
    for val in data_stream:
        if val in seen:
            duplicates += 1
        seen.add(val)
    return duplicates * 1.5


def evaluate_signal_quality(signals):
    total_power = 0
    for s in signals:
        if s < 0:
            total_power += abs(s) // 4
        else:
            total_power += s ** 0.5
    return int(total_power)


def generate_decoy_metrics(n):
    decoy_values = []
    for i in range(n):
        temp = (i * 7 + 13) % 19
        decoy_values.append(temp if temp % 2 == 0 else temp + 1)
    return decoy_values

# Irrelevant helper function with dead logic
def unused_diagnostics(config_map):
    status = {}
    for k, v in config_map.items():
        status[k] = (v + 5) * 2 if isinstance(v, int) else len(v)
    return status

# Unused transformation chain
intermediate_cache = [x**2 + 2*x + 1 for x in range(15) if x % 4 != 3]
shadow_buffer = {k: v for k, v in zip(['a','b','c'], [sum(range(i, i+3)) for i in [1,4,7]])}

# Real input data
health_logs = [88, 92, 76, 85, 90, 83, 77, 88, 95]
system_flags = {0: True, 1: False, 2: True, 3: True, 4: False}

# Distractor variables
baseline_readings = [x * 1.1 for x in health_logs if x > 80]
calibration_offset = sum(baseline_readings) / len(baseline_readings) if baseline_readings else 0

# Simulate auxiliary subsystems with misleading computations
aux_sensor_data = [x + (i*2) for i, x in enumerate(health_logs[:6])]
aux_thresholds = {0: 85, 1: 90, 2: 75, 3: 88, 4: 93}
phantom_score = monitor_subsystem_performance(aux_sensor_data, aux_thresholds)

# Another red herring path
data_stream_fragment = [88, 92, 76, 85, 90, 83, 77, 88]
duplicate_penalty = compute_data_integrity_check(data_stream_fragment)

# Signal processing decoy
signal_array = [-4, 16, -8, 25, 36, -12]
raw_quality = evaluate_signal_quality(signal_array)

# Generate meaningless metrics to distract
decoy_metrics = generate_decoy_metrics(10)

# Core logic embedded within noise
flag_count = sum(1 for k, v in system_flags.items() if v)
adjusted_logs = [x + 2 for x in health_logs if x >= 85]
log_sum = sum(adjusted_logs)

# Key computation hidden among distractors
reference_key = len(health_logs) + flag_count
scaling_factor = 3 if reference_key > 10 else 2

# Main analysis function combining multiple concepts
def analyze_system_state(logs, flags):
    # Use enumerate and conditional indexing
    indexed_weight = 0
    for idx, val in enumerate(logs):
        if idx % 2 == 0 and val > 80:
            indexed_weight += val // (idx + 1)

    # Use set operations to filter unique patterns
    unique_logs = set(logs)
    high_severity = {x for x in unique_logs if x < 85}
    medium_severity = {x for x in unique_logs if x >= 85}
    overlap_test = len(high_severity & medium_severity)

    # Dictionary-based state resolution
    state_map = {}
    for i, log in enumerate(logs):
        state_map[i] = log * (i % 4 + 1)

    # Critical aggregation
    base_value = sum(state_map.values()) // len(state_map)
    adjustment = len(medium_severity) - len(high_severity) + overlap_test

    # Final computation using prior hidden variables
    global scaling_factor
    result = (base_value + adjustment) * scaling_factor - phantom_score

    # Additional distraction inside function
    dummy_dict = {chr(65+i): i*result for i in range(3)}
    temp_list = [result - i for i in range(5) if i % 2 == 1]

    return result

# Execution point of interest
final_diagnostic = analyze_system_state(health_logs, system_flags)

# Print required output
print(f"Target result: {final_diagnostic}")