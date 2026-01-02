def process_signals(data, config):
    magnitude_sum = 0
    phase_correction = 0.0
    temp_buffer = []
    
    for idx, (val, weight) in enumerate(zip(data, config['weights'])):
        weighted_val = val * weight
        if abs(weighted_val) > config['threshold']:
            magnitude_sum += int(abs(weighted_val))
            
            # Irrelevant phase tracking (distractor)
            if idx % 2 == 0:
                phase_correction += 0.1
            else:
                phase_correction -= 0.05
            
            # Simulate signal reflection (unused)
            reflected = (weighted_val * 0.95) ** 2
            temp_buffer.append(reflected)

    # Secondary processing with distractors
    adjusted_sum = magnitude_sum
    decay_factor = 0.9
    for _ in range(3):
        adjusted_sum *= decay_factor
        decay_factor -= 0.1

    # Dummy statistical check (irrelevant)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0.0
    stability_score = avg_temp * phase_correction

    # Actual output computation
    result_offset = len(config['weights']) * config['base_offset']
    final_result = adjusted_sum + result_offset - 5
    return int(final_result)

# Input data and configuration
raw_readings = [12, -8, 15, 3, -20]
weights_list = [1.1, 0.9, 1.5, 0.4, 2.0]
calibration_threshold = 10
base_adjustment = 3

# Filtering irrelevant low-amplitude signals (preprocessing)
filtered_data = []
for x in raw_readings:
    if abs(x) >= calibration_threshold - 2:
        filtered_data.append(x)

# Unused alternate filter path (dead code path - distractor)
if False:
    filtered_data = [x for x in raw_readings if x % 2 == 0]

# Configuration dictionary (dict operation)
thresholds = {
    'weights': weights_list,
    'threshold': calibration_threshold,
    'base_offset': base_adjustment
}

# Intermediate checksum (irrelevant)
total_pairs = 0
for i, j in zip(raw_readings, weights_list):
    total_pairs += 1

# Signal processing pipeline
intermediate_state = [x * 2 for x in filtered_data if x > 0]  # Distractor accumulation
scaling_hint = sum(intermediate_state) / len(intermediate_state) if intermediate_state else 0

# Key execution point
final_output = process_signals(filtered_data, thresholds)
print(f"Target result: {final_output}")