import itertools

def analyze_signal(data, threshold=0.75):
    # Irrelevant signal processing (dead abstraction)
    filtered = [x for x in data if x > threshold]
    return sum(filtered) / len(data) if data else 0

def evaluate_health(timestamps, readings):
    # Distractor function: looks important but unused
    avg = sum(readings) / len(readings)
    anomalies = [t for t, r in zip(timestamps, readings) if r > avg * 1.5]
    return len(anomalies)

def generate_checksum(sequence):
    # Bit manipulation red herring
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 100) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)  # Rotate left
    return checksum % 1000

def main_pipeline(input_stream):
    # Core irrelevant data transformations
    raw_segments = [segment for segment in input_stream if len(segment) > 2]
    flat_data = list(itertools.chain.from_iterable(raw_segments))
    
    # Decoy statistical analysis
    mean_val = sum(flat_data) / len(flat_data) if flat_data else 0
    std_dev = (sum((x - mean_val) ** 2 for x in flat_data) / len(flat_data)) ** 0.5 if flat_data else 0
    normalized = [(x - mean_val) / std_dev for x in flat_data] if std_dev else flat_data
    
    # Real logic buried in noise
    event_log = [{'time': i, 'val': v, 'tag': 'SYS'} for i, v in enumerate(flat_data)]
    critical_events = [e for e in event_log if e['val'] > 0.85]
    
    # Simulate multiple system layers
    layers = ['L1', 'L2', 'L3']
    layer_map = {layer: [] for layer in layers}
    for e in critical_events:
        layer_key = layers[int(e['time']) % 3]
        layer_map[layer_key].append(e)
    
    # Unused complex structure
    summary_stats = {
        layer: {
            'count': len(entries),
            'values': [e['val'] for e in entries],
            'max_val': max([e['val'] for e in entries]) if entries else 0
        } for layer in layers
    }
    
    # Red herring: cryptographic-style hash (unused)
    entropy_pool = [hash(str(v)) % 10000 for v in flat_data[:5]]
    security_token = sum(entropy_pool[i] * (i + 1) for i in range(len(entropy_pool)))
    
    # Actual relevant computation chain starts here (obscured)
    log_entries = [e['val'] for e in event_log if e['val'] > 0.5]
    system_threshold = len([v for v in log_entries if v > 0.7])
    
    # Key distraction: recursive decoy
    def recurse_noise(n):
        if n <= 1: return 1
        return recurse_noise(n-1) + recurse_noise(n-2)
    
    # Lambda-based filtering (partially relevant)
    severity_func = lambda x: x ** 3 if x > 0.7 else x ** 2
    severities = [severity_func(v) for v in log_entries]
    
    # Dictionary operations with distractors
    metrics = {
        'raw_count': len(flat_data),
        'high_severity': len([s for s in severities if s > 0.5]),
        'total_load': sum(severities),
        'baseline': 0.618,
        'adjustment': 0
    }
    
    # Complex conditional mask (mostly irrelevant)
    if metrics['raw_count'] > 10 and mean_val < 1.0:
        metrics['adjustment'] = std_dev * 0.1
    elif security_token > 5000:
        metrics['adjustment'] = -0.05
    else:
        metrics['adjustment'] = 0.01
    
    # Core calculation buried in dictionary
    metrics['adjusted_load'] = metrics['total_load'] + metrics['adjustment'] * len(severities)
    
    # Critical function hidden among decoys
    def process_metrics(entries, thresh):
        # Actual answer depends on modular arithmetic and filtering
        valid = [v for v in entries if v > 0.6]
        grouped = [valid[i:i+thresh] for i in range(0, len(valid), thresh)]
        result = 0
        for group in grouped:
            if len(group) == thresh:
                # Modular reduction with exponentiation
                product = 1
                for g in group:
                    product *= (g * 10) % 7  # Scale and mod
                result += int(product ** 0.5)  # Square root of product
        return result + len(entries)  # Final contribution
    
    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_threshold)
    
    # Dead code path
    if False:
        backup = generate_checksum(severities)
        final_diagnostic = backup // 10
    
    # Print required result
    print(f"Target result: {final_diagnostic}")

# Simulated input data
input_stream = [
    [0.3, 0.4, 0.91, 0.87],
    [0.2, 0.65, 0.72, 0.93],
    [0.5, 0.55, 0.81, 0.69, 0.95],
    [0.4, 0.77, 0.83]
]

main_pipeline(input_stream)