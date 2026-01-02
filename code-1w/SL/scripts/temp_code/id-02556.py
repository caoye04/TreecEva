import itertools

def analyze_signal(data, threshold=0.75):
    """Irrelevant signal processing function (dead code path)."""
    filtered = [x for x in data if abs(x) > threshold]
    return sum(filtered) / len(filtered) if filtered else 0

def transform_sequence(seq):
    """Unused transformation function (distractor)."""
    return [((x * 3) + 2) % 7 for x in seq]

def validate_checksum(buffer):
    """Misleading validation logic with no impact on result."""
    checksum = 0
    for b in buffer:
        checksum ^= b
    return checksum == 0xFF

def compute_entropy(values):
    """Red herring: computes entropy but not used in final logic."""
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 6)

def extract_features(raw_log):
    """Processes log into feature set; partially relevant but masked by noise."""
    lines = raw_log.strip().split('\n')
    features = []
    for line in lines:
        parts = line.split(',')
        if len(parts) < 4:
            continue
        try:
            # Only third field matters; others are distractions
            val = float(parts[2])
            if 'ERROR' in line.upper():
                val *= 0.5
            features.append(val)
        except ValueError:
            pass
    return features

def normalize_vector(vec):
    """Unused normalization utility."""
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [round(x / magnitude, 6) for x in vec] if magnitude else vec

def evaluate_performance(metrics, weights):
    """Core logic: computes weighted score using specific conditions."""
    base_score = 0
    adjustment_factor = 1.0

    # Key conditional branching with nesting depth 3
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i % 2 == 0:
            if metric > 80:
                if weight > 0.1:
                    base_score += metric * weight * 1.1
                else:
                    base_score += metric * weight
            elif metric > 50:
                base_score += metric * weight * 0.8
            else:
                base_score += metric * weight * 0.5
        else:
            temp_val = metric ** 0.5
            if temp_val > 9:
                base_score += 90 * weight
            elif temp_val > 7:
                base_score += 75 * weight
            else:
                base_score += 60 * weight

    # Secondary adjustment via string-based flag check
    config_flag = 'ENABLE_PRECISION_TUNE'
    flag_lower = config_flag.lower()
    if 'precision' in flag_lower and 'tune' in flag_lower:
        adjustment_factor = 1.05

    # Apply adjustment only if certain iterator condition met
    index_pairs = list(itertools.combinations(range(len(metrics)), 2))
    high_corr_count = 0
    for i, j in index_pairs:
        if abs(metrics[i] - metrics[j]) < 10 and metrics[i] > 70:
            high_corr_count += 1

    if high_corr_count >= 3:
        adjustment_factor *= 1.02

    # Final computation
    final_score = int(round(base_score * adjustment_factor))

    # Decoy output variables
    debug_trace = f'Score computed at {final_score}'
    audit_log = [f'Metric_{k}: {v}' for k, v in enumerate(metrics)]

    return final_score

# Simulated input data
raw_system_log = '''
STATUS,OK,88.5,MEMORY_HIGH
WARNING,DISK,76.2,TEMP_NORMAL
ERROR,CPU,92.1,IO_WAIT
INFO,NETWORK,81.7,BANDWIDTH_OK
'''

# Extract features (only this part feeds forward)
extracted_metrics = extract_features(raw_system_log)

# Irrelevant transformations
signal_data = [0.1, 0.8, 0.9, 0.2]
analyzed_noise = analyze_signal(signal_data)
transformed_seq = transform_sequence([1, 2, 3, 4])

# Benchmark weights (meaningful)
benchmark_weights = [0.25, 0.30, 0.20, 0.25]

# Dead data structure
checksum_buffer = [0xAA, 0xBB, 0xCC, 0xDD]
is_valid = validate_checksum(checksum_buffer)

# Compute entropy of metrics (red herring)
entropy_value = compute_entropy(extracted_metrics)

# Normalize irrelevant vector
irrelevant_vec = [3, 4, 0, 2]
normalized_result = normalize_vector(irrelevant_vec)

# Key execution point
final_score = evaluate_performance(extracted_metrics, benchmark_weights)

# Output result
print(f"Result: {final_score}")