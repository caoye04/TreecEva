def preprocess_sequence(seq, offset=0):
    """Apply modular transformation and filter noise (distractor: not directly used in final result)"""
    processed = [(x * 3 + offset) % 17 for x in seq if x % 2 == 1]
    return [p for p in processed if p > 5]


def generate_reference_map(keys):
    """Create a decoy mapping (unused in actual logic)"""
    ref_map = {}
    for i, key in enumerate(keys):
        ref_map[key] = (i ** 2) % 13
    return ref_map  # Dead end


def compute_checksum(data):
    """Red herring function: looks important but unused"""
    checksum = 0
    for item in data:
        checksum ^= item * 7
    return checksum % 1000


def recursive_reduce(n, depth=0):
    """Compute alternating sum with exponential decay (actually used in baseline)"""
    if n <= 1 or depth > 5:
        return n
    return n - recursive_reduce(n // 2, depth + 1)


def build_histogram(data):
    """Count frequencies – used in distraction path"""
    hist = {}
    for x in data:
        hist[x] = hist.get(x, 0) + 1
    return hist


def transform_entry(val, shift):
    """Core transformation: val XOR shift then mod 97"""
    return (val ^ shift) % 97


def analyze_pattern(dataset, base):
    """Main analysis logic: sum transformed values filtered by prime indices"""
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5)+1):
            if k % i == 0:
                return False
        return True

    indices = list(range(len(dataset)))
    prime_indices = {i for i in indices if is_prime(i)}

    # Actual computation path
    shifted_vals = [transform_entry(v, base) for v in dataset]
    filtered_vals = [sv for i, sv in enumerate(shifted_vals) if i in prime_indices]
    return sum(filtered_vals)

# --- Main execution with extensive distractions ---
raw_input_stream = [12, 19, 23, 14, 7, 31, 44, 67, 89, 93, 101]
noise_floor = [2, 4, 6, 8, 10]
decoy_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Distractor: irrelevant preprocessing
scrubbed_data = preprocess_sequence(raw_input_stream, offset=5)
reference_lookup = generate_reference_map(['A', 'B', 'C', 'D'])
checksum_diagnostic = compute_checksum(raw_input_stream)  # Unused

# Real path begins here
baseline_shift = 0
for i in range(3):
    baseline_shift += recursive_reduce(13 + i * 4)

# Transform raw data using baseline
transformed_data = []
for idx, value in enumerate(raw_input_stream):
    if idx % 3 != 0:  # Skip every third element
        transformed_data.append(value * 2)
    else:
        transformed_data.append(value)

# Introduce more noise
freq_count = build_histogram(transformed_data)
weight_matrix = [[i+j for j in range(5)] for i in range(5)]  # Unused structure

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, baseline_shift)

print(f"Target result: {final_diagnostic}")