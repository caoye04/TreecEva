import math

# Simulated sensor array diagnostics with data transformation and filtering
def analyze_sensor_array(raw_readings, threshold):
    filtered_data = [x for x in raw_readings if abs(x) > threshold]
    normalized = list(map(lambda val: round(val / max(raw_readings), 3), filtered_data))
    return normalized

# Irrelevant helper: computes statistical dispersion (not used in final path)
def compute_dispersion(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 4)

# Data transformation pipeline
def transform_signal(signal_sequence, factor):
    shifted = [int(x * factor) % 100 for x in signal_sequence]
    reversed_chunk = shifted[::-1]  # slicing operation
    return [x for x in reversed_chunk if x % 2 == 0]

# Core processing function with multiple steps
def process_metrics(data_slice, settings):
    base_offset = settings['offset']
    accumulation = 0
    
    for i in range(len(data_slice)):
        if i % 2 == 0:
            accumulation += data_slice[i] * base_offset
        else:
            accumulation -= int(data_slice[i] / 2)
    
    # Introduce bit manipulation red herring
    decoy_mask = 0b101010
    masked_accum = accumulation ^ decoy_mask  # irrelevant to final logic
    
    # Conditional adjustment based on length (critical path)
    if len(data_slice) > 4:
        accumulation = accumulation // 2
    elif len(data_slice) == 3:
        accumulation = accumulation + 100
    else:
        accumulation = accumulation * 2
    
    # Apply logarithmic scaling only if positive
    if accumulation > 0:
        accumulation = int(math.log(accumulation + 1, 2)) * 3
    
    return accumulation

# Unused recursive function - dead code path
def recursive_sum(n):
    if n <= 1:
        return 1
    return n + recursive_sum(n - 1)

# Decoy configuration and fake analysis
fake_config = {
    'mode': 'debug',
    'buffer': 256,
    'active': False
}
fake_readings = [-23.5, 15.8, 90.1, -44.3, 12.9]
phantom_result = compute_dispersion(fake_readings)  # misleading intermediate

# Real data flow
config = {'offset': 7, 'active': True}
raw_input = [89.3, -12.7, 44.2, 67.1, -30.5, 55.8]
threshold_filter = 20

# Step-by-step execution with distractions
target_subset = [x for x in raw_input if x > 0]  # Positive values only
transformed_signal = transform_signal(target_subset, 1.5)

# Slice and transform again using lambda and slicing
preliminary_data = list(map(lambda z: z + 5, transformed_signal[1:4]))

# Main analysis branch
refined_readings = analyze_sensor_array(raw_input, threshold_filter)
digitized = [int(abs(x) * 100) for x in refined_readings]
processed_level = process_metrics(digitized, config)

# Multiple assignment red herring
backup_a, backup_b, backup_c = 0, 0, 0
if processed_level > 100:
    backup_a = 999
elif processed_level < 50:
    backup_b = 777
else:
    backup_c = 555

# Final computation - key statement
final_diagnostic = process_metrics(transformed_data, config)

# Correcting undefined variable from above line (distractor trap)
transformed_data = digitized[::2]  # slicing with step
final_diagnostic = process_metrics(transformed_data, config)

print(f"Result: {final_diagnostic}")