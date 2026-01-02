import itertools

# Simulated sensor array diagnostics with noise filtering and data transformation

def collect_signals(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return [round(n, 3) for n in normalized]


def generate_harmonics(base_freq, count):
    # Irrelevant function: simulates signal harmonics but not used in final path
    return [base_freq * (2 ** i) for i in range(count)]


def decode_pattern(sequence):
    # Decodes binary-like patterns from thresholds (not actually used)
    binary_str = ''.join(['1' if x > 0.5 else '0' for x in sequence[:8]])
    return int(binary_str, 2) if len(binary_str) == 8 else 0


def transform_signal_chain(data, method='fft'):
    # Complex-looking but mostly irrelevant transformation chain
    stage1 = [d * 1.03 for d in data]
    stage2 = [abs(s) ** 0.5 for s in stage1]
    if method == 'fft':
        stage3 = [round(s * 2.1, 3) for s in stage2]
    else:
        stage3 = [round(s + 1.1, 3) for s in stage2]
    
    # Distractor: unused advanced processing branch
    def wavelet_transform(seq):
        return [seq[i] - seq[i-1] for i in range(1, len(seq), 2)]
    
    return stage3

# Dead function – looks important but unused
def calculate_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    return -sum((count/total) * log(count/total, 2) for count in freq.values())

# Main processing pipeline

def extract_features(dataset):
    # Real feature extraction
    magnitude = sum([x**2 for x in dataset])
    peak = max(dataset)
    crossings = sum(1 for i in range(1, len(dataset)) if dataset[i-1] < 0 <= dataset[i])
    return {
        'magnitude': round(magnitude, 3),
        'peak': peak,
        'zero_crossings': crossings
    }


def process_metrics(features, cfg):
    score = 0
    score += int(features['magnitude'] * cfg['weight_m'])
    score += features['peak'] * cfg['weight_p']
    score += features['zero_crossings'] * cfg['weight_z']
    
    # Red herring: conditional that looks consequential but never triggers
    if score > 1000:
        anomaly = True
        correction_factor = 0.85
        score *= correction_factor  # Never reached
    
    return int(score)

# Irrelevant constants (distractors)
BASELINE_THRESHOLD = 0.764
CALIBRATION_ARRAY = list(itertools.accumulate([0.1]*50, lambda a, b: a + b * 0.95))
REFERENCE_PATTERN = [0.2, 0.4, 0.8, 1.6, 3.2][:]

# Configuration dictionary (used)
config = {
    'weight_m': 2.3,
    'weight_p': 15,
    'weight_z': 42
}

# Simulated raw sensor input (key input data)
raw_sensor_data = [-0.5, 0.2, 0.0, -0.3, 0.8, -0.1, 0.6, 0.0, 0.4, -0.7]

# Actual execution path
filtered_data = collect_signals(raw_sensor_data)
transformed_data = transform_signal_chain(filtered_data, method='fft')
features = extract_features(transformed_data)

# Critical statement
final_diagnostic = process_metrics(features, config)

# Distractor variables (look relevant but unused)
diagnostic_code = decode_pattern(transformed_data)
analysis_flag = diagnostic_code > 128
entropy_value = calculate_entropy([int(x*10) for x in transformed_data])
harmonics = generate_harmonics(50, 6)

# Unused lambda — looks functional but not connected to main logic
refine_fn = lambda arr: [a for a in arr if a > 0.2]

# Output result
print(f"Result: {final_diagnostic}")