def analyze_text_patterns(input_text):
    # Irrelevant frequency tracking (distractor)
    char_frequency = {}
    for char in input_text:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1

    # Semi-relevant preprocessing: normalize case and filter
    cleaned_text = ''.join([c.lower() for c in input_text if c.isalnum()])
    
    # Compute vowel count using list comprehension (relevant)
    vowels = set('aeiou')
    vowel_count = len([c for c in cleaned_text if c in vowels])

    # Consonant logic with distraction: unused consonant list
    consonant_list = [c for c in cleaned_text if c.isalpha() and c not in vowels]
    total_consonants = len(consonant_list)  # Used later

    # Red herring: palindrome check that isn't used directly
    is_palindrome = cleaned_text == cleaned_text[::-1]
    palindrome_bonus = 10 if is_palindrome else 0  # Not actually added anywhere

    # Word-level analysis
    words = [word for word in input_text.split() if len(word) > 1]
    unique_word_count = len(set(words))

    # Dummy transformation chain (distractor)
    transformed_words = []
    for word in words:
        temp = word.strip('!?.,').lower()
        if temp.endswith('ing'):
            transformed_words.append(temp[:-3])
        elif temp.startswith('pre'):
            transformed_words.append('early_' + temp)
    # transformed_words never used again

    # Core scoring logic (key path)
    base_score = len(cleaned_text) * 1.5
    diversity_penalty = 0.2 * len(char_frequency)  # More unique chars = lower penalty
    length_bonus = 5 if len(input_text) > 50 else 2
    
    # Critical formula
    intermediate = (vowel_count * 3) + (total_consonants * 2) + unique_word_count
    final_score = int((base_score - diversity_penalty + length_bonus) * (intermediate / 100))

    return final_score

# Main execution
input_str = "Exploring advanced code reasoning with complex patterns and intricate logic flows!"
final_score = analyze_text_patterns(input_str)
print(f"Result: {final_score}")