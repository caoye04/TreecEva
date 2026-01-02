import math

# Simulated sensor data processing system for aerospace telemetry
raw_readings = [0.78, 1.32, -0.45, 2.11, 0.93, -1.07, 1.65, -0.23, 0.88, 1.02]

def normalize_signal(data):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))
    normalized = [(x - mean_val) / std_dev for x in data]
    return normalized

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) / len(data)**0.5 < threshold]
    # Irrelevant transformation
    temp_shadow = [math.sin(x) * 0.1 for x in data]
    temp_shadow.sort(reverse=True)
    return filtered

def generate_harmonics(signal):
    # Adds harmonics for signal integrity analysis (mostly irrelevant)
    harmonic_pairs = []
    for i in range(len(signal)):
        if i % 3 == 0:
            harmonic_pairs.append((signal[i], signal[i] * math.cos(i)))
    # Dead code path - never used
    complex_envelope = [(a + b * 1j) for a, b in harmonic_pairs]
    return [abs(a + b) for a, b in harmonic_pairs]

def integrate_channels(primary, secondary):
    # Simulates dual-channel integration with phase offset
    combined = []
    phase_shift = 0.5
    for i in range(min(len(primary), len(secondary))):
        val = primary[i] * 0.7 + secondary[i] * math.exp(-phase_shift) * 0.3
        combined.append(round(val, 4))
    padding = [0.0] * (len(primary) - len(combined))
    return combined + padding

def slice_window(data, start=1, end=-2):
    # Critical slicing operation
    if end == -2:
        end = len(data) - 1
    window = data[start:end]
    # Distractor: meaningless bit manipulation
    mask = 0b1010
    masked_values = [i ^ mask & 0b1111 for i in range(len(window))]
    return window

def amplify_segments(data, factor=1.2):
    amplified = [x * factor for x in data]
    # Decoy normalization
    baseline_corrected = [x - 0.05 for x in amplified]
    return amplified

def compute_entropy(signal):
    # Entropy calculation (red herring)
    prob_dist = [abs(x) / sum(abs(v) for v in signal) for x in signal]
    entropy = -sum(p * math.log(p) for p in prob_dist if p > 0)
    return round(entropy, 4)

def detect_anomalies(signal):
    anomalies = []
    for i in range(1, len(signal)):
        if abs(signal[i] - signal[i-1]) > 0.8:
            anomalies.append(i)
    # Unused intermediate result
    anomaly_score = sum(anomalies) * 0.1 if anomalies else 0.0
    return anomalies

def analyze_signal(frames):
    # Main analysis function - contains key logic
    if not frames:
        return 0.0
    
    # Step 1: Compute weighted moving average
    wma = sum(frames[i] * (i+1) for i in range(len(frames))) / sum(i+1 for i in range(len(frames)))
    
    # Step 2: Apply decay envelope
    decayed = wma * (0.9 ** len(frames))
    
    # Step 3: Phase correction based on frame count
    corrected = decayed * math.pi / 4 if len(frames) > 3 else decayed
    
    # Step 4: Final diagnostic scaling
    scale_factor = 1000 / (1 + abs(corrected))
    diagnostic_value = int(abs(corrected * scale_factor))
    
    # Irrelevant branching
    if diagnostic_value > 500:
        adjustment = math.log(diagnostic_value, 10)
        final_adjusted = diagnostic_value - int(adjustment * 10)
    else:
        # This branch is misleading but not taken
        mock_recalibrate = [math.tan(x) for x in frames[:3]]
        final_adjusted = diagnostic_value + 50
    
    return diagnostic_value

# --- Execution Flow ---
# Raw signal acquisition
normalized_readings = normalize_signal(raw_readings)

# Outlier filtering (reduces list length)
filtered_readings = filter_outliers(normalized_readings)

# Harmonic generation (adds complexity)
harmonics = generate_harmonics(filtered_readings)

# Channel integration (combines signals)
integrated_signal = integrate_channels(filtered_readings, harmonics)

# Window slicing (critical step)
signal_window = slice_window(integrated_signal, start=2, end=-1)

# Amplify for clarity
amplified_window = amplify_segments(signal_window, factor=1.3)

# Redundant entropy check
entropy_metric = compute_entropy(amplified_window)

# Anomaly detection (unused result)
anomaly_indices = detect_anomalies(amplified_window)

# Signal processing complete
processed_frames = amplified_window

# --- Key Statement ---
final_diagnostic = analyze_signal(processed_frames)

# Output result
print(f"Result: {final_diagnostic}")