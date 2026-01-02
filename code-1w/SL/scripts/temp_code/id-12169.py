import math

# Simulated sensor fusion system for environmental monitoring
raw_readings = [3, 7, 1, 9, 4, 8, 2, 6, 5]
offset_compensation = 1.5
sampling_rate = 100

def apply_filter(data, factor=0.9):
    """Apply exponential smoothing (irrelevant to final result)"""
    filtered = [data[0]]
    for i in range(1, len(data)):
        filtered.append(factor * data[i] + (1 - factor) * filtered[-1])
    return filtered

# Irrelevant transformation chain
smoothed = apply_filter(raw_readings)
temp_normalized = [x / max(smoothed) for x in smoothed]
decoy_signal = [math.sin(x * 0.5) for x in temp_normalized]

# Core processing path begins here
adjusted_readings = [x + offset_compensation for x in raw_readings]
processed_data = {i: adjusted_readings[i]**2 for i in range(len(adjusted_readings))}

# Generate auxiliary maps with red herring entries
status_flags = {k: 'OK' if v > 6 else 'LOW' for k, v in processed_data.items()}
error_log = {}
for idx in range(len(processed_data)):
    if processed_data[idx] < 10:
        error_log[idx] = 'CALIBRATION_NEEDED'
    elif idx % 3 == 0:
        error_log[idx] = 'CHECK_ALIGNMENT'  # Distractor: unused later

# Threshold configuration (only specific keys matter)
threshold_map = {
    'critical': 50,
    'warning': 30,
    'info': 10,
    'debug': 1  # Red herring
}

# Decoy analysis function (never called)
def evaluate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5

# Actual analysis logic
state_registry = []
for key in sorted(processed_data.keys()):
    val = processed_data[key]
    if val > threshold_map['critical']:
        state_registry.append(3)
    elif val > threshold_map['warning']:
        state_registry.append(2)
    elif val > threshold_map['info']:
        state_registry.append(1)
    else:
        state_registry.append(0)

# Secondary transformation with misleading intermediate
encoded_state = 0
for bit in state_registry:
    encoded_state = (encoded_state << 2) | bit

# Linear search through dictionary keys (relevant only for index positioning)
search_order = list(threshold_map.keys())
index_pos = 0
for k in search_order:
    if k == 'warning':
        break
    index_pos += 1

# Case conversion on decoy string (pure distraction)
current_mode = "ReAl-TiMe MoNiToRiNg"
mode_label = ''.join([
    c.lower() if i % 2 == 0 else c.upper() 
    for i, c in enumerate(current_mode.replace('-', '').replace(' ', ''))
])

# Final diagnostic computation
running_total = 0
for i, val in processed_data.items():
    if i % 2 == 1:  # Only odd indices contribute
        running_total += int(math.sqrt(val))

# Key assignment statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Implementation of required function (was forward-referenced)
def analyze_readings(data_dict, thresholds):
    base_score = 0
    for k, v in data_dict.items():
        if v > thresholds['warning']:
            base_score += k * 2
        elif v > thresholds['info']:
            base_score += k
    # Additional logic involving dictionary operations
    flag_summary = {v for v in status_flags.values()}  # set from global
    modifier = len(flag_summary) * 3
    return base_score - modifier + encoded_state // 100

print(f"Target result: {final_diagnostic}")