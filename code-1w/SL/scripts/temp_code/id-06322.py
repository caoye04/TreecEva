import itertools

def analyze_pattern(sequence):
    # Irrelevant helper: computes frequency (not used in final result)
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    normalized = {k: v / len(sequence) for k, v in freq.items()}
    return normalized

def generate_pairs(data):
    # Distractor function: creates combinations but not used in critical path
    return list(itertools.combinations(data, 2))

def validate_checksum(arr):
    # Red herring: looks important but unused
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) * 3
    return checksum % 100 == 42

def transform_data(entries):
    # Complex transformation with irrelevant branches
    result = []
    temp_log = []
    for entry in entries:
        if isinstance(entry, str):
            cleaned = entry.strip().lower().replace('_', '')
            if cleaned.startswith('x'):
                continue  # dead filter
            elif len(cleaned) > 5:
                temp_log.append(len(cleaned))
                continue
        elif isinstance(entry, int):
            if entry < 0:
                temp_log.append(-1)
                continue
            transformed = (entry ** 2 + 3) % 7
            result.append(transformed)
    return result

def compute_entropy(values):
    # Unused advanced calculation
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 6)

def compute_aggregate(input_data, mode='strict'):
    # Core logic buried in distractions
    processed = transform_data(input_data)
    
    # Decoy data structures
    history_buffer = [0] * 10
    metadata_cache = {'version': '2.1', 'status': 'invalid'}
    temp_snapshot = processed.copy()
    
    # Key computation begins here
    filtered = [x for x in processed if x % 2 == 1]  # Keep odd numbers only
    
    # Simulate early termination condition (never triggers due to data)
    if mode == 'strict' and len(filtered) > 100:
        return -999
    
    # Real work: sum first 4 odd transformed values
    running_sum = 0
    count = 0
    for val in processed:
        if val % 2 == 1:
            running_sum += val
            count += 1
            if count == 4:  # Only take first 4 odd values
                break
    
    # More red herrings
    if count == 0:
        fallback = sum(temp_snapshot[:3]) % 8
        running_sum = fallback * 2
    
    scaling_factor = 7
    adjustment = len([x for x in input_data if isinstance(x, str)])
    
    # Final score calculation
    final_score = (running_sum * scaling_factor) - adjustment
    
    # Dead code paths
    if final_score < 0:
        final_score = abs(final_score)
    elif final_score == 0:
        final_score = 42

    # Logging decoy
    debug_trace = []
    for i in range(min(5, len(processed))):
        debug_trace.append(f"Step{i}: {processed[i]}")

    return final_score

# Main execution with mixed data types
raw_input = [10, 'x_data_3', 4, 5, 'info', 6, 7, 'label', 8, 9]

intermediate_analysis = analyze_pattern(['A', 'B', 'A'])
decoy_pairs = generate_pairs([1, 2, 3, 4])
checksum_valid = validate_checksum([1, 2, 3, 4, 5])
entropy_value = compute_entropy([2, 2, 2, 2])

# Critical statement
final_score = compute_aggregate(raw_input, mode='strict')

# Print result
print(f"Result: {final_score}")