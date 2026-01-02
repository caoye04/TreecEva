def analyze_pattern(sequence):
    """Irrelevant helper for signal pattern analysis (dead function)"""
    return [x ** 0.5 for x in sequence if x > 10]

# Distractor: Unused calibration data
calibration_map = {i: (i * 1.07 + 3) for i in range(15)}
offset_lookup = [j * 2 + 1 for j in range(20)]

# Sensor simulation parameters (some are misleading)
def generate_noise(level=0.5):
    return [abs((i * level) % 7 - 3) for i in range(8)]

noise_floor = sum(generate_noise(0.8))  # Red herring computation

# Real data processing chain
sensor_data = [18, 22, 14, 30, 16, 25, 19, 21]
thresh_hold_legacy = [20, 20, 20, 20]  # Obsolete threshold (distractor)
thresholds = {'low': 15, 'high': 24}

status_flags = []
accumulated_score = 0  # Misleading metric, unused later

for idx, reading in enumerate(sensor_data):
    if reading < thresholds['low']:
        status_flags.append('L')
        accumulated_score += 3
    elif reading > thresholds['high']:
        status_flags.append('H')
        accumulated_score -= 1
    else:
        status_flags.append('N')
        accumulated_score += 1

# Secondary transformation with zip and enumerate (relevant)
adjusted_values = []
for i, (char, val) in enumerate(zip(status_flags, sensor_data)):
    adjustment = 5 if char == 'H' else (-2 if char == 'L' else 0)
    adjusted_values.append(val + adjustment + (i % 3))

# Conditional expression block (relevant)
mode_override = 'aggressive' if sum(1 for c in status_flags if c == 'H') >= 3 else 'conservative'

def apply_correction(values, mode):
    corrected = []
    factor = 0.9 if mode == 'aggressive' else 1.1
    for v in values:
        corrected.append(v * factor)
    return [round(c) for c in corrected]

# Apply correction based on mode (critical path)
corrected_readings = apply_correction(adjusted_values, mode_override)

# Data alignment using enumerate and zip (key step)
aligned_pairs = list(zip(enumerate(corrected_readings), sensor_data))

primary_sum = 0
for (index, corrected), original in aligned_pairs:
    if index % 2 == 0:
        primary_sum += corrected // 2
    else:
        primary_sum += original // 3

# Final diagnostic logic (target assignment)
baseline = sum(sensor_data) / len(sensor_data)
deviation = sum(abs(cr - baseline) for cr in corrected_readings)

# Complex conditional expression combining multiple concepts
final_diagnostic = deviation if deviation > 30 \
    else (deviation * 2) if any(cr > 30 for cr in corrected_readings) \
    else (primary_sum + int(mode_override[0] == 'a'))

# Decoy output statements (distractors)
interim_result = noise_floor * 2  # Dead end
auxiliary_flag = len(calibration_map) > len(offset_lookup)  # Unused boolean

# Critical output: must print final_diagnostic
print(f"Result: {final_diagnostic}")