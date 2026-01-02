from itertools import combinations

def analyze_sequence(raw_input):
    # Convert to uppercase and filter alphanumeric
    cleaned = ''.join(ch.upper() for ch in raw_input if ch.isalnum())
    
    # Generate all 3-character subsequences
    subseqs = [cleaned[i:i+3] for i in range(len(cleaned)-2)]
    
    # Count frequency of each subsequence (distractor: not used later)
    freq_map = {}
    for seq in subseqs:
        freq_map[seq] = freq_map.get(seq, 0) + 1
    
    # Extract numeric values from original input
    digits = [int(c) for c in raw_input if c.isdigit()]
    
    # Compute rolling sum of consecutive pairs (irrelevant computation)
    rolling_sums = [digits[i] + digits[i+1] for i in range(len(digits)-1)] if len(digits) > 1 else []
    
    # Key transformation: square even digits, cube odd digits
    transformed = []
    for d in digits:
        if d % 2 == 0:
            transformed.append(d ** 2)
        else:
            transformed.append(d ** 3)
    
    return transformed

def validate_integrity(data):
    # Checksum validation (not actually used in final logic)
    checksum = sum(d * (i + 1) for i, d in enumerate(data)) % 101
    is_valid = checksum < 90  # Always true for small data
    
    # Additional distraction: find duplicate patterns in index sums
    indices_sum = sum(i for i, x in enumerate(data) if x > 5)
    has_duplicate = len(set(data)) != len(data)
    
    return is_valid  # Unused return value in main flow

def calculate_optimal_yield(transformed_values):
    # Base accumulation
    accumulator = 0
    temp_buffer = []
    
    for val in transformed_values:
        if val > 30:
            accumulator += val // 3  # Integer division
        else:
            accumulator += val * 2
        
        # Track intermediate states (semi-relevant)
        temp_buffer.append(accumulator % 25)
    
    # Use set to eliminate duplicates in buffer (key step)
    unique_remainders = len(set(temp_buffer))
    
    # Final adjustment using case conversion side-theme
    adjustment = len('threshold'.upper())  # Always 9
    
    # Distractor: unused combination generation
    if len(temp_buffer) >= 3:
        _ = list(combinations(temp_buffer, 3))  # Not stored or used
    
    final_yield = accumulator - unique_remainders * adjustment
    return final_yield

# Main execution flow
raw_data = "B2X9m4P7a1Q8n3Z6"

# Step 1: Process the raw input sequence
processed_data = analyze_sequence(raw_data)

# Step 2: Validate integrity (result not used - red herring call)
validation_result = validate_integrity(processed_data)

# Step 3: Calculate optimal yield based on transformed data
final_yield = calculate_optimal_yield(processed_data)

print(f"Result: {final_yield}")