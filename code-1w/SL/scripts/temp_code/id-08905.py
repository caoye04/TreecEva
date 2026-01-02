import math

# Simulated sensor array data with noise and redundancy
data_stream = [127, 255, 63, 191, 31, 159, 95, 223, 47, 175, 111, 239]
redundant_buffer = [0] * 12
normalization_key = 255.0
baseline_offset = 10

def apply_mask(x, mask=0x7F):
    # Irrelevant masking function for distraction
    return x & mask

def legacy_transform(val):
    # Obsolete transformation - red herring
    return int((val ** 0.5) * 16)

def is_stable_reading(x):
    # Determines if a reading is within acceptable fluctuation range
    return 32 <= x <= 224

def correct_nonlinear_distortion(x):
    # Real correction used in processing chain
    return x * (1 + 0.1 * math.sin(math.pi * x / 128))

def calculate_entropy(data):
    # Distractor: computes Shannon entropy but unused in main logic
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total if total else 0
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

calibration_factor = 0.987  # Precision calibration from lab measurements

# Step 1: Filter valid sensor readings
cleaned_readings = []
for val in data_stream:
    if is_stable_reading(val):
        cleaned_readings.append(val)

# Step 2: Apply nonlinear correction to compensate for hardware distortion
distortion_corrected = []
for x in cleaned_readings:
    corrected = correct_nonlinear_distortion(x)
    distortion_corrected.append(round(corrected, 6))

# Step 3: Normalize to [0,1] scale using normalization key
normalized = [round(x / normalization_key, 6) for x in distortion_corrected]

# Step 4: Amplify signal based on calibration factor
amplified = [round(x * calibration_factor, 6) for x in normalized]

# Step 5: Apply dynamic threshold filtering using adaptive lambda
dynamic_threshold = lambda amp: 0.45 + (calibration_factor - 0.9) * 0.1
filtered_data = [x for x in amplified if x > dynamic_threshold(0)]

# Step 6: Aggregate via weighted combination with exponential weighting
weights = [math.exp(i / len(filtered_data)) for i in range(len(filtered_data))] if filtered_data else [1]
total_weight = sum(weights)
weighted_sum = sum(w * v for w, v in zip(weights, filtered_data))
aggregate_measure = weighted_sum / total_weight if total_weight else 0

# Step 7: Process through diagnostic engine
def process_readings(data, calib):
    if not data:
        return -1
    
    # Compute moving average of first three elements (if available)
    sample_window = data[:3]
    moving_avg = sum(sample_window) / len(sample_window) if sample_window else 0
    
    # Apply calibration-sensitive transformation
    adjusted = moving_avg * (1 + (1 - calib))
    
    # Complex conditional logic with nested checks
    if calib > 0.95:
        if adjusted > 0.7:
            diagnostic_code = 5
        elif adjusted > 0.5:
            diagnostic_code = 4
        else:
            diagnostic_code = 3
    else:
        if adjusted > 0.8:
            diagnostic_code = 4
        elif adjusted > 0.6:
            diagnostic_code = 3
        else:
            diagnostic_code = 2
    
    # Final computation combining diagnostic code and aggregate measure
    final_score = (diagnostic_code * 1000) + int(aggregate_measure * 1000)
    
    # Dead code path - misleading return
    # if final_score < 0: return -999  
    
    return final_score

# Unused legacy pipeline - dead code for distraction
legacy_output = [legacy_transform(x) for x in data_stream]
masked_data = list(map(lambda z: apply_mask(z), data_stream))
entropy_value = calculate_entropy(data_stream)

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print result
print(f"Result: {final_diagnostic}")