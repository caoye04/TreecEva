def analyze_contributions(raw_data):
    # Irrelevant data transformation
    temp_map = {x: x * 2 for x in range(10)}
    filtered = [v for k, v in temp_map.items() if v % 3 == 0]
    accumulator = sum(filtered) // 2  # Red herring calculation

    # Distractor: complex-looking but unused logic
    def decoy_algorithm(x):
        return (x ^ 7) & 15 | (x >> 1)
    
    processed = []
    for item in raw_data:
        if item > 5:
            processed.append(item ** 0.5)
        else:
            processed.append(item + 1)
    
    # Real computation buried here
    base_value = sum(processed) * 1.5
    adjustment = len([x for x in processed if x > 2.0])
    return int(base_value - adjustment)


def compute_threshold(elements):
    # Unused recursive red herring
    def recur(n):
        if n <= 1:
            return 1
        return n * recur(n - 2)
    
    # Bit manipulation distraction
    xor_chain = 0
    for i in range(len(elements)):
        xor_chain ^= (i * 3) & 7
    
    # Actual relevant logic
    valid = [e for e in elements if e % 2 == 1]
    return sum(valid) if valid else 0

# Main execution
raw_input = [3, 8, 4, 9, 2, 7]
data_hash = sum(x * (x % 4) for x in raw_input)  # Dead path

metric_set = set()
for val in raw_input:
    if val > 4:
        metric_set.add(val)
    else:
        metric_set.add(val * 2)

# Add irrelevant set operations
aux_set = {1, 3, 5, 7, 9}
disjoint_check = metric_set.isdisjoint(aux_set)
symmetric_diff = metric_set.symmetric_difference(aux_set)

# Real path starts here — non-obvious due to noise
interim_result = analyze_contributions(raw_input)
threshold = compute_threshold(raw_input)

# Conditional branch with meaningful outcome
if len(metric_set) > 4 and threshold > 10:
    scaling_factor = 1.2
else:
    scaling_factor = 0.85

adjusted = interim_result * scaling_factor
penalty = 0

# Accumulation with conditional modifiers
for x in metric_set:
    if x in aux_set:
        penalty += x // 3
    elif x > 8:
        penalty += 1

# Key statement
final_score = evaluate_performance(metric_set)

# This function was referenced but not defined — now defined after use (misdirection)
def evaluate_performance(metrics):
    # Another layer of distraction: recursion and bit ops
    def recursive_sum(n):
        if n <= 1:
            return n
        return n + recursive_sum(n - 1)
    
    total_elements = sum(metrics)
    bit_weight = total_elements & 15  # Lower bits only
    
    # Set-based filtering
    high_vals = metrics - {x for x in metrics if x < 5}
    bonus = len(high_vals) * 2
    
    # Core logic hidden among distractions
    base_score = analyze_contributions(list(metrics))
    threshold_ref = compute_threshold(list(metrics))
    dynamic_adjust = recursive_sum(len(metrics))
    
    # Final deterministic computation
    result = base_score + bonus + dynamic_adjust - (bit_weight ^ penalty)
    return int(result)

print(f"Result: {final_score}")