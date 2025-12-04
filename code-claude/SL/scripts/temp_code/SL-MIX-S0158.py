from collections import Counter, defaultdict

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count occurrences of each word
    word_frequencies = Counter(words)
    
    # Track words by their length
    words_by_length = defaultdict(list)
    for word in words:
        words_by_length[len(word)].append(word)
    
    # Calculate some statistics
    total_words = len(words)
    unique_word_count = len(word_frequencies)
    
    # Find most common word length
    length_frequencies = {length: len(word_list) for length, word_list in words_by_length.items()}
    most_common_length = max(length_frequencies.items(), key=lambda x: x[1])[0] if length_frequencies else 0
    
    # Calculate a weighted score based on word frequencies
    weighted_score = sum(freq * (len(word) == most_common_length) for word, freq in word_frequencies.items())
    
    # Find words that appear exactly once
    unique_appearances = [word for word, count in word_frequencies.items() if count == 1]
    singleton_count = len(unique_appearances)
    
    # Calculate average word length (not used in final result)
    avg_length = sum(len(word) * freq for word, freq in word_frequencies.items()) / total_words if total_words > 0 else 0
    
    return {
        'total_words': total_words,
        'unique_words': unique_word_count,
        'most_common_length': most_common_length,
        'weighted_score': weighted_score,
        'singleton_count': singleton_count
    }

# Sample text
sample_text = "The quick brown fox jumps over the lazy dog. The dog was not very lazy after all."

# Process the text
results = analyze_text(sample_text)

# Extract key metrics
total_word_count = results['total_words']
unique_word_count = results['unique_words']
common_length = results['most_common_length']

# Some additional processing (not affecting the answer)
if unique_word_count > 10:
    importance_factor = 2
else:
    importance_factor = 1

quality_score = total_word_count * importance_factor

# Print the result we're interested in
print(f"Result: {unique_word_count}")