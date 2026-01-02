def analyze_convergence(values, threshold=0.001):
    """Irrelevant helper function that analyzes convergence but is not used in critical path."""
    steps = []
    for i, v in enumerate(values):
        if abs(v - threshold) < threshold:
            steps.append(i)
    return steps

# Irrelevant data structures (distractors)
decoys = {f'dummy_{i}': i * 1.5 for i in range(10)}
metadata_log = [(t, t**2 % 7) for t in range(5)]

# Real input data
event_sequence = [18, 2, 9, 1, 7, 3]
filter_mask = list(map(lambda x: x > 5, event_sequence))  # Boolean mask

# Misleading transformation chain (dead end)
intermediate_result = sum(x for x in event_sequence if x % 2 == 0)
shadow_copy = [x * 2 for x in event_sequence]

# Core relevant logic buried among noise
baseline = {1, 3, 7, 18}
optimization_trace = set()
for idx, val in enumerate(event_sequence):
    if filter_mask[idx]:
        optimization_trace.add(val)

# Decoy accumulation (looks important but unused)
cumulative = 0
for x in shadow_copy:
    cumulative += x ^ 5

# Conditional expression with red herring variables
temp_offset = len(metadata_log) if len(decoys) > 12 else 0

# Real computation starts here (well-hidden)
def compute_stability(indices, ref_set):
    score = 0
    for i in indices:
        if i in ref_set:
            score += i * 11
        else:
            score -= 3
    return score

# Another decoy function
def generate_synthetic_data(n):
    return [i ^ (i << 1) for i in range(n)]

# Critical data transformation using zip and enumerate (required python features)
paired_analysis = []
for i, (a, b) in enumerate(zip(event_sequence, filter_mask)):
    if b:
        paired_analysis.append((i, a))

# Bitwise distraction
bit_fiddling = 0
for x in [1, 2, 4, 8]:
    bit_fiddling |= x << 2

# Real processing function (obscured by noise)
def process_metrics(trace, base):
    # Set difference looks important but only intersection matters
    irrelevant_diff = base - trace
    core_elements = trace & base  # Only this matters
    
    # Use of lambda in non-trivial context (required feature)
    transform = lambda x: (x ** 2) + 5
    adjusted = [transform(x) for x in core_elements]
    
    # Accumulation with conditional logic
    total = 0
    for val in adjusted:
        if val > 20:
            total += val // 3
        else:
            total += val
    
    # Final adjustment using enumeration (required feature)
    for j, _ in enumerate(adjusted):
        if j % 2 == 1:
            total -= j * 2
    
    return total + len(core_elements)

# Dead code path - never executed but looks plausible
if __name__ == "__main__":
    debug_mode = False
    if debug_mode:
        print("Debug:", analyze_convergence([0.1, 0.01, 0.0005]))

# Key execution point buried in distractions
final_score = process_metrics(optimization_trace, baseline)

# Output result as required
print(f"Result: {final_score}")