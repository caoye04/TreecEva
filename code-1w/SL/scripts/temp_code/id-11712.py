import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 1) % 100

# Unused transformation chain
class LegacyFilter:
    def __init__(self, threshold):
        self.threshold = threshold

    def apply(self, val):
        return val > self.threshold

# Real processing components
def entropy_score(seq):
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    probabilities = [f / len(seq) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probabilities)

# Lambda-based dynamic weighting
weight_func = lambda x, base: round(math.sin(x) ** 2 * base, 6)

# Simulate sensor data with noise and redundancy
data_stream = [
    1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9,
    10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 15, 15, 15, 15
]

# Distractor: unused statistical summary
mean_val = sum(data_stream) / len(data_stream)
median_val = sorted(data_stream)[len(data_stream)//2]
mode_count = max([data_stream.count(x) for x in set(data_stream)])

# Secondary irrelevant computation: prime detection filter (unused path)
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
prime_mask = [is_prime(x) for x in range(20)]

# Core logic disguised among distractions
def compress_sequence(seq):
    result = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            result.append((seq[i-1], count))
            count = 1
    if seq:
        result.append((seq[-1], count))
    return result

# Higher-order function with zip and enumerate usage
def analyze_pattern(tuples):
    indices = []
    values = []
    for idx, (val, cnt) in enumerate(tuples):
        if cnt >= 4:
            indices.append(idx)
            values.append(val)
    # Use zip to pair derived attributes
    paired = list(zip(indices, values))
    offset_sum = sum(i + v for i, v in paired)
    return offset_sum

# Misleading recursive function (dead end)
def fibonacci_limit(n, limit=10):
    if n <= 1 or limit <= 0:
        return 1
    return fibonacci_limit(n-1, limit-1) + fibonacci_limit(n-2, limit-1)

# Real pipeline function
def process_pipeline(stream):
    # Step 1: Compress repeated values into tuples
    compressed = compress_sequence(stream)
    
    # Step 2: Analyze pattern for high-frequency blocks
    pattern_score = analyze_pattern(compressed)
    
    # Step 3: Compute entropy of unique elements
    unique_entropy = entropy_score(stream)
    
    # Step 4: Apply dynamic weight based on frequency score
    weighted_component = weight_func(pattern_score, 1000)
    
    # Step 5: Combine with entropy contribution
    intermediate = int(weighted_component + (unique_entropy * 100))
    
    # Step 6: Apply corrective shift based on stream length parity
    length_factor = 1 if len(stream) % 2 == 0 else -1
    adjusted = intermediate + (length_factor * 42)
    
    # Step 7: Filter through dummy but used calculation
    dummy_values = [dummy_transform(x) for x in stream[:5]]
    dummy_sum = sum(dummy_values)
    
    # Step 8: Final adjustment using dummy sum mod
    final = adjusted - (dummy_sum % 25)
    
    return final

# Key execution point
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Target result: {final_output}")