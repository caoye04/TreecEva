import math

# Simulated sensor data and calibration parameters
data_points = [3.2, 4.1, 2.8, 5.6, 6.3, 4.9, 2.2, 7.1, 8.0, 6.7]
baseline_shift = 0.37
sampling_rate = 100  # Hz
decay_factor = 0.88

# Irrelevant calibration curve (distractor)
calibration_curve = [(x, round(math.sin(x * 0.4) * 2.1, 2)) for x in range(10)]

# Real preprocessing: apply baseline correction and smoothing
shifted_data = [x + baseline_shift for x in data_points]
smoothed_data = []
for i in range(len(shifted_data)):
    window = shifted_data[max(0, i-2):i+1]
    smoothed_data.append(sum(window) / len(window))

# Misleading noise injection attempt (unused path)
noise_amplitude = 0.15
noisy_data = [x + noise_amplitude * math.cos(i) for i, x in enumerate(smoothed_data)]  # Not used

# Threshold configuration map (critical)
threshold_map = {
    'low': 3.5,
    'medium': 5.0,
    'high': 6.5
}

# Auxiliary diagnostic function (partially relevant)
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Decoy function – looks important but unused
def deprecated_normalization(arr, factor=1.0):
    max_val = max(arr)
    return [x / (max_val * factor) for x in arr]  # Dead code path

# Signal classification engine
def classify_peak(value, thresholds):
    if value < thresholds['medium']:
        return 'low'
    elif value < thresholds['high']:
        return 'medium'
    else:
        return 'high'

# Core analysis pipeline
def analyze_signal(signal, config):
    # Step 1: Identify peaks above medium threshold
    peaks = [x for x in signal if x >= config['medium']]
    
    # Step 2: Compute peak-to-average ratio
    avg_signal = sum(signal) / len(signal)
    if not peaks:
        return 0
    peak_avg_ratio = sum(peaks) / len(peaks) / avg_signal
    
    # Step 3: Apply logarithmic weighting based on classification
    classifications = [classify_peak(x, config) for x in peaks]
    weight_map = {'low': 0.5, 'medium': 1.2, 'high': 2.0}
    weighted_sum = sum(weight_map[cls] for cls in classifications)
    
    # Step 4: Combine with entropy of full signal
    signal_entropy = compute_entropy(signal)
    
    # Step 5: Final diagnostic score
    diagnostic_score = (peak_avg_ratio * weighted_sum) + (signal_entropy * 0.7)
    
    # Distractor computation (looks significant but not directly used)
    adjusted_score = diagnostic_score * decay_factor  # Unused
    normalized_peaks = [p / max(peaks) for p in peaks]  # Computed but irrelevant
    
    # Final adjustment using integer logic
    adjustment_factor = len([p for p in peaks if p >= config['high']])
    if adjustment_factor > 0:
        diagnostic_score += math.log(adjustment_factor + 1) * 1.5
    
    return round(diagnostic_score, 6)

# Unused data transformation chain (red herring)
transformed_chain = list(map(lambda x: x ** 2 % 4.7, filter(lambda x: x > 4.0, data_points)))

# Critical execution point
processed_data = smoothed_data
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")