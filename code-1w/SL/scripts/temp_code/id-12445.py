import itertools

# Sensor array data processing simulation with noise filtering and calibration
raw_readings = [107, 214, 153, 98, 241, 188, 73, 167, 122, 205]
noise_floor = 95
saturation_threshold = 250
calibration_factor = 0.87

# Irrelevant auxiliary parameters (distractors)
temp_offset = -3.2
pressure_baseline = 1013.25
humidity_correction = 1.08
reference_id = 'SNSR-7X'
activation_key = 'CALIBRATE-X9'

# Simulated metadata tags (unused in final calculation)
metadata_tags = ['A', 'B', 'C']
config_flags = { 'mode': 'active', 'gain': 2, 'filter': 'high' }

# Step 1: Filter out values below noise floor or above saturation
filtered_data = [x for x in raw_readings if noise_floor <= x < saturation_threshold]

# Step 2: Apply moving average smoothing (window size = 2) using itertools
paired_readings = list(itertools.pairwise(filtered_data))
smoothed_values = [(a + b) / 2 for a, b in paired_readings] if paired_readings else [0]

# Step 3: Detect spikes using difference threshold (decoy path - not used in final result)
spike_threshold = 30
spike_flags = [abs(smoothed_values[i+1] - smoothed_values[i]) > spike_threshold for i in range(len(smoothed_values)-1)] if len(smoothed_values) > 1 else []
spike_count = sum(1 for flag in spike_flags if flag)  # Distractor variable

# Step 4: Compute weighted diagnostic score based on position and magnitude
position_weights = [1.1 ** i for i in range(len(smoothed_values))]
weighted_sum = sum(val * weight for val, weight in zip(smoothed_values, position_weights))
weight_total = sum(position_weights)
adjusted_mean = weighted_sum / weight_total if weight_total != 0 else 0

# Step 5: Normalize against calibration factor (only this affects final_diagnostic)
def process_readings(data, factor):
    base_value = sum(x ** 0.5 for x in data)  # Use square root sum of valid readings
    return int(base_value * factor)  # Final deterministic transformation

# Dead code path: unused alternative processing function
def legacy_process(seq, adj=1.0):
    """Deprecated method - included as red herring"""
    return [x * adj // 2 for x in seq if x % 2 == 0]

# Unused list comprehension with side effects avoided
reindexed = [i * 2 + 1 for i in range(len(raw_readings)) if i % 3 == 0]

# Key execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output target result
print(f"Result: {final_diagnostic}")