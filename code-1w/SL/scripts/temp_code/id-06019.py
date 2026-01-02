import math

# Simulated sensor fusion system for environmental monitoring

def preprocess_readings(raw_samples):
    cleaned = []
    outlier_count = 0
    avg = sum(raw_samples) / len(raw_samples)
    variance_accum = 0

    for val in raw_samples:
        if abs(val - avg) > 2 * math.sqrt(sum((x - avg) ** 2 for x in raw_samples) / len(raw_samples)):
            outlier_count += 1
        else:
            variance_accum += (val - avg) ** 2
            cleaned.append(val)

    # Irrelevant transformation (distractor)
    normalized = [math.log(abs(x) + 1) for x in raw_samples]
    weighted_sum = sum(x * 0.9 for x in normalized)

    return cleaned

# Decoy function – looks important but unused in critical path
def legacy_calibrate(data):
    return [x * 0.98 + 5 for x in data]

# Bit manipulation red herring
def encode_flags(mode, active, priority):
    flag = 0
    flag |= (1 << 7) if mode else 0
    flag |= (priority & 0b111) << 3
    flag |= (active & 0b111)
    inverted = ~flag & 0xFF
    # Some meaningless bit juggling
    rotated = ((flag << 3) | (flag >> 5)) & 0xFF
    return rotated  # never used

# Unused statistical decoy
def rolling_average(series, window=3):
    if len(series) < window:
        return []
    return [sum(series[i:i+window]) / window for i in range(len(series)-window+1)]

# Real processing begins here
raw_sensor_data = [102, 98, 105, 45, 110, 103, 500, 101, 99, 104, 2000, 100]

# Filtering outliers
filtered_data = preprocess_readings(raw_sensor_data)

# Threshold configuration map (used later)
threshold_map = {
    'warning_low': 90,
    'warning_high': 110,
    'critical_range': lambda x: abs(x - 100) > 15,
    'scale_factor': 1.0
}

# Dead code branch - misleading control flow
if len(filtered_data) > 20:
    scaled_data = [x * 1.1 for x in filtered_data]
elif len(filtered_data) == 5:
    scaled_data = [x * 0.95 for x in filtered_data]
else:
    # This branch runs, but result not used
    temp_scaled = [x * 1.0 for x in filtered_data]  # distractor

# Dictionary-based routing table (some entries are decoys)
routing_table = {
    'A': lambda x: x + 10,
    'B': lambda x: x * 2,
    'DIAG': lambda x: x  # identity for diagnostic pass-through
}

# Critical analysis function
analyze_readings = lambda data, config: (
    sum(
        1 for x in data 
        if config['warning_low'] <= x <= config['warning_high']
    ) * 1000 + 
    sum(
        1 for x in data 
        if config['critical_range'](x)
    ) * 100 + 
    (len(data) > 5 and 50 or 25) + 
    (routing_table.get('DIAG', lambda x: 0)(42) // 7)  # evaluates to 6
)

# Unused advanced processing (distraction)
transformed = list(map(lambda x: x ** 2 - x * 3 + 2, filtered_data))
sliced_tail = transformed[-5:]  # looks important
sliced_head = transformed[:3]   # also unused

# Key execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Additional irrelevant operations to increase interference
checksum = 0
for i, v in enumerate(filtered_data):
    checksum ^= int(v) ^ i

# Final output
Result: {final_diagnostic}