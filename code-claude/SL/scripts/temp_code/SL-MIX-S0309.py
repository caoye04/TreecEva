def process_text_data(text):
    # Extract all digits from text
    digits = [int(char) for char in text if char.isdigit()]
    
    # Some processing on digits that won't affect our target
    transformed = [d * 2 if d > 5 else d for d in digits]
    
    # Define a sequence based on Fibonacci but with modification
    def modified_sequence(n):
        if n <= 1:
            return n
        return modified_sequence(n-1) + modified_sequence(n-2)
    
    # Generate sequence - only used for length calculation
    fibonacci_values = [modified_sequence(i) for i in range(4)]
    sequence_length = len(fibonacci_values) + 5  # We'll use this value
    
    # Create our actual working sequence
    base_sequence = list(range(1, sequence_length + 1))
    
    # Apply some transformations that seem important but aren't
    alternative_seq = [x**2 for x in base_sequence[:3]]
    irrelevant_value = sum(alternative_seq) / len(alternative_seq)
    
    # Determine valid elements using a seemingly complex but straightforward rule
    valid_indices = set([i for i in range(sequence_length) if i % 2 == 0])
    valid_sequence = [base_sequence[i] for i in valid_indices]
    
    # This is where we calculate our target value
    filtered_count = len(set(filter(lambda x: x % 2 == 0, valid_sequence)))
    
    # Additional calculations that don't affect our answer
    result_modifier = len(text) % 3
    if result_modifier > 0:
        temp_value = filtered_count * result_modifier
    else:
        temp_value = filtered_count
    
    return filtered_count

# Sample text to process
sample_text = "Python3.9"
result = process_text_data(sample_text)
print(f"Result: {result}")