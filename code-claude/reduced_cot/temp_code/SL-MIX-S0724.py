from collections import Counter

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Calculate some statistics
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    max_length = max(len(word) for word in words) if words else 0
    
    # Filter words by length
    short_words = {word: count for word, count in word_counts.items() if len(word) <= 3}
    medium_words = {word: count for word, count in word_counts.items() if 4 <= len(word) <= 6}
    long_words = {word: count for word, count in word_counts.items() if len(word) > 6}
    
    # Calculate word type ratios (not used in final calculation)
    short_ratio = sum(short_words.values()) / len(words) if words else 0
    medium_ratio = sum(medium_words.values()) / len(words) if words else 0
    long_ratio = sum(long_words.values()) / len(words) if words else 0
    
    # Create a scoring system based on word length
    word_scores = {}
    for word, count in word_counts.items():
        if len(word) <= 3:
            word_scores[word] = count * 1
        elif 4 <= len(word) <= 6:
            word_scores[word] = count * 2
        else:
            word_scores[word] = count * 3
    
    # Calculate total score (not used in final result)
    total_score = sum(word_scores.values())
    
    # Return word statistics
    return word_counts, avg_word_length, max_length, word_scores

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Analyze the text
word_stats, avg_length, max_len, scores = analyze_text(sample_text)

# Calculate letter frequencies (not used in final calculation)
letter_freq = Counter(''.join(sample_text.lower()).replace(' ', ''))
most_common_letter = letter_freq.most_common(1)[0][0]

# Filter some words for display purposes
filtered_words = [word for word, count in word_stats.items() if count > 1]

# Calculate the frequency sum - this is our target
total_frequency = sum(word_stats.values())

# Calculate another metric that's not directly used
average_frequency = total_frequency / len(word_stats) if word_stats else 0

# Display results
print(f"Number of unique words: {len(word_stats)}")
print(f"Average word length: {avg_length:.2f}")
print(f"Words appearing more than once: {filtered_words}")
print(f"Result: {total_frequency}")