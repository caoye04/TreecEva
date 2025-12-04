# Text analysis for a small corpus
def count_words(text):
    return len(text.split())

# Sample text from a children's story
story = "The cat sat on the mat. The dog jumped over the fence. The cat and dog played together."

# Process the text
words = story.split()
total_words = count_words(story)
avg_word_length = sum(len(word) for word in words) / total_words

# Count unique words (case-insensitive)
unique_words = len(set(word.lower() for word in words))

# Count words starting with 't' or 'T'
t_words = sum(1 for word in words if word.lower().startswith('t'))

# Calculate a score based on unique words and total words
diversity_score = (unique_words / total_words) * 100

print(f"Result: {unique_words}")