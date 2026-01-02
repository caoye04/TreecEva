def analyze_pattern(seq, rule_dict):
    count = 0
    temp_result = 0
    threshold = 3
    
    # Apply slicing to get middle segment
    mid_segment = seq[2:-2]
    
    # Rule-based counting using dictionary lookup
    for item in mid_segment:
        if item in rule_dict:
            count += rule_dict[item]
    
    # Conditional accumulation
    if count > threshold:
        temp_result = count * 2
    else:
        temp_result = count + 5
    
    # Final transformation
    result = temp_result - (len(seq) - len(mid_segment))
    
    return result

# Define input data
sequence = [1, 2, 3, 4, 5, 6, 7, 8]
rules = {3: 2, 4: 1, 5: 3}

# Execute function
target_var = 'result'
result = analyze_pattern(sequence, rules)
print(f'Result: {result}')