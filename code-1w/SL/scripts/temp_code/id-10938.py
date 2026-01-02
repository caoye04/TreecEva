import itertools

# Simulated sensor data processing with performance scoring
def collect_metrics(raw_data):
    readings = [x for x in raw_data if x > 0]
    filtered = readings[1::2]  # Every second reading
    normalized = [round(x / max(readings), 3) for x in filtered]
    return normalized

def apply_correction(values, factor=1.05):
    # Irrelevant correction function (not used in final path)
    return [v * factor for v in values]

def transform_sequence(seq):
    # Bit manipulation red herring
    transformed = []
    for i, val in enumerate(seq):
        bit_shifted = (int(val * 100) << 2) ^ 0xA
        transformed.append(bit_shifted)
    return transformed

def compute_baseline(data):
    # Dead code path — never actually used
    total = 0
    for d in data:
        total += d ** 0.5
    return total / len(data) if data else 0

def extract_features(series):
    # Real feature extraction with distractors
    features = {}
    for idx, val in enumerate(series):
        if idx % 3 == 0:
            features[f'p_{idx}'] = val ** 2
    # Distractor: unused intermediate
    temp_sum = sum(features.values()) + 1000  
    return features

def calculate_entropy(seq):
    # Misleading complex math
    from math import log2
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(seq)
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def weight_adjustment(w_list):
    # Unused weight transformer
    return [w * 1.1 for w in w_list]

def evaluate_performance(met, wts):
    # Core logic buried in noise
    scores = []
    keys = sorted(met.keys())
    for k in keys:
        scores.append(met[k])
    
    # Actual computation
    weighted_sum = 0
    for i in range(len(scores)):
        weighted_sum += scores[i] * wts[i % len(wts)]
    
    # Decoy operations
    dummy = (weighted_sum * 2) ^ 0xFF
    temp_result = [weighted_sum + i for i in range(5)]
    
    # Final answer derivation
    adjustment = len(scores) * 0.25
    final = int(weighted_sum - adjustment)
    
    # Red herring: unused zip + enumerate combo
    for i, (a, b) in enumerate(zip(temp_result, reversed(temp_result))):
        dummy_op = a ^ int(b) & 0xF
    
    return final

# Main execution block
if __name__ == '__main__':
    raw_input_data = [120, -5, 230, 89, 0, 195, 67, 301, 44, 150]
    
    # Irrelevant preprocessing chain
    processed = collect_metrics(raw_input_data)
    corrected = apply_correction(processed, 1.1)
    features_dict = extract_features(processed)
    
    # Real metric generation
    metrics = {}
    for i, p in enumerate(processed):
        if p > 0.3:
            metrics[f'm_{i}'] = int(p * 100)
    
    # Transform but don't use
    ignored_transformation = transform_sequence(list(metrics.values()))
    
    # Weight setup
    weights = [0.8, 1.2, 0.9, 1.1]
    adjusted_weights = weight_adjustment(weights)  # Unused
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")