from collections import defaultdict, Counter

# Text analysis for a research paper
def analyze_text(text):
    # Clean and normalize text
    normalized = text.lower().replace(',', '').replace('.', '')
    
    # Split into words
    words = normalized.split()
    
    # Count total words for statistics
    total_words = len(words)
    unique_words = len(set(words))
    
    # Track word frequencies
    word_frequencies = defaultdict(int)
    for word in words:
        if len(word) > 2:  # Only count words with more than 2 characters
            word_frequencies[word] += 1
    
    # Find most common words
    word_counter = Counter(word_frequencies)
    most_common_words = [word for word, _ in word_counter.most_common(3)]
    
    # Calculate character frequency (not used in final result)
    char_count = defaultdict(int)
    for char in normalized:
        if char.isalpha():
            char_count[char] += 1
    
    # Find difference between top two word frequencies
    if len(most_common_words) >= 2:
        top_frequency_difference = abs(word_frequencies[most_common_words[0]] - word_frequencies[most_common_words[1]])
    else:
        top_frequency_difference = 0
    
    # Calculate average word length (distractor)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Calculate modular sum of character frequencies (distractor)
    mod_sum = sum(count % 10 for count in char_count.values())
    
    return top_frequency_difference

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Perform analysis
result = analyze_text(sample_text)
print(f"Result: {result}")