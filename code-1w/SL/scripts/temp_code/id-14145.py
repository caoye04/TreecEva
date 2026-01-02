import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.2]
humidity_readings = [45, 47, 50, 44, 48, 52, 43, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
REFERENCE_VOLTAGE = 5.0

# Signal processing functions
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [round(x - mean_val, 3) for x in signal]

def detect_anomalies(data, threshold=1.5):
    avg = sum(data) / len(data)
    std_dev = (sum((x - avg) ** 2 for x in data) / len(data)) ** 0.5
    return [i for i, x in enumerate(data) if abs(x - avg) > threshold * std_dev]

def filter_noise(signal, window_size=3):
    filtered = []
    offset = window_size // 2
    for i in range(len(signal)):
        start = max(0, i - offset)
        end = min(len(signal), i + offset + 1)
        window = signal[start:end]
        filtered.append(round(sum(window) / len(window), 3))
    return filtered

# Decoy function – appears useful but not used in main logic
def deprecated_analysis(seq):
    result = 0
    for i in range(len(seq)):
        result += seq[i] * (0.9 ** i)
    return result

# Complex data transformation pipeline
raw_combinations = []
for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings):
    # Composite index with arbitrary weighting (some are distractions)
    composite = t * 1.2 + h * 0.1 - (p - 1000) * 0.05
    raw_combinations.append(round(composite, 3))

# Normalize the composite signal
normalized_combo = normalize_signal(raw_combinations)

# Apply noise filtering
filtered_combo = filter_noise(normalized_combo)

# Secondary derived features (some irrelevant)
gradient_sequence = []
for i in range(1, len(filtered_combo)):
    gradient_sequence.append(round(filtered_combo[i] - filtered_combo[i-1], 3))

# Dummy statistical summary (dead code path)
stats_summary = {
    'max_gradient': max(gradient_sequence),
    'min_gradient': min(gradient_sequence),
    'zero_crossings': sum(1 for i in range(1, len(gradient_sequence)) 
                         if gradient_sequence[i-1] * gradient_sequence[i] < 0),
    'mean_abs': round(sum(abs(g) for g in gradient_sequence) / len(gradient_sequence), 3)
}

# Unused transformation chain (red herring)
decimated_signal = [filtered_combo[i] for i in range(0, len(filtered_combo), 2)]
transformed = [math.sin(x * 0.5) for x in decimated_signal]
energy_estimate = sum(x**2 for x in transformed)

# Actual processing path begins here
anomaly_indices = detect_anomalies(filtered_combo, threshold=1.1)
cleaned_signal = [x for i, x in enumerate(filtered_combo) if i not in anomaly_indices]

# Further processing with dictionary operations
signal_metrics = {
    'count': len(cleaned_signal),
    'mean': sum(cleaned_signal) / len(cleaned_signal),
    'range': max(cleaned_signal) - min(cleaned_signal),
    'variance': sum((x - sum(cleaned_signal)/len(cleaned_signal))**2 for x in cleaned_signal) / len(cleaned_signal)
}

# Introduce set operations to remove duplicates (though none exist)
unique_rounded = list(set([round(x, 2) for x in cleaned_signal]))
unique_rounded.sort()

# Reconstruct a stabilized version using list comprehension and averaging
stabilized = [x for x in cleaned_signal if abs(x - signal_metrics['mean']) < signal_metrics['range'] * 0.75]

# Final diagnostic computation
processed_signals = [round(s ** 2 + 0.1 * i, 3) for i, s in enumerate(stabilized)]

def analyze_readings(readings):
    if not readings:
        return 0.0
    base_score = sum(math.cos(r * 0.2) for r in readings)
    length_factor = len(readings) * 0.8
    range_penalty = (max(readings) - min(readings)) * 0.3
    
    # Secondary adjustment based on pattern density
    rising_pairs = sum(1 for i in range(1, len(readings)) if readings[i] > readings[i-1])
    density_factor = rising_pairs / len(readings) if readings else 0
    
    # Final formula combines multiple subtle effects
    result = (base_score + length_factor - range_penalty) * (1 + density_factor * 0.25)
    
    # Dead code branch - never executed due to input constraints
    if len(readings) > 100:
        fallback = 0
        for val in readings:
            fallback += val * 0.01
        return fallback  # unreachable
    
    return round(result, 6)

# Execute key statement
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")