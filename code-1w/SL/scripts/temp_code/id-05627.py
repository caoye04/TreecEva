def analyze_sequence(data_stream):
    # Irrelevant preprocessing block (dead path)
    if len(data_stream) > 100:
        temp_buffer = [x ^ 255 for x in data_stream[:50]]
        normalization_factor = sum(temp_buffer) / len(temp_buffer)
    else:
        normalization_factor = 0.0  # Misleading default

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            transformed.append(val * 2 + (i % 7))
        elif i % 5 == 0:
            transformed.append(val + (i ** 2))
        else:
            transformed.append(val)

    # Unused recursive decoy function
    def compute_entropy(seq, depth=0):
        if depth >= 3 or len(seq) < 2:
            return 1
        mid = len(seq) // 2
        return compute_entropy(seq[:mid], depth + 1) + compute_entropy(seq[mid:], depth + 1)

    entropy_estimate = compute_entropy(data_stream[:10])  # Not used later

    # Actual relevant logic starts here
    window_size = 7
    sliding_windows = [data_stream[i:i+window_size] for i in range(0, len(data_stream)-window_size+1, 3)]

    # Extract key features with slicing and modular arithmetic
    feature_vector = []
    for window in sliding_windows:
        center_val = window[len(window)//2]
        edge_sum = sum(window[::3])  # Slicing operation
        modulated = (center_val * edge_sum) % 199
        feature_vector.append(modulated)

    # Secondary filtering based on conditional expression
    filtered_features = [f for f in feature_vector if f > 50 and (f % 2 == 1)]

    # Character counting analog: count occurrences of specific pattern
    pattern_count = 0
    for i in range(len(filtered_features) - 1):
        if (filtered_features[i+1] - filtered_features[i]) % 4 == 0:
            pattern_count += 1

    # Key computation chain
    base_seed = sum(filtered_features) + (pattern_count * 17)
    extended_seed = (base_seed ^ 0xABCDEF) & 0xFFFFF

    # Simulate hash construction
    partial_hash = 0
    for val in filtered_features:
        partial_hash = (partial_hash * 31 + val) % 1000007

    final_hash = (partial_hash + extended_seed) % 1000007

    prime_offset = 983  # Carefully chosen prime
    checksum = final_hash % prime_offset  # Critical execution point

    # Red herring: unrelated floating-point accumulation
    dummy_accumulator = 0.0
    for x in data_stream:
        dummy_accumulator += (x / (x + 1)) ** 0.5
    dummy_accumulator *= 1.2345

    # Output only the required result
    print(f"Result: {checksum}")

# Input data derived from deterministic process
input_stream = [(i * i + 3*i + 7) % 256 for i in range(89)]
analyze_sequence(input_stream)