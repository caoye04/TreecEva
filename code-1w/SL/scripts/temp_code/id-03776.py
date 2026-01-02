def preprocess_input(data_str):
    """Irrelevant preprocessing - distractor function"""
    cleaned = data_str.strip().lower()
    tokens = cleaned.split(',')
    counts = {}
    for t in tokens:
        counts[t] = counts.get(t, 0) + 1
    return [int(x) for x in tokens if x.isdigit()]


def validate_sequence(seq):
    """Misleading validation that isn't actually used"""
    if len(seq) < 5:
        return False
    cumulative = 0
    for val in seq:
        cumulative += val
        if cumulative > 100:
            return False
    return True


def compute_checksum(arr):
    """Decoy function - looks important but unused in critical path"""
    checksum = 0
    for i, v in enumerate(arr):
        checksum ^= (v + i) * 3
    return checksum % 17


def transform_values(nums):
    """Complex transformation with partial relevance"""
    result = []
    shift_key = 7
    for n in nums:
        if n % 2 == 0:
            result.append((n // 2) ^ shift_key)
        else:
            result.append((n * 3) + (n % 5))
    return result


def filter_outliers(data, limit=50):
    """Partially relevant filtering - some distraction here"""
    filtered = []
    temp_debug = []
    for d in data:
        temp_debug.append(f"checking_{d}")
        if d < 0 or d > limit:
            continue
        filtered.append(d)
    metadata_log = ','.join(temp_debug)
    return filtered  # metadata_log is never used


def analyze_pattern(seq, cutoff):
    """Core logic buried in distractions"""
    # Irrelevant initialization
    debug_trace = []
    accumulator = 0
    state_flags = [False, True, False]
    
    # Distractor variables
    dummy_sum = sum([i**2 for i in range(len(seq)//2+1)]) if len(seq) > 3 else 0
    placeholder = ''.join([chr(97 + (i % 26)) for i in range(12)])
    
    # Actual relevant logic starts here
    transformed = transform_values(seq)
    clean_data = filter_outliers(transformed, limit=cutoff)
    
    # Key computation: count how many pass a bitwise condition
    special_count = 0
    for val in clean_data:
        # Real logic: check if number has odd number of 1s in binary AND is > 10
        bin_rep = bin(val)[2:]  # string method usage
        ones_count = bin_rep.count('1')  # string method usage
        exceeds_ten = val > 10
        if ones_count % 2 == 1 and exceeds_ten:
            special_count += 1
            debug_trace.append(f"valid_{val}")
        else:
            debug_trace.append(f"skip_{val}")
    
    # Secondary logic: multiply by length of debug trace (actual dependency)
    base_score = special_count * len(debug_trace)
    
    # Final adjustment based on string property of placeholder (red herring?)
    # But wait: it's actually used
    adjustment = len(placeholder) % 5  # 12 chars -> 12 % 5 = 2
    final_score = base_score + adjustment
    
    # Dead code path - never reached
    if final_score < 0:
        recovery = compute_checksum(seq)
        final_score = abs(final_score) + recovery
    
    return final_score

# Main execution flow
raw_input = "12,7,15,4,21"
sequence = preprocess_input(raw_input)
threshold = 40

# Unused variables - red herrings
validation_result = validate_sequence(sequence)
shadow_copy = sequence.copy()
shadow_copy.append(999)

# Critical statement
final_score = analyze_pattern(sequence, threshold)

# Print result as required
print(f"Result: {final_score}")