from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def fetch_raw_readings():
    return [14, 17, 23, 14, 19, 23, 14, 28, 17, 23, 31, 19, 14]

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)

def normalize_signal(raw):
    max_val = max(raw)
    return [round(x / max_val, 6) for x in raw]

def apply_noise_filter(data, strength=0.1):
    # Irrelevant filtering for distraction
    return [x for i, x in enumerate(data) if i % 2 == 0]

def generate_frequency_map(data):
    freq_map = defaultdict(int)
    for item in data:
        freq_map[item] += 1
    return freq_map

def evaluate_coherence(sequence):
    coherence_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] >= sequence[i-1]:
            coherence_score += 1
    return coherence_score / (len(sequence) - 1) if sequence else 0

def derive_pattern_signature(data):
    # Complex but irrelevant transformation
    signature = 0
    for i, val in enumerate(data):
        signature ^= (val * (i + 1)) % 19
    return signature

def detect_anomalies(readings, limit=15):
    anomalies = []
    for idx, val in enumerate(readings):
        if val > limit and idx % 3 == 0:
            anomalies.append((idx, val))
    return anomalies

def calculate_baseline_drift(data):
    # Distractor function: not used in final result
    return sum(data[i+1] - data[i] for i in range(len(data)-1)) / (len(data) - 1)

def extract_critical_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return sorted(peaks, reverse=True)[:3] if peaks else [0]

def build_threshold_profile(dataset):
    profile = {}
    avg = sum(dataset) / len(dataset)
    profile['low'] = avg * 0.7
    profile['high'] = avg * 1.3
    profile['critical'] = avg * 1.6
    return profile

def assess_risk_level(score):
    # Dead code path — misleading
    if score < 10:
        return 'Low'
    elif score < 20:
        return 'Medium'
    else:
        return 'High'

def integrate_diagnostic_metrics(metrics):
    # Unused integration function (distractor)
    base = 1.0
    for m in metrics:
        base *= (m + 1)
    return base ** (1 / len(metrics))

def analyze_signal(data, thresholds):
    # Core logic: count how many normalized values exceed 'high' threshold
    count_above_high = 0
    for val in data:
        if val > thresholds['high']:
            count_above_high += 1
    
    # Secondary condition: only include those at even indices
    filtered_count = 0
    for i, val in enumerate(data):
        if i % 2 == 0 and val > thresholds['high']:
            filtered_count += 1
    
    # Final decision heuristic (actual answer path)
    if count_above_high >= 3:
        return 427  # High alert level
    elif filtered_count >= 2:
        return 219
    else:
        return 87

# Main execution flow
raw_sensor_data = fetch_raw_readings()
entropy_metric = compute_entropy(raw_sensor_data)
signal_normalized = normalize_signal(raw_sensor_data)

# Apply filter (but result not used — red herring)
denoised_signal = apply_noise_filter(signal_normalized)

# Generate various diagnostics (some irrelevant)
freq_analysis = generate_frequency_map(raw_sensor_data)
coherence_index = evaluate_coherence(raw_sensor_data)
pattern_key = derive_pattern_signature(raw_sensor_data)
anomaly_list = detect_anomalies(raw_sensor_data)
drift_rate = calculate_baseline_drift(raw_sensor_data)  # Computed but unused
peaks_of_interest = extract_critical_peaks(signal_normalized)

# Build threshold map for analysis
threshold_map = build_threshold_profile(signal_normalized)

# Extract peaks again — redundant call (distraction)
redundant_peaks = extract_critical_peaks(signal_normalized)

# Perform final analysis on processed data
processed_data = signal_normalized  # Critical assignment
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")