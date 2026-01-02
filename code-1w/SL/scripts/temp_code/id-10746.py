from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def load_sensor_metadata():
    return {
        'sensor_01': {'calibration': 0.98, 'active': True},
        'sensor_02': {'calibration': 1.02, 'active': False},
        'sensor_03': {'calibration': 0.99, 'active': True}
    }

def parse_timestamps(raw): 
    # Irrelevant parsing logic
    return [int(x.split('.')[0]) for x in raw if 'T' in x]

def validate_checksum(data):
    # Unused validation function (dead code path)
    return sum(data) % 256 == data[-1]

def decrypt_frame(frame):
    # Misleading decryption that isn't used in main flow
    return [b ^ 0xAA for b in frame]

def normalize_readings(readings, factor=1.0):
    # Real but partially irrelevant normalization
    return [round(r * factor, 3) for r in readings]

def filter_anomalies(stream):
    # Applies actual filtering used later
    threshold = 3.5
    return [x for x in stream if abs(x) < threshold]

def temperature_compensation(value, temp):
    # Distractor: not used in final computation
    return value * (1 + 0.002 * (temp - 25))

def shift_window(sequence, offset=1):
    # Bitwise manipulation red herring
    shifted = []
    for i in range(len(sequence)):
        val = int(abs(sequence[i] * 100))
        shifted.append((val << 1) ^ 0x55)
    return shifted

def extract_features(data_list):
    # Creates misleading feature set
    features = defaultdict(int)
    for d in data_list:
        features['count'] += 1
        if d > 0:
            features['positive'] += 1
        features['sum'] += d
    features['ratio'] = round(features['positive'] / features['count'], 2) if features['count'] else 0
    return dict(features)

def phase_align(samples, phase_shift=2):
    # Unused alignment logic
    return samples[phase_shift:] + samples[:phase_shift]

def compute_entropy(arr):
    # Decoy statistical analysis
    counts = Counter([round(x, 1) for x in arr])
    total = len(arr)
    return -sum((c/total) * math.log2(c/total) for c in counts.values())

def transform_coordinates(x, y):
    # Geospatial distraction
    lat = 37.0 + (x / 1000)
    lon = -122.0 + (y / 1000)
    return round(lat, 6), round(lon, 6)

def aggregate_temporal_blocks(data, size=3):
    # Real preprocessing step buried in noise
    blocks = []
    for i in range(0, len(data), size):
        block = data[i:i+size]
        if len(block) == size:
            blocks.append(sum(block))
    return blocks

def apply_noise_filter(signal):
    # Actually contributes to final result
    filtered = []
    for i, s in enumerate(signal):
        if i == 0:
            filtered.append(s)
        else:
            filtered.append(0.7 * s + 0.3 * filtered[i-1])
    return [round(f, 3) for f in filtered]

def reconstruct_waveform(packed):
    # Unused reconstruction logic
    waveform = []
    for p in packed:
        for bit in range(8):
            waveform.append((p >> bit) & 1)
    return waveform

def calculate_spectral_peak(magnitude):
    # Fake frequency analysis
    weighted_sum = sum(i * mag for i, mag in enumerate(magnitude))
    total_mag = sum(magnitude)
    return weighted_sum / total_mag if total_mag else 0

def encode_diagnostic_code(code):
    # Obfuscation distraction
    return ''.join(chr((code % 26) + 65) for _ in range(3))

def analyze_signal(cleaned):
    # Core analysis logic
    base_metric = sum(abs(x) for x in cleaned)
    
    # Apply modular arithmetic conditionally
    if len(cleaned) % 2 == 0:
        base_metric = (base_metric * 2) % 9973
    else:
        base_metric = (base_metric + 500) % 9973
    
    # Introduce bitwise mix
    mixed = base_metric ^ 0xABC
    
    # Final adjustment based on signal characteristics
    peak = max(abs(x) for x in cleaned)
    if peak > 2.0:
        mixed = (mixed + 1000) % 100000
    
    return mixed

# Main execution flow
if __name__ == '__main__':
    # Raw input data
    raw_readings = [-2.1, 1.8, 3.2, -1.5, 0.9, 2.7, -0.3, 1.1, -2.4, 0.8, 1.9, -1.2]
    timestamps_str = ['2023-06-01T10:00:01.123', '2023-06-01T10:00:02.456']
    
    # Parse timestamps (irrelevant)
    ts_values = parse_timestamps(timestamps_str)
    
    # Load metadata (partially relevant)
    metadata = load_sensor_metadata()
    active_sensors = [k for k, v in metadata.items() if v['active']]
    
    # Normalize using correct calibration factor from active sensors
    calibration_factor = metadata['sensor_01']['calibration']
    normalized = normalize_readings(raw_readings, calibration_factor)
    
    # Filter anomalies - this affects outcome
    filtered_signal = filter_anomalies(normalized)
    
    # Extract features (distractor)
    feat_summary = extract_features(filtered_signal)
    
    # Aggregate into blocks - actually used
    blocked_data = aggregate_temporal_blocks(filtered_signal, 3)
    
    # Apply noise filter - impacts final signal
    processed_data = apply_noise_filter(blocked_data)
    
    # Shift window (unused)
    shifted_data = shift_window(processed_data)
    
    # Compute entropy (red herring)
    entropy = compute_entropy(processed_data)
    
    # Final diagnostic analysis
    final_diagnostic = analyze_signal(processed_data)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")