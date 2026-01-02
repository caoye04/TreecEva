def process_segments(sequence, threshold):
    # Irrelevant pre-processing: reverse and slice (not affecting main logic)
    reversed_seq = sequence[::-1]
    tail = reversed_seq[:3]
    
    # Semi-relevant transformation
    normalized = [x % 7 for x in sequence]
    
    # Key state tracking variables
    count = 0
    accumulator = 0
    segment_sum = 0
    
    # Misleading auxiliary calculation (dead-end)
    dummy_product = 1
    for x in tail:
        dummy_product *= x + 1
    
    # Actual logic: find segments between occurrences of threshold
    indices = [i for i, x in enumerate(normalized) if x == threshold]
    if len(indices) < 2:
        return len(normalized) % 997
    
    # Extract middle segment using slicing
    start, end = indices[0], indices[-1]
    if start < end:
        segment = normalized[start+1:end]  # Slice between first and last threshold
    else:
        segment = []
    
    # Accumulate based on modular arithmetic and parity
    for val in segment:
        if val > 0:
            count += 1
            accumulator += val ** 2
    
    # Final computation combining multiple concepts
    if count > 0:
        segment_sum = accumulator // count
    else:
        segment_sum = 0
    
    # Distractor: unused loop with complex indexing
    temp_state = 0
    for i in range(len(normalized)):
        if i % 3 == 0 and i < len(reversed_seq):
            temp_state ^= normalized[i] & 5
    
    result = (segment_sum + len(segment)) * 2
    return result

# Main execution
data = [14, 21, 6, 3, 7, 1, 8, 7, 5, 2, 7, 9]
pivot = 7
tmp_var = sum(x * 2 for x in data) // len(data)  # Irrelevant summary statistic
result = process_segments(data, pivot)
print(f"Target result: {result}")