def preprocess_readings(sensor_log):
    processed = []
    for idx, val in enumerate(sensor_log):
        if idx % 3 == 0:
            processed.append(val * 1.05)
        elif idx % 7 == 0:
            processed.append(val * 0.98)
        else:
            processed.append(val + 2)
    return processed

# Irrelevant transformation chain (decoy)
def transform_sequence(data):
    result = []
    for i in range(len(data)):
        if i < 5:
            result.append(data[i] ** 0.5)
        else:
            result.append(data[i] // 2)
    return result

# Unused recursive red herring
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2)

# Decoy metric with misleading name
def compute_robustness_index(values):
    total = 0
    for v in values:
        if v > 50:
            total += v * 0.75
    return total // 3  # Dead-end computation

# Real aggregation logic
def aggregate_metrics(turbine_data, key_weights):
    temp_buffer = [0] * len(turbine_data)
    
    # Distractor: irrelevant initialization block
    baseline_offset = 127
    checksum = 0
    debug_trace = []
    for i in range(4):
        checksum += baseline_offset ^ (i + 10)
        debug_trace.append(checksum % 100)
    
    # Core logic disguised among noise
    weighted_sum = 0
    normalization_factor = 0
    
    for index, (reading, weight) in enumerate(zip(turbine_data, key_weights)):
        if reading < 0 or weight < 0:
            continue
        adjusted = reading * (weight / 100.0)
        weighted_sum += adjusted
        normalization_factor += weight / 100.0
    
    # Secondary correction pass
    correction_accumulator = 0.0
    for j, sample in enumerate(turbine_data):
        if j % 4 == 0 and j != 0:
            correction_accumulator += sample * 0.01
    
    # Final computation path (only this matters)
    if normalization_factor > 0:
        base_result = weighted_sum / normalization_factor
    else:
        base_result = 0
    
    final_adjustment = base_result + correction_accumulator - 8.6
    
    # Key assignment point
    final_diagnostic = int(round(final_adjustment))
    
    # Red herring: unused conditional branch
    if final_diagnostic in debug_trace:
        final_diagnostic *= 2  # Never reached due to logic
    
    return final_diagnostic

# Simulated sensor input (real data)
turbine_data = [85, 92, 78, 96, 88, 73, 89, 94, 82, 91]

# Calibration weights (aligned with turbine_data)
calibration_sequence = [95, 88, 102, 90, 93, 85, 97, 89, 94, 91]

# Preprocessing call (distractor - result not used in final calculation)
processed_turbine = preprocess_readings(turbine_data)

# Phantom function calls (dead code paths)
decoy_data = transform_sequence(calibration_sequence)
phantom_score = compute_robustness_index(turbine_data)
recursive_distractor(10)

# Critical execution point
final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)

print(f"Result: {final_diagnostic}")