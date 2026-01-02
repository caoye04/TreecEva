import itertools

# Simulated sensor data processing pipeline with diagnostic checks
def collect_samples():
    raw_data = [i * 0.7 for i in range(30)]
    offset_correction = sum([x % 2 for x in range(15)])  # red herring: not used later
    filtered = [x for x in raw_data if x > 5.0]
    return filtered

# Irrelevant transformation chain (dead path)
def legacy_normalize(data):
    if not data:
        return []
    max_val = max(data)
    return [x / max_val * 100 for x in data]  # unused function

# Real preprocessing with distractor variables
def preprocess(signal):
    window_size = 4
    segments = [signal[i:i+window_size] for i in range(0, len(signal), window_size)]
    
    # Distractor: complex but unused computation
    entropy_proxy = 0
    for seg in segments:
        if len(seg) == window_size:
            variance_like = sum((x - sum(seg)/len(seg))**2 for x in seg)
            entropy_proxy += variance_like ** 0.5
    entropy_proxy = round(entropy_proxy, 2)
    
    # Actual relevant transformation
    averaged = [sum(segment)/len(segment) for segment in segments if segment]
    scaled = [x * 1.85 for x in averaged]  # key scaling factor
    return scaled

# Signal feature extraction with misleading intermediate metrics
def extract_features(data):
    features = {}
    
    # Real feature
    features['peak'] = max(data) if data else 0
    
    # Distractor features (not used)
    features['smoothness'] = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    features['trend'] = (data[-1] - data[0]) / len(data) if data else 0
    features['noise_estimate'] = sum(x % 0.5 for x in data)  # irrelevant
    
    # Key derived value
    features['adjusted_peak'] = features['peak'] * 0.92
    return features

# Main analysis with conditional bypass and decoy logic
def analyze_signal(samples):
    if len(samples) == 0:
        return -999
    
    # Decoy control flow (never triggers in this case)
    special_flags = set()
    if any(x < 0 for x in samples):
        special_flags.add('NEGATIVE_DETECTED')
    if len(samples) > 100:
        special_flags.add('OVERFLOW')
    
    # Real logic path
    stats = {"mean": sum(samples)/len(samples)}
    features = extract_features(samples)
    
    # Complex but irrelevant set operation
    all_combinations = list(itertools.combinations([1,2,3], 2))
    combination_sum = sum(a + b for a, b in all_combinations)  # distractor
    
    # Critical calculation chain
    base = features['adjusted_peak']
    adjustment_factor = 1.0 + (stats["mean"] * 0.01)
    intermediate = base * adjustment_factor
    
    # Final mapping using integer logic
    bucket = int(intermediate // 10)
    lookup = {0: 50, 1: 73, 2: 91, 3: 107, 4: 124, 5: 143}
    mapped_value = lookup.get(bucket, 160)
    
    # Final adjustment
    final_score = mapped_value + int(stats["mean"])
    
    # THE KEY STATEMENT
    final_diagnostic = final_score * 2  # <-- Target execution point
    
    # Dead code path with misleading print
    if False:
        debug_dump = {"raw": samples, "intermediate": intermediate}
        print(f'Debug: {debug_dump}')
    
    return final_diagnostic

# Orchestration with unused components
def main_pipeline():
    raw_samples = collect_samples()                     # [5.6, 6.3, 7.0, ... , 20.3]
    processed_samples = preprocess(raw_samples)          # length 6, values ~[8.5, 11.8, ...]
    
    # Unused alternative branch
    if len(raw_samples) % 2 == 0:
        alt_path = [x * 0.9 for x in raw_samples]
        alt_path = legacy_normalize(alt_path)  # calls dead function
    
    # Execution of critical statement
    final_diagnostic = analyze_signal(processed_samples)
    
    # Additional noise
    audit_log = set()
    audit_log.add('STAGE1_COMPLETE')
    audit_trail = [f"Log_{i}" for i in range(len(audit_log))]  # unused
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
main_pipeline()