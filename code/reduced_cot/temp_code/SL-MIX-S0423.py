import itertools

def calculate_final_score(text_input):
    # Process character frequencies
    char_count = {}
    for char in text_input:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Calculate vowel bonus (distractor - not used in final score)
    vowels = 'aeiouAEIOU'
    vowel_bonus = sum(1 for char in text_input if char in vowels)
    
    # Process character pairs using itertools
    pairs = list(itertools.combinations(char_count.keys(), 2))
    pair_scores = []
    for pair in pairs:
        score = (char_count[pair[0]] + char_count[pair[1]]) * len(pair[0] + pair[1])
        pair_scores.append(score)
    
    # Calculate base score from unique characters
    unique_chars = len(char_count)
    base_score = unique_chars * 10
    
    # Apply multiplier based on text length (distractor - not used)
    length_multiplier = len(text_input) // 5
    
    # Final calculation using only relevant components
    final_score = base_score + (max(pair_scores) if pair_scores else 0)
    
    return final_score

text_data = "programming assessment"
result = calculate_final_score(text_data)
print(f"Result: {result}")