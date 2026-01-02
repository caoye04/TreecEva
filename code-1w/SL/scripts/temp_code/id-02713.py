import math

# Simulated sensor array data (irrelevant initialization)
sensor_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
raw_readings = [145, 267, 98, 412, 301]
calibration_offsets = {'alpha': 12, 'beta': -8, 'gamma': 5, 'delta': 0, 'epsilon': 15}

# Irrelevant string processing for metadata handling
header = "SENS-DATA-LOG-2024"
formatted_header = header.lower().replace('-', '_').strip()
log_id = formatted_header[5:9]  # Misleading extraction

# Real signal preprocessing begins
normalized = []
for i, val in enumerate(raw_readings):
    key = sensor_names[i]
    corrected = val + calibration_offsets[key]
    normalized.append(max(corrected, 0))

# Bit manipulation red herring (unused later)
temp_flag = 0
for x in normalized:
    temp_flag ^= (x & 7) << 2
    temp_flag += x % 3

# Create frequency mask (distractor)
frequency_weights = {f'band_{i}': math.sin(i * 0.5) for i in range(5)}
weighted_sum = sum(frequency_weights.values()) * 100  # Never used

# Actual processing path starts here
processed_data = [round(x ** 0.5, 2) for x in normalized if x > 100]

# Decoy list transformation
shadow_copy = processed_data[:]
for i in range(len(shadow_copy)):
    shadow_copy[i] = round(shadow_copy[i] / 3.0, 1)  # Distractor operation

# Threshold logic with set operations (mixed relevance)
thresh_levels = {15, 18, 22, 25}
active_thresholds = sorted(thresh_levels | {len(processed_data) * 3})  # Adds 9

# Map creation with irrelevant entries
threshold_map = {}
for t in active_thresholds:
    if t < 20:
        threshold_map[f'level_{t}'] = t * 1.1
    else:
        threshold_map[f'level_{t}'] = t * 0.9

# Dead recursive function (never called)
def compute_recursion(n):
    if n <= 1:
        return 1
    return n * compute_recursion(n - 2) + 2

# Real analysis function
def analyze_signal(data, thresholds):
    base_score = 0
    level_keys = sorted([int(k.split('_')[1]) for k in thresholds.keys()])
    
    # Slice-based filtering
    mid_range = level_keys[1:-1] if len(level_keys) > 2 else level_keys
    
    for reading in data:
        # String-based decision (uses slicing)
        code = f"R{int(reading)}"
        if code[1:] in {'12', '13', '14'}:
            base_score -= 5
        elif int(code[1:]) > 15:
            base_score += 7
    
    # Boolean logic chain with short-circuiting
    adjustment = 0
    if len(data) >= 3 and any(x > 18 for x in data) or not (len(data) == 1):
        if 22 in level_keys and 'level_25' in thresholds:
            adjustment = int(thresholds['level_25'] // 2)
        else:
            adjustment = -3
    else:
        adjustment = 10
    
    # Final computation with float arithmetic
    raw_total = sum(data)
    factor = thresholds[f'level_{mid_range[0]}'] if mid_range else 10
    intermediate = raw_total * (factor / 100)
    
    # Critical line: final_diagnostic depends only on this path
    final_diagnostic = base_score + adjustment + round(intermediate, 2)
    
    return final_diagnostic

# Execute main logic
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")