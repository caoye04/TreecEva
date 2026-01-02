import math

# Simulated sensor data processing pipeline for environmental anomaly detection
raw_readings = [3, 7, 15, 31, 63, 127]
baseline_offset = 2
calibration_factor = 1.25
sample_size = len(raw_readings)
adjusted_readings = [x + baseline_offset for x in raw_readings]

# Irrelevant auxiliary computation: energy consumption estimation (dead path)
power_levels = [120, 135, 150, 160, 145, 130]
total_energy = sum(power_levels) * 0.001  # kWh, unused later
average_power = total_energy / len(power_levels) if power_levels else 0

# Signal transformation with bit manipulation red herring
bit_shifted = []
for val in adjusted_readings:
    shifted = (val << 1) ^ 3  # Distraction: looks important but not used in final logic
    bit_shifted.append(shifted)

# Actual relevant transformation: detect exponential pattern via difference analysis
transformed_data = []
for i in range(1, len(adjusted_readings)):
    diff = adjusted_readings[i] - adjusted_readings[i-1]
    transformed_data.append(diff)

# Decoy function: simulates machine learning classification (never called)
def predict_anomaly_ml(data):
    weight_matrix = [[0.1, 0.9], [0.8, 0.2]]
    score = (data[0] * weight_matrix[0][0]) + (data[-1] * weight_matrix[1][1])
    return score > 0.5

# Real analysis function: recursive pattern validator
def validate_sequence(seq, index=0, cumulative=0):
    if index >= len(seq):
        return cumulative
    current = seq[index]
    is_power_of_two = current & (current - 1) == 0 and current != 0
    contribution = current if is_power_of_two else (current % 5) ** 2
    return validate_sequence(seq, index + 1, cumulative + contribution)

# Threshold calculation with slicing distraction
effective_slice = transformed_data[1:4]
spurious_metric = sum(effective_slice) / len(effective_slice) if effective_slice else 0
threshold = math.ceil(spurious_metric / 2)

# Conditional expression based override (rare case, not triggered)
override_flag = len(transformed_data) > 10
threshold = 5 if override_flag else threshold

# Dictionary-based state tracker (partial use)
status_log = {
    'init': 'complete',
    'transform': 'success',
    'validate': None,
    'final': 'pending'
}

# Core logic: analyze deviations against dynamic threshold
def analyze_pattern(pattern, limit):
    count_valid = 0
    magnitude_sum = 0.0
    for val in pattern:
        if val > limit:
            count_valid += 1
            magnitude_sum += val
    # Complex conditional expression with modular arithmetic
    adjustment = (count_valid % 3) if count_valid > 0 else -1
    score = (magnitude_sum / count_valid) * 10 if count_valid > 0 else 0
    normalized_score = round(score + adjustment, 4)
    
    # Slicing operation on temporary list
    history = [normalized_score - i for i in range(5)]
    recent = history[-3:]  # Last three predictions
    boost = sum(recent) / len(recent)
    
    # Final adjustment using dictionary lookup
    factors = {'low': 0.8, 'medium': 1.1, 'high': 1.3}
    level_key = 'high' if normalized_score > 40 else 'medium'
    final_score = normalized_score * factors.get(level_key, 1.0)
    
    return int(final_score)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Dead code path: alternate fusion algorithm
if sample_size < 5:
    temp_buffer = [0] * sample_size
    for idx, v in enumerate(adjusted_readings):
        temp_buffer[idx] = v ^ 0xFF

# Unused cleanup routine
def garbage_collect(*args):
    return len([x for x in args if x is not None])

garbage_collect(bit_shifted, power_levels, status_log)

# Status update (partial usage)
status_log['final'] = 'completed'

# Output result
print(f"Result: {final_diagnostic}")