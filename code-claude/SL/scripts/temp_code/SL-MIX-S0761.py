from collections import Counter

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalpha() else ' ' for c in text)
    
    # Split into words and count occurrences
    words = cleaned_text.split()
    word_count = len(words)
    
    # Find longest word
    longest_word = max(words, key=len) if words else ""
    longest_length = len(longest_word)
    
    # Count character frequencies in the text
    char_counter = Counter(c for c in cleaned_text if c.isalpha())
    most_common_char = char_counter.most_common(1)[0][0] if char_counter else ""
    
    # Create word stats using first letters
    word_stats = {}
    for word in words:
        if word:
            first_letter = word[0]
            word_stats[first_letter] = word_stats.get(first_letter, 0) + 1
    
    # Get the highest frequency count
    character_frequency = max(word_stats.values())
    
    return {
        "word_count": word_count,
        "longest_word": longest_word,
        "most_common_char": most_common_char,
        "character_frequency": character_frequency
    }

sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick!"
result = analyze_text(sample_text)
print(f"Result: {result['character_frequency']}")