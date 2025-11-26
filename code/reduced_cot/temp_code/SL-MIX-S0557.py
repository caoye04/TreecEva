from collections import Counter

def compute_checksum(data, mask):
    # Helper function to process data chunks
    process_chunk = lambda x: (x ^ 0xFF) & 0x7F
    
    # Main processing logic
    checksum = 0
    temp_buffer = []
    
    # Distractor: unused mask application (dead code path)
    masked_data = [d & mask for d in data]
    
    # Relevant processing
    for value in data:
        processed = process_chunk(value)
        temp_buffer.append(processed)
        checksum = (checksum + processed) % 256
    
    # Misleading intermediate computation
    fake_sum = sum(masked_data)  # Uses dead code result
    
    # Distractor: unused counter analysis
    freq_count = Counter(temp_buffer)
    most_common_val = freq_count.most_common(1)[0][0] if freq_count else 0
    
    # Key computation with bitwise operations
    hash_val = checksum ^ mask
    
    # Final adjustment with modular arithmetic
    final_result = (hash_val * 3 - 17) % 1000
    
    # More distractors: unused transformations
    backup_check = final_result | 0x80
    secondary_hash = backup_check ^ 0x55
    
    return final_result

# Main execution
mask_pattern = 0x3A
data_buffer = [45, 128, 77, 201, 92, 156]

# Distractor: alternative computation path (never used)
alt_buffer = [d + 10 for d in data_buffer]
alt_sum = sum(alt_buffer) % 500

# Core computation
final_hash = compute_checksum(data_buffer, mask_pattern)

# Print the target result
print(f"Result: {final_hash}")