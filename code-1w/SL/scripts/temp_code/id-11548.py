from itertools import combinations, cycle

# Sensor array diagnostic simulation with noise filtering and pattern validation

def analyze_sensor_pair(pair):
    a, b = pair
    if a == 0 or b == 0:
        return 0
    ratio = max(a, b) / min(a, b)
    if ratio > 2.5:
        return -1  # Invalid due to instability
    return (a + b) * 0.75

def generate_reference_sequence(length, key_seed=3):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[-1] + seq[-2])  # Fibonacci-like reference
    return [x % 7 for x in seq]  # Normalize to small range

def validate_pattern_consistency(data):
    counts = {i: data.count(i) for i in set(data)}
    modes = [k for k, v in counts.items() if v == max(counts.values())]
    return modes[0] if len(modes) == 1 else 6

# Raw sensor inputs (simulated)
sensor_inputs = [5, 0, 3, 4, 2, 8, 4, 0, 7, 1, 9, 4, 2, 6, 3]

# Irrelevant transformation: character mapping (distractor)
char_map = {i: chr(65 + (i * 3) % 26) for i in range(10)}
encoded_chars = [char_map.get(x % 10, 'X') for x in sensor_inputs]

def apply_noise_floor(values, floor=1):
    # Misleading function: looks important but not used in critical path
    return [max(floor, v) for v in values]

def simulate_failure_modes(data):
    # Dead code path — never called
    return [x * -1 for x in data if x % 3 == 0]

# Core processing pipeline
base_threshold = 3
filtered_data = [x for x in sensor_inputs if x != 0]  # Remove failed sensors

# Generate all valid pairs for cross-validation
valid_pairs = list(combinations([x for x in filtered_data if x >= base_threshold], 2))
pair_results = [analyze_sensor_pair(p) for p in valid_pairs]

clean_results = [r for r in pair_results if r > 0]  # Exclude invalid readings

# Decoy aggregation using itertools.cycle (misleading usage)
steady_cycle = cycle([1, 0, -1])
decoys = [next(steady_cycle) * x for x in clean_results[:5]]

def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    from math import log2
    return round(-sum(p * log2(p) for p in probs if p > 0), 6)

entropy_metric = calculate_entropy(clean_results) if clean_results else 0.0

# Reference sequence alignment check (distractor logic)
ref_seq = generate_reference_sequence(len(filtered_data))
alignment_score = sum(1 for a, b in zip(filtered_data, ref_seq) if a % 3 == b % 3)

# Secondary filter based on parity clustering (irrelevant)
parity_groups = {
    'even': [x for x in filtered_data if x % 2 == 0],
    'odd': [x for x in filtered_data if x % 2 == 1]
}

even_concentration = len(parity_groups['even']) / len(filtered_data)

# Real signal: aggregate clean pair results with offset
aggregate_signal = sum(clean_results) + len(valid_pairs) - alignment_score

# Final diagnostic computation (key statement)
final_diagnostic = int(aggregate_signal // 1.5)

# Extraneous output logs (distractors)
log_entry = f"DIAG:{hex(final_diagnostic)}:ENT:{entropy_metric:.4f}"
extra_analysis = [x ^ 7 for x in filtered_data]  # Bitwise red herring

# Output target result
print(f"Result: {final_diagnostic}")