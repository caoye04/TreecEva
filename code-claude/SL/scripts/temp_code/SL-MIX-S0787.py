from collections import Counter
import itertools

# Analyzing frequency of words in a document
document = "machine learning algorithms require data science skills and programming knowledge"
words = document.split()

# Count word occurrences by length
word_lengths = [len(word) for word in words]
avg_length = sum(word_lengths) / len(word_lengths)

# Process words based on their length
filtered_words = list(filter(lambda w: len(w) >= 5, words))

# Create frequency counter of filtered words
word_freq = Counter(filtered_words)

# Add some domain-specific words that weren't in original text
extra_terms = ['neural', 'networks']
for term in extra_terms:
    word_freq[term] = 1

# Remove words related to general skills
for skill in ['programming', 'skills']:
    if skill in word_freq:
        del word_freq[skill]

# Calculate final count of relevant technical terms
optimized_count = sum(word_freq.values())

# Round to nearest integer if needed
final_result = int(optimized_count)
print(f"Result: {final_result}")