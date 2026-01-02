import itertools

def analyze_pattern(sequence, mode='normal'):
    if mode == 'debug':
        return sum(x ** 2 for x in sequence if x % 2 == 0)
    return sum(1 for x in sequence if x > 0 and bin(x).count('1') % 2 == 0)

def validate_checksum(chunk):
    # Irrelevant validation logic (dead path)
    if len(chunk) == 0:
        return 0
    acc = 0
    for i, val in enumerate(chunk):
        acc ^= val * (i + 1)
    return acc % 17

def filter_anomalies(data, limit=256):
    # Distractor: uses lambda and list comprehension but not on critical path
    filtered = [x for x in data if 0 <= x <= limit]
    outlier_score = lambda seq: sum(1 for x in seq if x > 0.9 * limit)
    if outlier_score(filtered) > 3:
        return filtered[:5]
    return filtered

def build_lookup(keys, base_offset):
    # Unused function — red herring
    return {k: (k * base_offset) % 97 for k in keys}

def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return round(-sum(p * log2(p) for p in probabilities), 6)

def process_metrics(stream, config):
    # Core logic embedded within distractions
    segment_a = stream[::2]  # Even indices
    segment_b = stream[1::2]  # Odd indices

    # Irrelevant entropy computation
    _ = compute_entropy(segment_a)

    # Key transformation
    transformed = []
    for i, x in enumerate(segment_a):
        shifted = x >> (i % 4)
        masked = shifted & 0xF
        transformed.append(masked)

    # Decoy accumulation
    dummy_accum = 0
    for group in itertools.groupby(transformed, key=lambda x: x > 7):
        if group[0]:
            dummy_accum += len(list(group[1]))

    # Real computation begins: count specific bit patterns
    pattern_count = 0
    for val in segment_b:
        binary_rep = bin(val)[2:].zfill(8)
        # Look for alternating bit pattern '1010' or '0101' in any position
        for j in range(len(binary_rep) - 3):
            snippet = binary_rep[j:j+4]
            if snippet == '1010' or snippet == '0101':
                pattern_count += 1
                break  # Count one per number

    # Conditional mutation based on config
    threshold_met = any(t < 50 for t in config.values())
    adjustment = -17 if threshold_met else 10

    intermediate = pattern_count * 13

    # Multi-step final calculation
    temp_result = intermediate + adjustment
    temp_result *= 2
    temp_result -= (temp_result // 10)  # Subtract one-tenth (integer division)

    # Final mapping
    final_value = abs(temp_result - 4)  # Ensure positive offset

    # Critical assignment
    final_diagnostic = final_value

    # Dead code paths below
    if final_diagnostic < 0:
        build_lookup([1,2,3], 10)
    elif final_diagnostic == 42:
        validate_checksum([1,1,1])

    return final_diagnostic

# Simulated sensor data stream (deterministic input)
data_stream = [218, 170, 85, 204, 136, 195, 102, 150, 240, 51]
thresholds = {'t1': 60, 't2': 45, 't3': 70, 't4': 55}

# Trigger execution
final_diagnostic = process_metrics(data_stream, thresholds)
print(f"Result: {final_diagnostic}")