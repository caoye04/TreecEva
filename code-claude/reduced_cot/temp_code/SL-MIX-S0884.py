import itertools

def count_filtered_words(input_text):
    # Split text into words and convert to lowercase
    words = input_text.lower().split()
    
    # Filter out words that contain digits
    clean_words = [word for word in words if not any(char.isdigit() for char in word)]
    
    # Remove punctuation from words
    processed_words = [word.strip('.,!?;:()"') for word in clean_words]
    
    # Count words with more than 3 characters
    long_words = [word for word in processed_words if len(word) > 3]
    
    # Group identical words using itertools
    sorted_words = sorted(long_words)
    grouped_words = [(word, len(list(group))) for word, group in itertools.groupby(sorted_words)]
    
    # Count unique words that appear more than once
    frequent_words = len([word for word, count in grouped_words if count > 1])
    
    return frequent_words

# Sample text for analysis
text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Process text and count words
word_frequency = count_filtered_words(text)

# Display result
print(f"Result: {word_frequency}")