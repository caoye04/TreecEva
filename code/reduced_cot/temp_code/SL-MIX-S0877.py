def process_crypto_data(chunk):
    # Initialize tracking variables
    temp_sum = 0
    xor_mask = 0b1010
    char_counter = {}
    
    # Distractor: Process character frequencies (unused)
    for item in chunk:
        if isinstance(item, str):
            char = item.lower()
            char_counter[char] = char_counter.get(char, 0) + 1
    
    # Main logic: Process numerical data
    for item in chunk:
        if isinstance(item, int):
            # Apply bitwise operations and transformations
            transformed = (item ^ xor_mask) & 0xFF
            temp_sum += transformed
    
    # Distractor: Calculate unused metrics
    unused_metric = len(char_counter) * 7
    misleading_total = temp_sum + unused_metric
    
    # Final computation with integer division
    result = (temp_sum // 2) % 256
    
    return result

def analyze_dataset():
    # Sample data chunks with mixed types
    data_chunks = [
        [15, 42, 'A', 'b'],
        [28, 67, 'C', 'd'],
        [91, 33, 'E', 'f'],
        [124, 55, 'G', 'h'],
        [200, 89, 'I', 'j']
    ]
    
    # Distractor: Process multiple chunks (unused results)
    chunk_results = []
    for i, chunk in enumerate(data_chunks):
        if i % 2 == 0:
            res = process_crypto_data(chunk)
            chunk_results.append(res)
    
    # Key execution point
    final_result = process_crypto_data(data_chunks[-3:])
    
    # Print final result
    print(f"Target result: {final_result}")
    return final_result

# Execute the main function
if __name__ == "__main__":
    analyze_dataset()