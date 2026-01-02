from collections import defaultdict, Counter

# Simulated sensor data processing system for environmental monitoring
def fetch_raw_readings():
    return [127, 255, 83, 196, 72, 143, 201, 64, 95, 132, 177, 54, 111, 209, 37]

def apply_calibration(raw_values):
    calibrated = []
    base_shift = 17
    for val in raw_values:
        shifted = (val + base_shift) % 256
        adjusted = shifted ^ 42  # Arbitrary noise correction
        calibrated.append(adjusted)
    return calibrated

def compute_checksum(data):
    # Irrelevant function: checksum not used in final logic
    chk = 0
    for d in data:
        chk = (chk + d * 3) % 251
    return chk

def analyze_distribution(values):
    # Distractor analysis with no impact on result
    count_bin = defaultdict(int)
    for v in values:
        bucket = v // 32
        count_bin[bucket] += 1
    freq = Counter(count_bin)
    mode_bucket = freq.most_common(1)[0][0]
    return mode_bucket * 32  # Misleading intermediate value

def generate_threshold_map(raw_readings):
    # Real but indirectly used threshold logic
    high = sum(1 for x in raw_readings if x > 127)
    low = len(raw_readings) - high
    ratio = high / low if low else 0
    
    # Dead code path: never executed due to condition
    debug_flags = [False, True, False]
    if debug_flags[2] and ratio > 0.5:
        print('Debug recalibration triggered')  # Unreachable
        ratio *= 0.8
    
    default_thresh = 100 + int(ratio * 20)
    mapping = defaultdict(int)
    for i in range(5):
        mapping[f'zone_{i}'] = default_thresh + i * 5
    return mapping

def filter_anomalies(calibrated_data):
    # Real filtering operation
    cleaned = []
    for val in calibrated_data:
        if 50 <= val <= 200:
            cleaned.append(val)
    # Extra slicing distraction
    trimmed = cleaned[1:-1]  # Remove first and last
    restored = [cleaned[0]] + trimmed + [cleaned[-1]]  # Redundant reconstruction
    return restored

def derive_pattern_signature(data):
    # Complex but irrelevant pattern extraction
    sig = 0
    for i, d in enumerate(data):
        sig += (d ^ i) % 19
    return sig * 11

def extract_primary_signals(full_set):
    # Real signal extraction via slicing
    step_a = full_set[::2]   # Every other reading
    step_b = step_a[1:]      # Skip first
    return step_b

def calculate_entropy(readings):
    # Distractor: entropy calculation not used
    total = sum(readings)
    if total == 0:
        return 0.0
    probs = [r / total for r in readings]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def process_readings(signals, thresholds):
    # Core processing logic
    accumulation = 0
    zone_keys = sorted(thresholds.keys())
    for i, val in enumerate(signals):
        z = zone_keys[i % len(zone_keys)]
        if val > thresholds[z]:
            accumulation += val >> 2
        elif val == thresholds[z]:
            accumulation += val % 17
        else:
            accumulation -= val & 15
    # Final transformation
    accumulation ^= 987
    accumulation += len(signals) * 3
    return accumulation

# Main execution flow
raw_sensor_data = fetch_raw_readings()

calibrated_readings = apply_calibration(raw_sensor_data)

# Irrelevant checksum (distraction)
dummy_checksum = compute_checksum(calibrated_readings)

# Apply real but obfuscated filtering
filtered_data = filter_anomalies(calibrated_readings)

# Extract primary signals using slicing — critical step
primary_signals = extract_primary_signals(filtered_data)

# Generate threshold map based on original distribution — actually used
threshold_map = generate_threshold_map(raw_sensor_data)

# Additional distractor computations
mode_estimate = analyze_distribution(calibrated_readings)
signature_code = derive_pattern_signature(primary_signals)
entropy_value = calculate_entropy(primary_signals)  # Computed but unused

# Critical assignment: this determines the answer
final_diagnostic = process_readings(primary_signals, threshold_map)

print(f"Result: {final_diagnostic}")