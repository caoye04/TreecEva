def process_text(text):
    # Remove spaces and convert to lowercase
    processed = text.lower().replace(' ', '')
    # Count character frequencies for analysis
    char_freq = {}
    for char in processed:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # This frequency analysis isn't used in the final result
    most_common = ''
    max_freq = 0
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_common = char
    
    return processed

def calculate_word_value(word, value_dict):
    total = 0
    bonus_multiplier = 1
    
    # Track consecutive letters for bonus calculation
    prev_char = None
    streak = 1
    
    for i, char in enumerate(word):
        # Base value for each character
        char_value = value_dict.get(char, 0)
        
        # Apply position-based modification
        if i % 3 == 0:  # Every third position gets bonus
            char_value *= 2
        
        # Check for consecutive same letters
        if char == prev_char:
            streak += 1
            if streak >= 3:  # Triple consecutive letters trigger bonus
                bonus_multiplier = 1.5
        else:
            streak = 1
        
        # Special rule for vowels in second half of word
        if char in 'aeiou' and i >= len(word) // 2:
            char_value += 5
        
        total += char_value
        prev_char = char
    
    # Apply final multiplier
    return int(total * bonus_multiplier)

# Input text to process
input_text = "puzzle"

# Dictionary mapping letters to their point values
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Process input and generate alternative words (not used in final calculation)
processed_word = process_text(input_text)
alternate_words = [processed_word[::-1], processed_word[1:] + processed_word[0]]

# Calculate scores for all words
main_score = calculate_word_value(processed_word, letter_values)
alternate_scores = [calculate_word_value(word, letter_values) for word in alternate_words]

# Find highest scoring word (not used in final calculation)
best_word = processed_word
best_score = main_score
for i, score in enumerate(alternate_scores):
    if score > best_score:
        best_score = score
        best_word = alternate_words[i]

# Calculate final score based on original word
final_score = calculate_word_value(processed_word, letter_values)

print(f"Result: {final_score}")