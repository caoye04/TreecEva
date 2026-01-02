def analyze_sequence(data):
    # Irrelevant transformation: character frequency count
    char_freq = {}
    for char in ''.join(map(str, data)):
        char_freq[char] = char_freq.get(char, 0) + 1

    # Distractor: unused recursive function
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

    # Relevant: extract even-indexed elements and square them
    processed = [x**2 for i, x in enumerate(data) if i % 2 == 0]

    # Distractor: dead code path (never called)
    def deprecated_filter(arr):
        return [x for x in arr if x & 1]

    # Relevant: sum of squares at even indices
    total_power = sum(processed)

    # Misleading intermediate: bit manipulation with red herring
    magic_mask = 0b101010
    masked_result = total_power ^ magic_mask & 255

    # Irrelevant: set operations with no downstream use
    unique_values = set(data)
    extended_set = unique_values | {len(data), sum(data)//len(data)}
    extended_set.discard(min(data))

    return total_power


def compute_baseline_reference(seq):
    # Real computation: harmonic mean of non-zero elements
    filtered = [x for x in seq if x != 0]
    harmonic_mean = len(filtered) / sum(1/x for x in filtered) if filtered else 0
    
    # Distractor: unused zip with enumeration
    indexed_pairs = list(zip(enumerate(seq[::2]), enumerate(seq[1::2])))

    # Dead code: never executed logic
    if False:
        temp_state = [0] * len(seq)
        for i in range(len(temp_state)):
            temp_state[i] = seq[i] << 2
        return temp_state

    return harmonic_mean


def evaluate_performance(metrics, base):
    # Core logic: weighted combination
    signal_strength = metrics * 0.85
    adjustment_factor = (base * 1.2) if base > 0 else 0.5
    
    # Critical statement
    final_score = int(signal_strength - adjustment_factor + 100)
    
    # Decoy operation: looks important but unused
    checksum = 0
    for i, val in enumerate(str(final_score)):
        checksum ^= (i + 1) * ord(val)
    
    return final_score

# Main execution flow
sequence_data = [3, 7, 2, 8, 5, 9, 4, 6]
baseline = compute_baseline_reference(sequence_data)
metrics = analyze_sequence(sequence_data)

# Key assignment point
final_score = evaluate_performance(metrics, baseline)

print(f"Result: {final_score}")