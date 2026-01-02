import math

# Simulated sensor data and diagnostic system with distractors
def acquire_signal():
    raw_samples = [i * 0.1 for i in range(100)]
    noise_floor = 0.05
    return [math.sin(x) + noise_floor * math.cos(3 * x) for x in raw_samples]

def filter_noise(signal, threshold=0.1):
    # Irrelevant filtering path (not used in main flow)
    return [x for x in signal if abs(x) > threshold]

def transform_basis(signal):
    # Fourier-inspired magnitude approximation (used)
    transformed = []
    for k in range(10):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        magnitude = math.sqrt(real * real + imag * imag)
        transformed.append(magnitude)
    return transformed

def extract_features(freq_domain):
    peak_indices = [i for i, x in enumerate(freq_domain) if x == max(freq_domain)]
    avg_magnitude = sum(freq_domain) / len(freq_domain)
    return {'peaks': peak_indices, 'avg': avg_magnitude}

def validate_calibration(features):
    # Dead code path - looks important but unused
    if 'calib' not in features:
        return False
    return features['calib'] > 0.7

def compute_entropy(data):
    # Distractor function: looks relevant but not used in critical path
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def detect_anomalies(feature_set):
    # Misleading intermediate logic
    baseline = 0.85
    tolerance = 0.1
    if 'anomaly_score' in feature_set:
        return abs(feature_set['anomaly_score'] - baseline) > tolerance
    return False

def process_signal_chain(raw_signal):
    # Core processing chain with red herrings
    normalized = [x / max(map(abs, raw_signal)) for x in raw_signal]  # Normalize
    cleaned = [x for x in normalized if x != 0]  # Remove zeros (mostly redundant)

    # Apply transformation
    freq_rep = transform_basis(cleaned)

    # Feature extraction
    features = extract_features(freq_rep)

    # Inject irrelevant state
    features['timestamp'] = 1698723456
    features['source_id'] = 'SENSOR_ALPHA'

    # Critical derived value
    features['derived_key'] = int(round(features['avg'] * 1000))

    return features

def integrate_metadata(context, payload):
    # Unused integration logic (distractor)
    payload['context'] = context
    payload['version'] = '2.1'
    return payload

def analyze_signal(data_features):
    # Final analysis with conditional logic red herring
    if not isinstance(data_features, dict) or 'peaks' not in data_features:
        return -1

    primary_peak = data_features['peaks'][0]
    base_score = data_features['avg'] * 100

    # Bit manipulation decoy
    encoded = 0
    for i in range(8):
        encoded |= (1 << (primary_peak % 8))
        encoded ^= i

    # Real computation path
    adjustment = 0
    if primary_peak in {0, 1}:
        adjustment = 10
    elif primary_peak > 5:
        adjustment = -5
    else:
        adjustment = 3

    final_score = base_score + adjustment + data_features['derived_key']

    # Decoy set operations
    flags = {1, 2, 3, 4}
    mask = {2, 4, 6}
    intersection = flags & mask  # Never used
    symmetric_diff = flags ^ mask  # Also unused

    # Lambda-based transformation (required Python feature)
    scale_fn = lambda x: x * 1.05 if x > 50 else x * 0.95
    final_score = scale_fn(final_score)

    # Set operation red herring
    status_tags = set(['active', 'verified'])
    status_tags.add('diagnostic_mode')  # No effect on output

    return round(final_score, 4)

# Global constants (some irrelevant)
CALIBRATION_MATRIX = [[0.1, 0.9], [0.8, 0.2]]
SYSTEM_GAIN = 1.0
REFERENCE_OFFSET = -0.05
MAX_ITERATIONS = 500

# Unused control flow variables
emergency_override = False
debug_trace_enabled = True
log_level = 'VERBOSE'

# Main execution flow
sensor_data = acquire_signal()
processed_data = process_signal_chain(sensor_data)

# Dead assignment - looks like it does something
processed_data['validity'] = all(x > -1 for x in sensor_data)

# Key statement
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")