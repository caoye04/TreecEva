def preprocess_signal(data, factor=0.85):
    return [int(x * factor) for x in data if x > 0]


def shift_window(sequence, offset):
    return sequence[offset:] + sequence[:offset]


def evaluate_symmetry(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid + (len(arr) % 2):]
    return left == right[::-1]

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq_map = {}
    for item in set(data):
        freq_map[item] = data.count(item) / len(data)
    entropy = sum(-p * log(p, 2) for p in freq_map.values() if p > 0)
    return round(entropy, 4)

# Unused transformation chain
def transform_rle(data):
    if not data:
        return []
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            encoded.append((data[i-1], count))
            count = 1
    encoded.append((data[-1], count))
    return encoded

# Misleading intermediate processing
temp_cache = {}
dummy_flags = [False, True, False]

for i in range(3):
    temp_cache[f'key_{i}'] = i ** 3 + 2

# Core logic disguised among distractors
def analyze_pattern(seq, limit):
    # Step 1: Filter using lambda and slicing
    filtered = list(filter(lambda x: x % 2 == 1, seq[::2]))
    
    # Step 2: Apply bitwise masking
    masked = [x & 0b1111 for x in filtered]  # Keep lower 4 bits
    
    # Step 3: Count occurrences above threshold
    above_limit = len([x for x in masked if x > limit])
    
    # Step 4: Check symmetry in transformed window
    shifted = shift_window(masked, 1)
    symmetric = evaluate_symmetry(shifted)
    
    # Step 5: Use set operations to find uniqueness impact
    unique_count = len(set(masked))
    
    # Step 6: Compute weighted score
    weight = 7 if symmetric else 3
    score = above_limit * weight + unique_count
    
    # Step 7: Adjust with XOR-based correction
    correction = 0
    for i in range(len(masked)):
        correction ^= masked[i]  # Cumulative XOR
    
    # Step 8: Final adjustment using integer division
    final_score = (score * 2) // 3 + (correction // 4)
    
    return final_score

# Primary input signal
raw_input = [24, 17, 53, 12, 9, 44, 31, 8, 41, 14]

# Distraction block: unused signal paths
processed_A = preprocess_signal(raw_input, 0.75)
processed_B = [x for x in raw_input if x < 30]
transformed_RLE = transform_rle(processed_B)

# Actual relevant preprocessing
logic_sequence = [x - 10 for x in raw_input if x >= 14]  # Effective values: [24,17,53,12,9,44,31,8,41,14] -> [24,17,53,44,31,41,14]

# Threshold derived from set operation (irrelevant alternative path included)
alt_threshold_set = {5, 7, 9, 11, 13}
dynamic_set = {x % 7 for x in logic_sequence}  # {0,1,2,3,4}
threshold = len(dynamic_set.intersection({2,3,4,5}))  # yields 3

# Dead code path - never executed
if __debug__:
    debug_snapshot = logic_sequence.copy()

# Key execution point
final_diagnostic = analyze_pattern(logic_sequence, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")