from collections import Counter, defaultdict
import itertools

text = "the quick brown fox jumps over the lazy dog while the dog barks at the fox"

# Process text to analyze word frequencies
words = text.lower().split()
word_freq = Counter(words)

# Track word positions for potential analysis
word_positions = defaultdict(list)
for i, word in enumerate(words):
    word_positions[word].append(i)

# Calculate average word length for filtering criteria
avg_length = sum(len(word) for word in words) / len(words)
print(f"Average word length: {avg_length:.2f}")

# Create groups based on word length
short_words = [word for word in words if len(word) < 4]
medium_words = [word for word in words if 3 < len(word) < 6]
long_words = [word for word in words if len(word) >= 5]

# Some statistics that aren't directly used in the final calculation
total_chars = sum(len(word) for word in words)
max_freq = max(word_freq.values())
min_freq = min(word_freq.values())

# Filter words based on frequency and position
filtered_words = []
for word in words:
    # Words that appear exactly twice or are longer than average
    if word_freq[word] == 2 or len(word) > avg_length:
        filtered_words.append(word)

# Create pairs for analysis (not used in final result)
word_pairs = list(itertools.combinations(set(words), 2))
sample_pairs = word_pairs[:3] if word_pairs else []

# Count unique words after filtering
unique_word_count = len(set(filtered_words))

# Additional processing that doesn't affect the result
sorted_filtered = sorted(filtered_words)
reversed_filtered = list(reversed(filtered_words))

print(f"Result: {unique_word_count}")