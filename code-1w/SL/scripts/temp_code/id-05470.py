import math

# Simulated sensor array diagnostics with heavy distractions
def collect_signals():
    raw_signals = [0.88, -1.22, 3.14, 2.71, 1.41]
    offset = 0.5
    normalized = [(sig + offset) * 0.9 for sig in raw_signals]
    return normalized

# Irrelevant signal smoothing (dead path)
def smooth(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(data[-1])
    return smoothed

# Decoy transformation chain
def corrupt_signal(x):
    return (x ** 2) - (x // 0.5) if x > 0 else x * -1

# Real preprocessing step
def transform_signals(signals):
    processed = []
    for s in signals:
        if s > 1.0:
            processed.append(math.log(s) * 2)
        elif s < 0:
            processed.append(abs(s) ** 0.5)
        else:
            processed.append(s + 1)
    return [round(p, 3) for p in processed]

# Red herring: false diagnostic routine
def assess_stability(metrics):
    if not metrics:
        return False
    variance = sum([(m - sum(metrics)/len(metrics))**2 for m in metrics]) / len(metrics)
    return variance < 0.25

# Auxiliary function: computes checksum (irrelevant to final result)
def compute_checksum(arr):
    total = 0
    for val in arr:
        shifted = int(val * 100) % 7
        total ^= shifted
    return total

# Real processing pipeline
def analyze_pattern(seq):
    pattern_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            pattern_score += 1.5
        elif seq[i] == seq[i-1]:
            pattern_score += 0.5
        else:
            pattern_score -= 0.3
    return round(pattern_score, 2)

# Core logic disguised among distractors
def evaluate_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x) / len(data)
    return round(entropy, 4)

# Higher-order transformation using lambda and set operations
def apply_filters(dataset, mode='strict'):
    filter_func = lambda x: x > 0.5
    base_set = set([round(d, 1) for d in dataset])
    filtered_set = {x for x in base_set if filter_func(x)}
    return list(filtered_set)

# Main processing function with multiple concepts
config = {
    'threshold': 0.75,
    'mode': 'aggressive',
    'version': '3.1'
}

# Simulate corrupted intermediate results
dummy_cache = {'status': 'invalid', 'data': [corrupt_signal(x) for x in [-2, -1, 0, 1, 2]]}

# Unused recursive red herring
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 2)

# Actual entry point
raw_data = collect_signals()
transformed_data = transform_signals(raw_data)

# Distractor: fake analysis branches
stability = assess_stability(transformed_data)
checksum = compute_checksum(transformed_data)
pattern_index = analyze_pattern(transformed_data)

# Real but obscured computation path
def process_metrics(data, cfg):
    # Apply filtering (uses lambda and comprehension)
    cleaned = apply_filters(data)
    
    # Compute primary metric
    entropy_value = evaluate_entropy(cleaned)
    
    # Secondary derived metric
    magnitude = sum([x**2 for x in cleaned]) ** 0.5
    
    # Tertiary logic: conditional adjustment
    adjustment = 1.75 if len(cleaned) >= 3 else 1.2
    
    # Key calculation
    diagnostic_base = entropy_value * magnitude * adjustment
    
    # Final non-linear scaling
    final_score = int(diagnostic_base * 100) / 100.0  # Truncate to 2 decimals
    
    # Dead code: misleading rounding alternatives
    # precise = round(diagnostic_base, 3)
    # legacy = math.floor(diagnostic_base * 10) / 10.0
    
    return final_score

# Critical execution point
final_diagnostic = process_metrics(transformed_data, config)

# Output result as required
print(f"Target result: {final_diagnostic}")