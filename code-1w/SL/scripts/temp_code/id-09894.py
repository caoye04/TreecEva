import itertools

# Simulated biomedical signal processing pipeline with decoy analytics
def analyze_waveform(signal):
    if len(signal) < 5:
        return 0
    smoothed = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    trend = sum(smoothed[:4]) / 4 if len(smoothed) >= 4 else 0
    return trend * 1.7

def compute_entropy(data):
    # Irrelevant complexity: information theory decoy
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 3)

def evaluate_risk_level(biomarkers):
    # Dead code path — never actually used in final computation
    thresholds = {'tnsr': 3.1, 'kurt': 7.2, 'skew': 1.8}
    risk_score = 0
    for key, val in biomarkers.items():
        if val > thresholds.get(key, 10):
            risk_score += 1
    return risk_score

def generate_combinations(values):
    # Distractor: creates unused combinatorial outputs
    combs = []
    for r in range(2, 4):
        combs.extend(itertools.combinations(values, r))
    return len(combs)

def normalize_readings(readings):
    # Red herring normalization not used in final path
    mean_val = sum(readings) / len(readings)
    std_dev = (sum((x - mean_val)**2 for x in readings) / len(readings))**0.5
    return [(x - mean_val) / std_dev for x in readings]

def extract_features(trace):
    # Real feature extraction buried in noise
    peaks = [i for i in range(1, len(trace)-1) if trace[i-1] < trace[i] > trace[i+1]]
    peak_vals = [trace[i] for i in peaks]
    avg_peak = sum(peak_vals) / len(peak_vals) if peak_vals else 0
    return avg_peak, len(peaks)

def derive_stability_index(pattern):
    # Misleading stability metric (not used)
    diffs = [abs(pattern[i] - pattern[i-1]) for i in range(1, len(pattern))]
    return 100 / (1 + sum(diffs))

def filter_artifacts(stream, threshold=0.5):
    # Unused filtering logic — distracts from core
    return [x for x in stream if abs(x) > threshold]

def process_metrics(signature):
    # Core logic hidden among decoys
    a, b = extract_features(signature['channel_x'])
    c = analyze_waveform(signature['channel_y'])
    temp_score = (a * 1.3) + (b * 2.1) + (c * 0.8)
    
    # Critical transformation
    adjustment_factor = 1.25
    if temp_score > 15:
        adjustment_factor = 0.9
    elif temp_score < 5:
        adjustment_factor = 1.6
    
    final_score = temp_score * adjustment_factor
    
    # Decoy calculations below
    _ = compute_entropy(signature['channel_x'])
    _ = generate_combinations(signature['channel_y'])
    _ = derive_stability_index(signature['channel_y'])
    
    return int(round(final_score))

# Simulated sensor inputs
sensor_x = [0.1, 1.3, 0.9, 2.7, 0.4, 3.1, 1.2, 2.9]
sensor_y = [0.8, 1.1, 1.9, 2.4, 1.7, 0.6, 2.2]

# Auxiliary variables — red herrings
baseline_metrics = {"tnsr": 2.8, "kurt": 5.4, "skew": 1.1}
raw_spectrum = [127, 255, 191, 63, 31]
dummy_pairs = list(itertools.product([1, 2], ['a', 'b']))

# Unused intermediate transformations
shifted_signal = [x * 0.7 for x in sensor_x]
aggregated_stats = {
    'mean_x': sum(sensor_x)/len(sensor_x),
    'max_y': max(sensor_y),
    'entropy_x': compute_entropy([int(x*10) for x in sensor_x])
}

# Data structure with cross-references (decoy)
health_signature = {
    'patient_id': 'HMX-9021',
    'timestamp': '2023-11-05T14:30:00Z',
    'channel_x': sensor_x.copy(),
    'channel_y': sensor_y.copy(),
    'version': 'v2.1'
}

# Linear search for irrelevant condition
for i, val in enumerate(sensor_y):
    if val > 2.0:
        health_signature['first_peak_idx'] = i
        break

# Key execution point
final_diagnostic = process_metrics(health_signature)

# Print required output
print(f"Result: {final_diagnostic}")