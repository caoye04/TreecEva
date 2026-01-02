from collections import defaultdict, Counter
import math

# Simulated sensor array data (real values)
sensor_data = [127, 255, 89, 144, 201, 73, 151]

def apply_noise_filter(data):
    # Irrelevant preprocessing: applies a filter not used in final computation
    return [x & 0x7F for x in data]

def generate_checksum(seq):
    # Distractor function: computes checksum not used in main logic
    chk = 0
    for val in seq:
        chk ^= val
    return chk

calibration_matrix = [
    [1.0, 0.1, -0.05],
    [0.05, 1.0, 0.02],
    [-0.03, 0.07, 1.0]
]

# Dead code path — never invoked
def legacy_calibrate(x):
    return int(x * 0.97)

# Misleading intermediate transformation
temp_normalized = []
for val in sensor_data:
    if val > 128:
        temp_normalized.append(val * 0.8)
    else:
        temp_normalized.append(val * 1.05)

# Unused statistical analysis
mean_val = sum(sensor_data) / len(sensor_data)
variance = sum((x - mean_val) ** 2 for x in sensor_data) / len(sensor_data)
std_dev = math.sqrt(variance)

# Red herring: frequency analysis of byte patterns
byte_freq = Counter()
for val in sensor_data:
    byte_freq[val & 0xF] += 1
    byte_freq[val >> 4] += 1  # High nibble also counted

# Real processing begins here — obscured by prior noise
transformation_key = [0.5, 0.3, 0.2]
def process_readings(readings, matrix):
    accumulated = 0
    # Use enumerate and zip (required python features)
    for i, val in enumerate(readings):
        row = matrix[i % 3]
        weighted = 0
        for j, factor in enumerate(row):
            weighted += factor * (val % (j + 2))  # Nonlinear modulation
        accumulated += int(weighted) * (i + 1)
    
    # Secondary transformation using dictionary operations
    index_map = defaultdict(int)
    for idx, num in enumerate(readings):
        index_map[f"sensor_{idx}"] = num * (idx % 4 + 1)
    
    bonus_shift = 0
    for k, v in index_map.items():
        if 'sensor_2' in k or 'sensor_5' in k:
            bonus_shift += v % 19
    
    # Final result influenced by both paths
    raw_result = accumulated + bonus_shift
    
    # Apply bit manipulation red herring (unused)
    decoy_final = raw_result ^ 0xFFFF
    decoy_final = (decoy_final << 3) & 0xFFFFFF
    
    # Actual final adjustment based on controlled logic
    control_flag = sum(1 for x in readings if x > 100)
    if control_flag >= 4:
        raw_result -= 67  # Critical adjustment
    
    return raw_result

# Additional distractor: linear search for irrelevant threshold
def find_first_over(data, limit=150):
    for i, x in enumerate(data):
        if x > limit:
            return i
    return -1

trigger_point = find_first_over(sensor_data, 200)

# Case conversion distraction (suggested paradigm)
status_labels = ['OK', 'ERROR', 'WARNING']
upper_status = [label.lower().swapcase() for label in status_labels]  # No effect

# Key execution point
final_diagnostic = process_readings(sensor_data, calibration_matrix)

# Print result as required
print(f"Result: {final_diagnostic}")