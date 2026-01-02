import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw = [0.1, 0.4, 0.2, 0.8, 0.9, 0.7, 0.3, 0.6]
    offset = 0.05
    calibrated = [x + offset for x in raw]
    return calibrated

# Irrelevant auxiliary function – dead path
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 4)

# Signal conditioning with red herring transformations
def filter_noise(signal):
    filtered = []
    noise_floor = 0.15
    suppression_factor = 0.85
    for val in signal:
        if val > noise_floor:
            adjusted = (val - noise_floor) * suppression_factor
            filtered.append(round(adjusted, 4))
        else:
            filtered.append(0.0)
    # Distractor: intermediate metric with no impact
    peak = max(filtered) if filtered else 0.0
    avg_power = sum(x**2 for x in filtered) / len(filtered) if filtered else 0
    return filtered

# Data chunking – string-based splitting as per requirement
def segment_data(stream):
    indices = []
    for i in range(0, len(stream), 2):
        segment = stream[i:i+2]
        segment_label = '-'.join(f'{v:.3f}' for v in segment)
        indices.append((i, len(segment_label)))  # Store index and metadata length
    return indices

# Decoy analysis using string methods – irrelevant to final result
def assess_fragment_health(tags):
    stats = {'valid': 0, 'long': 0}
    for idx, tag_len in tags:
        if tag_len > 10:
            stats['long'] += 1
        status_str = f"CHK_{idx}_{tag_len}"
        if status_str.endswith('0') or 'CHK' in status_str:
            stats['valid'] += 1
    return stats['valid']

# Core transformation – masked within distractions
def encode_features(values):
    encoded = 0
    multiplier = 1
    for i, v in enumerate(reversed(values)):
        if i % 2 == 0:
            encoded += int(v * 100) * multiplier
            multiplier *= -1  # Alternating sign effect
        else:
            encoded -= int(v * 10) * multiplier
    return abs(encoded)

# Critical computation chain – answer derived here
def analyze_signal(dataset):
    # Linear search for first non-zero element
    start_idx = 0
    while start_idx < len(dataset) and dataset[start_idx] == 0:
        start_idx += 1
    if start_idx == len(dataset):
        start_idx = -1
    
    # Simple combinatorics: count valid pairs
    count = 0
    n = len(dataset)
    for i in range(n):
        for j in range(i+1, n):
            if abs(dataset[i] - dataset[j]) < 0.25:
                count += 1
    
    # Key logic: base value from pair count
    base_score = count * 17
    
    # Secondary influence: position of first non-zero
    pos_factor = (start_idx + 1) * 5 if start_idx >= 0 else 0
    
    # Final computation – this is the actual answer
    final_value = base_score - pos_factor + 3
    return final_value

# Unused recursive decoy
def recursive_diagnostics(level, cache={}):
    if level <= 1:
        return 1
    if level not in cache:
        cache[level] = recursive_diagnostics(level-1) + recursive_diagnostics(level-2)
    return cache[level]

# Main execution flow with heavy interference
if __name__ == '__main__':
    samples = collect_samples()
    processed = filter_noise(samples)
    
    # Distractor block: string manipulation side-channel
    labels = segment_data(processed)
    health_check = assess_fragment_health(labels)
    
    # Another irrelevant transformation
    feature_code = encode_features(processed)
    
    # This call looks important but is unused
    entropy_metric = compute_entropy(processed)
    
    # Red herring: Fibonacci-like structure with no use
    diag_depth = recursive_diagnostics(6)
    
    # CRITICAL STATEMENT
    final_diagnostic = analyze_signal(processed)
    
    # Output required format
    print(f"Target result: {final_diagnostic}")