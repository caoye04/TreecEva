from collections import defaultdict, Counter
import math

# Simulated sensor data processing with performance evaluation
def analyze_readings(raw_data):
    processed = []
    noise_floor = 0.05
    for reading in raw_data:
        if abs(reading) < noise_floor:
            continue
        processed.append(round(math.log(abs(reading)) * 100, 2))
    return processed

# Irrelevant helper: spectrum normalization (unused)
def normalize_spectrum(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Core metric computation
def compute_metrics(values):
    count = len(values)
    mean = sum(values) / count if count else 0
    variance = sum((x - mean) ** 2 for x in values) / count if count else 0
    peak = max(values, default=0)
    entropy = -sum((Counter(values)[v] / count) * math.log2(Counter(values)[v] / count) 
                  for v in Counter(values)) if count else 0
    return {
        'count': count,
        'mean': mean,
        'variance': round(variance, 4),
        'peak': peak,
        'entropy': round(entropy, 4)
    }

# Decoy function: network latency simulation (never called)
def simulate_latency(nodes):
    delays = defaultdict(lambda: 0.0)
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            delay = (hash(nodes[i]) ^ hash(nodes[j])) % 100 / 1000
            delays[(nodes[i], nodes[j])] = delay
    return delays

# Data validation (partially relevant)
def validate_entry(entry):
    if not isinstance(entry, (int, float)):
        return False
    if math.isnan(entry):
        return False
    return abs(entry) <= 1e6

# Main evaluation logic
def evaluate_performance(metrics, dataset):
    base_score = 0
    adjustment = 0.0
    
    # Red herring: unused weight map
    weights = {'count': 0.1, 'mean': 0.2, 'variance': -0.05, 'peak': 0.3, 'entropy': 0.4}
    
    # Conditional scoring with nested logic
    if metrics['count'] > 10:
        base_score += 25
        if metrics['mean'] > 50:
            base_score += 15
        elif metrics['mean'] > 30:
            base_score += 5
    else:
        base_score -= 10

    if metrics['peak'] > 90:
        adjustment += 20.5
    elif metrics['peak'] > 70:
        adjustment += 5.0
    else:
        adjustment -= 15.5

    # Complex condition involving set operations
    unique_values = set(dataset)
    outliers = {v for v in unique_values if v > 80 or v < 10}
    if len(outliers) > 5:
        adjustment -= 10.0

    # Bit manipulation decoy (computationally irrelevant)
    flag = 0b101010
    mask = 0b111100
    masked_flag = flag & mask
    debug_code = bin(masked_flag ^ 0b111111)

    # Lambda-based transformation (actually used)
    scale_func = lambda x: x * 1.5 if x > 0 else x * 0.5
    scaled_adjustment = scale_func(abs(adjustment))
    if adjustment < 0:
        scaled_adjustment = -scaled_adjustment

    # Final composition
    final_component = base_score + scaled_adjustment

    # Dead code path: unreachable due to structure
    for _ in range(0):  # Never executes
        final_component = math.sqrt(final_component) if final_component > 0 else 0

    return int(round(final_component))

# Simulated input data
raw_sensor_data = [
    0.01, -0.03, 0.005,  # Below noise floor (filtered out)
    2.1, 3.5, 1.8, 4.2, 5.1, 3.9, 2.7, 4.8, 5.5, 6.1, 3.3, 4.4,
    7.2, 6.8, 5.9, 8.1, 9.0, 7.7, 6.3, 5.4, 4.9, 8.8, 9.5
]

# Filtering and processing
filtered_data = [x for x in raw_sensor_data if validate_entry(x)]
processed_readings = analyze_readings(filtered_data)

# Extracting features
feature_set = compute_metrics(processed_readings)

# Simulated benchmark metadata (distractor)
benchmark_metadata = {
    'version': '2.1-alpha',
    'calibration': [0.01, 0.02, 0.015],
    'checksum': sum(hash(k) for k in ['init', 'phase2', 'final']) % 1000
}

# Key statement
final_score = evaluate_performance(feature_set, processed_readings)

# Output result
print(f"Result: {final_score}")