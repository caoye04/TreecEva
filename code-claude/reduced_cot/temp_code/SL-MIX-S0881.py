from collections import Counter, defaultdict

# Text analysis function to find common words that meet specific criteria
def analyze_text(text, min_length=3, excluded_chars='!@#$%^&*()_+='):
    # Preprocessing text
    text = text.lower()
    for char in excluded_chars:
        text = text.replace(char, '')
    
    # Split into words
    all_words = text.split()
    
    # Count word frequencies
    word_counts = Counter(all_words)
    
    # Track words by their first letter
    words_by_letter = defaultdict(list)
    for word in all_words:
        if len(word) > 0:  # Ensure word is not empty
            words_by_letter[word[0]].append(word)
    
    # Sort letters by number of words
    letter_popularity = sorted(words_by_letter.items(), 
                              key=lambda x: len(x[1]), 
                              reverse=True)
    
    # Get most common words
    common_words = [word for word, count in word_counts.most_common(10)]
    
    # Filter words by length criteria
    filtered_words = [word for word in all_words if len(word) >= min_length]
    
    # Calculate average word length (distraction)
    avg_length = sum(len(word) for word in all_words) / len(all_words) if all_words else 0
    
    # Find words that are both filtered and common
    valid_words_count = len([word for word in filtered_words if word in common_words])
    
    # Calculate a popularity score (distraction)
    popularity_score = sum(word_counts[word] for word in common_words)
    
    # Count vowels in common words (distraction)
    vowels = 'aeiou'
    vowel_count = sum(1 for word in common_words for char in word if char in vowels)
    
    print(f"Result: {valid_words_count}")
    return valid_words_count

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The dog was not very lazy, but the fox was certainly quick. Brown is a color that the fox happened to be."

result = analyze_text(sample_text, min_length=4)