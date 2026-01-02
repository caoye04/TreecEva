from itertools import combinations

# Simulated system diagnostics with mixed metrics
def generate_diagnostics():
    base_metrics = [12, 8, 15, 3, 9]
    derived_flags = [x % 4 == 0 for x in base_metrics]
    checksum = sum(x * (i + 1) for i, x in enumerate(base_metrics)) % 17
    
    # Irrelevant transformation (distractor)
    transformed = [((x << 2) | 1) ^ 5 for x in base_metrics]
    anomaly_mask = [t > 20 for t in transformed]

    return {
        'raw': base_metrics,
        'flags': derived_flags,
        'checksum': checksum,
        'anomalies': anomaly_mask,
        'size': len(base_metrics)
    }

# Decoy function – looks important but unused in critical path
def compute_robustness(data):
    if len(data) < 5:
        return -1
    temp = 0
    for i in range(len(data)):
        temp += (data[i] ** 2) % 7
    return temp // 3

# Auxiliary validation (partially relevant, mostly distraction)
def validate_integrity(diag):
    raw = diag['raw']
    csum = diag['checksum']
    expected = sum(raw[i] * (i % 3 + 1) for i in range(len(raw))) % 13
    
    # Red herring: modifies a local copy only
    adjusted = [(x + csum) % 25 for x in raw]
    if sum(adjusted) % 11 != 0:
        return False
    return expected == csum

# Core logic obscured by surrounding noise
def analyze_pattern(seq):
    count = 0
    for a, b in combinations(seq, 2):  # using itertools
        if (a + b) % 5 == 0 and abs(a - b) > 2:
            count += 1
    return count * 2

# Main evaluation with conditional expression and distractors
def evaluate_performance(diag):
    raw_data = diag['raw']
    flag_count = sum(1 for f in diag['flags'] if f)
    pattern_value = analyze_pattern(raw_data)
    
    # Complex conditional expression (key step)
    base_score = pattern_value if flag_count > 0 else sum(raw_data) // len(raw_data)
    
    # Irrelevant block — dead code path due to fixed conditions
    extra_bonus = 0
    if len(raw_data) > 10:
        extra_bonus = compute_robustness(raw_data)
    elif diag['size'] == 7:
        extra_bonus = 15

    # Multiple distractions below
    decoy_calc = 0
    for i, val in enumerate(raw_data):
        decoy_calc += (val ^ i) * (val % 3)  # misleading intermediate

    # Critical but non-obvious assignment
    adjustment_factor = 3 if validate_integrity(diag) else -2
    
    # Final computation — only some components are meaningful
    final_score = base_score + adjustment_factor * flag_count + extra_bonus
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
diagnostics = generate_diagnostics()
final_score = evaluate_performance(diagnostics)