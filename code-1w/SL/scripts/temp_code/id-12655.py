from collections import defaultdict, Counter
import math

def analyze_pattern(sequence):
    # Irrelevant function: analyzes character frequency but not used in final calculation
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return dict(freq)

def validate_checksum(values):
    # Dead-end validation function (not actually called)
    total = 0
    for i, v in enumerate(values):
        total += v * (i + 1)
    return total % 107

def transform_data(raw):
    # Misleading transformation with unused intermediate steps
    temp = [x ** 2 for x in raw if x > 0]
    filtered = [y for y in temp if y % 2 == 0]
    shifted = [z >> 1 for z in filtered]  # Bit manipulation red herring
    return shifted + [sum(temp) // len(temp)] if temp else [0]

def compute_entropy(vals):
    # Complex but irrelevant computation
    counts = Counter(vals)
    probs = [count / len(vals) for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def evaluate_thresholds(arr, limit=100):
    # Distractor logic path
    results = []
    for val in arr:
        if val < 10:
            results.append('LOW')
        elif val < limit:
            results.append('MID')
        else:
            results.append('HIGH')
    return results

def aggregate_features(dataset):
    # Unused aggregation with multiple layers
    feature_map = defaultdict(list)
    for key, group in dataset.items():
        feature_map['length'].append(len(group))
        feature_map['max_val'].append(max(group))
        feature_map['min_val'].append(min(group))
    return {k: sum(v) for k, v in feature_map.items()}

def process_metrics(data, config):
    # Core logic buried among distractions
    base = [x for x in data if isinstance(x, int) and x % 2 == 1]  # Only odd integers matter
    weighted_sum = 0
    for i, val in enumerate(base):
        factor = config.get(i % len(config), 1)
        weighted_sum += val * factor
    
    adjustment = len([c for c in config if c > 2])  # Count high-weight factors
    normalized = weighted_sum / (adjustment or 1)
    
    # Actual answer derived here
    outlier_check = [n for n in base if n > 50]
    penalty = len(outlier_check) * 10
    final_score = int(normalized - penalty)
    
    return final_score

# --- Main Execution with High Interference ---
if __name__ == '__main__':
    # Real input data
    raw_input = [15, -3, 42, 8, 77, 0, 91, 4, 33, 5]

    # Irrelevant preprocessing
    cleaned_data = [abs(x) for x in raw_input]
    sorted_data = sorted(cleaned_data, reverse=True)
    evens_only = [n for n in sorted_data if n % 2 == 0]

    # Multiple unused structures
    metadata_log = {
        'input_size': len(raw_input),
        'positive_count': len([x for x in raw_input if x > 0]),
        'negative_count': len([x for x in raw_input if x < 0]),
        'zero_count': len([x for x in raw_input if x == 0])
    }

    # Meaningless transformations
    bit_analysis = [bin(x).count('1') for x in cleaned_data]
    shift_results = [(x << 2) ^ 5 for x in evens_only]

    # Red herring data structure
    decoy_dataset = {
        'A': [10, 20, 30],
        'B': [15, 25],
        'C': [40, 50, 60, 70]
    }

    # Critical configuration (used in actual logic)
    weights = [3, 1, 4, 1, 5, 9, 2]  # Influences weighting in process_metrics

    # Key execution point — this call determines the answer
    final_score = process_metrics(raw_input, weights)

    # Print required output
    print(f"Result: {final_score}")