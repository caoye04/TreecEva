import math

# Simulated sensor fusion system for environmental anomaly detection
def collect_samples(duration, sample_rate):
    samples = []
    for t in range(0, duration * sample_rate):
        raw = (math.sin(0.1 * t) + 0.5 * math.cos(0.3 * t)) * math.exp(-0.002 * t)
        samples.append(round(raw + 0.1, 4))
    return samples


def filter_outliers(data, limit=2.0):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= limit * stdev], mean_val, stdev


def generate_pattern_key(sequence):
    # Irrelevant transformation - red herring
    transformed = [int(abs(x) * 100) % 7 for x in sequence]
    key_set = {i: transformed.count(i) for i in range(7)}
    return key_set


def compute_entropy(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

# Decoy function - never called but looks important
def legacy_diagnostic(signal_trace):
    cumulative = 0
    for i in range(len(signal_trace)):
        if i % 5 == 0:
            cumulative += math.tanh(signal_trace[i])
    return cumulative * 0.75

# Unused helper - dead code path
def normalize_range(data, new_min=-1, new_max=1):
    old_min, old_max = min(data), max(data)
    if old_min == old_max:
        return [0 for _ in data]
    return [(new_max - new_min) * (x - old_min) / (old_max - old_min) + new_min for x in data]

# Sensor calibration offset - irrelevant to final result
CALIBRATION_OFFSETS = {
    'alpha': 0.012,
    'beta': -0.008,
    'gamma': 0.015
}

# Main signal analysis logic
def extract_segments(trace, window_size=10):
    segments = []
    for i in range(0, len(trace) - window_size + 1, window_size // 2):
        segment = trace[i:i + window_size]
        avg = sum(segment) / len(segment)
        variance = sum((x - avg) ** 2 for x in segment) / len(segment)
        peak = max(abs(x) for x in segment)
        segments.append({'avg': avg, 'variance': variance, 'peak': peak})
    return segments


def build_threshold_map(segments):
    base_map = {}
    for i, s in enumerate(segments):
        base_map[i] = {
            'level_1': abs(s['avg']) * 1.5,
            'level_2': s['variance'] * 2.0,
            'critical': s['peak'] > 0.8
        }
    return base_map


def analyze_signal(buffer, thresholds):
    # Core logic hidden among distractions
    active_count = 0
    for idx, entry in enumerate(thresholds.values()):
        if idx >= len(buffer) or idx not in thresholds:
            continue
        val = buffer[idx]
        level1 = entry['level_1']
        level2 = entry['level_2']
        if val > level1:
            active_count += 1
            if val > level2:
                active_count += 2
    
    # Real answer derived here
    diagnostic_code = (active_count * 17) ^ 0xAB
    
    # Distractor computation
    temp_signature = set()
    for b in buffer[::3]:
        temp_signature.add(int(b * 100) % 13)
    signature_score = sum(temp_signature)
    
    # Another decoy calculation
    slice_analysis = buffer[5:-5:2]
    if len(slice_analysis) > 0:
        dummy_metric = sum(slice_analysis) / len(slice_analysis)
        diagnostic_code -= int(dummy_metric * 10)

    return diagnostic_code

# Global constants - some are misleading
BASE_SENSITIVITY = 0.78
CRITICAL_BANDWIDTH = 128
TEMPORAL_WINDOW = 40

# Data collection phase
raw_data = collect_samples(duration=6, sample_rate=20)
cleaned_data, _, _ = filter_outliers(raw_data, limit=1.8)

# Generate useless intermediate products
entropy_value = compute_entropy([int(x * 100) % 10 for x in cleaned_data])
pattern_fingerprint = generate_pattern_key(cleaned_data)

# Signal processing pipeline
signal_segments = extract_segments(cleaned_data, window_size=8)
threshold_map = build_threshold_map(signal_segments)

# Circular buffer simulation
pattern_buffer = [s['avg'] for s in signal_segments][1::2]
pattern_buffer.extend([s['variance'] for s in signal_segments][::3])

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Additional noise - unused variables
aggregate_risk = sum(s['peak'] for s in signal_segments if s['variance'] > 0.01)
segment_count = len(signal_segments)
baseline_drift = cleaned_data[0] - cleaned_data[-1]

print(f"Result: {final_diagnostic}")