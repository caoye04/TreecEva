import itertools

def analyze_frequency(stream):
    # Irrelevant analysis function (dead end)
    freq = {}
    for item in stream:
        freq[item] = freq.get(item, 0) + 1
    return freq

def validate_checksum(chunk):
    # Distractor: looks important but unused in critical path
    return sum(chunk) % 7 == 0

def transform_data(seq):
    # Real transformation: maps values using arithmetic and bit ops
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append((val ** 2) ^ 5)  # Square and XOR
        else:
            transformed.append(val * 3 + (i & 3))  # Multiply and add bitwise
    return transformed

def filter_outliers(arr):
    # Misleading intermediate: used to confuse data flow
    mean_val = sum(arr) / len(arr)
    return [x for x in arr if abs(x - mean_val) < 100]

def accumulate_weighted(values):
    # Core logic part 1: weighted accumulation with zip
    weights = [i % 4 + 1 for i in range(len(values))]
    paired = zip(values, weights)
    total = 0
    for val, w in paired:
        total += val * w
    return total

def recursive_reduce(n):
    # Bit manipulation via recursion
    if n <= 1:
        return 1
    return (n & 1) + recursive_reduce(n >> 1)  # Count set bits recursively

def compute_final_score(raw):
    # Main computation with multiple layers
    stage1 = transform_data(raw)
    
    # Red herring: checksum validation not actually filtering
    valid_chunks = []
    for chunk in [stage1[i:i+4] for i in range(0, len(stage1), 4)]:
        if validate_checksum(chunk):  # Always true due to data, but unclear
            valid_chunks.extend(chunk)
    
    # Actual relevant path begins
    cleaned = filter_outliers(stage1)  # Some filtering occurs
    
    # Use enumerate and conditional expression
    adjusted = [cleaned[i] + (10 if i % 3 == 0 else -2) for i in range(len(cleaned))]
    
    # Core accumulation
    base_score = accumulate_weighted(adjusted)
    
    # Decoy operation: looks like it affects result
    temp_debug = list(itertools.accumulate([1, -1, 2, -2, 3]))  # Unused
    
    # Final adjustment using recursive bit counter on length
    size_factor = recursive_reduce(len(adjusted))
    final_score = base_score + (size_factor * 5)
    
    # Critical print
    return final_score

# Simulated sensor data stream (deterministic input)
data_stream = [12, 7, 9, 14, 6, 8, 11, 13]

# Execution
final_score = compute_final_score(data_stream)
print(f"Result: {final_score}")