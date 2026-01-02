from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == (i % 3):  # Irrelevant pattern check
            count += 1
    return count

def compute_entropy(data):
    # Dummy entropy calculation (not used in final result)
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = sum(-(f / len(data)) * log2(f / len(data)) for f in freq.values())
    return round(entropy, 4)

def evaluate_performance(log_entries, thresholds):
    valid_entries = [e for e in log_entries if e >= thresholds['min_valid']]
    
    # Distractor: complex but unused data transformation
    transformed = list(combinations(valid_entries, 2))
    pair_sums = [a + b for a, b in transformed if a != b]
    avg_pair = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    
    # Actual logic begins here
    base_score = sum(1 for v in valid_entries if v > thresholds['high_threshold'])
    penalty = 0
    
    # Conditional expression used
    adjustment = 5 if base_score > 3 else 2
    
    for idx, val in enumerate(valid_entries):
        if idx > 0 and val < valid_entries[idx - 1]:
            penalty += 1  # Penalty for non-monotonicity
    
    # Simulate state tracking across iterations
    running_total = 0
    for v in valid_entries:
        running_total += v * 0.1
        if running_total > thresholds['cap_limit']:
            running_total = thresholds['cap_limit']
            break
    
    # Final score depends only on base_score, adjustment, and penalty
    final_score = base_score + adjustment - penalty
    
    # Red herring variables
    debug_info = {'processed': len(valid_entries), 'penalty_applied': penalty}
    temp_result = compute_entropy([1, 2, 2, 3])  # Unused call
    
    return int(final_score)

# Main execution
log_data = [4, 7, 6, 8, 9, 5]
limits = {
    'min_valid': 5,
    'high_threshold': 6,
    'cap_limit': 3.0
}

# Trigger analysis (analyze_pattern is never called)
_ = [analyze_pattern([1, 0, 2, 1]) for _ in range(2)]

final_score = evaluate_performance(log_data, limits)
print(f"Result: {final_score}")