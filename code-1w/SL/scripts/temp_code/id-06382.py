import itertools

# Simulated sensor data processing with red herrings and complex flow
def fetch_raw_readings():
    return [0.7, 1.2, 0.4, 2.5, 1.8, 3.0, 2.1, 1.6]

def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0:
            filtered.append(data[i])
        else:
            filtered.append((data[i] + data[i-1]) / 2)
    return filtered

def compute_entropy(signal):
    total = sum(signal)
    probs = [s / total for s in signal]
    entropy = -sum(p * __import__('math').log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def generate_combinations(seq):
    # Irrelevant distractor: unused combinatorial explosion
    combs = []
    for r in range(1, len(seq)+1):
        combs.extend(itertools.combinations(seq, r))
    return combs  # Never used

def validate_checksum(structure):
    # Fake validation logic with misleading intermediate values
    checksum = 0
    for item in structure:
        if isinstance(item, (int, float)):
            checksum += int(item * 10) % 7
    return checksum % 3 == 0

def extract_features(signal):
    peaks = [i for i in range(1, len(signal)-1) if signal[i] > signal[i-1] and signal[i] > signal[i+1]]
    troughs = [i for i in range(1, len(signal)-1) if signal[i] < signal[i-1] and signal[i] < signal[i+1]]
    return {
        'peak_count': len(peaks),
        'trough_count': len(troughs),
        'amplitude_ratio': sum(signal) / (len(peaks) or 1),
        'variance_proxy': sum((x - sum(signal)/len(signal))**2 for x in signal) / len(signal)
    }

def transform_signal(signal, mode='advanced'):
    if mode == 'basic':
        return signal[::2]
    elif mode == 'advanced':
        # Real transformation: reverse and scale every third element
        result = signal[::-1]
        for i in range(2, len(result), 3):
            result[i] *= 1.5
        return result
    else:
        return [round(x, 1) for x in signal]

def analyze_pattern(data, config):
    # Core logic hidden among distractions
    feature_set = extract_features(data)
    
    # Distractor block: complex but unused logic
    shadow_analysis = {}
    for key, val in feature_set.items():
        shadow_analysis[f'sh_{key}'] = (val * 1.7) % 0.99
    
    # Another red herring: recursive decoy
    def explore_branch(depth, acc):
        if depth <= 0:
            return acc
        return explore_branch(depth - 1, acc * 0.9 + 0.1)
    
    _ = explore_branch(5, feature_set['peak_count'])
    
    # Actual answer derivation path
    base_score = feature_set['amplitude_ratio']
    adjustment = 0
    if feature_set['peak_count'] >= 2:
        adjustment += 0.8
    if feature_set['trough_count'] >= 1:
        adjustment -= 0.3
    
    entropy_marker = compute_entropy(data[:4])  # Uses partial data
    adjustment += (entropy_marker * 0.1)
    
    final_value = base_score + adjustment
    return round(final_value, 6)

def main():
    # Entry point with multiple distractions
    raw = fetch_raw_readings()
    cleaned = apply_noise_filter(raw)
    
    # Unused alternate processing paths
    sparse_data = [x for i, x in enumerate(cleaned) if i % 3 == 0]
    paired_tuples = list(zip(sparse_data, [x*2 for x in sparse_data]))
    mapped_dict = {f'idx_{i}': v for i, v in enumerate(paired_tuples)}
    
    # Real data path
    transformed_data = transform_signal(cleaned, mode='advanced')
    
    # Configuration with irrelevant fields
    config = {
        'version': '2.1',
        'debug_mode': False,
        'threshold': 0.85,
        'window_size': 4,
        'padding': None,
        'features_enabled': ['f1', 'f3'],
        'normalization_factor': 1.0
    }
    
    # Dead code path - looks important but unused
    if validate_checksum(transformed_data):
        fallback = sum(x for x in transformed_data if x < 1.5)
    else:
        fallback = None
    
    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()