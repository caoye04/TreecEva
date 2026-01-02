from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (real and decoy)
sensor_readings = [14, 19, 24, 28, 33, 35, 37, 40, 42, 45]
dummy_readings = [x ** 0.5 for x in sensor_readings if x % 3 == 0]  # Irrelevant computation

# Noise filtering with misleading intermediate steps
def filter_noise(data, level=2):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        if abs(data[i] - avg) > level:
            smoothed.append(avg)
        else:
            smoothed.append(data[i])
    smoothed.append(data[-1])
    return smoothed

# Signal baseline correction - relevant
def correct_baseline(signal, base=20):
    return [x - base for x in signal]

# Decoy function: looks important but unused
def deprecated_normalization(vec):
    max_val = max(vec)
    return [x / max_val for x in vec]

# Data transformation pipeline
processed_data = filter_noise(sensor_readings)
processed_data = correct_baseline(processed_data)

# Threshold logic with red herring structure
threshold_config = {
    'low': 5,
    'medium': 10,
    'high': 15
}

# Misleading dynamic update (never used later)
dynamic_weights = {k: v * 1.5 for k, v in threshold_config.items()}
dynamic_weights['critical'] = 25

# Actual threshold map used in analysis
threshold_map = defaultdict(int)
threshold_map.update({'low': 3, 'medium': 7, 'high': 12})

# Auxiliary statistical distraction
data_counter = Counter([int(x) // 5 for x in processed_data])
total_variance = sum((x - sum(processed_data)/len(processed_data))**2 for x in processed_data)

# Core diagnostic logic with short-circuiting and bit manipulation
def evaluate_risk_level(value, config):
    if value < config['low']:
        return 1
    elif value < config['medium']:
        return 2
    elif value < config['high']:
        return 3
    else:
        return 4

# Signal analyzer with composite logic
def analyze_signal(cleaned_signal, thresholds):
    # Bitwise feature extraction (relevant)
    binary_flags = [int(x > 0) << 1 | int(x % 2 == 0) for x in cleaned_signal]
    
    # Frequency of risk categories
    risk_scores = [evaluate_risk_level(abs(x), thresholds) for x in cleaned_signal]
    
    # Hidden arithmetic chain: sum of squares mod 1000
    magic_sum = sum(x*x for x in cleaned_signal if x > 0)
    checksum = magic_sum % 1000
    
    # Conditional override path (dead code - never triggers due to data)
    if any(x > 100 for x in cleaned_signal):
        return checksum - 500  # Red herring
    
    # Real result computation: weighted combination
    count_by_risk = Counter(risk_scores)
    aggregate = 0
    for risk, count in count_by_risk.items():
        if risk == 1:
            aggregate += count * 3
        elif risk == 2:
            aggregate += count * 7
        elif risk == 3:
            aggregate += count * 11
        elif risk == 4:
            aggregate += count * 13
    
    # Final adjustment using modular arithmetic and case logic
    final_shift = len([x for x in binary_flags if x & 2])  # Count how many were positive
    final_shift = (final_shift * checksum) % 19
    
    return aggregate + final_shift

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")