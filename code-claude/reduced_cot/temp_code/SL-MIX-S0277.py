import itertools

def word_filter(text, min_length=3):
    """Filter words by minimum length"""
    words = text.lower().split()
    return [word for word in words if len(word) >= min_length]

# Sample phrases from a language learning application
phrase1 = "programming challenges improve logical thinking skills"
phrase2 = "algorithms require careful implementation"
phrase3 = "logical reasoning helps solve complex problems"

# Process phrases with different parameters
processed_phrases = []
for phrase in [phrase1, phrase2, phrase3]:
    # Apply word filtering with default parameter
    filtered = word_filter(phrase)
    processed_phrases.append(filtered)

# Calculate similarity metrics
total_words = sum(len(phrase) for phrase in processed_phrases)
avg_word_length = sum(len(word) for phrase in processed_phrases for word in phrase) / total_words

# Find words that appear in all phrases (not used in final calculation)
common_words = set(processed_phrases[0])
for phrase in processed_phrases[1:]:
    common_words &= set(phrase)

# Generate all possible pairs for comparison
phrase_pairs = list(itertools.combinations(range(len(processed_phrases)), 2))
pair_similarities = []

# Calculate similarity between pairs (distraction)
for i, j in phrase_pairs:
    shared = len(set(processed_phrases[i]) & set(processed_phrases[j]))
    pair_similarities.append(shared)

# Select phrases for letter analysis
filtered_words = []
for i, phrase in enumerate(processed_phrases):
    # Select words based on position
    if i == 0:
        selected = phrase[0:3]  # First three words from first phrase
    elif i == 1:
        selected = phrase[1:3]  # Second and third words from second phrase
    else:
        selected = phrase[0:2]  # First two words from third phrase
    filtered_words.append(''.join(selected))

# Count unique letters in each filtered text
unique_letters = [len(set(text)) for text in filtered_words]

# Find letters common to all three filtered texts
common_letters = len(set(filtered_words[0]) & set(filtered_words[1]) & set(filtered_words[2]))

# Calculate a weighted metric (not used in final result)
weighted_metric = sum(unique_letters) - 2 * common_letters

print(f"Result: {common_letters}")