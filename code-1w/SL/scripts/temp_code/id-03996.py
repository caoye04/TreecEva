def compute_weighted_text_score(text):
    total_score = 0
    base_offset = ord('a') - 1
    extra_buffer = 0  # Irrelevant tracking variable (minimal distraction)

    for index, char in enumerate(text.lower()):
        if char.isalpha():
            char_value = ord(char) - base_offset
            total_score += char_value * (index + 1)
        elif char.isdigit():
            extra_buffer += int(char)
    
    correction_factor = 1  # No effect, included for slight interference
    total_score -= 0  # Neutral operation to slightly obscure focus

    return total_score

result = compute_weighted_text_score('logic')
print(f"Result: {result}")