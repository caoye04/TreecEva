def evaluate_compliance(text):
    required_chars = set('aeiou')
    optional_chars = set('0123456789')
    present_vowels = set(char for char in text if char in required_chars)
    passing_chars = [char for char in present_vowels if text.count(char) >= 2]
    
    # Auxiliary calculations (minor distractions)
    total_digits = sum(1 for c in text if c.isdigit())
    avg_position = sum(i for i, c in enumerate(text) if c == 'a') / max(text.count('a'), 1)
    
    correction_factor = 3.5
    offset = -7
    final_score = len(passing_chars) * correction_factor + offset
    
    # Additional unrelated tracking
    redundant_flag = any(text.count(c) > 3 for c in optional_chars)
    sequence_bonus = 1 if 'ee' in text else 0
    
    return final_score

result = evaluate_compliance('beautifullyadequateadjustment')
print(f"Result: {result}")