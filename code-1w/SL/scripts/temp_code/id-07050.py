def preprocess_signal(raw_samples):
    # Irrelevant transformation (dead code path)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in raw_samples if x > sum(raw_samples) / len(raw_samples)]
    padded = [0] * 3 + raw_samples + [0] * 3
    return padded  # Actual function ignores this; red herring


def transform_features(data, key_offset=7):
    # Distractor: complex but unused computation
    entropy_approx = 0
    for x in data:
        if x != 0:
            entropy_approx += x * x
    entropy_approx = round(entropy_approx ** 0.5, 4)

    # Real transformation
    shifted = [(x + key_offset) % 256 for x in data]
    modulated = [abs(shuffled_index_shift(x, len(data))) for x in shifted]
    return modulated


def shuffled_index_shift(value, size):
    # Bit manipulation red herring
    temp = (value << 3) | (value >> 5)
    temp ^= 0b101010
    temp %= size if size > 0 else 1
    return value ^ temp  # Final result only depends on XOR with index-like shift


def compute_checksum(data):
    base = 17
    checksum = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            checksum += val * base
        else:
            checksum -= val
        base = (base * 31) % 10007
    return checksum % 987653

# Entry point data
raw_input = [12, 45, 67, 23, 89, 34, 56]

# Distraction block: irrelevant data structures
stats_summary = {
    'mean': sum(raw_input) / len(raw_input),
    'peak': max(raw_input),
    'noise_floor': min(raw_input) + 2,
    'dummy_flag': False
}

# Unused recursive function (decoy)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# More distractions: slicing with no impact
segment = raw_input[2:5]
reversed_segment = segment[::-1]

# Actual relevant pipeline
processed = preprocess_signal(raw_input)
transformed_data = transform_features(processed, key_offset=11)
# Key statement
checksum = compute_checksum(transformed_data)

# Print final target result
print(f"Result: {checksum}")