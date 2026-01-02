import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [56, 61, 59, 66, 70, 52, 48, 75]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1018, 1020, 1009]

# Irrelevant transformation - red herring (bit manipulation on pressure)
def obscure_data(data):
    result = 0
    for val in data:
        result ^= int(val) << 2
    return result

obfuscated_pressure_key = obscure_data(pressure_readings)  # Dead end

# Signal processing pipeline
def filter_outliers(signal, threshold=1.5):
    mean_val = sum(signal) / len(signal)
    std_dev = (sum((x - mean_val) ** 2 for x in signal) / len(signal)) ** 0.5
    return [x for x in signal if abs(x - mean_val) <= threshold * std_dev]

def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in signal]

def generate_frequency_bands(signal):
    # Create artificial harmonics using itertools
    base = normalize_signal(signal)
    doubled = [x * 2 for x in base]
    halved = [x / 2 for x in base]
    combined = list(itertools.chain(*zip(base, doubled, halved)))
    return combined[:len(signal)]  # Truncate to original length

# Misleading diagnostic path (unused)
def legacy_diagnostic(seq):
    acc = 1
    for i in range(len(seq)):
        if i % 3 == 0:
            acc *= seq[i] + 0.1
    return int(acc % 1000)

legacy_flag = legacy_diagnostic(humidity_readings)  # Distractor

# Real processing chain
filtered_temp = filter_outliers(temperature_readings, 1.8)
normalized_temp = normalize_signal(filtered_temp)
frequency_enhanced = generate_frequency_bands(normalized_temp)

# Composite signal mixing (relevant)
processed_signals = []
for i in range(len(frequency_enhanced)):
    mixed = frequency_enhanced[i] * 0.7 + normalized_temp[i % len(normalized_temp)] * 0.3
    processed_signals.append(round(mixed, 6))

# Fake fusion algorithm (dead code)
def bogus_fusion(a, b):
    return [(x + y) / 2 for x, y in zip(a[::2], b[1::2])]

phantom_fusion = bogus_fusion(temperature_readings, humidity_readings)  # Unused

# Actual analysis function
def analyze_readings(signal):
    # Weighted moving average with decay
    weights = [0.4, 0.3, 0.2, 0.1]
    smoothed = []
    for i in range(len(signal)):
        total_weight = 0.0
        weighted_sum = 0.0
        for j, w in enumerate(weights):
            if i - j >= 0:
                weighted_sum += signal[i - j] * w
                total_weight += w
        smoothed.append(weighted_sum / total_weight if total_weight > 0 else signal[i])
    
    # Final diagnostic metric: sum of squares above median
    median_val = sorted(smoothed)[len(smoothed) // 2]
    active_energy = sum((x - median_val) ** 2 for x in smoothed if x > median_val)
    return round(active_energy, 6)

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")