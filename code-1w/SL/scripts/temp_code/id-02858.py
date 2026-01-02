def analyze_pattern(sequence, depth=0):
    if depth >= 3:
        return sum([x ** 2 for x in sequence if x % 2 == 0])
    transformed = [sequence[i] + i for i in range(len(sequence))]
    return analyze_pattern(transformed, depth + 1)

# Irrelevant helper (decoy)
def deprecated_hash(seq):
    return sum([ord(c) for c in ''.join(map(str, seq))]) % 100

# Unused but plausible-looking utility
calculate_entropy = lambda seq: len(set(seq)) / (len(seq) + 1e-5)

# Distractor data
temp_buffer = [1, 1, 2, 3, 5, 8, 13]
diagnostic_trace = {'iterations': 0, 'flags': [], 'status': 'nominal'}

# Core logic disguised among noise
data_sequence = list(range(10, 20))
offset_map = {i: val % 7 for i, val in enumerate(data_sequence)}

# Misleading intermediate computation (never used)
baseline_metric = sum([v * (k + 1) for k, v in offset_map.items()]) // 3

# Real processing begins
processed = []
for idx, val in enumerate(data_sequence):
    shifted = val ^ (idx << 1)  # Bit manipulation
    processed.append(shifted)

# Tuple unpacking and slicing distraction
chunk_a = processed[:5]
chunk_b = processed[5:]
head, *middle, tail = chunk_a + [sum(chunk_b)]

# Red herring control flow
if len(middle) > 3:
    diagnostic_trace['flags'].append('MID_OVERFLOW')
    # Dead branch due to logic
    temp_result = [x for x in middle if x & 1]
else:
    pass  # Placeholder

# Actual key function
def compute_integrity_score(seq, mode="basic"):
    base = 0
    if mode == "basic":
        base = sum(seq[i] for i in range(0, len(seq), 2))
    elif mode == "advanced":
        base = sum([seq[i] * seq[-i-1] for i in range(len(seq))])
    else:  # hybrid mode
        evens = seq[::2]
        odds = seq[1::2]
        paired = zip(evens, sorted(odds, reverse=True))
        base = sum(a ^ b for a, b in paired)
        # Inject modular arithmetic
        base = (base + analyze_pattern(odds)) % 976543
    return base + len(seq)

# Decoy function call (no effect)
_ = deprecated_hash(temp_buffer)

# Critical assignment with high interference
final_checksum = compute_integrity_score(data_sequence, mode="hybrid")

# Final output
print(f"Result: {final_checksum}")