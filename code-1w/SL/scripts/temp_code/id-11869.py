import itertools

# Simulated sensor array readings (with noise and redundancy)
sensor_ids = [101, 102, 103, 104, 105]
raw_readings = [87, 105, 93, 110, 88]
statuses = ['active', 'active', 'standby', 'active', 'failed']

# Irrelevant auxiliary data (distractor)
timestamps = [1623456780 + i * 60 for i in range(5)]
duplicate_buffer = [[x] * 3 for x in raw_readings]

# Calibration profiles (only one will be used)
calibration_map = {101: 0.95, 102: 1.05, 103: 1.0, 104: 0.98, 105: 1.02}
calibration_backup = {k: v * 1.01 for k, v in calibration_map.items()}  # unused decoy

# Misleading intermediate computations (red herring)
avg_reading = sum(raw_readings) / len(raw_readings)
adjusted_avg = avg_reading * 1.03  # looks important but isn't used
variance_proxy = sum((x - avg_reading) ** 2 for x in raw_readings) / len(raw_readings)

# Data pairing and filtering using meaningful Python idioms
paired_data = list(zip(sensor_ids, raw_readings, statuses))
filtered_data = [item for item in paired_data if item[2] == 'active']

# Extract calibration factors for active sensors only
active_calibration = [calibration_map[sid] for sid, _, status in filtered_data if status == 'active']

def apply_noise_correction(values, method='ema'):
    # Fake correction function with dead code paths
    if method == 'ema':
        alpha = 0.3
        corrected = [values[0]]
        for i in range(1, len(values)):
            corrected.append(alpha * values[i] + (1 - alpha) * corrected[-1])
        return corrected
    elif method == 'sma':
        window = 2
        return [sum(values[max(0, i - window + 1):i + 1]) / (i + 1) for i in range(len(values))]  # unused path
    else:
        return values  # unreachable due to fixed call

# Spurious signal processing chain (distractor)
noise_profile = [abs(hash(str(v)) % 10) for v in raw_readings]
denoised_signal = apply_noise_correction(noise_profile, 'ema')
smoothed = [raw_readings[i] - denoised_signal[i] for i in range(len(raw_readings))]

# Core diagnostic logic hidden among distractions
def analyze_trend(data_list):
    """Compute weighted trend index using bitwise influence on significance"""
    total_impact = 0
    for idx, (sid, reading, _) in enumerate(data_list):
        # Bit manipulation based on sensor ID and position
        magic_seed = (sid ^ idx) & 0xFF  # Use lower byte
        weight = (magic_seed >> 2) % 5 + 1  # Weight between 1-5
        contribution = reading * weight * 0.1
        total_impact += contribution
    return total_impact

# Secondary transformation with red herring control flow
def transform_sequence(seq, key_fn=lambda x: x**0.5):
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(key_fn(val) * 1.1)
        else:
            transformed.append(val * 0.9)
    return transformed

# Decoy recursive function (never called)
def recursive_diagnostics(depth, acc=0):
    if depth <= 0:
        return acc
    return recursive_diagnostics(depth - 1, acc + (depth & 1) * depth)

# Real processing function buried in complexity
def process_readings(data, base_factor):
    # Multiple steps with plausible but irrelevant sub-calculations
    indices = [i for i in range(len(data))]
    indexed_pairs = list(zip(indices, data))
    
    # Use of enumerate and zip together (required idiom)
    processed_items = []
    for i, (_, (sid, reading, _)) in enumerate(indexed_pairs):
        calib = calibration_map[sid]
        adjusted = reading * calib * base_factor
        processed_items.append((i, adjusted, sid))
    
    # Complex but ultimately simple aggregation
    sorted_items = sorted(processed_items, key=lambda x: x[1], reverse=True)
    top_three = sorted_items[:3]
    
    # Final computation involving multiple concepts
    trend_value = analyze_trend(data)
    base_sum = sum(item[1] for item in top_three)
    
    # Bitwise combination of components (core logic)
    int_component = int(base_sum & 0xFFFF)  # Clamp to 16-bit
    frac_component = (trend_value * 0.01) & 0xFF  # Use float as int mask
    
    final_score = int_component - frac_component
    
    # One more distraction: unused transformation
    dummy_seq = transform_sequence([final_score], lambda x: x / 2)
    
    return final_score

# Hidden dependency: this factor is critical but looks arbitrary
calibration_factor = ((len(filtered_data) * 3) ^ 17) * 0.01

# Key execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output requirement
print(f"Target result: {final_diagnostic}")