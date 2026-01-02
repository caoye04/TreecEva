import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [56, 58, 61, 59, 63, 66, 68, 70]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1013, 1010, 1009]

# Irrelevant transformation: historical weather indices (unused)
historical_indices = [0.87, 0.83, 0.91, 0.88, 0.93, 0.95, 0.90, 0.85]
index_mapping = {i: val for i, val in enumerate(historical_indices)}

# Distractor function: unused seasonal adjustment
def apply_seasonal_factor(data, season='summer'):
    factor = {'spring': 1.05, 'summer': 1.0, 'autumn': 0.98, 'winter': 0.92}.get(season, 1.0)
    return [x * factor for x in data]

# Unused noise filter (decoy)
def remove_noise(signal, threshold=1.5):
    filtered = []
    for x in signal:
        if abs(x - sum(signal) / len(signal)) < threshold:
            filtered.append(x)
    return filtered

# Signal processing pipeline
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    std_dev = (sum((x - mean_val) ** 2 for x in signal) / len(signal)) ** 0.5
    return [(x - mean_val) / std_dev for x in signal]

def detect_outliers(normalized, threshold=2.0):
    return [i for i, x in enumerate(normalized) if abs(x) > threshold]

def integrate_multi_sensor(temps, humids, presss):
    # Weighted fusion: temperature (0.5), humidity (0.3), pressure (0.2)
    composite = []
    for t, h, p in zip(temps, humids, presss):
        norm_t = (t - 20) / 10
        norm_h = (h - 50) / 50
        norm_p = (p - 1000) / 50
        score = 0.5 * norm_t + 0.3 * norm_h - 0.2 * norm_p
        composite.append(round(score, 4))
    return composite

# Real processing begins here
normalized_temps = normalize_signal(temperature_readings)
outlier_positions = detect_outliers(normalized_temps, 1.8)

# Decoy list comprehension with no downstream use
spurious_flags = [f"flag_{i}" for i in range(len(humidity_readings)) if i % 3 == 0 and i not in outlier_positions]

# Actual signal generation
raw_fusion = integrate_multi_sensor(temperature_readings, humidity_readings, pressure_readings)

# Process signals through filtering and thresholding
processed_signals = []
for val in raw_fusion:
    if val > 0.4:
        processed_signals.append(int(val * 100) + 5)
    elif val < 0.1:
        processed_signals.append(int(val * 100) - 2)
    else:
        processed_signals.append(int(val * 100))

# Unused bitmask simulation (distractor)
bitmask_layers = []
for i in range(3):
    layer = 0
    for j, bit in enumerate([1 if (i+j) % 2 == 0 else 0 for _ in range(8)]):
        layer |= (bit << j)
    bitmask_layers.append(layer)

# Set operation to identify stable readings (used)
stable_threshold_set = set(range(8)) - set(outlier_positions)
adjusted_signals = [processed_signals[i] for i in sorted(stable_threshold_set)]

# Analyze final diagnostics
def analyze_readings(signals):
    total_energy = 0
    peak_count = 0
    baseline = sum(signals) / len(signals)
    
    for s in signals:
        if s > baseline * 1.1:
            peak_count += 1
            total_energy += s ** 1.1
        elif s < baseline * 0.9:
            total_energy += s ** 0.9
        else:
            total_energy += s
    
    # Complex diagnostic formula
    diagnostic_score = (total_energy / 100) * (1 + 0.1 * peak_count)
    return int(diagnostic_score)

# Final computation
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")