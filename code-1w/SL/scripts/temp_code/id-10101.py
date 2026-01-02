import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 23.9, 24.7]
humidity_readings = [45, 48, 50, 44, 52, 49, 47]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B3', 'C9', 'D1', 'E8']
redundant_flags = [True, False, True, False, True]

def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def detect_anomalies(series):
    # Real logic: count values above 0.8 after normalization
    norm = normalize(series)
    anomalies = [i for i, x in enumerate(norm) if x > 0.8]
    return len(anomalies)

def compute_entropy(data):
    # Distractor function - not used in final result
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return round(entropy, 4)

def generate_combinations(items):
    # Dead code path - creates confusion with signal processing
    combos = []
    for r in range(2, len(items)+1):
        combos.extend(itertools.combinations(items, r))
    return combos[:10]  # Truncate to avoid explosion

def filter_outliers(data, threshold=1.5):
    # Real preprocessing step
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def phase_shift_correction(signal, shift=1):
    # Real transformation: circular shift
    return signal[shift:] + signal[:shift]

def integrate_signals(*signals):
    # Combine multiple normalized signals element-wise
    normalized = [normalize(s) for s in signals]
    integrated = [sum(vals)/len(vals) for vals in zip(*normalized)]
    return integrated

def classify_pattern(sequence):
    # Distractor: uses itertools but irrelevant
    groups = [list(g) for k, g in itertools.groupby(sequence, key=lambda x: x > 0.5)]
    pattern_code = ''.join(str(len(group) % 10) for group in groups if group)
    return pattern_code or '0'

def temporal_weighting(data, decay=0.9):
    # Real weighting function applied in processing
    weights = [decay ** i for i in range(len(data)-1, -1, -1)]
    weighted_sum = sum(d * w for d, w in zip(data, weights))
    return weighted_sum / sum(weights)

def analyze_readings(composite_signal):
    # Final analysis - critical function
    baseline = sum(composite_signal) / len(composite_signal)
    volatility = sum(abs(composite_signal[i] - composite_signal[i-1]) 
                     for i in range(1, len(composite_signal)))
    score = (baseline * 1000) + (volatility * 100)
    return int(round(score))

# Begin actual processing chain
filtered_temp = filter_outliers(temperature_readings)
normalized_humidity = normalize(humidity_readings)

# Apply real phase correction
shifted_pressure = phase_shift_correction(pressure_readings, 2)

# Integrate three processed signals
processed_signals = integrate_signals(
    filtered_temp,
    normalized_humidity,
    normalize(shifted_pressure)
)

# Irrelevant computations (red herrings)
anomaly_count = detect_anomalies(humidity_readings)
entropy_value = compute_entropy([int(x) for x in pressure_readings])
signal_combinations = generate_combinations(legacy_codes)
pattern_fingerprint = classify_pattern(processed_signals)

# Apply temporal weighting - actually modifies the signal used in final step
weighted_signal = [temporal_weighting(processed_signals, 0.95)] * len(processed_signals)

# Final diagnostic depends on this statement
final_diagnostic = analyze_readings(processed_signals)

# Print target result
print(f"Target result: {final_diagnostic}")