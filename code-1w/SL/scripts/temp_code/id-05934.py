import math

# Simulated sensor array data (real signal embedded in noise)
sensor_readings = [3.2, 1.8, 4.5, 0.9, 6.7, 2.3, 8.1, 1.0, 5.4, 3.3]

def generate_baseline(length):
    # Distractor: irrelevant function for alternate calibration
    return [math.sin(i * 0.5) for i in range(length)]

def filter_noise(data, window=3):
    # Apply moving average to smooth noise
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        segment = data[start:end]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

def compute_entropy(values):
    # Distractor: computes information-theoretic entropy (not used in final result)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def extract_peaks(series, sensitivity=2.0):
    # Identify significant peaks above dynamic baseline
    mean_val = sum(series) / len(series)
    deviation = sensitivity * (sum((x - mean_val) ** 2 for x in series) / len(series)) ** 0.5
    peaks = [x for x in series if x > mean_val + deviation]
    return sorted(peaks, reverse=True)

def build_threshold_map(levels=5):
    # Create multi-level detection thresholds
    base = 2.5
    return {i: base * (1.4 ** i) for i in range(levels)}

def evaluate_stability(metric):
    # Distractor: evaluates system stability (dead code path)
    if metric < 1.0:
        return 'CRITICAL'
    elif metric < 3.0:
        return 'WARNING'
    else:
        return 'STABLE'

def transform_features(raw):
    # Apply logarithmic scaling and square transformation
    scaled = [math.log(x + 1) for x in raw]
    powered = [s ** 2 for s in scaled]
    return [p * 1.75 for p in powered]

def validate_integrity(checksum, data_length):
    # Distractor: integrity check not actually affecting logic
    expected = (data_length * 3) % 7
    return checksum % 7 == expected

def analyze_signal(signal_data, thresholds):
    # Core analysis with conditional branching and list comprehension
    high_activity = [val for val in signal_data if val > thresholds[2]]
    
    if len(high_activity) < 3:
        score = sum(signal_data) * 0.5
    else:
        peak_contrib = sum([min(p, 7.0) for p in high_activity[:4]])  # Cap influence
        base_contrib = sum(signal_data) * 0.3
        adjustment = math.cos(len(high_activity))  # Minor trigonometric tweak
        score = peak_contrib + base_contrib + adjustment
    
    # Final nonlinear mapping
    normalized = math.tanh(score / 20.0)
    diagnostic_code = int(normalized * 100000)  # Scale to integer code
    return diagnostic_code

# Irrelevant preprocessing chain (distractors)
baseline_correction = generate_baseline(len(sensor_readings))
entropy_metric = compute_entropy(sensor_readings)
stability_status = evaluate_stability(entropy_metric)

# Relevant processing pipeline
filtered_data = filter_noise(sensor_readings)
enhanced_features = transform_features(filtered_data)
peak_list = extract_peaks(enhanced_features, sensitivity=1.8)

# Build necessary configuration
threshold_map = build_threshold_map(levels=5)

# Validate dummy checksum (irrelevant but looks important)
dummy_checksum = sum(int(x) for x in sensor_readings)
integrity_ok = validate_integrity(dummy_checksum, len(sensor_readings))

# Key execution point
final_diagnostic = analyze_signal(enhanced_features, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")