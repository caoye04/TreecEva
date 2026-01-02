import math

def analyze_sensor_array(raw_readings, threshold, mode='diagnostic'):
    # Irrelevant pre-processing (distractor)
    normalized = [x * 1.05 for x in raw_readings if x > -100]
    outliers = [x for x in normalized if x > threshold * 1.5]
    adjusted = [x * 0.9 for x in normalized]

    # Real filtering logic (key path)
    filtered_data = []
    cumulative_shift = 0
    for i, val in enumerate(raw_readings):
        if i % 2 == 0 and val > threshold:
            shifted = val - (i * 0.1)
            filtered_data.append(shifted)
        else:
            filtered_data.append(val + 0.01)

    # Dead code path (misleading)
    if mode == 'calibration_only':
        return sum(adjusted) % 7

    # Unused complex transformation (red herring)
    def decoy_transform(seq):
        return [math.sin(x) + math.cos(x * 2) for x in seq]

    return filtered_data

def compute_baseline(readings):
    # Bit manipulation distractor
    magic_seed = 13
    for r in readings:
        magic_seed ^= int(r) & 7
    base = sum(readings) / len(readings)
    return base * (magic_seed | 3)

def apply_correction(data, factor):
    # Modular arithmetic with irrelevant branching
    corrected = []
    for d in data:
        temp = d * factor
        if temp < 0:
            temp = abs(temp) % 17
        elif temp > 100:
            temp = temp % 97
        corrected.append(round(temp, 3))
    # Early return red herring
    if len(corrected) > 1000:
        return corrected[:10]
    return corrected

def process_readings(data, factor):
    # Core computation mixed with noise
    intermediate = []
    checksum = 0
    
    # Use of enumerate and zip (required feature)
    indices = list(range(len(data)))
    for idx, (i, val) in enumerate(zip(indices, data)):
        if idx == 0:
            result = val * factor
        elif idx % 3 == 0:
            result = val + factor
        else:
            result = val ** 1.1 - factor

        # Bitwise distraction
        checksum ^= int(result) & 15

        intermediate.append(result)

    # Conditional branch with early break (irrelevant)
    for x in intermediate:
        if x > 1000:
            break

    # Final processing (only this matters)
    valid_results = [x for x in intermediate if x > 10]
    final_diagnostic = int(sum(valid_results) / len(valid_results)) if valid_results else 0
    
    # Misleading side calculation (decoy)
    alt_score = 0
    for v in intermediate:
        alt_score += int(v) | 5
    
    return final_diagnostic

# Main execution flow
raw_sensor_data = [12.5, 18.3, 9.1, 23.7, 14.2, 8.8, 19.5, 11.6]
calibration_factor = 2.1

# Initial irrelevant steps
baseline_ref = compute_baseline(raw_sensor_data)
dummy_list = [x**2 for x in raw_sensor_data if x < 15]
status_flags = [1 if x > 10 else 0 for x in dummy_list]

# Key data filtering (relevant)
filtered_data = analyze_sensor_array(raw_sensor_data, threshold=10.0, mode='diagnostic')

# Apply meaningless correction (distractor)
corrected_data = apply_correction(filtered_data, 1.05)

# Critical statement: this determines the answer
final_diagnostic = process_readings(filtered_data, calibration_factor)

print(f"Result: {final_diagnostic}")