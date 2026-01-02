from itertools import combinations

def analyze_pattern(sequence):
    magnitude = sum([x ** 2 for x in sequence if x % 2 == 0])
    offset = len([x for x in sequence if x < 0]) * 3
    phantom_sum = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            phantom_sum += sequence[i] ^ sequence[i + 1]
    return magnitude - offset

def validate_sequence(seq):
    if len(seq) < 4:
        return False
    sorted_check = sorted(seq)
    duplicates = len(seq) - len(set(seq))
    threshold = sorted_check[2] if len(sorted_check) > 2 else 0
    return all(x >= threshold for x in seq) and duplicates <= 2

def compute_integrity_value(stream, mode="basic"):
    base_weight = 0
    temp_accum = 0
    control_flag = False
    
    for idx, val in enumerate(stream):
        if val == 0:
            continue
        if mode == "hybrid" and idx % 5 == 0:
            pair_gen = list(combinations([val, idx, len(stream)], 2))
            temp_accum += sum(a * b for a, b in pair_gen)
        base_weight += abs(val) * (idx + 1)
        
    if mode == "hybrid":
        adjustment = analyze_pattern(stream)
        base_weight += adjustment // 4
    
    # Irrelevant block - dead code path under current inputs
    if control_flag:
        fallback = 0
        for c in str(base_weight):
            fallback ^= ord(c)
        temp_accum += fallback
    
    return base_weight + temp_accum

# Simulate sensor data ingestion
raw_readings = [3, -1, 4, 1, 5, 9, 2, 6, -8, 5]
data_stream = [x * 2 for x in raw_readings if x != 5]  # Filter out 5s and scale

# Pre-check with no side effects
is_valid = validate_sequence(data_stream)

# Compute diagnostic metrics (some irrelevant)
diagnostic_pairs = []
for i, j in combinations(range(len(data_stream)), 2):
    if data_stream[i] + data_stream[j] == 0:
        diagnostic_pairs.append((i, j))

pair_count = len(diagnostic_pairs)
phantom_metric = sum(data_stream) * pair_count if pair_count > 0 else 0

# Core computation
final_checksum = compute_integrity_value(data_stream, mode="hybrid")

# Print result as required
print(f"Result: {final_checksum}")