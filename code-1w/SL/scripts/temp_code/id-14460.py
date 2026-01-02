def calculate_final_score(words):
    total_score = 0
    char_count_map = {}
    
    for word in words:
        for char in word:
            if char.isalpha():
                lowercase_char = char.lower()
                char_count_map[lowercase_char] = char_count_map.get(lowercase_char, 0) + 1
    
    base_scores = []
    for idx, (char, count) in enumerate(sorted(char_count_map.items())):
        score = (idx + 1) * count  # letter position in alphabet times frequency
        base_scores.append(score)
    
    multiplier = len(words) % 4 + 1
    adjusted_scores = [score * multiplier for score in base_scores]
    
    temp_sum = sum(adjusted_scores[:len(adjusted_scores)//2 + 1])
    total_score = temp_sum - (len(char_count_map) % 7)
    
    return total_score

# Irrelevant helper (distractor)
def validate_word(word):
    return all(c.isalpha() for c in word)

# Main execution
dictionary_terms = ['algorithm', 'function', 'variable', 'loop']
irrelevant_counter = 0
for term in dictionary_terms:
    if 'a' in term:
        irrelevant_counter += 1

# Key computation
total_score = calculate_final_score(dictionary_terms)
print(f"Result: {total_score}")