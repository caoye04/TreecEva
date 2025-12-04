# Word frequency analyzer for text processing

def word_processor(text):
    # Convert to lowercase and split by spaces
    words = text.lower().split()
    
    # Process words to remove punctuation
    cleaned_words = [word.strip('.,!?;:"()') for word in words]
    return cleaned_words

# Sample text from a short poem
text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."

# Dictionary to track word occurrences (not used in final calculation)
word_counts = {}
for word in word_processor(text):
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Lambda function to get most common words (not used in final calculation)
get_common = lambda d: [k for k, v in d.items() if v > 1]
common_words = get_common(word_counts)

# Calculate number of unique words
unique_words = len(set(word_processor(text)))

print(f"Result: {unique_words}")