def transform_signal(raw_values, scale_factor):
    adjusted = [x * scale_factor for x in raw_values]
    offset = sum(adjusted) // len(adjusted)
    return [x + offset for x in adjusted]


def filter_outliers(data_stream, limit):
    cleaned = []
    for val in data_stream:
        if abs(val) < limit:
            cleaned.append(val)
    return cleaned


def generate_checksum(sequence):
    checksum = 0
    for i, num in enumerate(sequence):
        checksum ^= (num + i) & 0xFF
    return checksum


def decode_pattern(signal):
    if not signal:
        return 0
    peak = max(signal)
    trough = min(signal)
    return (peak - trough) // 2 if peak > 0 else 0


def analyze_readings(readings, config_map):
    base = config_map['base_offset']
    factor = config_map['gain']
    mode_flag = config_map['mode'] == 'aggressive'
    
    temp_series = [int(x * factor) for x in readings]
    
    # Conditional expression used here
    adjustment = sum(temp_series) // len(temp_series) if mode_flag else base
    
    refined = [x + adjustment for x in temp_series]
    
    spike_count = 0
    for val in refined:
        if val > 100:
            spike_count += 1
    
    # Dead code path - never executed due to fixed config
    secondary_filter = []
    for x in refined:
        if x % 7 == 0:  # Rare condition, but included as distractor
            secondary_filter.append(x)
    
    # Irrelevant statistical distraction
    mean_val = sum(refined) / len(refined)
    variance = sum((x - mean_val) ** 2 for x in refined) / len(refined)
    entropy_proxy = abs(mean_val) / (variance + 1)
    
    # Key logic branch affecting output
    if spike_count > 3:
        result = len(refined) * 17
    elif spike_count == 0:
        result = -len(refined) * 5
    else:
        result = int(abs(mean_val) // (entropy_proxy + 0.1))

    # Unused but plausible-looking transformation
    decoy_shift = tuple((result >> i) & 1 for i in range(8))
    parity_check = sum(decoy_shift) % 2
    
    return result + parity_check  # Minor tweak, but deterministic

# Simulated sensor input
raw_sensor_data = [1.2, 3.4, 2.1, 5.6, 0.9, 4.3, 6.7, 3.3, 2.5, 5.1]

# Irrelevant preprocessing chain
scaled_signal = transform_signal(raw_sensor_data, 10)
cleaned_signal = filter_outliers(scaled_signal, 100)

# Distraction: unused checksum
unused_checksum = generate_checksum(cleaned_signal)

# Another red herring: pattern decoding with no impact
pulse_width = decode_pattern(cleaned_signal)

# Actual processing begins here
interim_readings = [x * 1.5 for x in raw_sensor_data]  # Re-process original
processed_data = filter_outliers([int(x) for x in interim_readings], 50)

# Configuration map with misleading entries
threshold_map = {
    'base_offset': 10,
    'gain': 3.0,
    'mode': 'normal',  # switches conditional logic
    'window_size': 5,      # unused
    'tolerance': 0.05,   # unused
    'debug': True        # unused
}

# Distractor variables
auxiliary_stats = {
    'count': len(processed_data),
    'max_raw': max(raw_sensor_data),
    'checksum': generate_checksum(processed_data)  # used to look important
}

# Hidden character counting distraction (never used)
log_entry = "Sensor readings nominal."
char_count = sum(1 for c in log_entry if c.isalpha())

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output target
print(f"Result: {final_diagnostic}")