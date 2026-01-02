import itertools

# Simulated sensor array data (temperature in millidegrees)
sensor_readings = [23450, 25670, 22890, 26780, 24100, 27340, 21980, 28450, 23450, 25670]

def apply_calibration(raw_values):
    # Real calibration logic
    scale_factor = 0.987
    return [int(x * scale_factor) for x in raw_values]

def detect_anomalies(data_stream):
    anomalies = []
    for i in range(1, len(data_stream)):
        if abs(data_stream[i] - data_stream[i-1]) > 1500:
            anomalies.append((i, data_stream[i]))
    return anomalies

def smooth_data(sequence):
    # Moving average with window size 3 (unused in final logic)
    smoothed = []
    for i in range(len(sequence)):
        start = max(0, i - 1)
        end = min(len(sequence), i + 2)
        window = sequence[start:end]
        smoothed.append(sum(window) // len(window))
    return smoothed

def calculate_entropy(data):
    # Irrelevant entropy calculation (distractor)
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Fake log approximation
    return round(entropy, 6)

def filter_outliers(values, limit=27000):
    # Only values below limit are considered valid
    return list(filter(lambda x: x < limit, values))

def compute_derived_index(seq):
    # Complex transformation chain (partially relevant)
    shifted = [(x >> 4) for x in seq]  # Right shift by 4 bits
    modded = [v % 89 for v in shifted]
    return sum(modded) // len(modded)

def generate_checksum(values):
    # Checksum using bitwise operations (unused)
    chk = 0
    for v in values:
        chk ^= v
        chk = (chk << 1) & 0xFFFF | (chk >> 15)
    return chk & 0xFFFF

def threshold_func(x):
    # Dynamic threshold based on bit patterns
    return (x & 1) == 1 and (x % 7) < 5

def process_readings(readings, predicate):
    # Core processing logic
    base_offset = 20000
    adjusted = [r - base_offset for r in readings]
    mapped = list(map(lambda x: x * 2 if predicate(x) else x // 2, adjusted))
    grouped = [list(g) for k, g in itertools.groupby(mapped, key=lambda y: y > 3000)]
    selected_group = grouped[0] if len(grouped) > 0 else []
    reduction = 0
    for val in selected_group:
        if val > 1000:
            reduction += val // 3
        else:
            reduction -= val
    return reduction

# --- Main execution with distractions ---
raw_data = sensor_readings.copy()

calibrated_data = apply_calibration(raw_data)

# Distractor: anomaly detection (not used later)
anomaly_list = detect_anomalies(calibrated_data)

# Distractor: smoothing and entropy (dead ends)
smoothed_data = smooth_data(calibrated_data)
entropy_value = calculate_entropy(smoothed_data)
checksum_value = generate_checksum(calibrated_data)  # Unused

# Relevant path begins here
filtered_data = filter_outliers(calibrated_data, limit=27000)

index_diagnostic = compute_derived_index(filtered_data)  # Partially used red herring

# Key statement
final_diagnostic = process_readings(filtered_data, threshold_func)

# Print required output
print(f"Result: {final_diagnostic}")