from collections import Counter, defaultdict

def process_text(text):
    # Remove punctuation and convert to lowercase
    processed = ''.join(c.lower() if c.isalnum() else ' ' for c in text)
    return processed

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
processed_text = process_text(sample_text)

# Split into words
words = processed_text.split()

# Track word lengths for potential analysis
word_lengths = [len(word) for word in words]
avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
median_length = sorted(word_lengths)[len(word_lengths)//2] if word_lengths else 0

# Create word frequency counter
word_stats = Counter(words)

# Calculate some statistics (some relevant, some not)
max_word = max(words, key=len)
min_word = min(words, key=len)
word_variety = len(word_stats) / len(words) if words else 0

# Group words by their first letter
first_letter_groups = defaultdict(list)
for word in words:
    if word:
        first_letter_groups[word[0]].append(word)

# Count words starting with each letter
letter_counts = {letter: len(words) for letter, words in first_letter_groups.items()}

# Find the most common letter to start a word
most_common_letter = max(letter_counts.items(), key=lambda x: x[1]) if letter_counts else ('', 0)

# Find the word with highest frequency
highest_frequency = max(word_stats.values())

# Create a reversed mapping of frequency to words
freq_to_words = defaultdict(list)
for word, freq in word_stats.items():
    freq_to_words[freq].append(word)

# Words that appear exactly twice
double_words = freq_to_words.get(2, [])

# Total characters in the text (excluding spaces and punctuation)
char_count = sum(len(word) for word in words)

print(f"Result: {highest_frequency}")