def analyze_pattern(sequence):
    count_map = {}
    for idx, val in enumerate(sequence):
        if val not in count_map:
            count_map[val] = 0
        count_map[val] += (idx % 3) + 1
    
    # Distractor: Unused transformation
    transformed = [x ^ 7 for x in sequence if x % 2 == 0]
    temp_sum = sum(transformed) * 0.5

    return count_map


def validate_sequence(seq):
    # Irrelevant validation logic (not used)
    if len(seq) < 5:
        return False
    cumulative = 0
    for i in range(len(seq)):
        cumulative += seq[i] * (i + 1)
    return cumulative % 97 == 0


def calculate_integrity(data, keys):
    offset = len(keys) % 8
    base_value = 0
    checksum = 0
    
    # Main logic with distractors
    for i, (d, k) in enumerate(zip(data, keys)):
        shifted = d << (k % 4)
        base_value += shifted
        if i % 2 == 0:
            checksum ^= (shifted + offset) & 255
        else:
            checksum += (shifted ^ offset) % 19

    # Secondary loop with partial relevance
    parity = 0
    for d in data:
        parity ^= d
    
    # Dead code: this block has no effect on output
    if parity > 100:
        backup = [parity >> j for j in range(3)]
        for b in backup:
            base_value -= b % 7

    # Core contribution to answer
    final_checksum = (base_value ^ checksum) & 65535
    
    # Extra red herring variables
    dummy = sum(base_value % (j+1) for j in range(1, 5)) / 4
    anomaly_flag = dummy > 1000
    
    return final_checksum

# Setup inputs
sequence_input = [12, 7, 15, 12, 9, 7]
recovery_keys = [3, 5, 2, 6, 4, 3]
data_stream = [105, 88, 110, 92, 101, 89]

# Irrelevant function call (distractor)
analyze_pattern(sequence_input)

# Key computation
final_checksum = calculate_integrity(data_stream, recovery_keys)

print(f"Result: {final_checksum}")