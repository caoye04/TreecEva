import math

# Simulated sensor data preprocessing pipeline
raw_readings = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 2.1, 6.3, 3.7, 4.0]
baseline_offset = 2.5
decoy_offset = 1.8
scaling_factor = 0.9

# Irrelevant statistical measures (distractors)
dummy_mean = sum(raw_readings) / len(raw_readings)
dummy_variance = sum((x - dummy_mean) ** 2 for x in raw_readings) / len(raw_readings)
entropy_proxy = -sum(x * math.log(x) for x in raw_readings if x > 0)  # Unused

# Signal transformation chain
filtered_readings = [x for x in raw_readings if x > 3.0]  # Filter noise
normalized_readings = [(x - baseline_offset) * scaling_factor for x in filtered_readings]

# Multiple irrelevant transformations
shifted_data = [x + 0.5 for x in normalized_readings]  # Dead path
inverted_data = [1.0 / x for x in normalized_readings if x != 0]  # Unused

# Core processing function
transformed_data = []
def transform_entry(val):
    if val < 1.0:
        return val ** 2
    elif val < 2.0:
        return math.sqrt(val)
    else:
        return val * math.log(val) if val > 0 else 0

for item in normalized_readings:
    transformed_data.append(transform_entry(item))

# Decoy analysis functions
def analyze_pattern(seq):  # Unused
    return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

def compute_momentum(seq):  # Unused
    return sum(x * (i+1) for i, x in enumerate(seq))

# Threshold logic with lambda abstraction
defect_filter = lambda x: x > 1.5
threshold_func = lambda x: defect_filter(x) and (math.sin(x) > -0.5)

# Auxiliary diagnostic chain
intermediate_flags = [int(threshold_func(x)) for x in transformed_data]
activation_count = sum(intermediate_flags)

# Secondary validation (distraction)
reference_weights = [0.1, 0.3, 0.4, 0.2]
weighted_check = sum(w * v for w, v in zip(reference_weights, transformed_data[:4]))  # Unused

# Red herring: complex bit manipulation with no impact
temp_bits = 0
for x in raw_readings:
    temp_bits ^= int(x * 10) & 0xFF
temp_bits = (temp_bits << 3) | (temp_bits >> 5)  # Obfuscation only

# Main diagnostic processor
def process_metrics(data, threshold):
    valid_entries = [x for x in data if threshold(x)]
    if not valid_entries:
        return 0.0
    
    # Multi-step aggregation
    squared_sum = sum(x * x for x in valid_entries)
    mean_val = sum(valid_entries) / len(valid_entries)
    fluctuation_index = sum(abs(a - b) for a, b in zip(valid_entries, valid_entries[1:]))
    
    # Complex composite score
    adjustment = math.cos(mean_val) if mean_val > 0 else 0
    raw_score = squared_sum * (1 + adjustment) + fluctuation_index * 0.1
    
    # Final clamping to diagnostic range
    clamped_score = max(10, min(raw_score, 999))
    return round(clamped_score)

# Execute core logic
calibration_phase = True
if calibration_phase:
    final_diagnostic = process_metrics(transformed_data, threshold_func)

# Print result for evaluation
print(f"Result: {final_diagnostic}")