from itertools import combinations
import math

def analyze_text(text):
    # Irrelevant text analysis function (dead end)
    words = text.split()
    word_lengths = [len(w) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths)
    return avg_length

def compute_hash(data):
    # Misleading hashing operation with no effect on result
    h = 0
    for item in data:
        h = (h * 31 + hash(str(item))) % 1000000
    return h

def transform_values(arr, factor=1.5):
    # Distractor transformation (not used in final logic)
    transformed = []
    for x in arr:
        if x % 2 == 0:
            transformed.append(int(x * factor))
        else:
            transformed.append(int(x // factor))
    return transformed

def filter_outliers(seq, threshold=2):
    # Dead code path: looks useful but not used
    mean_val = sum(seq) / len(seq)
    std_dev = (sum((x - mean_val) ** 2 for x in seq) / len(seq)) ** 0.5
    return [x for x in seq if abs(x - mean_val) <= threshold * std_dev]

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    base = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            base += metrics[i] * weights[i]
        else:
            base -= metrics[i] * 0.5
    
    # Apply non-linear adjustment using modular arithmetic
    adjusted = (base ** 2) % 97
    
    # Conditional branch that actually matters
    if adjusted > 50:
        adjusted = 100 - adjusted
    
    # Character counting distractor (used to mislead)
    label = "performance_v1"
    char_count = len(set(label))  # distinct chars: p,e,r,f,o,m,a,n,v,1 => 10
    
    # Set operation that seems important but isn't used
    expected_keys = {'cpu', 'mem', 'io', 'net'}
    received_keys = set(f'key_{c}' for c in 'abc') | {'key_d'}
    missing = expected_keys - {f'key_{c}' for c in 'abcdefgh'}
    
    # Real manipulation: uses string method and conditional logic
    flag_str = "success_condition_met"
    if 'cond' in flag_str and flag_str.endswith('met'):
        adjusted *= 2
    
    # Bitwise red herring
    mask = 0b101010
    masked = adjusted & mask  # unused
    
    # Final computation using itertools: only some combinations matter
    valid_pairs = 0
    for pair in combinations(metrics, 2):
        if (pair[0] + pair[1]) % 7 == 0:
            valid_pairs += 1
    
    # This early return is NOT triggered (misdirection)
    if valid_pairs > 20:
        return -999
    
    # Actual answer derivation
    scaling_factor = len([p for p in combinations(weights, 2) if p[0] != p[1]])  # C(6,2)=15
    final_value = int(adjusted + valid_pairs * 1.5 + scaling_factor)
    
    return final_value

# Main execution block
if __name__ == '__main__':
    # Initialize with realistic-looking data
    metrics = [85, 92, 78, 96, 88, 73]
    weights = [0.2, 0.15, 0.25, 0.1, 0.2, 0.1]

    # Irrelevant preprocessing steps
    normalized_metrics = [m / 100 for m in metrics]
    inverted_weights = [1 - w for w in weights]

    # Unused recursive structure
    def recursive_sum(n):
        if n <= 1:
            return n
        return n + recursive_sum(n - 2)

    # Call decoy functions
    _ = compute_hash(metrics + weights)
    _ = transform_values(metrics)
    _ = filter_outliers(metrics)

    # Key statement where answer is computed
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")