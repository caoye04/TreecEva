from collections import Counter

# Analyze text for unique characters after filtering
text = "Hello, World! Programming is fun."
filtered_text = ""

# Convert to lowercase for consistency
lowercase_text = text.lower()

# Count character frequencies
char_counts = Counter(lowercase_text)

# Filter out non-alphabetic characters
for char in lowercase_text:
    if char.isalpha() or char.isspace():
        filtered_text += char

# Calculate statistics
total_chars = len(filtered_text)
word_count = len(filtered_text.split())
unique_chars = len(set(filtered_text))
most_common = char_counts.most_common(1)[0][0]

print(f"Result: {unique_chars}")