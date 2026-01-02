import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9, 22.5]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 53, 49, 46]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014, 1013]

# Irrelevant calibration constants for unused sensors (distractor)
ph_calibration_offset = 0.23
flow_rate_multiplier = 1.07
vibration_threshold = 8.4

# Misleading intermediate transformation (dead path)
def compute_ph_stability(raw_logs):
    return sum([abs(log - 7.0) for log in raw_logs]) / len(raw_logs)

# Unused function simulating legacy system compatibility (red herring)
def legacy_compatibility_layer(data_chunk):
    shifted = 0
    for i in range(len(data_chunk)):
        shifted ^= int(data_chunk[i] * 100) << (i % 4)
    return shifted % 97

# Signal processing pipeline
noise_floor = 0.15
detrended_temps = [t - noise_floor for t in temperature_readings]
scaled_humidity = [(h / 100) ** 0.5 for h in humidity_readings]

# Apply Hann window smoothing to temperature (relevant preprocessing)
window_size = 3
hann_window = [0.5 * (1 - math.cos(2 * math.pi * i / (window_size - 1))) if window_size > 1 else 1.0 for i in range(window_size)]

# Convolution with padding
smoothed_temps = []
for i in range(len(detrended_temps)):
    total_weight = 0
    weighted_sum = 0
    for j in range(window_size):
        idx = min(max(i + j - 1, 0), len(detrended_temps) - 1)
        weight = hann_window[j]
        weighted_sum += detrended_temps[idx] * weight
        total_weight += weight
    smoothed_temps.append(weighted_sum / total_weight)

# Frequency domain analysis via simple DFT approximation (partially relevant)
def dft_magnitude(signal, freq_index):
    N = len(signal)
    real = sum(signal[n] * math.cos(2 * math.pi * freq_index * n / N) for n in range(N))
    imag = sum(signal[n] * math.sin(2 * math.pi * freq_index * n / N) for n in range(N))
    return math.sqrt(real**2 + imag**2)

# Extract dominant frequency energy (used later)
fundamental_energy = dft_magnitude(smoothed_temps, 2)
harmonic_energy = dft_magnitude(smoothed_temps, 4)

# Compute cross-correlation between temp and pressure (distractor)
corr_temp_pressure = 0
mean_temp = sum(smoothed_temps) / len(smoothed_temps)
mean_press = sum(pressure_readings) / len(pressure_readings)
std_temp = math.sqrt(sum((t - mean_temp)**2 for t in smoothed_temps) / len(smoothed_temps))
std_press = math.sqrt(sum((p - mean_press)**2 for p in pressure_readings) / len(pressure_readings))
for i in range(len(smoothed_temps)):
    corr_temp_pressure += ((smoothed_temps[i] - mean_temp) * (pressure_readings[i] - mean_press)) / (std_temp * std_press)
corr_temp_pressure /= len(smoothed_temps)

# Bitmask analysis of discrete states (relevant but obscured)
discrete_states = [int(t > 24.0) << 2 | int(h > 50) << 1 | int(p < 1015) for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings)]
state_transitions = 0
for i in range(1, len(discrete_states)):
    state_transitions += bin(discrete_states[i] ^ discrete_states[i-1]).count('1')

# Data slicing for anomaly detection window (relevant)
anomaly_window = smoothed_temps[-5:]
baseline_ref = sum(smoothed_temps[:-5]) / len(smoothed_temps[:-5])
anomalies = [abs(x - baseline_ref) > 1.0 for x in anomaly_window]

# Dictionary-based rule engine for diagnostics (core logic)
diagnostic_rules = {
    'thermal_gradient': lambda x: sum(x[i+1] - x[i] for i in range(len(x)-1)) / len(x),
    'instability_index': lambda x: max(x) - min(x),
    'spectral_ratio': lambda fe, he: he / fe if fe != 0 else 0,
    'transition_load': lambda st: st / 10.0
}

# Apply rules to generate features
feature_vector = [
    diagnostic_rules['thermal_gradient'](smoothed_temps),
    diagnostic_rules['instability_index'](smoothed_temps),
    diagnostic_rules['spectral_ratio'](fundamental_energy, harmonic_energy),
    diagnostic_rules['transition_load'](state_transitions)
]

# Lambda-based dynamic weighting (key concept)
adaptive_weights = list(map(lambda f: 0.5 + (f * 0.1) if abs(f) > 0.5 else 0.25, feature_vector))

# Redundant normalization (distractor)
normalized_features = [f / (1 + abs(f)) for f in feature_vector]

# Simulated neural threshold activation (misleading)
activation_potential = 0
for feat, weight in zip(normalized_features, adaptive_weights):
    activation_potential += feat * weight * 0.7

# Final signal processor using slice and dictionary lookup (critical)
processed_signals = {
    'values': smoothed_temps[::2],  # Every other reading
    'anomaly_count': sum(anomalies),
    'energy_focus': fundamental_energy,
    'complexity_metric': state_transitions * diagnostic_rules['instability_index'](smoothed_temps)
}

# Core analysis function (depends on processed_signals)
def analyze_readings(signal_data):
    readings = signal_data['values']
    base_score = sum(readings) / len(readings)
    
    # Additional corrections based on metadata
    if signal_data['anomaly_count'] > 0:
        base_score -= 0.5
    if signal_data['energy_focus'] > 2.0:
        base_score += 0.3
    
    # Complex adjustment using bitwise manipulation (key step)
    raw_transition = int(signal_data['complexity_metric'])
    adjusted_metric = (raw_transition ^ 0xAA) & 0xFF  # Bit flip and mask
    final_adjustment = (adjusted_metric >> 3) - 12
    
    # Apply final adjustment
    result = base_score + (final_adjustment * 0.01)
    
    # Dead code branch (red herring)
    if result < 0:
        result = abs(result) * 1.5
    
    return round(result, 4)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")