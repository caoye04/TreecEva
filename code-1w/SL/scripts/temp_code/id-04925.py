from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

def analyze_sequence(seq):
    # Misleading variable names and red herrings
    stats = defaultdict(int)
    frequencies = Counter(seq)
    total = 0
    temp_buffer = []
    accumulator = 0

    # Real logic begins: process only even-indexed prime digits
    primes = {2, 3, 5, 7}

    for i, char in enumerate(str(seq)):
        digit = int(char)
        stats['digit_count'] += 1
        if i % 2 == 0:  # Only even indices
            if digit in primes:
                total += digit * (i + 1)  # Weight by position

    # Distractor: complex-looking but unused transformation
    transformed = list(map(lambda x: (x[0] * 2, x[1] ** 0.5), enumerate(frequencies.items())))
    for k in frequencies:
        if frequencies[k] > 1:
            accumulator -= len(k.__str__())  # Meaningless operation

    # Another decoy calculation with zip and enumerate (no effect)
    indices = list(range(len(str(seq))))
    pairs = list(zip(indices, [x * 0.1 for x in map(int, str(seq))]))
    for idx, (i, val) in enumerate(pairs):
        accumulator += idx * val if i % 3 == 0 else 0

    # Critical path: summation depends only on total from prime digits at even indices
    summation = total * 17

    # Pivot computed from length parity (red herring branch)
    length_str = len(str(seq))
    pivot = 3 if length_str % 2 == 0 else 7
    pivot *= 2  # Additional obfuscation

    # Finalize function defined inside to increase nesting
    def finalize(value, key):
        # Bit manipulation decoy
        masked = value ^ 0xFF
        shifted = (value << 2) & 0xFFFF

        # Actual computation hidden among distractions
        result = (value + key) % 97
        result = result * key
        # Irrelevant floating point noise
        noise = sum(math.sin(i) for i in range(1, 5)) * 0.001
        return int(result - noise)  # Deterministic due to fixed inputs

    # Dead code: unreachable branch
    if False:
        temp_buffer.append(summation)
        return sum(temp_buffer)

    checksum = finalize(summation, pivot)
    return checksum

# Entry point
sequence_input = 231457913
result_value = analyze_sequence(sequence_input)
print(f"Result: {result_value}")