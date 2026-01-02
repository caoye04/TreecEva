import itertools

# Simulated sensor array data from distributed environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.2]
humidity_readings = [56, 58, 60, 55, 62, 59, 54, 57]
pressure_readings = [1013, 1015, 1012, 1010, 1016, 1014, 1011, 1013]

# Irrelevant auxiliary arrays (distractors)
baseline_offsets = [0.1, -0.2, 0.3, -0.1, 0.0, 0.2, -0.3, 0.1]
calibration_factors = [1.01, 0.99, 1.02, 0.98, 1.00, 1.03, 0.97, 1.01]
noise_floor = [0.05, 0.07, 0.06, 0.08, 0.05, 0.09, 0.04, 0.06]

# Misleading preprocessing (dead path)
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 1.1 for x in data]

# Unused transformation chain
smoothed_temps = [round(t * 1.01 + 0.2, 2) for t in temperature_readings]
dew_points = [round(t - ((100 - h) / 5), 2) for t, h in zip(temperature_readings, humidity_readings)]

# Core processing pipeline
epoch_timestamps = list(range(1623456000, 1623456000 + 8))
reading_pairs = list(zip(temperature_readings, humidity_readings, epoch_timestamps))

# Generate sliding window features (3-element windows)
windowed_data = []
for i in range(len(reading_pairs) - 2):
    window = reading_pairs[i:i+3]
    avg_temp = sum(w[0] for w in window) / 3
    avg_humid = sum(w[1] for w in window) / 3
    time_span = window[-1][2] - window[0][2]
    stability_index = avg_temp / (avg_humid + 1)
    windowed_data.append((avg_temp, avg_humid, stability_index, time_span))

# Apply conditional filtering using stability thresholds
critical_windows = []
for wt, wh, si, ts in windowed_data:
    if si < 0.4 or si > 0.45:
        critical_windows.append((wt, wh, si, ts))

# Simulate diagnostic signal extraction
signal_peaks = []
for i, (wt, wh, si, ts) in enumerate(critical_windows):
    peak_metric = wt * (wh ** 0.5) * (si + 0.1)
    signal_peaks.append((i, peak_metric))

# Secondary filter based on peak significance
significant_peaks = [p for p in signal_peaks if p[1] > 70]

# Construct optimized path using itertools.chain for flattening nested conditions
expanded_diagnostics = list(itertools.chain.from_iterable(
    [[p[1] * 0.95, p[1] * 1.05] for p in significant_peaks if p[0] % 2 == 0]
))

# Additional red herring: unused FFT-like transformation
frequency_components = []
for i in range(len(expanded_diagnostics) - 1):
    delta = expanded_diagnostics[i+1] - expanded_diagnostics[i]
    phase = delta * 3.14159 / 180
    frequency_components.append(phase ** 2)

# Actual key computation path
aggregated_signals = [
    sig * 1.1 for sig in expanded_diagnostics 
    if sig > 65
]

# Decoy function that is never called
def deprecated_analysis(x):
    return sum([v ** 0.7 for v in x]) / len(x)

# Tuple unpacking with distractor variables
if len(aggregated_signals) >= 2:
    first_signal, second_signal = aggregated_signals[0], aggregated_signals[1]
    temp_offset = first_signal - 23.5
    humid_factor = second_signal / 57
else:
    first_signal = second_signal = temp_offset = humid_factor = 0

# Bit manipulation decoy (irrelevant to final result)
bitwise_diagnostic = 0
for val in pressure_readings:
    bitwise_diagnostic ^= int(val) & 0xFF

# Core logic disguised among distractions
rolling_adjustment = 0.0
for i, val in enumerate(aggregated_signals):
    rolling_adjustment += val * (0.9 ** i)

# Final processing function with conditional expression
threshold_met = len(significant_peaks) >= 1
scaling_factor = 2.5 if threshold_met else 1.0

# Key statement containing the answer
def process_metrics(path_data, extra_diag):
    base_score = sum(path_data) / len(path_data)
    penalty = 0.3 * len(extra_diag) if len(extra_diag) > 3 else 0.1 * len(extra_diag)
    adjustment = 1.75 if base_score > 70 else 1.25
    return int((base_score * adjustment - penalty) * scaling_factor)

final_diagnostic = process_metrics(aggregated_signals, frequency_components)

# Print required output
print(f"Result: {final_diagnostic}")