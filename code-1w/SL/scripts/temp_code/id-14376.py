def sensor_calibrate(raw):    
    # Irrelevant calibration function (dead end)
    return [x * 0.98 for x in raw]


def preprocess(sequence):
    # Distractor: unused transformation
    offset = 5
    return [x + offset for x in sequence]


def decode_signal(signal_stream):
    # Complex but irrelevant decoding logic
    decoded = []
    for i, val in enumerate(signal_stream):
        if i % 2 == 0:
            decoded.append(val * 1.1)
        else:
            decoded.append(val * 0.9)
    return decoded


def filter_noise(data, threshold=10):
    # Real usage: filters out values below threshold
    result = []
    for x in data:
        if x > threshold:
            result.append(x)
    return result


def accumulate_trend(values):
    # Accumulates trend using enumerate for indexing
    trend = 0
    for idx, val in enumerate(values):
        trend += val * (idx + 1)  # Weight by position
    return trend


def pair_measurements(primary, secondary):
    # Uses zip to align two streams (red herring)
    paired = []
    for p, s in zip(primary, secondary):
        paired.append((p, s, abs(p - s)))
    return paired


def analyze_readings(clean_data):
    # Critical function: computes diagnostic metric
    base_score = 0
    for i, reading in enumerate(clean_data):
        if reading > 20:
            base_score += reading * (i % 3 + 1)
        else:
            base_score -= reading
    adjustment = len(clean_data) // 2
    return base_score - adjustment

# Main execution flow
raw_sensor_data = [12, 15, 23, 8, 31, 19, 27]

# Irrelevant preprocessing chain
calibrated = sensor_calibrate(raw_sensor_data)
decoded = decode_signal(calibrated)
offset_data = preprocess(calibrated)

# Real signal path begins here
filtered = filter_noise(calibrated)

# Distractor: unused pairing
aux_sensors = [10, 14, 25, 9, 30, 18, 26]
temp_pairs = pair_measurements(filtered, aux_sensors[:len(filtered)])

# Real processing step
processed_data = []
for val in filtered:
    processed_data.append(int(val) + 2)  # Minor correction

# Another red herring: unused accumulation
trend_value = accumulate_trend(processed_data)

# Key statement
final_diagnostic = analyze_readings(processed_data)

print(f"Result: {final_diagnostic}")