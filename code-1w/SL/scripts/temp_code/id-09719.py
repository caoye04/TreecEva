def analyze_pattern(input_str):
    # Preprocess string: remove spaces and convert to lowercase
    cleaned = input_str.replace(' ', '').lower()
    
    # Extract digits and letters separately
    digits = [int(c) for c in cleaned if c.isdigit()]
    letters = [c for c in cleaned if c.isalpha()]
    
    # Compute various metrics (some are distractions)
    digit_sum = sum(digits)
    digit_count = len(digits)
    letter_count = len(letters)
    uppercase_count = len([c for c in input_str if c.isupper()])  # distraction
    reversed_letters = ''.join(reversed(letters))
    
    # Compute average of digits, default to 0 if none
    avg_digits = digit_sum / digit_count if digit_count > 0 else 0
    
    # Determine sequence weight based on alphabetical order pattern
    increasing_pairs = 0
    for i in range(len(letters) - 1):
        if letters[i] < letters[i+1]:
            increasing_pairs += 1
    sequence_weight = increasing_pairs / len(letters) if letters else 0
    
    # Adjust average based on letter patterns (irrelevant if no digits)
    adjustment_factor = 0.0
    if letter_count > 0:
        if 'x' in letters or 'z' in letters:
            adjustment_factor = 0.3
        elif 'e' in letters:
            adjustment_factor = 0.1
        else:
            adjustment_factor = 0.05
    adjusted_avg = avg_digits * (1 + adjustment_factor)
    
    # Bonus logic based on palindrome-like structure in letters
    normalized = ''.join(letters)
    is_palindrome = normalized == normalized[::-1]
    bonus_multiplier = 10 if is_palindrome and digit_count > 1 else 5
    
    # Dead code path - never executed under current logic
    if False:
        bonus_multiplier *= 2
        adjusted_avg += 100
    
    # Key computational statement
    final_score = adjusted_avg + bonus_multiplier * sequence_weight
    
    # Print result for verification
    print(f"Result: {final_score}")
    return final_score

# Execute with sample input
result = analyze_pattern("R2A3X5Z")