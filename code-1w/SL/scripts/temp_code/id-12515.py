import math

# Simulated sensor array diagnostics with embedded logic chain

def analyze_sensor_readings(readings):
    if not readings:
        return 0
    filtered = [r for r in readings if r > 0]
    if len(filtered) < 3:
        return -1
    avg = sum(filtered) / len(filtered)
    variance = sum((x - avg) ** 2 for x in filtered) / len(filtered)
    return math.sqrt(variance) if variance > 0.1 else round(avg % 3)

# Legacy compatibility wrapper (distractor)
def legacy_calibrate(x):
    return (x * 0.987 + 1.23) ** 0.5

# Unused but plausible-looking utility (dead code path)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core transformation pipeline
def transform_signal(signal, mode='standard'):
    if mode == 'boost':
        return [s * 1.5 for s in signal]
    elif mode == 'attenuate':
        return [s * 0.7 for s in signal]
    return [s + 0.1 for s in signal]

# Data normalization with red herring branches
def normalize_vector(vec):
    mag = math.sqrt(sum(v ** 2 for v in vec))
    if mag == 0:
        return vec
    result = [v / mag for v in vec]
    # Distractor: irrelevant phase adjustment
    phase_shift = sum(result) * 0.05
    adjusted = [r + phase_shift for r in result]
    return adjusted  # Original normalization is what matters

# Conditional processing using lambda and ternary
validate_entry = lambda x: x >= 0.5 if isinstance(x, float) else False

def evaluate_thresholds(entries, config):
    passed = 0
    for entry in entries:
        val = entry.get('value', 0)
        key = entry.get('type', 'unknown')
        limit = config.get(key, 1.0)
        # Complex conditional expression (mixed relevance)
        status = 'high' if val > limit * 1.5 else ('medium' if val > limit else 'low')
        if status != 'low' and validate_entry(val):
            passed += 1
    return passed if passed % 2 == 0 else passed + 1

# Aggregation with misleading intermediate transformations
def aggregate_signals(sensors):
    raw_sequences = []
    noise_floor = 0.02
    for name, data in sensors.items():
        clean_data = [d for d in data if abs(d) > noise_floor]
        if name.startswith('aux'):
            transformed = transform_signal(clean_data, 'attenuate')
        elif name.endswith('primary'):
            transformed = transform_signal(clean_data, 'boost')
        else:
            transformed = transform_signal(clean_data)
        raw_sequences.append(sum(transformed[:5]))
    
    # Irrelevant frequency analysis (decoy)
    def compute_dft(sequence):
        N = len(sequence)
        dft = []
        for k in range(N):
            real = sum(sequence[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
            imag = -sum(sequence[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
            dft.append(complex(real, imag))
        return dft
    
    # Actual relevant computation buried here
    base_scores = [analyze_sensor_readings([s]) for s in raw_sequences]
    return sum(abs(s) for s in base_scores)

# Main data processor with nested logic
def process_metrics(data_set, thresholds):
    # Initial decoy: unused statistical moment calculation
    def calculate_skewness(arr):
        n = len(arr)
        if n == 0 or all(x == arr[0] for x in arr):
            return 0.0
        mean = sum(arr) / n
        std = (sum((x - mean) ** 2 for x in arr) / n) ** 0.5
        if std == 0:
            return 0.0
        skew = (sum((x - mean) ** 3 for x in arr) / n) / (std ** 3)
        return skew
    
    # Real work begins
    aggregated = []
    for key, values in data_set.items():
        if 'sensor' in key:
            temp = sum(v ** 2 for v in values) ** 0.5
            category = 'type_a' if temp > 10 else 'type_b'
            decision = 'accept' if evaluate_thresholds([
                {'value': temp, 'type': category}
            ], thresholds) > 0 else 'reject'
            if decision == 'accept':
                aggregated.append(temp * 0.8)
        elif 'control' in key:
            # Dead branch with misleading computation
            control_score = sum(math.tanh(x) for x in values)
            normalized_score = control_score / len(values) if values else 0
            # This score is never used downstream
    
    # Critical nesting level 4: conditional lambda within list comprehension
    processed = [
        (lambda x: x * 1.1 if x < 15 else (x * 1.05 if x < 25 else x * 0.95))(val)
        for val in aggregated
        if val is not None
    ]
    
    # Final integration with distractor variables
    baseline = sum(processed)
    adjustment_factor = 0.95
    # Fake correction based on unused entropy
    # entropy_value = compute_entropy([int(p) for p in processed])  # commented out but present as idea
    final_score = baseline * adjustment_factor
    
    # The actual answer emerges from this deterministic path
    diagnostic_weight = 2.0 if final_score > 20 else 1.5
    final_diagnostic = int(final_score * diagnostic_weight)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Setup test data with meaningful structure
sensor_network = {
    'sensor_primary': [1.2, 0.8, 2.1, 1.9, 0.5],
    'sensor_aux_1': [-0.3, 0.4, 0.6, 0.2, -0.1],
    'sensor_aux_2': [0.9, 1.1, 0.7, 1.3, 0.8],
    'control_node_a': [0.1, -0.2, 0.3],
    'control_node_b': [-0.4, 0.5, 0.0]
}

threshold_map = {
    'type_a': 5.0,
    'type_b': 1.5,
    'default': 2.0
}

# Aggregate data using realistic pipeline
aggregate_data = {}
for node, readings in sensor_network.items():
    if 'sensor' in node:
        magnitude = sum(r ** 2 for r in readings) ** 0.5
        smoothed = [r * 0.95 for r in readings]
        corrected = [r + 0.05 for r in smoothed]
        aggregate_data[node] = corrected
    else:
        # Control nodes get dummy entries (irrelevant)
        aggregate_data[node] = [0.0] * len(readings)

# Key execution point
final_diagnostic = process_metrics(aggregate_data, threshold_map)
