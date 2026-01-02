import math

# Simulated sensor data processing with embedded diagnostics
raw_readings = [3, 7, 2, 8, 5, 9, 4, 6, 1, 8]
offset_correction = 1.5
calibration_map = {i: round(math.sin(i) * 100, 2) for i in range(10)}

# Irrelevant auxiliary variables (distractors)
temp_log = {'status': 'OK', 'version': '2.1.0', 'mode': 'diagnostic'}
debug_trace = [0] * len(raw_readings)
redundant_copy = raw_readings.copy()
metadata_checksum = sum(len(key) for key in temp_log.keys())

# Signal preprocessing chain
adjusted_readings = [x + offset_correction for x in raw_readings]
scaled_readings = [int(x * calibration_map[i % 10]) for i, x in enumerate(adjusted_readings)]

# Bit manipulation layer (mixed paradigm)
bit_encoded = []
for val in scaled_readings:
    transformed = (val ^ 255) + 1  # Invert bits and adjust
    if transformed < 0:
        transformed = abs(transformed) | 128
    bit_encoded.append(transformed)

# Decoy function - never called
def legacy_process(data):
    return [d >> 2 for d in data if d % 3 == 0]

# String-based tagging system (Python-specific feature)
def generate_tag(value):
    tag_base = "" + ("HIGH" if value > 150 else "LOW")
    checksum_str = f"{value}{tag_base}"
    return checksum_str.lower().replace("high", "h").replace("low", "l")

tags = [generate_tag(v) for v in bit_encoded]

# Set operations: track unique categories (Python-specific feature)
category_set = set()
for tag in tags:
    if 'h' in tag:
        category_set.add('critical')
    elif 'l' in tag:
        category_set.add('normal')
    category_set.add('assessed')  # Always add

# Conditional transformation tree
transformed_data = []
for i, val in enumerate(bit_encoded):
    if i % 4 == 0:
        transformed_data.append(val // 2)
    elif i % 3 == 0 and val > 100:
        transformed_data.append(val - 50)
    else:
        transformed_data.append((val + 10) * 2)

# Dead code path - unreachable under current logic
if len(category_set) > 10:
    transformed_data = [x for x in transformed_data if x % 2 == 0]
    offset_correction *= 2  # Unused reassignment

# Dictionary-based state machine simulation
state_weights = {
    'critical': 3,
    'normal': 1,
    'assessed': 2
}
base_score = 0
for cat in category_set:
    if cat in state_weights:
        base_score += state_weights[cat] * len([t for t in tags if cat[0] in t])

# UNUSED intermediate result (red herring)
avg_transformed = sum(transformed_data) / len(transformed_data) if transformed_data else 0
max_deviation = max(transformed_data) - min(transformed_data)

# Core analysis function with complex logic
def analyze_signal_pattern(signal_list):
    length = len(signal_list)
    if length == 0:
        return 0
    
    # Compute moving average of every 3 elements
    averages = []
    for i in range(length - 2):
        avg = (signal_list[i] + signal_list[i+1] + signal_list[i+2]) / 3
        averages.append(avg)
    
    # Count peaks above median
    sorted_vals = sorted(signal_list)
    median_val = sorted_vals[length // 2]
    peak_count = 0
    for val in signal_list:
        if val > median_val * 1.1:
            peak_count += 1
    
    # Apply exponential weighting to later elements
    weighted_sum = 0.0
    for idx, value in enumerate(signal_list):
        weight = math.exp(idx / length)
        weighted_sum += value * weight
    
    # Combine metrics with nonlinear transformation
    composite = (weighted_sum * 0.1) + (peak_count ** 2) * 5
    if len(averages) > 0:
        composite -= min(averages)
    
    # Final adjustment using bit count
    bit_population = 0
    for num in signal_list:
        bit_population += bin(int(num)).count('1')
    
    result = int(composite - bit_population + base_score)  # Uses outer-scope base_score
    
    # Intentional decoy operation (no effect)
    _temp = [math.sqrt(r) for r in signal_list if r > 0]
    
    return result

# Key execution point
final_diagnostic = analyze_signal_pattern(transformed_data)

# Print required output
print(f"Result: {final_diagnostic}")