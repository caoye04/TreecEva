import math

# Simulated sensor fusion system for environmental monitoring

def collect_samples(base, count):
    return [base * (i + 1) ** 1.5 for i in range(count)]

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    # Irrelevant filtering logic (not used in final path)
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

def transform_frame(signal):
    # Complex transformation with red herring operations
    shifted = [math.sin(x / 10.0) for x in signal]
    modulated = [s * 1.75 for s in shifted]
    envelope = sum(abs(m) for m in modulated) / len(modulated)
    # Distractor: unused transformed frames
    normalized_frame = [m / envelope for m in modulated]
    return normalized_frame  # Not actually used in critical path

def generate_checksum(values):
    # Decoy function: looks important but not part of main logic
    checksum = 0
    for v in values:
        checksum ^= int(v * 100) & 0xFF
    return checksum

def slice_window(data, start, end):
    # Uses slicing - required Python feature
    return data[start:end] if end <= len(data) else data[start:]

def integrate_segments(segments):
    # Aggregates multiple signal segments
    total_power = 0.0
    for seg in segments:
        segment_sum = sum(abs(x) for x in seg)
        total_power += segment_sum * 0.85
    return total_power

def decode_phase_offset(raw):
    # Bit manipulation red herring
    offset_code = int(sum(raw) % 32)
    rotated = (offset_code << 3) | (offset_code >> 5)
    masked = rotated & 0x1F
    return masked - 16  # Returns between -16 and 15

def temporal_align(signal_list):
    # Applies alignment using slicing and padding
    min_len = min(len(s) for s in signal_list)
    aligned = [s[-min_len:] for s in signal_list]  # Reverse slicing
    transposed = [[row[i] for row in aligned] for i in range(min_len)]
    return transposed

def compute_entropy(data):
    # Unused sophisticated analysis (distractor)
    from collections import Counter
    counts = Counter(round(x, 1) for x in data)
    total = sum(counts.values())
    entropy = -sum((freq / total) * math.log2(freq / total) for freq in counts.values())
    return round(entropy, 4)

def flag_anomalies(readings):
    # Dead-end logic path
    warnings = []
    for r in readings:
        if r > 100:
            warnings.append('HIGH')
        elif r < 10:
            warnings.append('LOW')
    return warnings

def preprocess_signal(raw):
    # Main relevant preprocessing
    scaled = [x * 0.02 for x in raw]
    clipped = [min(max(x, -1.0), 1.0) for x in scaled]
    return clipped

def extract_features(signal):
    # Critical feature extraction
    magnitude = sum(x ** 2 for x in signal) ** 0.5
    zero_crossings = sum(1 for i in range(1, len(signal)) if signal[i-1] < 0 <= signal[i])
    peak_to_peak = max(signal) - min(signal)
    return {
        'rms': magnitude / len(signal)**0.5,
        'zc': zero_crossings,
        'pp': peak_to_peak
    }

def aggregate_diagnostics(features_list):
    # Combines diagnostic metrics
    avg_rms = sum(f['rms'] for f in features_list) / len(features_list)
    total_zc = sum(f['zc'] for f in features_list)
    max_pp = max(f['pp'] for f in features_list)
    score = (avg_rms * 100) + (total_zc * 10) + (max_pp * 5)
    return round(score, 2)

def analyze_readings(processed):
    # Final analysis step - target execution point
    all_features = []
    for p in processed:
        feats = extract_features(p)
        all_features.append(feats)
    diagnostic_score = aggregate_diagnostics(all_features)
    return int(diagnostic_score)

# --- Main Execution with High Interference ---

# Irrelevant initialization block
system_status = {'initialized': True, 'nodes': 7, 'uptime': 1247}
signal_log = set()
active_channels = {1, 2, 3, 5, 8}
backup_config = {"gain": 1.8, "bias": -0.3, "window": 24}

# Generate primary sensor data
raw_sensors = []
for base_freq in [12.0, 18.5, 9.2]:
    samples = collect_samples(base_freq, 40)
    raw_sensors.append(samples)

# Apply irrelevant outlier filtering (result not used later)
decoy_filtered = [filter_outliers(sensor) for sensor in raw_sensors]

# Transform each signal frame (computationally heavy but unused result)
transformed_frames = []
for raw in raw_sensors:
    frame = transform_frame(raw)
    transformed_frames.append(frame)

# Preprocess signals - this is the actual critical path
processed_signals = []
for raw in raw_sensors:
    cleaned = preprocess_signal(raw)
    processed_signals.append(cleaned)

# Introduce distractor: slice irrelevant window
focus_window = slice_window(processed_signals[0], 10, 25)

# Align signals temporally (used to justify complexity, but result ignored)
aligned_set = temporal_align(processed_signals)

# Extract checksums for integrity (decoy security measure)
for sig in processed_signals:
    chk = generate_checksum(sig)

# Flag anomalies (dead-end call)
anomaly_flags = flag_anomalies(processed_signals[0])

# Compute entropy on aligned data (unused advanced metric)
if aligned_set:
    entropy_value = compute_entropy(aligned_set[0])

# Extract phase offset (irrelevant to final result)
phase_shift = decode_phase_offset(raw_sensors[0])

# Integrate segments from transformed frames (red herring)
total_energy = integrate_segments(transformed_frames)

# Perform actual feature extraction on PREPROCESSED signals
# This is where the real work begins

# --- CRITICAL EXECUTION POINT ---
final_diagnostic = analyze_readings(processed_signals)

# Output the target result
print(f"Target result: {final_diagnostic}")