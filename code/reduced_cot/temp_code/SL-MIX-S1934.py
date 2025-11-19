from itertools import combinations

def generate_test_patterns(base_pattern, depth):
    patterns = [base_pattern]
    for _ in range(depth):
        new_pattern = patterns[-1] ^ (patterns[-1] >> 1)
        patterns.append(new_pattern & 0xFFFF)  # Keep within 16 bits
    return patterns

def calculate_verification_metric(pattern_list):
    metrics = []
    for pattern in pattern_list:
        pop_count = bin(pattern).count('1')
        metrics.append(pop_count ^ (pattern & 0xF))
    return sorted(metrics)

# Initialize circuit parameters
initial_circuit_state = 0b1011001110001111
sequence_depth = 4

# Generate test patterns through XOR-based transformation
circuit_patterns = generate_test_patterns(initial_circuit_state, sequence_depth)

# Apply metric calculation and sort results
pattern_metrics = calculate_verification_metric(circuit_patterns)

# Create verification key using set operations and bitwise logic
unique_metrics = frozenset(pattern_metrics)
verification_components = [
    sum(unique_metrics) & 0xFF,
    (max(unique_metrics) << 2) ^ min(unique_metrics),
    len(unique_metrics) * 7
]

# Final verification key computation
verification_key = 0
for i, component in enumerate(verification_components):
    verification_key ^= (component << (i * 3))

print(f"Result: {verification_key}")