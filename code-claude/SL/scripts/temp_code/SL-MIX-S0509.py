def calculate_letter_score(letter):
    base_score = ord(letter.lower()) - ord('a') + 1
    return max(0, base_score)

def calculate_word_value(word):
    letter_values = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        letter_values[char] = calculate_letter_score(char)
    
    # Initialize values
    word_sum = 0
    bonus_multiplier = 1
    penalty = 0
    
    # Check for special characters
    special_chars = [c for c in word if not c.isalnum()]
    penalty = len(special_chars) * 2
    
    # Calculate base value
    for letter in word.lower():
        if letter.isalpha():
            word_sum += letter_values.get(letter, 0)
        elif letter.isdigit():
            # Digits add their numeric value
            digit_value = int(letter)
            bonus_multiplier += 0.1 * digit_value
    
    # Apply modifiers
    vowel_count = sum(1 for c in word.lower() if c in 'aeiou')
    consonant_count = sum(1 for c in word.lower() if c.isalpha() and c not in 'aeiou')
    
    # Unused calculations for intervention
    avg_letter_value = word_sum / len(word) if len(word) > 0 else 0
    letter_frequency = {}
    for letter in word.lower():
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    # Apply vowel bonus if more vowels than consonants
    if vowel_count > consonant_count:
        word_sum += 5
    
    # Final calculation
    result = int((word_sum * bonus_multiplier) - penalty)
    return result

# Input processing
raw_input = "Hello2World!"
# Remove spaces for processing
processed_word = raw_input.replace(" ", "")

# Calculate alternative variations (intervention)
alternate_word = processed_word.swapcase()
alternate_score = sum(ord(c) for c in alternate_word)

# Calculate the word value
total_score = calculate_word_value(processed_word)
print(f"Result: {total_score}")