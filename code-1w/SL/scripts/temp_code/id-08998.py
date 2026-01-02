def compute_integrity_score(data_sequence):
    # Irrelevant transformation: base scaling (dead path)
    scale_factor = 1.75
    scaled_values = [x * scale_factor for x in data_sequence if x % 2 == 0]

    # Distractor: unused statistical calculation
    avg_val = sum(data_sequence) / len(data_sequence) if data_sequence else 0
    deviation_sq = [(x - avg_val) ** 2 for x in data_sequence]
    variance = sum(deviation_sq) / len(deviation_sq) if deviation_sq else 0

    # Key preprocessing: filter and transform relevant elements
    filtered = [x for x in data_sequence if x > 0 and x % 3 != 0]
    mapped = list(map(lambda x: (x << 1) ^ 7, filtered))  # Bit shift and XOR

    # Dead-end recursive helper (never called)
    def recursive_transform(seq, idx):
        if idx >= len(seq):
            return 0
        return seq[idx] + recursive_transform(seq, idx + 1)

    # Another red herring: complex but unused structure
    class DataNode:
        def __init__(self, value):
            self.value = value
            self.flag = (value % 11) == 0

    node_chain = [DataNode(x) for x in mapped[:len(mapped)//2]]
    flagged_count = sum(1 for node in node_chain if node.flag)

    # Actual computation begins here
    accumulator = 0
    for i, val in enumerate(mapped):
        if i % 2 == 0:
            accumulator += val * (i + 1)
        else:
            accumulator -= val // (i + 1) if i + 1 != 0 else 0

    # Intermediate decoy result
    temp_result = (accumulator + 12345) & 0xFFFF

    # Secondary irrelevant accumulation
    redundant_total = sum(x ^ (x >> 2) for x in filtered)

    # Core logic embedded within noise
    running_xor = 0
    for x in filtered:
        running_xor ^= x

    final_sum = accumulator + running_xor

    # Misleading masking operation (partially relevant)
    mask = (flagged_count << 4) | (len(node_chain) & 0xF)
    checksum = final_sum ^ (temp_result & mask)  # Critical statement

    # Final distraction: string-based encoding never used
    encoded_tag = ''.join(chr((x % 26) + 97) for x in [final_sum % 26, temp_result % 26])

    return checksum

# Input data with deterministic behavior
data_stream = [12, -5, 8, 15, 0, 21, 4, 9, 11]
result = compute_integrity_score(data_stream)
print(f"Result: {result}")