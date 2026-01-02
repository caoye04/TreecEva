import math

# Simulated sensor fusion system for environmental monitoring

def preprocess_sensor(data, offset=0.1):
    return [x + offset for x in data if x > 0.5]

# Irrelevant helper - decoy function (dead path)
def legacy_calibrate(x):
    return (x * 0.98) + 0.5

# Unused transformation chain
def transform_chain(values):
    temp_a = [v ** 0.5 for v in values]
    temp_b = [t * 2 for t in temp_a]
    return [math.sin(b) for b in temp_b]

# Real signal processing path
def extract_features(signal_list):
    features = {}
    for i, sig in enumerate(signal_list):
        if i % 2 == 0:
            features[f'even_{i}'] = round(sig * 1.05, 4)
        else:
            features[f'odd_{i}'] = round(sig * 0.97, 4)
    return features

# Red herring: complex but unused bit manipulation
def obfuscate_key(n):
    n ^= (n << 3)
    n &= 0xFFFFFFFF
    n ^= (n >> 7)
    return n ^ (n << 11)

# Signal combiner with dictionary operations
def combine_sources(src_a, src_b, weights=(0.6, 0.4)):
    combined = []
    for a, b in zip(src_a, src_b):
        combined.append(weights[0] * a + weights[1] * b)
    return combined

# Distractor: elaborate but unused recursive structure
def fibonacci_threshold(limit, acc=None):
    if acc is None:
        acc = [0, 1]
    next_val = acc[-1] + acc[-2]
    if next_val >= limit:
        return acc
    return fibonacci_threshold(limit, acc + [next_val])

# Core diagnostic logic (used)
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)

# Data validation decoy (never called)
def validate_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= int(val * 100) & 0xFF
    return checksum == 0xAA

# Real processing pipeline
raw_data_1 = [0.8, 0.3, 1.2, 0.9, 0.6]
raw_data_2 = [0.7, 0.4, 1.1, 1.0, 0.5]

# Apply preprocessing with filtering
filtered_1 = preprocess_sensor(raw_data_1, offset=0.05)
filtered_2 = preprocess_sensor(raw_data_2, offset=0.08)

# Combine using weighted fusion
fused_signal = combine_sources(filtered_1, filtered_2)

# Extract temporal-spatial features
def process_temporal(data_sequence):
    indexed = list(enumerate(data_sequence))
    shifted = [(i, val * (1 + i*0.02)) for i, val in indexed]
    return [s[1] for s in shifted]

processed_signals = process_temporal(fused_signal)

# Feature extraction with dictionary mapping
feature_map = extract_features(processed_signals)

# Decoy list comprehension with no effect
decoys = [math.tan(math.pi / (i+1)) for i in range(1, 6) if i % 2 == 0]

# Unused lambda stored in dict - red herring
decoy_ops = {
    'scale': lambda x: x * 1.5,
    'attenuate': lambda x: x * 0.7,
    'noop': lambda x: x
}

# Critical analysis function
def analyze_readings(readings):
    # Compute statistical dispersion
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    
    # Compute entropy as complexity measure
    entropy = compute_entropy([abs(r) + 0.1 for r in readings])
    
    # Apply domain-specific weighting
    metric_a = std_dev * 100
    metric_b = entropy * 50
    
    # Final diagnostic score
    final_score = metric_a + metric_b - (mean_val * 10)
    
    # Irrelevant intermediate assignment (distractor)
    temp_diagnostic = metric_a - metric_b + 200
    
    # Key result
    final_diagnostic = int(round(final_score))
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")