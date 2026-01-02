import math

# Simulated sensor array data (irrelevant structure)
raw_data_stream = [0.1, 0.3, 0.4, 0.7, 1.2, 1.8, 2.1, 2.9, 3.0, 3.1]
sensor_offsets = {'alpha': 0.15, 'beta': -0.05, 'gamma': 0.25}
calibration_matrix = [[1.1, 0.9], [0.95, 1.05]]

# Irrelevant preprocessing steps
temp_buffer = []
for val in raw_data_stream:
    temp_buffer.append(round(val ** 2 + sensor_offsets['alpha'], 3))

# Real signal processing begins here
filtered_signals = [x for x in raw_data_stream if x > 0.5]
smoothed_signals = []
for i in range(len(filtered_signals)):
    window = filtered_signals[max(0, i-1):i+2]
    smoothed_signals.append(sum(window) / len(window))

# Misleading statistical analysis (dead path)
mean_signal = sum(smoothed_signals) / len(smoothed_signals)
variance_proxy = sum((x - mean_signal) ** 2 for x in smoothed_signals) / len(smoothed_signals)
fluctuation_index = math.sqrt(variance_proxy) if variance_proxy > 0.5 else 0.0

# Decoy function that is never called
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Unused transformation chain
transformed = list(map(lambda x: math.sin(x * 0.5), smoothed_signals))
segmented = [transformed[i:i+2] for i in range(0, len(transformed), 2)]
aggregated = [sum(segment) for segment in segmented]

# Core logic buried within distractions
def extract_features(series):
    peaks = []
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(series[i])
    return peaks

feature_set = extract_features(smoothed_signals)

# Secondary irrelevant calculation chain
drift_estimate = 0.0
for j in range(1, len(raw_data_stream)):
    drift_estimate += abs(raw_data_stream[j] - raw_data_stream[j-1])
drift_estimate /= len(raw_data_stream) - 1

# More decoy variables
critical_threshold = 2.5
stability_ratio = (max(smoothed_signals) - min(smoothed_signals)) / mean_signal if mean_signal != 0 else 0

# Actual computation path (non-obvious due to distractions)
baseline_reference = [x for x in smoothed_signals if x < 2.0]
adjusted_baseline = [x * 1.1 for x in baseline_reference]
compression_factor = len(smoothed_signals) / len(baseline_reference) if baseline_reference else 1

# Key intermediate result buried in noise
effective_amplitude = sum(adjusted_baseline) * compression_factor

# Auxiliary function with red herring parameters
def normalize_series(data, factor=1.0, offset=0.0, mode='legacy'):
    if mode == 'legacy':
        return [d * factor + offset for d in data]
    else:
        return [d / (factor + 1e-6) for d in data]

# Unused normalization call
# normalized_test = normalize_series(smoothed_signals, factor=0.8, offset=0.1, mode='legacy')

processed_signals = [round(x, 3) for x in smoothed_signals if x > 1.0]

# Another misleading metric
dominant_frequency = len([x for x in processed_signals if x > 2.0])

# Core analysis function (looks like it depends on many inputs but doesn't)
def analyze_metrics(signals):
    if not signals:
        return 0
    # Only uses length and max value - other computations were distractions
    signal_power = len(signals) * max(signals)
    correction_term = 1.0
    if len(signals) >= 4:
        correction_term *= 1.2
    if max(signals) > 2.5:
        correction_term *= 0.9
    return round(signal_power * correction_term, 3)

# Critical execution point
final_diagnostic = analyze_metrics(processed_signals)

print(f"Result: {final_diagnostic}")