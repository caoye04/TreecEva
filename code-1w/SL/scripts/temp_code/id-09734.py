import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [14, 28, 42, 56, 70, 84, 98]
offset_compensation = 1.5
scaling_factor = 2.0
dummy_counter = 0
useless_sum = 0
placeholder_list = []
ignored_threshold = 50

# Irrelevant accumulation (distractor)
for reading in raw_readings:
    useless_sum += reading % 7
    placeholder_list.append(reading * 0.1)

def deprecated_filter(data):
    # Dead function - never called
    return [x for x in data if x > 30]

# Transform readings with offset and scaling
calibrated_readings = [(r + offset_compensation) * scaling_factor for r in raw_readings]

# Generate auxiliary metadata (mostly irrelevant)
metadata_map = {}
for idx, val in enumerate(calibrated_readings):
    metadata_map[f'sensor_{idx}'] = {
        'raw': raw_readings[idx],
        'calibrated': val,
        'flagged': val > 60,
        'checksum': (idx + val) % 13
    }
    dummy_counter += 1  # Misleading counter increment

# Decoy transformation path (unused)
if len(calibrated_readings) > 10:
    transformed_data = [x / 2 for x in calibrated_readings]
elif sum(calibrated_readings) < 1000:
    transformed_data = [x * 1.1 for x in calibrated_readings]
else:
    transformed_data = [x for x in calibrated_readings]

# Actual transformation used
transformed_data = list(map(lambda x: x if x < 80 else 80 + (x - 80) ** 0.5, calibrated_readings))

# Extraneous set operations (distractor)
unique_values = set(transformed_data)
excluded_set = {x for x in unique_values if x < 30}
overlap_check = unique_values & excluded_set

# Complex threshold function with red herring logic
threshold_func = lambda x: True if (x > 75 and (x % 5 == 0 or x % 7 == 0)) else False

# Secondary decoy analysis function (never invoked)
def evaluate_outlier_sequence(data):
    count = 0
    for i in range(1, len(data)):
        if data[i] - data[i-1] > 10:
            count += 1
    return count > 3

# Core analysis logic with conditional expression and nesting
def analyze_pattern(signal, threshold_criteria):
    if not signal:
        return -1
    
    peak = max(signal)
    base_ref = sum([x for x in signal if x < 60]) / len([x for x in signal if x < 60])
    
    high_freq_components = 0
    volatility_score = 0
    
    for val in signal:
        if threshold_criteria(val):
            high_freq_components += 1
        if val > base_ref + 10:
            volatility_score += (val - base_ref) * 0.3
    
    # Deeply nested decision logic with distractors
    adjustment_factor = 0
    if peak > 90:
        if high_freq_components >= 3:
            if volatility_score > 15:
                adjustment_factor = 2.5
            else:
                adjustment_factor = 1.2  # Misleading branch
        else:
            temp_val = math.log(peak)  # Computation that looks important but unused
            adjustment_factor = 0.8
    elif peak > 80:
        adjustment_factor = 1.8
    else:
        adjustment_factor = 1.0
    
    # Final computation using correct path
    diagnostic_value = (base_ref + high_freq_components * 3.7 + adjustment_factor * 4.2)
    
    # Conditional expression with embedded logic
    final_score = diagnostic_value if diagnostic_value > 0 else abs(diagnostic_value) * 0.5
    
    return int(round(final_score))

# Execute main analysis
interim_result = analyze_pattern(calibrated_readings, lambda x: x > 100)  # Incorrect criteria (red herring call)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")