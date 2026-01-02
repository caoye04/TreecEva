def analyze_pattern(text):
    count_vowels = sum(1 for c in text.lower() if c in 'aeiou')
    count_consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    special_chars = sum(1 for c in text if not c.isalnum() and not c.isspace())

    base_score = count_vowels * 2 + count_consonants

    if special_chars > 2:
        adjustment_factor = 1.5
    else:
        adjustment_factor = 1.0

    processed_score = base_score * adjustment_factor

    # Final adjustment based on character pattern match count
    if text.endswith('!') and 'error' in text.lower():
        processed_score -= 5
    elif text.count(' ') > 3:
        processed_score += 3

    return processed_score

result = analyze_pattern('User input error! Please retry.')
print(f"Target result: {result}")