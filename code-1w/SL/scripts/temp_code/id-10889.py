import itertools

def generate_sequence(n):
    """Generate a Fibonacci-like sequence with custom rules."""
    seq = [1, 1]
    for i in range(2, n):
        next_val = seq[i-1] + seq[i-2] + (i % 3)
        seq.append(next_val)
    return seq

def filter_outliers(data, threshold=50):
    """Remove values above threshold (distraction: not actually used in final path)."""
    return [x for x in data if x <= threshold]

def transform_values(data):
    """Apply non-linear transformation to data."""
    transformed = []
    for x in data:
        if x % 2 == 0:
            transformed.append(x ** 2 // 3)
        else:
            transformed.append(x * 2 + 1)
    return transformed

def compute_entropy(data):
    """Calculate entropy-like metric for distraction."""
    total = sum(data)
    probs = [d / total for d in data]
    from math import log2
    return -sum(p * log2(p) for p in probs)

def extract_cycles(data):
    """Find repeating subpatterns (unused red herring function)."""
    cycles = []
    for i in range(1, len(data)//2 + 1):
        chunk = data[:i]
        repeated = (data[i:i+i] == chunk)
        if repeated:
            cycles.append(len(chunk))
    return cycles or [0]

def analyze_pattern(seq):
    """Core analysis: sum every third element then modulate."""
    # Key logic: sum every third element starting at index 0
    key_elements = [seq[i] for i in range(0, len(seq), 3)]
    base_sum = sum(key_elements)
    
    # Additional transformation
    adjusted = base_sum * 2 - len(seq)
    
    # Introduce bit manipulation red herring
    decoy_mask = 0b110101
    masked = adjusted ^ decoy_mask  # irrelevant operation
    
    # Real computation continues independently
    multiplier = len([x for x in seq if x > 5])
    final_score = adjusted + (multiplier * 3)
    
    # More distractions
    temp_result = compute_entropy(seq) * 100
    dummy_cycle = extract_cycles(seq)
    
    # Final step
    final_diagnostic = final_score + (masked & 0)  # neutralize decoy
    return final_score  # note: final_diagnostic = final_score due to & 0

# Irrelevant setup variables (distractors)
data_source = [2, 4, 6, 8, 10]
baseline_offset = 999
legacy_flag = True

# Generate real working data
raw_sequence = generate_sequence(12)
filtered_data = filter_outliers(raw_sequence, 75)
transformed_data = transform_values(filtered_data)

# Unused complex structure (dead path)
permutation_pool = list(itertools.permutations([1, 2, 3], 3))
combination_stats = [sum(combo) for combo in itertools.combinations_with_replacement((2,4), 3)]

# Critical execution point
temp_shadow = [x for x in transformed_data if x % 4 == 0]
interim_mask = 0xFF
final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")