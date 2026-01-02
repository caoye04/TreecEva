import math

def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if x > 0.5]
    normalized = [val / max(filtered) for val in filtered]
    return normalized

def compute_entropy(values):
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return entropy

def shift_window(data, window_size=3):
    """Misleading function - not used in final computation"""
    result = []
    for i in range(len(data) - window_size + 1):
        result.append(sum(data[i:i+window_size]))
    return result

def generate_checksum(sequence):
    """Dead code path - never called"""
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= int(val * 100) + idx
    return checksum

def evaluate_stability(metrics):
    if len(metrics) == 0:
        return 0.0
    mean_metric = sum(metrics) / len(metrics)
    variance = sum((m - mean_metric) ** 2 for m in metrics) / len(metrics)
    return math.sqrt(variance)

def decode_sequence(signal):
    decoded = []
    for s in signal:
        if s < 0.7:
            decoded.append(1)
        elif s > 0.9:
            decoded.append(3)
        else:
            decoded.append(2)
    return decoded

def analyze_pattern(data, config):
    # Key transformation chain
    magnitude = sum(d ** 2 for d in data)
    category_map = {1: 'A', 2: 'B', 3: 'C'}
    inverted = [1.0 / (1 + math.exp(-d)) for d in data]
    activation_sum = sum(inverted)

    # Red herring variables
    temp_buffer = [math.sin(x) for x in data]
    dummy_score = compute_entropy(temp_buffer)
    baseline_shift = evaluate_stability(temp_buffer)

    # Actual relevant logic buried here
    threshold_met = [1 if x > config['limit'] else 0 for x in inverted]
    pattern_strength = sum(threshold_met) * activation_sum

    adjustment_factor = config.get('factor', 1.5)
    if pattern_strength > 5:
        adjustment_factor *= 1.2

    # Final computation
    result = int(pattern_strength * adjustment_factor) - 100

    # Decoy operation (no effect)
    for _ in range(2):
        result = abs((result ^ 42) % 1000)

    return result

# Main execution flow
raw_sensor_data = [0.61, 0.72, 0.58, 0.95, 0.67, 0.83, 0.76, 0.69]

# Irrelevant preprocessing
smoothed_data = [math.cos(x) for x in raw_sensor_data]
dummy_metrics = [s * 2 for s in smoothed_data if s < 0.8]

# Real processing begins
filtered_diagnostic = preprocess_signal(raw_sensor_data)
transformed_data = decode_sequence(filtered_diagnostic)

# Configuration with misleading entries
thresholds = {
    'limit': 0.65,
    'factor': 1.8,
    'debug_mode': True,
    'timeout': 300,
    'limit_decoy': 0.45  # unused
}

# Unused recursive red herring
def recursive_waste(n):
    if n <= 1:
        return 1
    return recursive_waste(n-1) + recursive_waste(n-2)

# Dead code path
if False:
    wasted_effort = [x for x in transformed_data if x > 5]
    final_diagnostic = -999

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")