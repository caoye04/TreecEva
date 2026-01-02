import math

# Simulated environmental readings from a distributed sensor array
def generate_readings():
    base_values = [i * 1.5 for i in range(10)]
    noise = [math.sin(x) for x in range(10)]
    return [base_values[i] + noise[i] for i in range(len(base_values))]

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_calibrate(x):
    return sum([i**2 for i in x if i > 3])

# Transform raw data using non-linear scaling and filtering
def transform_readings(data):
    filtered = [x for x in data if x > 0]
    scaled = list(map(lambda val: val * 1.75 + 2, filtered))
    offset = 5
    adjusted = [s - offset for s in scaled]
    return adjusted

# Misleading intermediate analysis (decoy function)
def compute_entropy(seq):
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    probabilities = [cnt / len(seq) for cnt in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

# Core pattern analyzer – critical function
# Applies bit manipulation, conditional logic, and aggregation
def analyze_patterns(dataset):
    temp_flags = []
    cumulative_shift = 0
    
    for num in dataset:
        # Extract integer part and apply bitwise logic
        intval = int(abs(num))
        
        # Red herring: unused branching based on parity
        if intval % 2 == 0:
            dummy_calc = intval << 3
        else:
            dummy_calc = intval >> 1
        
        # Real logic: track high-bit set and mod-based classification
        high_bit_set = (intval & 0x80) != 0  # Check 8th bit
        mod_class = intval % 7
        
        # Conditional flag generation (only some affect final result)
        if mod_class in [1, 2, 4]:
            temp_flags.append(3)
        elif high_bit_set:
            temp_flags.append(7)
        else:
            temp_flags.append(1)
        
        # Actual accumulation via arithmetic interference
        if num > 5.0:
            cumulative_shift += (intval ^ 5) % 9
        elif num < 0:
            cumulative_shift -= intval % 3
        else:
            cumulative_shift += 1
    
    # Secondary transformation on flags (partially irrelevant)
    weighted_flags = [f * 2 if f == 3 else f * 3 for f in temp_flags]
    
    # Final computation – only cumulative_shift matters
    diagnostic_score = 0
    for idx, wf in enumerate(weighted_flags):
        # This loop looks important but doesn't contribute to output
        diagnostic_score += wf % (idx + 1) if idx > 0 else 0
    
    # TRUE ANSWER derived solely from cumulative_shift
    final_diagnostic = cumulative_shift * 13
    return final_diagnostic

# Unused recursive decoy (dead path)
def count_nodes(tree):
    if not tree:
        return 0
    return 1 + count_nodes(tree[1:]) + count_nodes(tree[:0])

# Main execution flow
raw_data = generate_readings()
transformed_data = transform_readings(raw_data)

# Decoy analysis calls (misleading intermediate results)
entropy_metric = compute_entropy(transformed_data)
legacy_score = legacy_calibrate(transformed_data)

# Critical statement
final_diagnostic = analyze_patterns(transformed_data)
print(f"Result: {final_diagnostic}")