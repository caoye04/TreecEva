import itertools

def analyze_sequence(data):
    """Irrelevant function: analyzes sequence patterns (dead code path)"""
    if not data:
        return 0
    acc = 0
    for i in range(len(data)):
        acc += data[i] * (i + 1)
    return acc

def preprocess_signal(signal):
    """Distraction: signal processing that isn't used in final computation"""
    filtered = [x for x in signal if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]

def compute_entropy(values):
    """Misleading intermediate calculation - looks important but unused"""
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def transform_features(features):
    """Another decoy transformation with slicing and combinations"""
    chunks = [features[i:i+3] for i in range(0, len(features), 3)]
    transposed = list(itertools.zip_longest(*chunks, fillvalue=0))
    flattened = [item for sublist in transposed for item in sublist]
    return flattened[:len(features)]

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjusted = [m - base for m in metrics]
    squared_errors = [(val ** 2) for val in adjusted if val < 1.5]
    
    # Red herring: complex bit manipulation on irrelevant copy
    temp_data = [int(x * 10) & 0xFF for x in metrics]
    mask_result = sum([(t ^ 0xAA) & 0x0F for t in temp_data])  # unused
    
    # Real logic continues
    window_avg = sum(squared_errors[:3]) / len(squared_errors[:3]) if squared_errors else 0
    
    # Another distraction: recursive call with dead branch
    def integrate_feedback(score, level=0):
        if level > 5:
            return score * 0.8  # never reached
        return score
    
    preliminary = window_avg * 12.5
    correction_factor = len([x for x in metrics if x > base]) * 0.7
    
    # Actual answer derivation
    final_score = int(preliminary + correction_factor)
    
    # Fake post-processing
    noise_floor = [final_score >> i for i in range(3)]
    dummy_shift = (final_score << 2) | 0x55
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Irrelevant data structures
    raw_readings = [0.8, 1.3, 1.7, 0.6, 2.1, 0.9]
    processed = preprocess_signal([x * 100 for x in raw_readings])
    entropy = compute_entropy([int(x*10) for x in processed])
    
    # Distractor variables
    feature_set = [3.2, 1.8, 4.5, 2.7, 3.9]
    transformed = transform_features(feature_set)
    sequence_score = analyze_sequence([int(f*10) for f in transformed])
    
    # Relevant inputs hidden among noise
    metrics = [4.2, 3.8, 5.1, 4.0, 4.4]  # performance metrics
    baseline = 4.0
    
    # Critical statement
    final_score = evaluate_performance(metrics, baseline)
    
    # Print required output
    print(f"Result: {final_score}")