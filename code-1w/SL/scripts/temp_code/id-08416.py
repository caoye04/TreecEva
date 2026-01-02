import itertools

# Simulated sensor data from industrial filtration system
turbidity_readings = [0.87, 1.02, 0.93, 1.15, 0.76, 0.88, 1.01, 0.95]
pressure_cycles = [3.2, 3.5, 3.1, 3.8, 3.0, 3.3, 3.6, 3.4]
temperature_logs = [22.1, 21.8, 22.5, 21.9, 22.3, 22.0, 21.7, 22.4]

# Irrelevant preprocessing: temperature normalization (not used in final calculation)
normalized_temps = [round((t - min(temperature_logs)) / (max(temperature_logs) - min(temperature_logs)), 4) for t in temperature_logs]
baseline_temp = sum(normalized_temps) / len(normalized_temps)
adjusted_temps = [t - baseline_temp for t in normalized_temps]

# Decoy function: analyzes pressure but returns unused result
def analyze_pressure_stability(pressures):
    diffs = [abs(p - pressures[i-1]) for i, p in enumerate(pressures) if i > 0]
    stability_score = sum(diffs) / len(diffs)
    return round(stability_score, 3)

# Unused call to decoy function
pressure_consistency = analyze_pressure_stability(pressure_cycles)

# Real signal processing chain begins
raw_signal = [t * 100 for t in turbidity_readings]  # Amplify readings

# Apply moving average filter (window size = 3)
filtered_signal = []
for i in range(len(raw_signal)):
    if i < 2:
        window = raw_signal[:i+1]
    else:
        window = raw_signal[i-2:i+1]
    filtered_signal.append(sum(window) / len(window))

# Threshold filtering using adaptive baseline
baseline = sum(filtered_signal) / len(filtered_signal)
adapted_signals = []
for val in filtered_signal:
    if val > baseline * 1.05:
        adapted_signals.append(val * 0.9)
    elif val < baseline * 0.95:
        adapted_signals.append(val * 1.1)
    else:
        adapted_signals.append(val)

# Introduce artificial harmonics (distraction with itertools)
frequency_components = list(itertools.accumulate([1, -1, 1, -1, 1, -1, 1, -1], lambda x, y: x + y))
harmonic_noise = [f * 0.05 for f in frequency_components]

# Add noise then immediately remove it (red herring operation)
distorted_signals = [a + h for a, h in zip(adapted_signals, harmonic_noise)]
cleaned_signals = [d - h for d, h in zip(distorted_signals, harmonic_noise)]  # Exact reversal

# Final processing stage
saturation_correction = [min(s, 95.0) for s in cleaned_signals]
processed_signals = [round(s ** 0.5, 3) for s in saturation_correction]  # Nonlinear transformation

# Correction factor derived from unused temperature analysis (misleading dependency)
correction_factor = round(1 + (baseline_temp * 0.01), 4)  # baseline_temp comes from irrelevant path

# KEY STATEMENT: Critical computation point
filtration_yield = sum(processed_signals) * correction_factor

# Dead code path: alternative calculation never reached
if False:
    backup_weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    fallback_yield = sum(s * w for s, w in zip(processed_signals, backup_weights))
    filtration_yield = fallback_yield

# Another distraction: permutation analysis of pressure (unused)
pressure_perms = list(itertools.permutations(pressure_cycles[:3]))
permutation_complexity = len(pressure_perms) * 1.5

print(f"Result: {filtration_yield}")