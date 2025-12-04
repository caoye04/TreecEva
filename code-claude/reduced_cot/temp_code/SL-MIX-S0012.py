def analyze_text(input_text):
    # Dictionary mapping letters to their point values
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    # Process text: lowercase and remove punctuation
    processed_text = input_text.lower()
    filtered_text = ''.join(c for c in processed_text if c.isalnum())
    
    # Count character frequencies
    char_count = {}
    for char in filtered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate letter distribution statistics (distraction)
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = sum(char_count.get(v, 0) for v in vowels)
    consonant_count = sum(char_count.get(c, 0) for c in consonants)
    
    # Calculate word metrics (distraction)
    word_lengths = [len(word) for word in processed_text.split()]
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Find unique characters in descending order of frequency (distraction)
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    most_common = sorted_chars[0] if sorted_chars else ('', 0)
    
    # Calculate text complexity score based on letter values
    text_score = sum(letter_values[c] for c in filtered_text if c in letter_values)
    
    # Apply bonus multiplier based on text length (distraction)
    length_bonus = 1.0
    if len(filtered_text) > 50:
        length_bonus = 1.2
    elif len(filtered_text) > 30:
        length_bonus = 1.1
    
    # Calculate alternative score (distraction)
    alt_score = text_score * length_bonus
    
    # Calculate weighted score based on character distribution (distraction)
    ratio = vowel_count / consonant_count if consonant_count > 0 else 0
    weighted_score = text_score * (1 + ratio/10)
    
    return text_score

# Sample text to analyze
sample_text = "Python programming is fun and rewarding!"
input_text = sample_text

# Analyze the text and get the score
result = analyze_text(input_text)
print(f"Result: {result}")