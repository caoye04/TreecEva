def calculate_final_score(raw_data):
    # Preprocessing: filter valid entries and extract numeric values
    valid_entries = [x for x in raw_data if isinstance(x, str) and x.isdigit()]
    numeric_values = [int(x) for x in valid_entries]
    
    # Irrelevant transformation: reverse string representations (not used)
    reversed_strings = [x[::-1] for x in raw_data if isinstance(x, str)]
    
    # State tracking variables for debugging (semi-relevant)
    total_elements = len(raw_data)
    filtered_count = len(numeric_values)
    
    # Core logic: compute weighted sum using modular arithmetic
    weights = [(i % 4) + 1 for i in range(len(numeric_values))]
    weighted_sum = sum(val * weights[i] for i, val in enumerate(numeric_values))
    
    # Secondary processing: normalize by length (if non-zero)
    normalization_factor = max(filtered_count, 1)
    normalized_score = weighted_sum / normalization_factor
    
    # Additional distraction: simulate checksum on original data (unused)
    checksum = 0
    for item in raw_data:
        if isinstance(item, str):
            for char in item:
                checksum += ord(char) % 7
    checksum = checksum % 100
    
    # Apply conditional adjustment based on data size
    if total_elements > 5:
        adjustment = 10
    else:
        adjustment = 3
    
    # Final scoring with adjustment
    final_score = int(normalized_score + adjustment)
    
    return final_score

# Input data with mixed types and red herrings
data = ['12', 'abc', '3', '45', '6', None, '789', {}, '0', 'xyz']

# Execute main computation
final_score = calculate_final_score(data)

# Output result
print(f"Result: {final_score}")