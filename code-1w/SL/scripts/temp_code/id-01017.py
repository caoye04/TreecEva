def analyze_sequence(sequence):
    base_value = len(sequence)
    upper_count = sum(1 for c in sequence if c.isupper())
    lower_count = sum(1 for c in sequence if c.islower())
    
    if upper_count > lower_count:
        adjustment_factor = 1.5
    else:
        adjustment_factor = 0.8
    
    processed_score = (base_value * adjustment_factor) + 2
    
    temp_offset = sequence.find('X')  # potential red herring
    if temp_offset == -1:
        temp_offset = 1
    
    processed_score += temp_offset * 0.1
    
    def final_adjustment(score):
        return int(score * 2) // 3
    
    processed_score = final_adjustment(processed_score)
    
    return processed_score

result = analyze_sequence('HeLLoWorld')
print(f"Result: {result}")