import itertools

def analyze_text(text):
    # Count character frequencies
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Find most common characters (not used in final calculation)
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    top_chars = [c for c, _ in sorted_chars[:3]]
    
    # Calculate word frequencies
    words = text.lower().split()
    word_freqs = {}
    for word in words:
        cleaned = ''.join(c for c in word if c.isalpha())
        if cleaned:
            word_freqs[cleaned] = word_freqs.get(cleaned, 0) + 1
    
    return word_freqs, top_chars

def calculate_letter_values(text):
    # Assign values to letters based on position in alphabet
    letter_values = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Distractor calculation - reverse position values
    reverse_values = {letter: 26 - i for i, letter in enumerate(alphabet)}
    
    # Actual values used
    for i, letter in enumerate(alphabet):
        letter_values[letter] = i + 1
        
    return letter_values

def calculate_final_score(word_freqs, bonus_chars):
    letter_values = calculate_letter_values("abcdefghijklmnopqrstuvwxyz")
    
    # Base score calculation
    base_score = 0
    for word, freq in word_freqs.items():
        # Calculate word value
        word_value = 0
        for char in word:
            if char.isalpha():
                word_value += letter_values.get(char.lower(), 0)
        
        # Add to base score weighted by frequency
        base_score += word_value * freq
    
    # Apply bonuses for special characters
    bonus_multiplier = 1.0
    for char in bonus_chars:
        if char in itertools.islice(word_freqs.keys(), 5):
            bonus_multiplier += 0.1
    
    # Calculate potential alternative score (not used)
    alt_score = sum(letter_values.get(char, 0) for char in ''.join(word_freqs.keys()))
    
    # Final calculation
    return int(base_score * bonus_multiplier)

# Sample text analysis
sample_text = "The quick brown fox jumps over the lazy dog."
word_freqs, bonus_chars = analyze_text(sample_text)

# Bonus adjustment (distractor)
bonus_adjustment = len(bonus_chars) * 5
if 'z' in bonus_chars:
    bonus_adjustment += 10

# Calculate the final score
total_score = calculate_final_score(word_freqs, bonus_chars)

# Distractor calculation that doesn't affect final result
adjusted_score = total_score + bonus_adjustment - bonus_adjustment

print(f"Result: {total_score}")