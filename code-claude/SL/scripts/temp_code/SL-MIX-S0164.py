# Analyzing text data for words with common prefixes
text = "The theater is showing theatrical performances that are theoretically entertaining"
words = text.lower().split()

# Find the most common 3-letter prefix
prefix_dict = {}
for word in words:
    if len(word) >= 3:
        prefix = word[:3]
        prefix_dict[prefix] = prefix_dict.get(prefix, 0) + 1

# Get the most frequent prefix
common_prefix = ""
max_count = 0
for prefix, frequency in prefix_dict.items():
    if frequency > max_count:
        max_count = frequency
        common_prefix = prefix

# Count words that start with the most common prefix
count = len([word for word in words if word.startswith(common_prefix)])

# Some additional operations with the text
total_chars = sum(len(word) for word in words)
avg_word_length = total_chars / len(words)

print(f"Result: {count}")