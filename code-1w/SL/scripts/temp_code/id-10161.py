import itertools

# Simulated sensor metrics with noise and redundant data
def generate_diagnostics():
    base_values = [0.88, 0.92, 0.76, 0.81, 0.94]
    adjustments = [0.02, -0.03, 0.01, 0.04, -0.02]
    derived = []
    for i in range(len(base_values)):
        # Irrelevant transformation
        temp = (base_values[i] + adjustments[i]) * 1.05
        derived.append(round(temp, 2))
    return derived

# Legacy function — unused but looks important
def legacy_normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Red herring: complex-looking but unused bit manipulation
def entropy_mask(values):
    mask = 0b1010
    result = []
    for v in values:
        bits = int(v * 100) ^ mask
        bits = (bits << 2) | (bits >> 6)
        result.append(bits % 100 / 100.0)
    return result

# Real computation path obscured by distractions
def extract_key_metrics(raw_logs):
    parsed = {}
    for line in raw_logs:
        if 'STATUS' in line:
            parts = line.split(':')
            key = parts[1].strip()
            val_str = parts[2].strip()
            try:
                parsed[key] = float(val_str)
            except ValueError:
                parsed[key] = 0.0
    # Extract only relevant fields; others are distractions
    metrics = [
        parsed.get('latency', 0.0),
        parsed.get('throughput', 0.0),
        parsed.get('error_rate', 0.0),
        parsed.get('jitter', 0.0),
        parsed.get('bandwidth', 0.0)
    ]
    return [round(m, 2) for m in metrics]

# Core logic buried among decoys
def compute_aggregate(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    total_weight = sum(weights)
    
    # Distractor: irrelevant normalization chain
    temp_data = [m ** 2 for m in metrics if m > 0.5]
    temp_avg = sum(temp_data) / len(temp_data) if temp_data else 0.0
    adjusted_sum = weighted_sum + (temp_avg * 0.05)  # Misleading adjustment
    
    # Actual answer not affected by above
    return round(weighted_sum / total_weight, 6)

# Unused recursive distraction
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Simulated input data — contains red herrings
def main():
    raw_system_logs = [
        'LOG:STATUS:latency:0.88',
        'LOG:STATUS:throughput:0.92',
        'LOG:STATUS:error_rate:0.15',  # Note: low error rate is good
        'LOG:STATUS:jitter:0.76',
        'LOG:STATUS:bandwidth:0.81',
        'DEBUG:STATUS:cache_hit:0.94',  # irrelevant
        'INFO:STATUS:temperature:45C'   # invalid format
    ]

    # Irrelevant preprocessing
    diagnostics = generate_diagnostics()
    masked_diagnostics = entropy_mask(diagnostics)
    normalized_diagnostics = legacy_normalize(diagnostics)

    # Real data flow
    metrics = extract_key_metrics(raw_system_logs)
    
    # Weights for scoring — critical
    weights = [3, 4, 5, 2, 3]  # error_rate has highest weight (inverted later)

    # Invert error rate since lower is better
    if len(metrics) >= 3:
        metrics[2] = 1.0 - metrics[2]  # Now 0.85

    # Final computation
    final_score = compute_aggregate(metrics, weights)
    
    # Dead code branch — looks like it might affect result
    if final_score > 1.0:
        final_score = 0.99
    
    # Additional decoy: sorting unrelated data
    fake_ranks = [0.91, 0.85, 0.77, 0.93, 0.88]
    sorted_ranks = sorted(fake_ranks, reverse=True)
    rank_pairs = list(itertools.combinations(sorted_ranks, 2))
    
    # Print required output
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()