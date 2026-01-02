from collections import defaultdict, Counter
import math

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.9, 23.7, 22.1, 21.9, 25.6]
humidity_readings = [45, 48, 52, 58, 61, 56, 50, 47, 44, 53]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1007, 1010, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5', 'J0']
error_flags = [False, False, True, False, False, False, True, False, False, False]

# Misleading preprocessing path (dead code - never used)
def legacy_transform(values):
    return [round(v * 1.02 + 3.7, 1) for v in values if v > 0]

def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

# Complex but partially irrelevant transformation chain
def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    if max_val == min_val:
        return [0.5] * len(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

def compute_entropy(values):
    count_dict = Counter([round(v, 1) for v in values])
    total = len(values)
    entropy = -sum((freq/total) * math.log2(freq/total) for freq in count_dict.values())
    return round(entropy, 4)

# Unused recursive function (decoy)
def recursive_dampen(arr, depth=0):
    if depth >= 3 or len(arr) < 2:
        return arr
    halved = [x * 0.9 for x in arr]
    return recursive_dampen(halved, depth + 1)

# Real processing begins here
filtered_temp = filter_outliers(temperature_readings, threshold=1.8)
normalized_temp = normalize_signal(filtered_temp)

displacement_map = defaultdict(float)
for i, t in enumerate(normalized_temp):
    displacement_map[f'node_{i}'] = t * math.sin(i * 0.5)

# Simulate signal interference pattern (partially relevant)
interference_pattern = []
for i in range(len(normalized_temp)):
    phase = math.cos(i * 0.3) * math.sin(i * 0.7)
    interference_pattern.append(phase * 0.1)

adjusted_signal = [a + b for a, b in zip(normalized_temp, interference_pattern)]

def extract_features(signal):
    features = {}
    features['length'] = len(signal)
    features['peak'] = max(signal)
    features['trough'] = min(signal)
    features['mean'] = sum(signal) / len(signal)
    features['variance'] = sum((x - features['mean'])**2 for x in signal) / len(signal)
    features['zero_crossings'] = sum(1 for i in range(1, len(signal)) if signal[i-1] * signal[i] < 0)
    return features

# Extract features from adjusted signal
signal_features = extract_features(adjusted_signal)

# Parallel processing of humidity (mostly irrelevant)
normalized_humidity = normalize_signal(humidity_readings)
humidity_entropy = compute_entropy(normalized_humidity)

# Pressure trend analysis (distractor with misleading intermediate result)
pressure_trend = [pressure_readings[i+1] - pressure_readings[i] for i in range(len(pressure_readings)-1)]
avg_pressure_change = round(sum(pressure_trend) / len(pressure_trend), 3)

# Core diagnostic logic (key path)
processed_signals = []
for val in adjusted_signal:
    # Apply non-linear compression
    compressed = math.log(1 + abs(val)) * (1 if val >= 0 else -1)
    processed_signals.append(round(compressed, 4))

# Secondary feature extraction on processed signals
processed_stats = {
    'count_positive': len([v for v in processed_signals if v > 0]),
    'sum_absolute': sum(abs(v) for v in processed_signals),
    'range': max(processed_signals) - min(processed_signals)
}

# Final analysis using both signal and metadata
system_health = []
system_health.append(processed_stats['count_positive'] * 10)
system_health.append(int(signal_features['peak'] * 100))
system_health.append(int(abs(signal_features['trough']) * 50))

# Critical computation hidden among distractors
def analyze_readings(proc_sig):
    # Weighted combination based on empirical calibration
    w1, w2, w3 = 0.3, 0.5, 0.2
    metric_a = sum(1 for x in proc_sig if x > 0.1)  # Active nodes
    metric_b = int(sum(abs(x) for x in proc_sig) * 10)  # Total energy
    metric_c = int(max(proc_sig) * 100)  # Peak response
    
    # Decoy calculation (never used)
    fake_score = (metric_a * 7 + metric_b // 10 + metric_c * 2) % 999
    
    # Actual diagnostic formula
    raw_diagnostic = w1 * metric_a + w2 * (metric_b / 100.0) + w3 * metric_c
    
    # Final adjustment based on entropy (red herring - constant effect)
    dummy_entropy = compute_entropy([0.1, 0.3, 0.5, 0.7, 0.9])
    adjustment = math.sqrt(dummy_entropy)  # Always same value
    
    final_value = raw_diagnostic * adjustment
    return int(round(final_value))

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")