def analyze_text_patterns(input_str):
    char_frequency = {}
    for c in input_str:
        char_frequency[c] = char_frequency.get(c, 0) + 1
    
    # Distractor: vowel analysis (not used later)
    vowels = 'aeiou'
    vowel_count = sum(char_frequency.get(v, 0) for v in vowels)
    consonant_count = len(input_str) - vowel_count - char_frequency.get(' ', 0)

    # Relevant: count uppercase vs lowercase
    upper_count = sum(1 for c in input_str if c.isupper())
    lower_count = sum(1 for c in input_str if c.islower())

    # Distractor: reverse slicing for palindrome check (unused)
    reversed_str = input_str[::-1]
    is_palindrome = input_str == reversed_str

    # Semi-relevant: word-level stats
    words = input_str.split()
    word_lengths = [len(w) for w in words]
    avg_word_length = sum(word_lengths) / len(word_lengths) if words else 0

    # Key computation chain starts here
    letter_grade = 'B' if avg_word_length > 4 else 'C'
    complexity_bonus = 0
    if upper_count > lower_count * 0.5 and len(words) > 3:
        complexity_bonus += 10
    
    # Use list comprehension and slicing to extract even-positioned letters
    even_letters = [c for i, c in enumerate(input_str) if i % 2 == 0 and c.isalpha()]
    unique_even_letters = len(set(even_letters))

    base_score = len(input_str) % 17
    adjustment_factor = (unique_even_letters * 3) // 2
    
    temp_result = []
    for i in range(min(5, len(word_lengths))):
        if word_lengths[i] % 2 == 0:
            temp_result.append(word_lengths[i] + base_score)
        else:
            temp_result.append(word_lengths[i] - 1)
    
    # Final score calculation – this is the key point
    final_score = base_score + adjustment_factor - len(words) + complexity_bonus
    
    # Red herring: modify final_score in a way that doesn't actually change anything
    if False:
        final_score *= 2
    
    # Another distraction: unused transformation
    transformed = ''.join(chr((ord(c) - ord('a') + 3) % 26 + ord('a')) if c.islower() else c for c in input_str)

    return final_score

# Simulate execution context
raw_data = "Dynamic Programming Solves Problems"
interim_result = analyze_text_patterns(raw_data)
scaling_constant = 1
final_score = interim_result * scaling_constant
print(f"Target result: {final_score}")