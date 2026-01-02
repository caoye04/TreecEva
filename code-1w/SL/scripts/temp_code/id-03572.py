import itertools

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return all(d == diffs[0] for d in diffs)

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Unused transformation path
def transform_data(arr):
    return [x ** 2 - x for x in arr if x % 2 == 0]

# Distractor: complex but unused bitwise analysis
def analyze_bitwise(nums):
    result = 0
    for n in nums:
        result ^= (n & (n << 1)) | (n >> 2)
    return result % 17

# Real logic starts here
def filter_valid_entries(records, threshold=5):
    valid = []
    for r in records:
        if sum(1 for x in r['values'] if x > 0) >= threshold:
            valid.append(r)
    return valid

def generate_baseline_profile(data_stream):
    window_size = 4
    moving_averages = [
        sum(data_stream[i:i+window_size]) / window_size
        for i in range(len(data_stream) - window_size + 1)
    ]
    # Only use first and last average for final logic
    return (moving_averages[0], moving_averages[-1])

def evaluate_performance(metrics, base):
    base_lower, base_upper = base
    adjusted = []
    for val in metrics:
        if val < base_lower:
            adjusted.append(val * 1.2)
        elif val > base_upper:
            adjusted.append(val * 0.85)
        else:
            adjusted.append(val * 1.05)
    
    # Key computation
    raw_total = sum(adjusted)
    penalty = 0
    
    # Check for arithmetic sequences in subsets
    for subset in itertools.combinations(adjusted, 3):
        if analyze_pattern(sorted(subset)):
            penalty += 5
    
    # Apply penalty only if more than two violations
    if penalty > 10:
        raw_total -= penalty
    
    # Final scaling based on set uniqueness
    unique_count = len(set(round(x, 0) for x in adjusted))
    diversity_factor = unique_count / len(adjusted)
    
    intermediate = raw_total * diversity_factor
    
    # Final adjustment using distractor variables
    decoy_value = compute_entropy([1,2,2,3,3,3,4,4,5])  # This is computed but not used directly
    dummy_shift = analyze_bitwise([7, 13, 19, 25])       # Also computed but irrelevant
    
    # Actual final formula
    final_score = int(intermediate - 42 + dummy_shift * 0)  # Neutralized
    return final_score

# Main execution
if __name__ == '__main__':
    # Input dataset
    entries = [
        {'id': 'A1', 'values': [3, 6, 8, 5, 7, 9]},
        {'id': 'B2', 'values': [2, 4, 1, 0, 3, 2]},
        {'id': 'C3', 'values': [5, 7, 9, 6, 8, 10]},
        {'id': 'D4', 'values': [1, 3, 2, 4, 1, 2]},
        {'id': 'E5', 'values': [4, 8, 12, 7, 11, 15]}
    ]

    # Step 1: Filter valid entries
    valid_entries = filter_valid_entries(entries, threshold=4)
    
    # Extract metric values
    metric_pool = []
    for entry in valid_entries:
        avg = sum(entry['values']) / len(entry['values'])
        metric_pool.append(avg)
    
    # Generate baseline from a separate stream
    sensor_stream = [5, 7, 6, 8, 5, 9, 11, 10]
    baseline = generate_baseline_profile(sensor_stream)
    
    # Evaluate performance
    final_score = evaluate_performance(metric_pool, baseline)
    
    # Print result
    print(f"Result: {final_score}")