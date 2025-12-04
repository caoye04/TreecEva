# Text processing utility to analyze word frequencies in academic papers

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    import string
    cleaned = ''.join(char.lower() if char not in string.punctuation else ' ' for char in text)
    return cleaned

# Sample abstract from a research paper
abstract = "Machine learning models have demonstrated remarkable performance across various domains. However, their black-box nature often limits transparency and interpretability. This paper proposes a novel framework for explainable AI that maintains high accuracy while providing meaningful explanations."

# Process the abstract
processed_text = preprocess_text(abstract)

# Split into words
all_words = processed_text.split()

# Some common academic stopwords
stopwords = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'that', 'this', 'their'}

# Filter out stopwords
filtered_words = [word for word in all_words if word not in stopwords]

# Calculate word statistics
total_words = len(all_words)
removed_words = total_words - len(filtered_words)

# Initialize parameters
min_length = 5  # Only consider words with at least 5 characters
max_length = 12  # Track words with at most 12 characters (not used in final calculation)

# Calculate unique words for a different analysis (not used in final calculation)
unique_words = set(filtered_words)
unique_count = len(unique_words)

# Find words that exceed max_length (not used in final calculation)
long_words = [word for word in filtered_words if len(word) > max_length]
long_count = len(long_words)

# Create a frequency distribution (not directly used in final answer)
word_freq = {}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Get words that appear more than once (not used in final calculation)
repeated_words = {word for word, count in word_freq.items() if count > 1}

# Count words meeting minimum length criteria
valid_word_count = sum(1 for word in filtered_words if len(word) >= min_length)

# Calculate average word length (not used in final calculation)
avg_length = sum(len(word) for word in filtered_words) / len(filtered_words) if filtered_words else 0

# Apply a transformation formula (not used in final calculation)
transformed_count = lambda count, factor: count * factor
adjusted_count = transformed_count(valid_word_count, 1.5)

print(f"Result: {valid_word_count}")