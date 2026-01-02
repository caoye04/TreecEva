def analyze_efficiency(data_map, threshold=0.75):
    efficiency_list = []
    for key, values in data_map.items():
        if len(values) == 0:
            continue
        avg_val = sum(values) / len(values)
        if avg_val > threshold:
            efficiency_list.append((key, avg_val))
    return efficiency_list


def transform_keys(str_list):
    # Irrelevant string transformation with distractors
    transformed = [s.upper().replace('X', '').strip() for s in str_list]
    filtered = [t for t in transformed if len(t) > 2]
    joined = ''.join(filtered)
    split_parts = joined.split('Y')
    cleaned = [part[:3] for part in split_parts if part.startswith('A')]
    return set(cleaned)  # Dead-end operation


def compute_entropy(num_list):
    from math import log
    total = sum(num_list)
    if total == 0:
        return 0.0
    probabilities = [n / total for n in num_list if n > 0]
    entropy = -sum(p * log(p) for p in probabilities)
    return round(entropy, 6)


def detect_patterns(seq):
    # Complex but irrelevant pattern detector
    patterns = {}
    for i in range(len(seq) - 2):
        triplet = tuple(seq[i:i+3])
        if triplet not in patterns:
            patterns[triplet] = 0
        patterns[triplet] += 1
    frequent = {k: v for k, v in patterns.items() if v >= 2}
    return len(frequent)  # Unused result

# Decoy data structures
historical_data = {
    'Q1': [0.6, 0.8, 0.7],
    'Q2': [0.9, 0.95, 0.85],
    'Q3': [],
    'Q4': [0.5, 0.4, 0.3]
}

auxiliary_tags = ['Xref', 'Xact', 'Ymain', 'Xopt', 'Ysub']

# Real input data (camouflaged among decoys)
metrics_log = {
    'latency': [120, 150, 130, 140],
    'throughput': [85, 90, 88, 92],
    'errors': [2, 1, 3, 0],
    'retries': [1, 0, 2, 1]
}

# Misleading computations
raw_entropy = compute_entropy([5, 3, 8, 2])
detected_triples = detect_patterns([1, 2, 3, 2, 3, 4, 1, 2, 3])
efficiency_results = analyze_efficiency(historical_data)

# String distractor chain
transformation_set = transform_keys(auxiliary_tags)

# Relevant logic buried within distractions
baseline_adjustment = 1.2
adjustment_factor = 0
for metric, values in metrics_log.items():
    mean_val = sum(values) / len(values)
    if metric == 'latency':
        adjustment_factor += mean_val * 0.01
    elif metric == 'throughput':
        adjustment_factor += mean_val * 0.02
    elif metric == 'errors':
        adjustment_factor -= mean_val * 0.1
    elif metric == 'retries':
        adjustment_factor -= mean_val * 0.05

# Core evaluation function with mixed operations
def evaluate_performance(log_data, factor):
    score_components = {}
    
    # Extract and normalize relevant metrics
    for name, readings in log_data.items():
        total = sum(readings)
        count = len(readings)
        average = total / count
        
        if name == 'latency':
            normalized = (150 - average) / 150  # Invert so lower latency = higher score
        elif name == 'throughput':
            normalized = average / 100
        else:
            normalized = max(0, 1 - average / 10)
            
        score_components[name] = round(normalized, 4)
    
    # Composite scoring with weighting
    base_score = (
        score_components['latency'] * 0.4 +
        score_components['throughput'] * 0.4 +
        score_components['errors'] * 0.1 +
        score_components['retries'] * 0.1
    )
    
    # Apply adjustment factor derived earlier
    adjusted_score = base_score * (1 + factor / 100)
    
    # Final transformation using bit manipulation (red herring level)
    temp_key = int(adjusted_score * 10000)
    masked = temp_key ^ 0b110101  # Bitwise XOR with arbitrary mask
    inverted = ~masked & 0xFFFF  # One's complement with masking
    final_decimal = inverted / 10000.0  # Convert back to decimal
    
    # BUT - correction: final_score should actually be adjusted_score, not final_decimal
    # The bitwise operations are a red herring
    final_score = adjusted_score  # Critical override
    
    return final_score

# Execute main logic
final_score = evaluate_performance(metrics_log, adjustment_factor)

print(f"Target result: {final_score}")