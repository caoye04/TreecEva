from collections import defaultdict, Counter
import math

def analyze_peaks(values):
    # Irrelevant function: analyzes peaks but not used in final computation
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(i)
    return len(peaks)

def dummy_transform(seq):
    # Dead code path: never called
    return [x ** 0.5 for x in seq if x > 0]

def validate_range(seq, low, high):
    # Distractor function: checks bounds but doesn't affect output
    return all(low <= x <= high for x in seq)

def compute_entropy(weights):
    # Misleading intermediate: looks important but unused
    total = sum(weights)
    probs = [w / total for w in weights]
    return -sum(p * math.log(p) for p in probs if p > 0)

def extract_features(data, config):
    # Complex distractor with nested logic and red herrings
    feature_set = defaultdict(float)
    temp_buffer = []
    
    for idx, (k, v) in enumerate(zip(config.keys(), data)):
        if k == 'amplitude':
            feature_set['rms'] += v ** 2
        elif k == 'frequency' and v > 50:
            temp_buffer.append(v % 7)
        else:
            feature_set['baseline'] += v / (idx + 1)
    
    feature_set['rms'] = math.sqrt(feature_set['rms'])
    feature_set['buffer_sum'] = sum(temp_buffer) * 0.1  # Unused downstream
    
    # Decoy transformation
    decoy = [math.sin(x) for x in range(len(temp_buffer))]
    return feature_set

def process_metrics(data, weights):
    # Core logic embedded within distractions
    adjusted = []
    for i, val in enumerate(data):
        adjustment = 1.0
        if i % 2 == 0:
            adjustment = weights[i % len(weights)] + 0.5
        else:
            adjustment = weights[(i + 1) % len(weights)] - 0.2
        adjusted.append(val * adjustment)
    
    # Real computation path begins here
    magnitude = sum(abs(x) for x in adjusted)
    
    # Bit manipulation red herring
    bit_flag = 0
    for x in adjusted:
        if x > 0:
            bit_flag |= 1 << min(int(math.log(abs(x) + 1, 2)), 10)
    
    # Actual critical calculation
    base_score = 0
    for j, adj_val in enumerate(adjusted):
        if j < len(weights):
            weight_idx = j % len(weights)
            contribution = adj_val * weights[weight_idx]
            if contribution > 0:
                base_score += math.floor(contribution)
            else:
                base_score -= abs(int(contribution)) // 2
    
    # Final non-linear transformation
    scaling_factor = len([x for x in adjusted if x > 0]) or 1
    normalized = base_score / scaling_factor
    
    # Critical statement
    final_score = int(normalized + 17.9) - 3
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input setup
    raw_data = [4, -8, 6, 3, -2, 9, 5]
    weights = [0.7, 1.3, 0.9, 1.1]
    config_map = {'amplitude': 0, 'phase': 1, 'frequency': 2, 'offset': 3}
    
    # Irrelevant preprocessing
    filtered_data = [x for x in raw_data if x != -999]
    shifted = [(x + 5) % 10 for x in raw_data]
    
    # Call to decoy analysis
    peak_count = analyze_peaks(shifted)
    valid = validate_range(raw_data, -10, 10)
    entropy = compute_entropy(weights)  # Computed but unused
    
    # Real feature extraction (partially relevant)
    features = extract_features(raw_data, config_map)
    
    # Key assignment - target of question
    final_score = process_metrics(raw_data, weights)
    
    # Output result
    print(f"Result: {final_score}")