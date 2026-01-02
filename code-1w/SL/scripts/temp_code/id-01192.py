def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.73
    scale_factor = 1.08
    for val in raw_values:
        corrected = (val + offset) * scale_factor
        if corrected > 100:
            corrected = 98.6  # clamp to safe upper limit
        calibrated.append(round(corrected, 2))
    return calibrated

raw_sensor_data = [85, 92, 96, 74, 101, 88]

# Irrelevant preprocessing: simulates noise filtering but unused later
calibrated_noise_floor = list(map(lambda x: x * 0.95 + 2.1, raw_sensor_data))
temp_buffer = [x - 1 for x in calibrated_noise_floor if x > 50]

# Distractor: complex set operations with no impact on final result
sensor_ids = {'S1', 'S2', 'S3', 'S4'}
active_sensors = {'S1', 'S3', 'S4'}
dormant_sensors = sensor_ids - active_sensors
redundant_check = dormant_sensors.intersection({'S2', 'S5'})

# Real data path begins here
processed_data = sensor_calibration(raw_sensor_data)

# Misleading transformation chain (partially used)
baseline_shift = sum([x * 0.1 for x in processed_data])
adjusted_readings = [x - baseline_shift for x in processed_data]
smoothed = [round(x * 0.85, 2) for x in adjusted_readings]  # not used directly

# Critical intermediate step
aggregated_diagnostics = {
    'mean_raw': sum(raw_sensor_data) / len(raw_sensor_data),
    'peak_calibrated': max(processed_data),
    'stability_index': processed_data[1] - processed_data[0],
    'complexity_flag': len(processed_data) > 5 and processed_data[-1] < 95
}

# Decoy function that looks important but is never called
def compute_integrity_score(data):
    prime_count = 0
    for d in data:
        if d > 1:
            for i in range(2, int(d)//2):
                if d % i == 0:
                    break
            else:
                prime_count += 1
    return prime_count * 1.5

# Unused recursive red herring
def binary_weight(n):
    if n <= 1:
        return n
    return n % 2 + binary_weight(n // 2)

weight_sum = sum(binary_weight(int(x)) for x in processed_data[:3])

# Real analysis function
def analyze_readings(readings):
    threshold = 90.0
    above_threshold = [r for r in readings if r >= threshold]
    below_threshold = [r for r in readings if r < threshold]
    
    # Simulate diagnostic logic with multiple steps
    score_a = len(above_threshold) * 10
    score_b = sum(below_threshold) / len(below_threshold) if below_threshold else 0
    score_c = 5 if len(above_threshold) >= 3 else -5
    
    # Hidden dependency on case conversion via dictionary key lookup
    mode_map = {k.upper(): v for k, v in {'fast': 1, 'normal': 2, 'deep': 3}.items()}
    analysis_mode = 'DEEP' if score_a > 25 else 'NORMAL'
    mode_bonus = mode_map.get(analysis_mode, 0)
    
    # Final computation
    raw_total = sum(readings)
    adjustment = raw_total * 0.05
    base_diagnostic = score_a + score_b + score_c + mode_bonus
    final_adjustment = abs(base_diagnostic) ** 0.5
    
    # The actual answer
    return int(base_diagnostic - final_adjustment)

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)

# Output result as required
print(f"Result: {final_diagnostic}")