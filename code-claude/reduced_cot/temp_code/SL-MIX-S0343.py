from collections import Counter, defaultdict

def analyze_sequence(data):
    # Initialize tracking variables
    unique_counts = defaultdict(int)
    bit_mask = 0
    frequency_score = 0
    
    # Process each element in the data
    for idx, num in enumerate(data):
        # Track occurrences of each value
        unique_counts[num] += 1
        
        # Apply some bitwise operations for data integrity check
        if idx % 3 == 0:
            bit_mask ^= (num & 0x0F)  # XOR with lower 4 bits
        elif idx % 3 == 1:
            bit_mask |= ((num & 0x0F) << 4)  # OR with shifted lower 4 bits
        else:
            # This doesn't affect bit_mask but seems like it might
            temp_bits = bit_mask & (num & 0x0F)
    
    # Calculate a secondary metric (not used in final result)
    secondary_metric = sum(k * v for k, v in unique_counts.items())
    
    # Create a set of unique values (not directly used in result)
    unique_values = set(data)
    redundant_set = {x for x in data if x > 5}  # Distracting operation
    
    # Calculate the main score
    frequency_score = sum(unique_counts.values()) - bit_mask
    
    # Apply conditional adjustment (not affecting the result)
    if secondary_metric > 100:
        adjustment = len(unique_values) * 2
    else:
        adjustment = len(unique_values)
    
    # This appears important but doesn't change frequency_score
    potential_modifier = (bit_mask >> 2) & 0x3F
    
    return frequency_score

# Sample data for analysis
sample_data = [7, 3, 5, 7, 8, 5, 2, 9, 7, 3]

# Process the data
result = analyze_sequence(sample_data)
print(f"Result: {result}")