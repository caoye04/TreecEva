import math

# Simulated sensor data acquisition
def acquire_sensor_readings():
    raw_signals = [0.8, 1.2, -0.4, 3.1, 2.9, -1.1, 0.05]
    calibration_offset = 0.23
    adjusted = [sig + calibration_offset for sig in raw_signals]
    return adjusted

# Signal filtering with irrelevant alternate methods
def filter_noise(data):
    # Relevant: Moving average filter
    window_size = 3
    smoothed = []
    for i in range(len(data) - window_size + 1):
        window_avg = sum(data[i:i+window_size]) / window_size
        smoothed.append(window_avg)
    
    # Irrelevant: Unused FFT attempt (red herring)
    def fft_transform(seq):
        n = len(seq)
        if n <= 1: return seq
        even = fft_transform(seq[0::2])
        odd = fft_transform(seq[1::2])
        return [even[i] + complex(0, -2*math.pi*i/n) * odd[i] for i in range(n//2)] + \
               [even[i] - complex(0, -2*math.pi*i/n) * odd[i] for i in range(n//2)]

    # Irrelevant: Unused wavelet coefficients
    wavelet_cache = [data[i] * math.cos(i * 0.5) for i in range(len(data)) if i % 2 == 0]
    wavelet_cache = [w ** 2 for w in wavelet_cache]  # Dead computation

    return smoothed

# Data normalization with misleading branches
def normalize_signal(filtered):
    min_val = min(filtered)
    max_val = max(filtered)
    range_val = max_val - min_val
    
    # Distractor: unused dynamic threshold
    dynamic_threshold = range_val * 0.618
    temp_adjust = [x for x in filtered if abs(x) > dynamic_threshold]  # Computed but unused
    temp_adjust = [t * 1.5 for t in temp_adjust]  # More dead code

    # Relevant: Z-score normalization
    mean_val = sum(filtered) / len(filtered)
    variance = sum((x - mean_val) ** 2 for x in filtered) / len(filtered)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_val) / std_dev for x in filtered]
    
    # Extra distraction: outlier detection not used downstream
    outliers = [z for z in z_scores if abs(z) > 2.0]
    outlier_mask = [abs(x) > 2.0 for x in z_scores]  # Unused boolean mask

    return z_scores

# Feature extraction with decoy logic
def extract_features(normalized):
    # Relevant: statistical moments
    moment_2 = sum(x**2 for x in normalized) / len(normalized)
    moment_4 = sum(x**4 for x in normalized) / len(normalized)
    kurtosis_like = moment_4 / (moment_2 ** 2) if moment_2 != 0 else 0

    # Distractor: frequency binning (irrelevant)
    bins = [0, 0, 0, 0, 0]
    for val in normalized:
        if val < -1: bins[0] += 1
        elif val < -0.5: bins[1] += 1
        elif val < 0.5: bins[2] += 1
        elif val < 1.0: bins[3] += 1
        else: bins[4] += 1
    entropy_estimate = -sum((b/len(normalized)) * math.log(b/len(normalized)+1e-9) for b in bins)  # Not used

    # Distractor: phase simulation (dead path)
    phase_shifts = []
    for i in range(len(normalized)):
        shift = math.sin(i * 0.3) * math.cos(i * 0.7)
        phase_shifts.append(shift * normalized[i])
    phase_shifts = [p ** 3 for p in phase_shifts]  # Unused transformation

    # Only kurtosis_like is actually used later
    return {'kurtosis_metric': kurtosis_like, 'entropy': entropy_estimate}

# Final diagnostic logic with red herring function call
def analyze_signal(data_features):
    # Extract only relevant metric
    k_metric = data_features['kurtosis_metric']
    
    # Irrelevant: mock classification tree (never executed)
    def decision_tree_classify(x):
        if x < 0.5:
            return "Class A"
        elif x < 1.8:
            return "Class B"
        else:
            return "Class C"
    
    # Decoy function that looks important
    def compute_health_index(values):
        h_index = 0
        for v in values:
            if v > 1.0:
                h_index += math.log(v) * 0.7
            elif v > 0:
                h_index += v * 0.3
        return max(0, 100 - h_index*10)
    
    # Actual logic: deterministic formula using k_metric
    adjustment_factor = 42.5
    baseline_score = 1000
    decay_rate = 0.15
    
    # Critical calculation
    intermediate = baseline_score * math.exp(-decay_rate * k_metric)
    final_diagnostic = int(intermediate + adjustment_factor)
    
    return final_diagnostic

# Orchestration with unused diagnostics
raw_data = acquire_sensor_readings()
processed_noise = filter_noise(raw_data)
normalized_signal = normalize_signal(processed_noise)
extracted = extract_features(normalized_signal)
final_diagnostic = analyze_signal(extracted)

# Misleading print statements (simulating debug output)
diag_log = ["SYS_OK", "CAL_PASS", "FILTER_ACTIVE"]
for entry in diag_log:
    pass  # Simulate logging

print(f"Result: {final_diagnostic}")