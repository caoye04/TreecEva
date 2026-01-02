import math

def analyze_phase_shift(frequency, amplitude, phase):
    if frequency <= 0:
        return 0.0
    shift = amplitude * math.sin(phase)
    adjusted = shift * math.log(frequency + 1)
    return round(adjusted, 4)

def compute_checksum(data_sequence):
    checksum = 0
    for val in data_sequence:
        checksum ^= int(val * 100) % 256
    return checksum

def evaluate_signal_integrity(raw_samples):
    if len(raw_samples) == 0:
        return 0
    peak = max(raw_samples)
    trough = min(raw_samples)
    window_size = len(raw_samples) // 4 or 1
    smoothed = [sum(raw_samples[i:i+window_size]) / window_size 
                for i in range(0, len(raw_samples), window_size)]
    avg = sum(smoothed) / len(smoothed)
    return abs(peak - trough) > 1.5 * avg

def extract_timing_segments(timestamps):
    intervals = []
    for i in range(1, len(timestamps)):
        intervals.append(round(timestamps[i] - timestamps[i-1], 3))
    return intervals

def decode_payload(header, payload):
    magic_key = header[:3]
    if magic_key != 'XYZ':
        return None
    try:
        decoded = []
        for ch in payload:
            decoded.append(ord(ch) & 0x7F)
        return decoded
    except:
        return []

def filter_anomalies(measurements, threshold=0.95):
    mean_val = sum(measurements) / len(measurements)
    deviances = [abs(x - mean_val) for x in measurements]
    limit = threshold * mean_val
    return [x for x in measurements if abs(x - mean_val) < limit]

def compress_vector(vec):
    result = []
    for i in range(0, len(vec), 2):
        pair_sum = sum(vec[i:i+2])
        result.append(pair_sum)
    return result

def validate_handshake(signal_code, retries=3):
    attempts = 0
    while attempts < retries:
        if signal_code & (1 << 3):
            return True
        signal_code = signal_code ^ (attempts * 2)
        attempts += 1
    return False

def generate_system_profile():
    profile = {
        'version': '2.1.9',
        'build': 'alpha',
        'features': ['A', 'B', 'C'],
        'flags': 0b110101,
        'active': True
    }
    return profile

def update_registry(entry, registry):
    key = entry.get('id')
    if key:
        registry[key] = entry
    return registry

def aggregate_metrics(log, flags):
    base_score = 0
    for record in log:
        if 'delta' in record:
            base_score += record['delta'] * 100
    flag_modifier = bin(flags).count('1')
    adjusted_score = base_score * (1 + flag_modifier / 10)
    if flags & 0b1000:
        adjusted_score -= 50
    return int(round(adjusted_score))

# Simulated telemetry data stream
timestamps = [1.0, 1.305, 1.608, 2.115, 2.92, 3.525, 4.03, 4.635, 5.14, 5.845]
data_stream = [0.21, 0.43, 0.62, 0.87, 0.93, 0.76, 0.54, 0.33, 0.12]

# Irrelevant signal analysis (red herring)
signal_phases = [math.pi/6, math.pi/3, math.pi/2]
amplitude_seq = [1.1, 1.4, 0.9]
freq_seq = [2.0, 4.5, 3.2]
phase_analysis = [analyze_phase_shift(f, a, p) for f, a, p in zip(freq_seq, amplitude_seq, signal_phases)]

# Decoy payload processing
dummy_header = 'XYZ'
dummy_payload = 'abc\x80def'
decoded_units = decode_payload(dummy_header, dummy_payload)

# Real timing extraction
timing_intervals = extract_timing_segments(timestamps)
filtered_intervals = filter_anomalies(timing_intervals)
smoothed_data = [round(x, 3) for x in data_stream if x > 0.2]

# Compute derived metrics
data_checksum = compute_checksum(smoothed_data)
integrity_status = evaluate_signal_integrity(smoothed_data)
compressed_smoothed = compress_vector([int(x*100) for x in smoothed_data])

# System state emulation
system_profile = generate_system_profile()
system_flags = system_profile['flags']
handshake_valid = validate_handshake(system_flags, retries=5)

# Build timing log with multiple fields (only 'delta' matters)
timing_log = []
for i, interval in enumerate(filtered_intervals):
    entry = {
        'id': f'T{i}',
        'timestamp': timestamps[i+1],
        'interval': interval,
        'delta': round(interval * 1.5, 3),
        'quality': 'high' if interval < 0.8 else 'medium'
    }
    timing_log.append(entry)

# Registry accumulation (unused distractor)
registry_db = {}
for item in timing_log:
    update_registry(item, registry_db)

# Final diagnostic computation (TARGET STATEMENT)
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result
print(f"Result: {final_diagnostic}")