def calculate_word_score(text):
    # Dictionary of letter values (like in word games)
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    # Process the text
    words = text.lower().split()
    
    # Track frequency for bonus calculation
    letter_frequency = {}
    for word in words:
        for char in word:
            if char.isalpha():
                letter_frequency[char] = letter_frequency.get(char, 0) + 1
    
    # Calculate baseline score
    base_score = 0
    for word in words:
        word_length = len(word)
        for char in word:
            if char in letter_values:
                base_score += letter_values[char]
    
    # Calculate bonus points
    unique_letters = set(letter_frequency.keys())
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = unique_letters - vowels
    
    # Bonus formula - not directly affecting the final score
    bonus_potential = len(consonants) * 2 - len(vowels)
    
    # Apply multiplier based on word count
    if len(words) >= 5:
        base_score *= 2
    elif len(words) <= 2:
        base_score = int(base_score * 0.8)
    
    return base_score

# Original text with some noise
original_text = "The quick brown fox jumps over the lazy dog"
reversed_text = original_text[::-1]

# Text preprocessing (distraction)
processing_mode = "standard"
preprocessed_text = original_text.lower()

if processing_mode == "advanced":
    preprocessed_text = preprocessed_text.replace("the", "a")

# Filter text (keeping only certain words)
words_to_keep = set(["quick", "brown", "fox", "jumps", "lazy"])
filtered_text = " ".join([word for word in preprocessed_text.split() if word in words_to_keep])

# Calculate alternative scores (distractions)
char_count = len(filtered_text)
word_count = len(filtered_text.split())
alternative_score = char_count * word_count

# Calculate the actual word score
word_score = calculate_word_score(filtered_text)

# Final adjustments (not affecting word_score)
final_display_score = word_score
if char_count > 20:
    final_display_score += 10

print(f"Result: {word_score}")