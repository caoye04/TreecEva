def analyze_pattern(seq, threshold=5):
    count = 0
    for i, val in enumerate(seq):
        if val > threshold:
            count += (i * val) % 7
    return count

def generate_key_matrix(base_seq):
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    temp_sum = 0
    for i in range(4):
        for j in range(4):
            matrix[i][j] = (base_seq[(i + j) % len(base_seq)] ^ (i << 2)) % 15
            temp_sum += matrix[i][j] * (i + 1)
    # Distractor: irrelevant transformation
    inverted = [15 - x for x in base_seq]
    return matrix, temp_sum

def evaluate_consistency(arr):
    score = 0
    for a, b in zip(arr, arr[1:]):
        if a != 0:
            score += (b // a) if b % a == 0 else -1
    return score

def transform_sequence(raw, key):
    transformed = []
    for idx, item in enumerate(raw):
        if idx % 3 == 0:
            transformed.append((item + key) % 127)
        elif idx % 5 == 0:
            transformed.append((item * 2) ^ key)
        else:
            transformed.append(item)
    # Dead code path (never reached due to logic)
    if False and len(transformed) > 100:
        return [x for x in reversed(transformed)]
    return transformed

def compute_integrity_score(data, mode="basic"):
    base_weight = sum(x for x in data if x % 2 == 0)
    shift_factor = len([x for x in data if x > 10])
    
    # Misleading intermediate checksums
    checksum_a = sum(data) * 3 % 19
    checksum_b = 0
    for i, v in enumerate(data):
        checksum_b ^= (v + i) % 11
    
    if mode == "detailed":
        return (base_weight + shift_factor) * checksum_a
    elif mode == "hybrid":
        proxy = 0
        for i, (a, b) in enumerate(zip(data, reversed(data))):
            if i % 2 == 0 and a > b:
                proxy += (a - b) * (i + 1)
        # Key computation branch
        adjustment = analyze_pattern(data, threshold=6)
        secondary = evaluate_consistency(data)
        hybrid_score = (proxy + adjustment) % 1000
        final_scalar = (shift_factor + hybrid_score) // 3
        return (hybrid_score * 2) + final_scalar - secondary
    else:
        return base_weight % 25

# Main execution with red herrings
raw_data = [3, 7, 12, 19, 8, 4, 11, 14]
offset_key = sum(raw_data) % 13

# Irrelevant transformations (distractors)
data_copy = raw_data.copy()
data_copy.reverse()
duplicate_filtered = [x for x in data_copy if x != 8]

# Unused function call (dead code)
generate_key_matrix(raw_data)

# Transform but do not use result
transformed_out = transform_sequence(raw_data, offset_key)
symbol_map = {i: chr(97 + (i % 26)) for i in range(20)}

# Critical statement
final_checksum = compute_integrity_score(data_sequence=raw_data, mode="hybrid")

print(f"Result: {final_checksum}")