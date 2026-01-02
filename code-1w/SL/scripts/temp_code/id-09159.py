def analyze_trend(data, threshold=0.5):
    trend = 0
    noise_counter = 0
    temp_accum = 0
    
    for i in range(len(data)):
        if i > 0 and data[i] > data[i-1]:
            trend += 1
        elif data[i] < threshold:
            noise_counter += 1
        temp_accum += (data[i] * 2) % 3
    
    return trend


def preprocess_signal(signal_str):
    cleaned = signal_str.strip().lower().replace('x', '0').replace('y', '1')
    binary_vals = [int(c) for c in cleaned if c in '01']
    sum_check = sum(b for b in binary_vals)
    parity = sum_check % 2
    
    # Distractor: irrelevant transformation
    inverted = [1 - b for b in binary_vals if parity]
    return binary_vals if len(binary_vals) > 3 else [0]


def compute_entropy(values):
    from math import log2
    freq_map = {}
    total = len(values)
    if total == 0:
        return 0.0
    
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p) if p > 0 else 0
    
    # Dead code path (never used)
    if entropy < 0.1:
        return 0.0
    
    return round(entropy, 6)


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

# Misleading function that looks important but isn't used in final logic
def deprecated_metric(x):
    return (x ** 2 + 3*x + 1) % 7

# Simulated sensor metric data (binary pattern string)
sensor_log = "X1Y0X11Y001"

# Parse and extract meaningful signal
raw_signal = preprocess_signal(sensor_log)

# Generate Fibonacci-like sequence as decoy data
decoy_sequence = generate_sequence(len(raw_signal) + 5)

# Analyze trend on raw signal (treated as numeric)
trend_strength = analyze_trend([float(x) for x in raw_signal])

# Compute entropy of signal distribution
signal_entropy = compute_entropy(raw_signal)

# Baseline calibration (irrelevant to final result but looks critical)
calibration_matrix = [[i*j for j in range(3)] for i in range(3)]
total_calibration = sum(sum(row) for row in calibration_matrix)

# Key data structure: metric_data combines relevant and irrelevant features
metric_data = {
    'trend': trend_strength,
    'entropy': signal_entropy,
    'length': len(raw_signal),
    'sum': sum(raw_signal),
    'aux': total_calibration  # red herring
}

baseline = {
    'threshold': 2,
    'weight_a': 1.5,
    'weight_b': 0.8,
    'decay': 0.9
}

# Core evaluation logic with conditional expression and string method distraction
def evaluate_performance(metrics, config):
    t = metrics['trend']
    e = metrics['entropy']
    L = metrics['length']
    s = metrics['sum']
    
    # Distractor: unused variable with complex derivation
    phantom_score = (L * e + t) ** 0.5 if s > 0 else -1
    
    # Actual computation path (non-obvious due to distractions)
    adjustment = config['weight_a'] if e > 1.0 else config['weight_b']
    base = (t * adjustment) + (s * config['decay'])
    
    # Nested conditional expression using string methods on dummy data
    tag = f"T{t}_E{int(e)}".upper().replace('_', '')
    multiplier = 2 if 'E0' not in tag else 1  # tag never contains E0
    
    intermediate = base * multiplier
    
    # Final correction based on length (key dependency)
    final = intermediate - (5 if L < 4 else 2)
    
    # Dead branch (never reached due to logic)
    if phantom_score < 0 and False:
        final = 0
        
    return int(final)

# Execution point of interest
final_score = evaluate_performance(metric_data, baseline)

# Output result
print(f"Result: {final_score}")