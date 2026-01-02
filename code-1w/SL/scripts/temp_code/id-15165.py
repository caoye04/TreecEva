import math

# Irrelevant helper function (decoy)
def unused_signal_filter(x):
    return [val for val in x if val % 3 != 0]

# Another decoy function with dead logic
def legacy_compatibility_check(data):
    temp = 0
    for i in range(len(data)):
        if i % 7 == 0:
            temp += data[i] * 0.1
    return temp  # Never used

# Core transformation function
def transform_sequence(seq, key_offset):
    shifted = [(x + key_offset) * 2 for x in seq]
    processed = []
    for val in shifted:
        if val > 100:
            processed.append(int(val / 2))
        elif val < 50:
            processed.append(val + 25)
        else:
            processed.append(val)
    return processed

# Red herring: complex-looking but unused bit manipulation
def hidden_bitmask_analysis(n):
    result = 0
    for i in range(8):
        result |= (n << i) & (1 << (i * 2))
    return result + 113

# Unused statistical distraction
def compute_frequencies(arr):
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    return {k: v for k, v in freq_map.items() if v > 1}

# Recursive reduction with early termination
def recursive_reduce(values, threshold):
    if sum(values) <= threshold:
        return sum(values)
    
    if len(values) == 1:
        return values[0] % 7
    
    mid = len(values) // 2
    left = recursive_reduce(values[:mid], threshold)
    right = recursive_reduce(values[mid:], threshold)
    
    if left > 20 or right > 20:
        return left - right  # Early divergence
    
    return left + right

# Character counting distraction (unused)
def count_vowels_in_label(label):
    vowels = 'aeiou'
    return sum(1 for c in label.lower() if c in vowels)

# Main analysis function
def analyze_pattern(data):
    # Step 1: Apply non-linear scaling
    scaled = [math.ceil(x * 1.7) for x in data]
    
    # Step 2: Filter based on parity and index
    filtered = [v for i, v in enumerate(scaled) if (i + v) % 2 == 0]
    
    # Step 3: Accumulate with conditional logic
    accumulator = 0
    for num in filtered:
        if num % 4 == 0:
            accumulator += int(math.sqrt(num))
        elif num % 3 == 0:
            accumulator += num // 3
        else:
            accumulator -= num % 5
    
    # Step 4: Final adjustment using recursive result
    temp_buffer = [accumulator + i for i in range(5)]
    adjustment = recursive_reduce(temp_buffer, 10)
    final_score = accumulator + adjustment
    
    # Critical assignment point
    final_diagnostic = final_score * 2 - 17
    return final_diagnostic

# --- Distractor Variables and Dead Code Paths ---
baseline_reference = [12, 15, 22, 31, 44, 51, 63, 74]
legacy_mode_enabled = True
redundant_flag = False
auxiliary_cache = {'state': 0, 'buffer': [], 'active': False}

# Unused transformation chain
temp_result = transform_sequence(baseline_reference, 13)
_ = legacy_compatibility_check(temp_result)
_ = compute_frequencies(temp_result)

# --- Key Execution Path ---
primary_input = [7, 11, 13, 17, 19, 23]
transformed_data = transform_sequence(primary_input, 20)
# The following line contains the critical execution point
final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")