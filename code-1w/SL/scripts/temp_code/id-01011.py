def analyze_sequence(seq):
    length = len(seq)
    if length == 0:
        return 0
    
    # Distractor: counting vowels in string representation (irrelevant)
    seq_str = ''.join(map(str, seq))
    vowel_count = sum(1 for c in seq_str.lower() if c in 'aeiou')
    
    # Real logic begins: filter even numbers > 5
    filtered = [x for x in seq if x % 2 == 0 and x > 5]
    
    # Distractor: sorting in multiple ways
    sorted_asc = sorted(filtered)
    sorted_desc = sorted(filtered, reverse=True)
    temp_result = sorted_asc[-1] * 2 if sorted_asc else 0
    
    # More real logic: compute product of positions of numbers divisible by 4
    positions_product = 1
    found_any = False
    for i, val in enumerate(seq):
        if val % 4 == 0:
            positions_product *= (i + 1)
            found_any = True
    if not found_any:
        positions_product = 0
    
    # Combine intermediate results
    base_score = sum(filtered) + positions_product
    return base_score


def normalize_string(s):
    # Irrelevant helper function with misleading name
    s_clean = s.strip().upper().replace(' ', '_')
    checksum = sum(ord(c) for c in s_clean)
    return s_clean, checksum

# Main data processing pipeline
data_stream = [3, 8, 12, 7, 16, 9, 10, 4]
processed_data = []

# Simulate chunked processing (some chunks do nothing useful)
for i in range(0, len(data_stream), 3):
    chunk = data_stream[i:i+3]
    chunk_sum = sum(chunk)
    chunk_max = max(chunk)
    
    # Distractor: string transformation on numeric data (no effect)
    _ = normalize_string(f"block_{i//3}")
    
    # Only every second chunk contributes meaningfully
    if (i // 3) % 2 == 0:
        processed_data.append(chunk_sum)
    else:
        processed_data.append(chunk_max)

# Additional distractor: sort and reverse without use
backup_copy = processed_data.copy()
sorted_backup = sorted(backup_copy, key=lambda x: -x)
reversed_sorted = sorted_backup[::-1]

# Core scoring logic
processed_data.append(analyze_sequence(data_stream))

# Final aggregation with red herring variables
total_elements = len(processed_data)
duplicate_check = len(set(processed_data)) < len(processed_data)
scaling_factor = 1.5 if duplicate_check else 1.0

# Misleading complex expression that doesn't affect final result
shadow_score = (sum(reversed_sorted) * 0.5) + (sorted_desc[0] if 'sorted_desc' in locals() else 0)

# Actual final computation
def calculate_final_score(scores):
    raw = sum(score * (i + 1) for i, score in enumerate(scores))
    adjustment = len([s for s in scores if s > 10])
    return int(raw - adjustment)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")