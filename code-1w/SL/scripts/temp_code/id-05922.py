from collections import defaultdict

# Simulate sensor data processing pipeline with noise filtering and thresholding
def process_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if x > 25 and x < 95]
    
    # Track frequency of readings (distractor: not used in final logic)
    freq_map = defaultdict(int)
    for val in raw_readings:
        freq_map[val] += 1
    
    temp_sum = sum(filtered_data)
    temp_count = len(filtered_data)
    
    # Apply exponential smoothing factor (semi-relevant, but overridden later)
    if temp_count > 0:
        smoothed_avg = temp_sum / temp_count * 1.08
    else:
        smoothed_avg = 0
    
    return temp_sum, temp_count

# Diagnostic mode flag (distractor variable)
diagnostic_mode = True
log_buffer = []

# Raw sensor inputs from environmental monitoring station
readings = [30, 45, 20, 60, 85, 100, 70, 25, 90, 55, 40, 95, 50]

# Preprocess: remove exact multiples of 10 (simulates calibration filter)
calibrated = [x for x in readings if x % 10 != 0]

# Secondary validation: only keep values where bit count is odd (XOR trick)
valid_bits = []
for v in calibrated:
    bit_count = bin(v).count('1')
    if bit_count % 2 == 1:
        valid_bits.append(v)

# Compute base metric
base_metric = sum(valid_bits) // (len(valid_bits) or 1)

# Determine quality tier using conditional expression (distractor)
tier = 'A' if base_metric >= 60 else 'B' if base_metric >= 45 else 'C'

# Additional unused diagnostic calculation (dead code path)
if diagnostic_mode:
    max_jump = 0
    for i in range(1, len(readings)):
        diff = abs(readings[i] - readings[i-1])
        if diff > max_jump:
            max_jump = diff
    log_buffer.append(f'Max jump: {max_jump}')

# Core evaluation function combining arithmetic and logical constraints
def evaluate_performance(data, threshold=42):
    total = 0
    count = 0
    penalty = 0
    
    for x in data:
        if x < threshold:
            total += x ** 0.5  # square root contribution
            count += 1
        else:
            total += x // 3
            if x % 2 == 0:
                penalty += 1  # even numbers above threshold cost 1 point
    
    # Final adjustment: reduce by half the penalty
    adjusted_total = total - (penalty * 0.5)
    
    # Tertiary adjustment based on bitwise condition (used)
    if len(data) & 1:  # if odd length
        adjusted_total *= 1.1
    
    return int(adjusted_total)

# Execute main logic
final_score = evaluate_performance(valid_bits)

print(f"Result: {final_score}")