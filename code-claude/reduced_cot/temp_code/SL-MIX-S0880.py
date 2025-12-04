from collections import Counter

# Text analysis function
def analyze_text(text):
    # Count character frequencies
    char_count = Counter(text.lower())
    
    # Assign values to characters (a=1, b=2, etc.)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_values = []
    
    for char in text:
        if char.lower() in alphabet:
            # Position in alphabet (0-indexed) + 1
            position = alphabet.index(char.lower()) + 1
            char_values.append(position)
    
    # Calculate word value (sum of character values)
    word_value = sum(char_values)
    
    # Calculate letter diversity
    unique_letters = len([c for c in char_count if c in alphabet])
    
    return word_value, unique_letters

# Sample text
text = "Python"

# Analyze the text
word_value, unique_letters = analyze_text(text)

print(f"Result: {word_value}")