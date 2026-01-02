def analyze_text_patterns(text_a, text_b):
    set_a = set(text_a.lower())
    set_b = set(text_b.lower())
    
    # Extract vowels present in either text
    vowels = set('aeiou')
    vowels_in_a = set_a.intersection(vowels)
    vowels_in_b = set_b.intersection(vowels)
    vowel_count = len(vowels_in_a.union(vowels_in_b))
    
    # Find common alphabetic characters
    common_chars = set_a.intersection(set_b)
    common_alphas = {ch for ch in common_chars if ch.isalpha()}
    
    # Irrelevant distraction: count digits (not used in final logic)
    digit_count_a = sum(1 for ch in text_a if ch.isdigit())
    digit_count_b = sum(1 for ch in text_b if ch.isdigit())
    total_digits = digit_count_a + digit_count_b  # Unused variable (minor interference)
    
    # Key computation
    final_score = len(common_chars) + (vowel_count % 7)
    return final_score

# Execution
result = analyze_text_patterns("LogicProven2023", "PythonLover2024")
print(f"Result: {result}")