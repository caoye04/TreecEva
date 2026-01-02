import math

# Simulated sensor data processing with performance diagnostics
def analyze_sensor_readings(readings):
    if not readings:
        return 0

    # Irrelevant transformation: normalize to z-scores (not used in final result)
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_val) / std_dev for x in readings] if std_dev > 0 else [0] * len(readings)

    # Relevant logic: count valid high-frequency signals
    high_freq_count = 0
    threshold = 75
    for val in readings:
        if val > threshold and val % 2 == 1:
            high_freq_count += 1

    return high_freq_count


def calculate_efficiency_index(data):
    # Misleading function: computes a metric that looks important but is unused
    base = sum(x * x for x in data if x > 0)
    penalty = len([x for x in data if x < 50])
    return int(base / (penalty + 1)) if penalty + 1 != 0 else base


def extract_signal_pattern(sequence):
    # Complex but partially irrelevant pattern extraction
    pattern_code = 0
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            pattern_code ^= val  # Bitwise mix
        elif i % 4 == 0:
            pattern_code += val % 7
    
    # Dead code path: never executed due to prior conditions
    if len(sequence) > 1000:
        extra_boost = math.log(len(sequence))
        pattern_code += int(extra_boost)

    return pattern_code


def validate_integrity(checksum, ref):
    # Distractor: complex validation not impacting final score
    if checksum == 0:
        return False
    return (checksum ^ ref) % 9 == 0

# Unused helper that appears critical
def compute_thermal_compensation(temp_log):
    comp_factor = 0
    for t in temp_log:
        comp_factor += math.sin(t / 10) * math.cos(t / 20)
    return round(comp_factor, 3)

# Core aggregation logic with subtle dependencies
def aggregate_performance(dataset):
    raw_metrics = []
    decoy_accumulator = 0  # Looks important but isn't used

    for entry in dataset:
        sensor_analysis = analyze_sensor_readings(entry['signals'])
        signal_fingerprint = extract_signal_pattern(entry['signals'])
        
        # Conditional expression (required Python feature)
        adjusted_weight = 1.5 if sensor_analysis > 3 else 0.8
        
        # Compute intermediate metric (partially relevant)
        contribution = sensor_analysis * adjusted_weight + (signal_fingerprint % 10)
        raw_metrics.append(contribution)
        
        # Dead computation: builds up value that's never used
        decoy_accumulator += int(math.sqrt(abs(contribution - adjusted_weight)))

    # Real answer depends on sorted second element
    sorted_metrics = sorted(raw_metrics)
    mid_index = len(sorted_metrics) // 2
    median_value = sorted_metrics[mid_index]

    # Final nonlinear transformation
    stability_bias = 0.9 if len(dataset) % 2 == 1 else 1.1
    precision_factor = 0.05 * len([m for m in raw_metrics if m > 10])

    # Key statement: this determines the final output
    final_score = int((median_value * stability_bias) + precision_factor * 100)

    # Irrelevant print that distracts from actual return
    # print(f'Decoy accumulator: {decoy_accumulator}')

    return final_score

# Simulated benchmark data (deterministic input)
benchmark_data = [
    {'id': 'A7', 'signals': [68, 76, 79, 82, 91, 45], 'temp': [23, 25, 24]},
    {'id': 'B2', 'signals': [70, 77, 88, 95, 63, 52, 81], 'temp': [26, 27, 25, 24]},
    {'id': 'C9', 'signals': [50, 60, 70, 80], 'temp': [22, 23]},
    {'id': 'D4', 'signals': [85, 73, 92, 66, 77, 88, 99, 101], 'temp': [28, 29, 30]},
    {'id': 'E1', 'signals': [40, 55, 65], 'temp': [21, 20]}
]

# Execution point of interest
final_score = aggregate_performance(benchmark_data)
print(f'Target result: {final_score}')