import math

# Sensor data processing simulation with red herrings and complex distractions
def collect_diagnostics():
    raw_readings = [127, 255, 192, 64, 31, 88, 143, 201]
    thresholds = {'low': 64, 'high': 192}
    calibration_map = {i: round(math.cos(i * 0.1), 4) for i in range(10)}
    temp_buffer = [x ^ 0xFF for x in raw_readings]  # irrelevant bit-flipped copy

    # Real processing begins: extract values in mid-range
    filtered_data = [x for x in raw_readings if thresholds['low'] < x < thresholds['high']]

    # Decoy transformation chain
    transformed = []
    for val in raw_readings:
        if val > 200:
            transformed.append(val // 3 + 7)
        elif val < 50:
            transformed.append(val * 2)
    # END of decoy - transformed is never used

    # Fake checksum that looks important
    checksum = 0
    for b in temp_buffer:
        checksum = (checksum << 1 | (checksum >> 7)) ^ b
    checksum %= 1000  # Looks critical but unused

    # Distractor: spurious statistical analysis
    mean_fake = sum(temp_buffer) / len(temp_buffer)
    variance_fake = sum((x - mean_fake) ** 2 for x in temp_buffer) / len(temp_buffer)
    entropy_approx = -sum(math.log(abs(x) + 1e-5) for x in temp_buffer[:4])  # partial, misleading

    # Dictionary-based mode detection (red herring)
    mode_flags = {}
    for i, val in enumerate(filtered_data):
        mode_flags[f'node_{i}'] = 'active' if val & 8 else 'standby'
    status_summary = ''.join(mode_flags.values()).count('active')

    # Actual signal processing path
    def enhance_signal(seq, factor):
        return [round(math.sqrt(x) * factor, 3) for x in seq]

    # Obfuscated calibration lookup
    keys = sorted(calibration_map.keys())
    calibration_factor = calibration_map[keys[len(keys)//2]]  # middle key: 5 -> cos(0.5)

    enhanced = enhance_signal(filtered_data, calibration_factor)

    # Multi-step aggregation
    aggregate = 0.0
    for val in enhanced:
        aggregate += val * 1.5
        if aggregate > 100:
            aggregate -= 50  # artificial limiter, not triggered here

    # Final diagnostic computation
    final_diagnostic = int(sum(filtered_data) + round(aggregate))

    # DEAD CODE PATH: emergency override simulation (never reached)
    override_codes = {(1, 0): 'A', (0, 1): 'B'}
    for a in range(2):
        for b in range(2):
            if a == b:
                code_key = (a, b)
                lookup = override_codes.get(code_key, 'X')

    # Unused tuple unpacking distraction
    metadata_tuple = ('sensor_v4', 'site_7', 142857, 'calibrated')
    _, _, serial_number, _ = metadata_tuple
    serial_check = serial_number % 997

    return final_diagnostic

# Execution entry point
def process_readings(data, factor):
    # This function appears to do work but just returns a derived scalar
    base_sum = sum(d ** 0.5 for d in data)
    adjustment = math.floor(factor * 100)
    return int(base_sum + adjustment)

# Main call
result_value = collect_diagnostics()
final_diagnostic = process_readings([96, 128], 0.8776)  # cos(0.5) ≈ 0.8776
print(f"Result: {final_diagnostic}")