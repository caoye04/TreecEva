def sensor_calibration(sequence):
    calibrated = []
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            calibrated.append(val * 1.1)
        elif i % 4 == 0:
            calibrated.append(val + 2.5)
        else:
            calibrated.append(val)
    return [round(x, 2) for x in calibrated]


def extract_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append((i, data[i]))
    return peaks


def generate_checksum(labels):
    checksum = 0
    for idx, label in enumerate(labels):
        checksum += (idx + 1) * len(label)
    return checksum

# Irrelevant helper function (dead code path)
def deprecated_filter(arr):
    return [x for x in arr if x > 0]

# Unused complex transformation
def transform_coordinates(coords):
    result = []
    for x, y in coords:
        transformed_x = x * 0.5 + 3.2
        transformed_y = y ** 0.5 - 1.1
        result.append((transformed_x, transformed_y))
    return result

# Misleading intermediate variables
temp_log = [1.2, 3.4, 2.1, 5.6, 4.3, 7.8, 6.5]
dummy_labels = ['A', 'B', 'C', 'D', 'E']
active_channels = [True, False, True, True, False]

# Real processing begins
raw_readings = [15, 22, 18, 25, 14, 21, 19, 24, 17, 23]
offset_map = {i: i*0.3 for i in range(len(raw_readings))}

processed_data = []
for idx, reading in enumerate(raw_readings):
    adjusted = reading - (idx % 4) + (idx // 2)
    processed_data.append(adjusted)

# Simulate side-channel diagnostics (irrelevant)
side_diagnostics = []
for i, p in enumerate(processed_data):
    if p % 2 == 0:
        side_diagnostics.append(p * 1.5)
    else:
        side_diagnostics.append(p * 0.8)

# Decoy aggregation
aggregated_noise = sum([x for x in side_diagnostics if x > 20])
dropped_packets = len(processed_data) // 4

# Threshold logic with tuple unpacking
def build_thresholds(base_values, factor=0.75):
    indices = list(range(len(base_values)))
    factors = [factor ** ((i+1) % 3) for i in indices]
    return {i: base_values[i] * f for i, f in zip(indices, factors)}

threshold_map = build_thresholds(processed_data, 0.68)

# Core analysis function
def analyze_readings(readings, thresholds):
    count_above = 0
    cumulative_shift = 0.0
    history = []

    for pos, val in enumerate(readings):
        thresh = thresholds.get(pos, 0)
        if val > thresh * 1.1:
            count_above += 1
            cumulative_shift += (val - thresh)
        history.append(val * 0.95)

    # Secondary pass using enumerate and zip
    corrections = sensor_calibration(history)
    total_drift = 0.0
    for c, orig in zip(corrections, readings):
        total_drift += abs(c - orig)

    # Final diagnostic calculation
    peak_info = extract_peaks(readings)
    severity_score = len(peak_info) * 100
    stability_factor = (count_above * 50) + round(cumulative_shift)
    final_score = severity_score - stability_factor + int(total_drift)

    # This is the actual answer variable
    final_diagnostic = abs(final_score) + dropped_packets

    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")