from collections import Counter, defaultdict

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    clean_text = ''
    for char in text:
        if char.isalnum() or char.isspace():
            clean_text += char.lower()
        
    # Split into words
    words = clean_text.split()
    
    # Count word frequencies
    word_freq = Counter(words)
    most_common_word = word_freq.most_common(1)[0][0]
    least_common_count = min(word_freq.values())
    
    # Calculate average word length
    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words) if words else 0
    
    # Track word lengths
    word_lengths = [len(word) for word in words]
    word_length_counts = Counter(word_lengths)
    
    # Create a mapping of length to words
    length_to_words = defaultdict(list)
    for word in words:
        length_to_words[len(word)].append(word)
    
    # Find longest and shortest words
    max_length = max(word_lengths) if word_lengths else 0
    min_length = min(word_lengths) if word_lengths else 0
    
    # Calculate some statistics that won't affect the final result
    unique_words = len(word_freq)
    vowel_count = sum(char in 'aeiou' for char in clean_text)
    consonant_count = sum(char.isalpha() and char not in 'aeiou' for char in clean_text)
    
    # Find the most common word length
    most_common_word_length = word_length_counts.most_common(1)[0][0]
    
    # Calculate a complexity score (not used in final result)
    complexity = (avg_length * unique_words) / (max_length if max_length > 0 else 1)
    
    return most_common_word_length

# Sample text for analysis
sample = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."
result = analyze_text(sample)
print(f"Result: {result}")
