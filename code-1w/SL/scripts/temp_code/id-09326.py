from collections import defaultdict, Counter

def preprocess_data(raw):
    # Irrelevant preprocessing function (dead code path)
    temp_map = defaultdict(int)
    for char in raw:
        temp_map[char] += 1
    return dict(temp_map)

def utility_checksum(data):
    # Misleading checksum calculation (distractor)
    return sum((i + val) * 2 for i, val in enumerate(data)) % 1000

def transform_sequence(seq):
    # Transforms sequence but introduces red herring values
    shifted = [((x * 3) + 7) % 256 for x in seq]
    decoy_sum = sum(shifted[::2]) * 0.5  # Unused distracting computation
    normalized = [x / max(shifted) for x in shifted]
    return [int(x * 100) for x in normalized]

def evaluate_pair(a, b):
    # Used in a rarely-hit condition (rare branch)
    if a < b:
        return (a ^ b) + (a & 5)
    return (a + b) // 2

def analyze_pattern(weights, seq):
    # Core logic with distractors
    weighted_pairs = []
    total = 0
    temp_result = 0

    # Real transformation used in computation
    transformed_seq = transform_sequence(seq)

    # Distractor: unused but plausible intermediate
    freq_analysis = Counter(transformed_seq)
    avg_freq = sum(freq_analysis.values()) / len(freq_analysis) if freq_analysis else 0

    # Real logic begins
    for i, (w, val) in enumerate(zip(weights, transformed_seq)):
        if i % 3 == 0:
            total += w * val
        elif i % 3 == 1:
            total -= w + (val % 7)
        else:
            if val > 50:
                total += evaluate_pair(w, val) // 3
            else:
                total -= w

        # Distractor: complex-looking but unused accumulation
        temp_result ^= (w << 2) | (i & val)

    # Another red herring: conditional that never triggers due to data constraints
    if any(x > 200 for x in weights):
        total *= 0.9

    # Final adjustment based on actual pattern
    length_factor = len(seq) if len(seq) > 5 else 1
    total = (total // length_factor) + 42

    # Critical assignment
    final_score = total * 2

    # Dead code: never executed
    debug_log = defaultdict(list)
    for idx, item in enumerate(zip(seq, weights)):
        debug_log['items'].append((idx, item))

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    raw_string = "hellochecksum"
    base_weights = [12, 7, 19, 4, 8, 15, 21, 6]
    signal_sequence = [10, 20, 30, 40, 50, 60, 70, 80]

    # Irrelevant calls (distraction)
    _ = preprocess_data(raw_string)
    _ = utility_checksum(base_weights)

    # Key statement
    final_score = analyze_pattern(base_weights, signal_sequence)

    print(f"Result: {final_score}")