def sensor_calibration(sequence):
    calibrated = []
    offset = 7
    gain = 1.2
    for val in sequence:
        adjusted = (val + offset) * gain
        if adjusted > 100:
            adjusted = 95  # safety cap
        calibrated.append(adjusted)
    return calibrated

# Irrelevant auxiliary function - decoy
def compute_entropy(data):
    import math
    freq_map = {}
    total = len(data)
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused transformation - red herring
def transform_legacy_format(raw):
    return [x * 0.95 + 3.1 for x in raw if x % 2 == 0]

# Core processing pipeline
def filter_outliers(stream, limit):
    clean = []
    for x in stream:
        if abs(x - 50) <= limit:  # centered around baseline
            clean.append(x)
    return clean

# Data fusion from multiple sources - misleading complexity
def merge_streams(primary, secondary):
    merged = []
    for i in range(min(len(primary), len(secondary))):
        fused = (primary[i] + secondary[i]) / 2
        merged.append(fused)
    return merged + primary[len(secondary):]

# Actual analysis logic (obscured by noise)
def analyze_readings(readings, cutoff):
    count_above = 0
    running_total = 0
    peak = float('-inf')
    for reading in readings:
        running_total += reading
        if reading > cutoff:
            count_above += 1
        if reading > peak:
            peak = reading
    avg = running_total / len(readings) if readings else 0
    # Critical formula: weighted diagnostic score
    return int((avg * 1.8) + (count_above * 12) - (peak // 10))

# Simulated raw input data
raw_sensor_data = [45, 52, 38, 67, 41, 56, 33, 72, 48, 54]
legacy_buffer = [88, 23, 55, 61, 47]  # unused but referenced in decoy

# Processing steps with distractions
offset_compensated = sensor_calibration(raw_sensor_data)
decoy_entropy = compute_entropy([1, 1, 2, 2, 3])  # irrelevant computation

# Real signal path
filtered_stream = filter_outliers(offset_compensated, 25)

# Fake fusion attempt - distractor
fake_fusion = merge_streams(offset_compensated, legacy_buffer)
fake_avg = sum(fake_fusion) / len(fake_fusion)  # misleading intermediate

# Final processing
processed_data = [x + 1.5 for x in filtered_stream]  # slight correction
threshold = 60.0

# Noise variables - dead code paths
buffer_snapshot = {"timestamp": 12345, "status": "idle", "data_len": len(raw_sensor_data)}
temp_audit_log = []
for item in raw_sensor_data:
    if item > 70:
        temp_audit_log.append("HIGH")

# Key execution point
diagnostic_weight = 1.0 if len(processed_data) > 5 else 0.8
baseline_score = sum(processed_data) * diagnostic_weight

final_diagnostic = analyze_readings(processed_data, threshold)
print(f"Result: {final_diagnostic}")