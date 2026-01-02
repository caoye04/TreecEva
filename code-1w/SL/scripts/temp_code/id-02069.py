import itertools

# Irrelevant helper function (dead code path)
def analyze_frequency(data):
    return {k: data.count(k) for k in set(data)}

# Misleading transformation chain
def transform_sequence(seq):
    shifted = [x << 1 for x in seq]  # Bit manipulation red herring
    filtered = [x for x in shifted if x > 10]
    return [x ^ 3 for x in filtered]  # XOR decoy

# Unused complex generator
def generate_pairs(lst):
    for a in lst:
        for b in lst:
            yield (a, b)

# Core logic buried in distractions
def extract_features(raw):
    tokens = raw.split(',')
    values = [int(x.strip()) for x in tokens[1::2]]  # Take every second number
    base_sum = sum(values)
    offset = len(tokens) % 7
    adjusted = base_sum + (offset ** 2)
    return adjusted

# Distractor: elaborate but unused statistical function
def compute_moving_averages(data, window=3):
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result

# Key processing function with embedded logic
weights = [0.8, 1.2, 0.9, 1.1]

segment_data = "45,12,67,8,34,15,22,7"

# Heavily padded context
initial_check = len(segment_data) > 10
flag_state = (initial_check and True) or False

# Multiple irrelevant assignments
tmp_buffer = []
for i in range(3):
    tmp_buffer.append(i * i + 2)

# Fake data reconstruction
decoys = list(itertools.permutations([1, 2, 3], 2))
corrupted = [sum(pair) for pair in decoys if pair[0] != 2]

# Real but obscured computation begins
parsed = [int(x) for x in segment_data.replace(' ', '').split(',')]
evens_only = parsed[::2]  # indices 0,2,4,6
odds_selected = [x for x in parsed if x % 5 == 0]  # filtering red herring

# Actual relevant transformation
feature_vector = []
for i, val in enumerate(evens_only):
    if i % 2 == 0:
        feature_vector.append(val // 3)
    else:
        feature_vector.append(val * 2)

# Critical distraction: multiple similar operations
shadow_result = sum([x * 0.5 for x in feature_vector])
side_calc = sum(odds_selected) - evens_only[0]

# Main calculation disguised among others
def process_segments(data_str, weight_map):
    nums = [int(x) for x in data_str.split(',')]
    
    # Real feature extraction
    segment_sums = []
    for i in range(0, len(nums), 2):
        if i+1 < len(nums):
            segment_sums.append(nums[i] + nums[i+1]*2)
    
    # Weighted combination
    total = 0.0
    for idx in range(len(weight_map)):
        if idx < len(segment_sums):
            total += segment_sums[idx] * weight_map[idx]
    
    # Final adjustment using slicing
    history = [total, total*0.9, total*1.1]
    correction = sum(history[-2:]) / 2
    return int(correction + 0.5)  # Round to nearest integer

interim = extract_features(segment_data)

# Unused recursive distraction
def binary_decompose(n, acc=[]):
    if n <= 1:
        return acc + [n]
    return binary_decompose(n // 2, acc + [n % 2])

# Decoy control flow
if len(weights) == 4:
    dummy = [w ** 2 for w in weights]
    temp_result = sum(dummy) / 4
else:
    temp_result = 0

# Key execution point
final_score = process_segments(segment_data, weights)

# Multiple print statements to obscure output focus
print(f"Diagnostics: {len(tmp_buffer)} buffers")
print(f"Decoy count: {len(corrupted)}")
print(f"Feature baseline: {interim}")
print(f"Side calculation: {side_calc}")
print(f"Target result: {final_score}")