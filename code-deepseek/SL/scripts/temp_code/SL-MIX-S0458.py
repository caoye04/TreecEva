from collections import Counter

# Analyze word frequency in a sample text
sample_text = "python programming python code python algorithm python data python structure"
words = sample_text.split()
word_counter = Counter(words)

# Calculate some intermediate values for analysis
total_words = len(words)
unique_words = len(word_counter)

# Find frequency of target word
target_word = "python"
final_count = word_counter[target_word]

print(f"Result: {final_count}")