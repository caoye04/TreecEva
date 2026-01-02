import math

def analyze_sensor_array(raw_readings, threshold=0.75):
    # Irrelevant pre-processing: noise floor simulation (dead code path)
    noise_floor = [math.sin(i * 0.1) for i in range(len(raw_readings))]
    enhanced_noise = list(map(lambda x: round(x, 3), noise_floor))

    # Core data transformation
    normalized = [x / 100.0 for x in raw_readings]
    filtered = [x for x in normalized if x > threshold]

    # Distractor: unused signal smoothing
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-1):min(i+2, len(normalized))]
        smoothed.append(sum(window) / len(window))

    # Unused feature extraction via lambda
    peak_detector = lambda arr: max(arr) - min(arr) if len(arr) > 1 else 0
    dynamic_range = peak_detector(normalized)

    return filtered


def compute_calibration(readings):
    base_ref = sum([i * 0.01 for i in range(1, len(readings)+1)])
    adjustment = math.log(len(readings) + 1) if len(readings) > 0 else 0
    
    # Decoy calculation with bit manipulation (irrelevant)
    magic_key = 0
    for i in range(len(readings)):
        magic_key ^= (i << 2) | 1
    
    # Actual calibration logic
    factor = round(base_ref + adjustment, 4)
    return factor


def process_readings(data, factor):
    # Simulate diagnostic computation
    temp_results = []
    for idx, val in enumerate(data):
        adjusted_val = val * factor
        if idx % 2 == 0:
            adjusted_val += 0.1
        else:
            adjusted_val -= 0.05
        temp_results.append(adjusted_val)
    
    # Secondary transformation using zip and enumerate
    paired = list(zip(temp_results, [x**2 for x in temp_results]))
    derived = [a + b/100 for a, b in paired]

    # Final aggregation
    aggregate = sum(derived)

    # Red herring: complex bitwise checksum (unused)
    checksum = 0
    for d in derived:
        int_part = int(abs(d * 100))
        checksum = (checksum << 1) ^ int_part
        checksum = checksum & 0xFFFF

    # Final diagnostic score
    final_diagnostic = int(round(aggregate * 1000))
    return final_diagnostic

# Main execution sequence
raw_input_data = [85, 92, 78, 96, 88, 76, 91, 87, 93, 89]

# Dead code block: alternate processing path never taken
if False:
    alternate_route = [x + 10 for x in raw_input_data]
    processed_alt = analyze_sensor_array(alternate_route, 0.5)

# Real computation begins
filtered_data = analyze_sensor_array(raw_input_data, 0.85)
calibration_factor = compute_calibration(filtered_data)

# Key statement
final_diagnostic = process_readings(filtered_data, calibration_factor)

print(f"Result: {final_diagnostic}")