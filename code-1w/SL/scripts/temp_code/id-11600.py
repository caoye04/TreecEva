def normalize_values(data):
    max_val = max(data)
    min_val = min(data)
    return [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in data]

# Irrelevant helper function (dead code path)
def calculate_entropy(values):
    from math import log
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probabilities)

def apply_weighting(series, weights):
    return [s * w for s, w in zip(series, weights)]

def filter_outliers(data, threshold=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    low = q1 - threshold * iqr
    high = q3 + threshold * iqr
    return [x for x in data if low <= x <= high]

def decode_string(key):
    # Distractor: string manipulation with no real impact
    shifted = ''.join(chr((ord(c) - ord('a') + 2) % 26 + ord('a')) for c in key.lower() if c.isalpha())
    reversed_str = shifted[::-1]
    title_case = reversed_str.title()
    return title_case.replace('X', 'A')  # More red herring

def transform_metrics(raw_scores):
    # Normalize raw scores
    normalized = normalize_values(raw_scores)
    
    # Apply logarithmic scaling (only on subset - misleading!)
    scaled = [x if i % 2 == 0 else (x + 1) for i, x in enumerate(normalized)]
    
    # Simulate noise injection (but not actually used)
    noise = [0.01 * i for i in range(len(scaled))]
    noisy_data = [a + b for a, b in zip(scaled, noise)]  # Dead end
    
    # Actually use filtered version
    filtered = filter_outliers(scaled, threshold=2.0)
    return filtered if len(filtered) >= 3 else normalized  # Fallback logic

def evaluate_performance(metrics, weights):
    # Transform metrics (core step)
    processed = transform_metrics(metrics)
    
    # Dummy dictionary for logging (distractor)
    logs = {
        'input_length': len(metrics),
        'processed_length': len(processed),
        'timestamp': '2023-11-05',
        'version': '2.1-alpha',
        'checksum': hash(str(metrics)) % 10000
    }
    
    # Unused complex dict comprehension
    _ = {f"item_{i}": {'raw': m, 'adj': p} for i, (m, p) in enumerate(zip(metrics, processed[:len(metrics)]))}
    
    # Re-normalize after transformation?
    if len(processed) > 1:
        re_normalized = normalize_values(processed)
    else:
        re_normalized = processed
    
    # Now apply weights (must match length)
    min_len = min(len(re_normalized), len(weights))
    weighted = apply_weighting(re_normalized[:min_len], weights[:min_len])
    
    # Aggregate score
    base_score = sum(weighted)
    
    # Bonus logic based on string decode (fake dependency)
    magic_key = "cxefg"  # Looks important
    decoded = decode_string(magic_key)
    bonus_factor = 1.0
    if 'D' in decoded:  # Will never happen due to shift
        bonus_factor = 1.2
    
    # Hidden trap: decoded string is 'Egcig' -> no 'D'
    final_score = base_score * bonus_factor
    
    # Additional red herring: tuple unpacking with unused vars
    config = ('algorithm_x', 0.95, 'active', True, 42)
    method, threshold, status, enabled, _ = config
    
    # Final adjustment: only if enabled and valid length
    if enabled and len(weighted) >= 3:
        final_score += threshold  # Add 0.95
    
    return final_score

# Main execution
raw_metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Unused variables - distractions
baseline = [70, 75, 72, 78, 74]
covariance_matrix = [[1.0, 0.3], [0.3, 1.0]]
scaling_mode = 'dynamic'
temp_buffer = list(range(100))

# Key execution point
final_score = evaluate_performance(raw_metrics, weights)
print(f"Result: {final_score}")