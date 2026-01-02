def analyze_data_stream(raw_input):
    # Simulate processing a data stream with noise filtering
    tokens = raw_input.split(',')
    
    # Irrelevant transformation: reverse every token (not used in final logic)
    reversed_tokens = [t[::-1] for t in tokens]
    
    # Parse numeric values from original tokens
    parsed_values = []
    for token in tokens:
        stripped = token.strip()
        if stripped.isdigit():
            parsed_values.append(int(stripped))
        elif stripped.startswith('-') and stripped[1:].isdigit():
            parsed_values.append(int(stripped))
    
    # Misleading intermediate: count negatives (used nowhere)
    negative_count = len([v for v in parsed_values if v < 0])
    
    # Distractor: create shifted version of values (unused)
    shifted_values = [v << 1 for v in parsed_values]  # Bitwise distraction
    
    # Core logic: identify valid entries based on magnitude and parity
    valid_entries = []
    for v in parsed_values:
        if abs(v) > 5:
            if v % 2 == 0:
                valid_entries.append(v)
    
    # Another red herring: slice first half of valid entries (but not assigned)
    valid_entries[:len(valid_entries)//2]
    
    # Key computation step
    filtered_sum = sum(valid_entries)
    
    # Print result as required
    print(f"Result: {filtered_sum}")
    
    return filtered_sum

# Execute with sample input
data_str = "10,-3,8,12,4,-7,6,15,2"
analyze_data_stream(data_str)