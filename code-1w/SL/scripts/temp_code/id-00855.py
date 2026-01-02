import itertools
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(data_stream):
    filtered = [x for x in data_stream if x > 0]
    normalized = [round(math.log(x), 3) for x in filtered]
    reshaped = list(itertools.chain.from_iterable([(x, x ** 0.5) for x in normalized[:5]]))
    return reshaped[:10]

# Irrelevant transformation - dead end function
def deprecated_calibrate(signal):
    return [s * 0.98 + 2.1 for s in signal if s < 5]

# Data enhancement with distractor logic
def augment_data(seq):
    augmented = []
    for i, val in enumerate(seq):
        if i % 3 == 0:
            augmented.append(val * 1.1)
        elif i % 3 == 1:
            augmented.append(val + 0.5 * (i // 2))
        else:
            augmented.append(abs(val - 0.3))  # Distractor branch
    padding = [0.1] * (12 - len(augmented))
    return augmented + padding  # Padded with irrelevant values

# Core analysis function - relevant path
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values[:8]]  # Only first 8 matter
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Secondary processing with misleading intermediate output
def generate_diagnostics(metrics):
    peak = max(metrics)
    avg = sum(metrics) / len(metrics)
    variance = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    threshold_flag = peak > 3.0  # Misleading boolean
    score = avg * (1 + variance) if threshold_flag else avg
    return {'score': round(score, 3), 'peak': peak, 'valid': threshold_flag}

# Main transformation pipeline
def transform_signal(raw):
    stage1 = preprocess_sensor_readings(raw)
    stage2 = augment_data(stage1)
    # Injecting decoy computation
    _ = [x * x for x in stage2 if x < 0.5]  # Unused list comp
    cleaned = [x for x in stage2 if x > 0.25]  # Real filter
    return cleaned

# Final analysis using combinatorics and entropy
def analyze_sequence(transformed):
    # Extract non-repeating pairs
    pairs = list(itertools.combinations(transformed, 2))
    magnitudes = [abs(a - b) for a, b in pairs[:15]]  # Limit to first 15
    # Add some constant bias (irrelevant)
    bias_offsets = [0.01 * i for i in range(len(magnitudes))]
    adjusted = [m + b for m, b in zip(magnitudes, bias_offsets)]
    # Actual key computation
    entropy_value = compute_entropy(adjusted)
    diagnostics = generate_diagnostics(adjusted)
    # Final result derived from core reasoning
    final_score = entropy_value * 1000
    return int(round(final_score))

# Simulated input data
initial_readings = [12.5, 6.8, 15.2, 3.1, 9.7, 0.5, 14.3, 7.4, 2.9, 11.6]

# Execution chain
processed_data = preprocess_sensor_readings(initial_readings)
deprecated_result = deprecated_calibrate(processed_data)  # Dead path
transformed_data = transform_signal(initial_readings)
final_diagnostic = analyze_sequence(transformed_data)
print(f"Target result: {final_diagnostic}")