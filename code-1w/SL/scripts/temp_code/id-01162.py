import itertools

# Simulated sensor array data (real values)
sensor_readings = [145, 203, 98, 167, 255, 134, 189, 76]

calibration_offsets = [12, -8, 5, -15, 0, 10, -5, 7]

# Irrelevant auxiliary calibration constants (distractor)
reference_frequencies = [440, 880, 1320, 1760]
amplitude_modulation_table = {i: i * 1.05 for i in range(100)}

# Signal preprocessing stage
def apply_calibration(readings, offsets):
    calibrated = []
    for i in range(len(readings)):
        calibrated.append(readings[i] + offsets[i])
    return calibrated

# Noise filtering using moving average (relevant)
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window = signal[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Irrelevant function: frequency domain analysis (dead path)
def compute_fourier_peaks(signal):
    peak_magnitudes = []
    for i in range(0, len(signal), 2):
        if i + 1 < len(signal):
            peak_magnitudes.append((signal[i]**2 + signal[i+1]**2)**0.5)
    return peak_magnitudes

# Data binning by magnitude ranges (distractor)
def categorize_levels(values):
    categories = {'low': 0, 'medium': 0, 'high': 0}
    for v in values:
        if v < 100:
            categories['low'] += 1
        elif v < 200:
            categories['medium'] += 1
        else:
            categories['high'] += 1
    return categories

# Real-time anomaly detection logic (relevant)
def detect_anomalies(signal, sensitivity=0.15):
    anomalies = []
    for i in range(1, len(signal)):
        change = abs(signal[i] - signal[i-1])
        baseline = (signal[i] + signal[i-1]) / 2
        if baseline > 0 and (change / baseline) > sensitivity:
            anomalies.append(i)
    return anomalies

# Threshold map generation based on dynamic ranges (relevant)
def generate_threshold_map(data):
    base_threshold = sum(data) / len(data)
    variance = sum((x - base_threshold) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return {
        'normal': base_threshold - std_dev,
        'warning': base_threshold,
        'critical': base_threshold + 2 * std_dev
    }

# Diagnostic analyzer combining multiple metrics (core logic)
def analyze_signal(data, thresholds):
    # Count how many points exceed each threshold level
    counts = {'normal': 0, 'warning': 0, 'critical': 0}
    for val in data:
        if val >= thresholds['critical']:
            counts['critical'] += 1
        elif val >= thresholds['warning']:
            counts['warning'] += 1
        elif val >= thresholds['normal']:
            counts['normal'] += 1
    
    # Compute diagnostic score (this is the real answer path)
    score_components = [
        counts['normal'] * 1,
        counts['warning'] * 3,
        counts['critical'] * 7
    ]
    
    # Decoy aggregation methods (misleading paths)
    fake_aggregates = []
    for r in itertools.product([1, 2], repeat=3):
        fake_aggregates.append(sum(r[i] * score_components[i] for i in range(3)))
    
    temp_result = sum(score_components) + len(fake_aggregates) // 10  # red herring
    
    # Actual final computation (non-obvious due to noise)
    adjustment_factor = len([x for x in data if x > 150])
    raw_score = sum(score_components)
    
    # Final diagnostic uses raw_score and adjustment_factor
    final_value = raw_score * 2 - adjustment_factor
    
    # Dead code branch: never executed but looks important
    if False:
        fallback = 0
        for chunk in itertools.groupby(data, key=lambda x: x > 100):
            fallback += len(list(chunk[1]))
        final_value = fallback
    
    return final_value

# Unused recursive helper (distractor)
def recursive_summer(seq, idx=0):
    if idx >= len(seq):
        return 0
    return seq[idx] + recursive_summer(seq, idx + 1)

# Main execution flow
adjusted_readings = apply_calibration(sensor_readings, calibration_offsets)
smoothed_signal = smooth_signal(adjusted_readings)

# Irrelevant frequency analysis call (no impact)
fourier_analysis = compute_fourier_peaks(smoothed_signal)

# Anomaly detection (partially relevant for context)
anomaly_indices = detect_anomalies(smoothed_signal, sensitivity=0.18)

# Binning used nowhere (distractor)
level_distribution = categorize_levels(smoothed_signal)

# Real processing begins here
processed_data = [x * 1.02 for x in smoothed_signal]  # minor gain correction

# Generate actual threshold map
threshold_map = generate_threshold_map(processed_data)

# Core diagnostic call — this produces the answer
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")