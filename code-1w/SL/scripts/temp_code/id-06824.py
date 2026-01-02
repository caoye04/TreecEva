def compute_text_score(text):
    char_weights = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    total_score = 0
    
    for index, char in enumerate(text.lower()):
        if char in char_weights:
            char_value = char_weights[char]
            total_score += char_value * (index + 1)
    
    extra_bonus = 0
    for i in range(3):
        extra_bonus += i  # Irrelevant computation
    
    return total_score

result = compute_text_score("education")
print(f"Result: {result}")