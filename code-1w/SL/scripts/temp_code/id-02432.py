import itertools

# Simulate a sensor fusion system for thermal regulation in industrial reactor
def collect_sensor_data():
    # Real data stream simulation (simplified)
    return [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]

# Irrelevant function: simulates pressure readings (distractor)
def collect_pressure_readings():
    pressures = []
    for i in range(7):
        pressures.append(101.3 + i * 0.4 + (i % 2) * 0.1)
    return pressures  # Never used

# Misleading transformation chain
def transform_signal(data):
    shifted = [x - 20 for x in data]
    amplified = [round(x * 1.05, 2) for x in shifted]
    filtered = list(itertools.dropwhile(lambda x: x < 3.5, amplified))
    if len(filtered) == 0:
        filtered = [0.0]  # Fallback that won't trigger
    return filtered

# Decoy function with complex logic but no impact
def analyze_stability_pattern(temp_sequence):
    trend_changes = 0
    for i in range(1, len(temp_sequence)):
        if (temp_sequence[i] - temp_sequence[i-1]) * (temp_sequence[i-1] - temp_sequence[i-2]) < 0 if i > 1 else False:
            trend_changes += 1
    score = trend_changes * 1.5
    return round(score, 2)  # Computed but unused

# Core calculation obscured by noise
def compute_entropy(signal):
    total = sum(signal)
    normalized = [x / total for x in signal]
    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * __import__('math').log(p)
    return round(entropy, 4)

# Higher-order function distractor
def create_validator(threshold):
    def validate(value):
        return value > threshold
    return validate

# Main processing pipeline
sensor_data = collect_sensor_data()

# Dead code path 1: data validation that's never invoked
critical_validator = create_validator(50.0)

# Irrelevant combinatorics on indices
index_pairs = list(itertools.combinations(range(len(sensor_data)), 2))
mean_pair_diff = sum(abs(sensor_data[i] - sensor_data[j]) for i, j in index_pairs) / len(index_pairs) if index_pairs else 0

# Transform data through multiple layers
processed_signal = transform_signal(sensor_data)

# Compute auxiliary metrics (some are red herrings)
efficiency_index = len(processed_signal) / len(sensor_data)
drift_estimate = max(sensor_data) - min(sensor_data)
baseline_shift = sensor_data[0] - 20.0

# Hidden critical step: generate efficiency log from raw sensor data
raw_entropy = compute_entropy(sensor_data)
efficiency_log = [efficiency_index, raw_entropy, drift_estimate, baseline_shift]

# Analyze stability (result ignored)
stability_score = analyze_stability_pattern(sensor_data)

# Pressure data collected but not used (major red herring)
pressure_profile = collect_pressure_readings()
pressure_variance = sum((p - sum(pressure_profile)/len(pressure_profile))**2 for p in pressure_profile)

# Critical assignment buried in noise
thermal_capacity = None

# Complex conditional with misleading branches
if len(processed_signal) > 3:
    adjustment_factor = 1.25
    if raw_entropy > 1.0:
        scaling_vector = [adjustment_factor * x for x in efficiency_log[:3]]
        intermediate_sum = sum(scaling_vector)
        if intermediate_sum > 5.0:
            thermal_capacity = intermediate_sum * efficiency_log[1]
        else:
            # This branch seems plausible but won't execute
            backup_weights = [0.5, 0.3, 0.2]
            thermal_capacity = sum(w * x for w, x in zip(backup_weights, efficiency_log))
    else:
        # Alternative path using bit manipulation (never reached)
        raw_bits = int(sum(sensor_data)) << 2
        thermal_capacity = raw_bits & 0xFFFF
else:
    # Fallback using XOR folding (not triggered)
    folded = 0
    for val in sensor_data:
        folded ^= int(val)
    thermal_capacity = folded / 100.0

# Final correction based on hidden rule
if thermal_capacity is not None and thermal_capacity > 0:
    # Apply final calibration using unused pressure variance as distraction
    dummy_correction = pressure_variance * 0.001  # Computed but not applied
    thermal_capacity = round(thermal_capacity - 0.15, 4)  # Actual final step

print(f"Result: {thermal_capacity}")