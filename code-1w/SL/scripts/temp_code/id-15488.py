def analyze_readings(data, threshold):
    count_above = 0
    temp_sum = 0
    adjusted_values = []
    
    for val in data:
        if val > threshold * 1.2:
            count_above += 1
        if val > threshold:
            temp_sum += val
            adjusted_values.append(val * 0.95)
        else:
            adjusted_values.append(val * 1.05)

    avg_adjusted = sum(adjusted_values) / len(adjusted_values)
    return temp_sum, count_above, avg_adjusted

baseline = 42
readings = [38, 45, 50, 40, 60, 35, 55]

# Misleading intermediate calculations
offset = 7
shadow_factor = (baseline - offset) * 0.1
fudge_factor = 0.0
for i in range(len(readings)):
    if readings[i] % 5 == 0:
        fudge_factor += 0.01

# Unused transformation via lambda
transform = lambda x: x ** 0.5 * 3.14
unused_transforms = [transform(x) for x in readings if x < 50]

# Core logic disguised among red herrings
raw_total, high_count, mean_corrected = analyze_readings(readings, baseline)

# Simulate calibration drift (irrelevant to final result)
calibration_log = []
for step in range(3):
    calibration_log.append((step, baseline * (0.9 + step * 0.05)))

# Key computation with distractor variables
consistency_score = 100 - abs(len(readings) * 2 - high_count * 5)
weighting = 0.8 if high_count > 3 else 0.6

# Critical assignment point
final_score = int(raw_total * weighting + consistency_score - shadow_factor)

# Additional irrelevant state tracking
diagnostic_snapshot = {
    'version': '2.1',
    'valid': True,
    'checksum': sum([len(str(x)) for x in readings])
}

# Output must follow required format
print(f"Result: {final_score}")