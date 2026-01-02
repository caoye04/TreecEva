import math

# Simulated sensor data processing pipeline with red herrings
def collect_telemetry():
    return [0.1, -0.5, 2.3, -1.7, 4.4, -3.2, 0.9, 1.1]

# Irrelevant transformation - decoy function
def transform_coordinates(x, y):
    lat = x * math.pi / 180
    lon = y * math.pi / 180
    radius = 6371
    return radius * math.acos(math.sin(lat) * math.sin(lon) + math.cos(lat) * math.cos(lon))

# Unused but plausible filter
def legacy_filter(data):
    return [x for x in data if abs(x) > 0.5]

# String-based status tracker - distractor with string method usage
def generate_status_code(code_type):
    base = f"STATUS_{code_type.upper()}"
    suffix = ''.join(reversed(base[:4]))
    return f"{base}_V2_{suffix.lower()}"

# Core signal filter (used)
def apply_noise_gate(signal, threshold=1.0):
    return [x for x in signal if abs(x) >= threshold]

# Bit manipulation red herring
def encode_flags(mode, active, level):
    flag = 0
    flag |= (mode & 0b111)
    flag <<= 3
    flag |= (active << 5)
    flag <<= 2
    flag |= (level & 0b11)
    return flag ^ 0b10101  # Decoy computation

# Data enrichment with unused result
def annotate_peaks(signal):
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peak_str = f"PEAK_{i:02d}"
            peaks.append(peak_str.upper().replace('K', 'X'))
    return peaks  # Never used

# Real processing step buried in noise
def integrate_signal(filtered):
    total = 0.0
    for val in filtered:
        if val < 0:
            total += math.sqrt(abs(val)) * -1
        else:
            total += math.sqrt(val)
    return total

# Complex conditional routing - only one branch is relevant
def route_processing(path_id, data):
    if path_id == "A1":
        return [x * 1.1 for x in data]
    elif path_id.startswith("B"):
        return [x * 0.9 for x in data]
    elif len(path_id) > 5 and 'x' in path_id:
        return [x * 2 for x in data]
    else:
        return data  # Default case is taken

# Main processor combining multiple concepts
def process_signal(config, samples):
    # Distractor variables
    calibration_matrix = [[1, 0], [0, 1]]
    checksum = sum(len(str(x)) for x in [123, 456, 789])  # Useless
    temp_log = generate_status_code('diagnostic')

    # Actual signal flow begins
    gated = apply_noise_gate(samples, config['threshold'])

    # Dead code path due to string comparison
    mode_flag = encode_flags(5, True, 3)
    if mode_flag == 99999:  # Never true
        gated = [x * 2 for x in gated]

    # Annotate but don't use
    peak_labels = annotate_peaks(samples)

    # Route based on config
    routed = route_processing(config['path'], gated)

    # Integration is key
    integrated = integrate_signal(routed)

    # Final adjustment
    scaling_factor = 1.5 if config.get('boost') else 1.0
    final_value = integrated * scaling_factor

    # Extra confusion
    metadata_tag = f"PROC_{math.floor(final_value)}"
    metadata_tag = metadata_tag.strip('P').replace('_', '')

    return final_value

# Configuration with misleading fields
filter_chain = {
    'threshold': 1.5,
    'path': 'DEFAULT',
    'boost': True,
    'debug_mode': generate_status_code('debug'),
    'version_key': transform_coordinates(45.0, 90.0),
    'flags': encode_flags(3, False, 1)
}

# Raw input data
raw_samples = collect_telemetry()

# Execute main logic
final_output = process_signal(filter_chain, raw_samples)

print(f"Result: {final_output}")