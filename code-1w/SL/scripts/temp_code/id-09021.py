from itertools import combinations

# Simulate evaluation of candidate solutions in a constrained search space
def evaluate_candidate(seq):
    if len(seq) == 0:
        return 0
    base = sum(seq)
    penalty = 0
    
    # Irrelevant distraction: counting even-odd transitions (not used in final score)
    transitions = 0
    for i in range(len(seq) - 1):
        if (seq[i] % 2) != (seq[i+1] % 2):
            transitions += 1  # unused
    
    # Semi-relevant: apply modular penalty based on sequence length
    if len(seq) > 3:
        penalty += len(seq) % 4
    else:
        penalty -= len(seq) // 2
    
    # Core logic: reward sequences where sum is divisible by length
    if len(seq) > 0 and base % len(seq) == 0:
        base *= 2
    
    return base - penalty

# Generate all possible 3-element subsequences from a controlled set
def generate_candidates(elements):
    valid_groups = []
    total_iter_calls = 0  # Distraction counter
    
    for k in range(2, 5):
        combs = list(combinations(elements, k))
        total_iter_calls += len(combs)  # Tracked but not used
        for c in combs:
            if sum(c) < 20:  # Constraint to limit search space
                valid_groups.append(c)
    
    return valid_groups

# Main computation
def compute_aggregate(data_set):
    candidates = generate_candidates(data_set)
    scores = []
    
    temp_debug_log = []  # Dead storage
    
    for cand in candidates:
        score = evaluate_candidate(cand)
        scores.append(score)
        temp_debug_log.append((cand, score))  # Collected but unused
    
    # Compute aggregate using trimmed mean logic
    sorted_scores = sorted(scores)
    trim_count = len(sorted_scores) // 4
    trimmed = sorted_scores[trim_count:-trim_count] if trim_count > 0 else sorted_scores
    
    # Final score calculation with rounding
    raw_mean = sum(trimmed) / len(trimmed) if trimmed else 0
    final_value = int(round(raw_mean + 0.5))  # Ensure deterministic integer
    
    # Unrelated intermediate: find max product of any two adjacent original values
    max_product = 0
    for i in range(len(data_set) - 1):
        product = data_set[i] * data_set[i+1]
        if product > max_product:
            max_product = product  # Not used in result
    
    return final_value

# Execution entry point
data_input = [2, 3, 5, 7, 11]
intermediate_analysis = [x**2 for x in data_input if x % 2 == 1]  # Distraction list
normalization_factor = sum(intermediate_analysis) / len(intermediate_analysis) if intermediate_analysis else 1

final_score = compute_aggregate(data_input)
print(f"Result: {final_score}")