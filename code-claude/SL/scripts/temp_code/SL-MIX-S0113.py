def analyze_text(text):
    # Count word frequencies
    word_counts = {}
    for word in text.lower().split():
        clean_word = ''.join(c for c in word if c.isalnum())
        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
    
    # Find words with highest frequency
    max_freq = max(word_counts.values()) if word_counts else 0
    popular_words = [word for word, count in word_counts.items() if count == max_freq]
    
    # Calculate letter statistics
    all_letters = ''.join(word_counts.keys())
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    vowel_count = sum(1 for c in all_letters if c in vowels)
    consonant_count = sum(1 for c in all_letters if c in consonants)
    
    # Process the most popular word with the most letters
    chosen_word = max(popular_words, key=len) if popular_words else ''
    
    # Filter the word to keep only letters that appear in both vowels and consonants sets
    # (This is a distraction - no letter can be both a vowel and consonant)
    both_sets = vowels.intersection(consonants)
    filtered_word = chosen_word
    
    # Apply a transformation based on letter position
    transformed = ''
    for i, char in enumerate(filtered_word):
        if i % 2 == 0 and char in vowels:
            transformed += char.upper()
        else:
            transformed += char
    
    # Calculate unique letters in the word
    unique_letters = len(set(filtered_word))
    
    # Calculate a meaningless metric (distraction)
    complexity_score = (vowel_count * 1.5) - (consonant_count * 0.5)
    
    print(f"Most frequent word: {chosen_word}")
    print(f"Unique letters: {unique_letters}")
    return unique_letters

sample_text = "the quick brown fox jumps over the lazy dog"
result = analyze_text(sample_text)
print(f"Result: {result}")