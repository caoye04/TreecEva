def process_sequence(items):
    temp_buffer = []
    checksum = 0
    accumulator = 1
    
    for i, val in enumerate(items):
        if i % 2 == 0:
            temp_buffer.append(val ** 2)
        else:
            temp_buffer.append(val + i)
        
        # Irrelevant string processing (distractor)
        status_str = f"Processing item {i}: {val}"
        if 'even' in status_str.lower():
            accumulator *= 2  # Dead logic - never executes

    # Secondary loop with partial relevance
    filtered = [x for x in temp_buffer if x % 3 != 0]
    
    running_total = 0
    for num in filtered:
        running_total += num * 2
        checksum ^= num  # Unused checksum

    # Key computation embedded within noise
    scale_factor = len(items) // 2
    intermediate = sum(filtered) + scale_factor
    
    # Bitwise distraction
    mask = 0b1101
    masked_value = intermediate & mask
    
    # Actual answer derivation
    final_output = (intermediate * 3) % 97
    
    # More red herrings
    metadata_log = [
        f"Size: {len(items)}",
        f"Final hash: {hash(tuple(items)) % 1000}"
    ]
    
    return final_output

# Main execution
sequence = [4, 7, 2, 5, 8, 3]
final_output = process_sequence(sequence)
print(f"Result: {final_output}")