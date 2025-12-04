# Analyze text for unique character distribution

text = "Hello, World! Python is amazing."

# Remove some punctuation marks
punctuation = [",", ".", "!", "?", ";"]
filtered_text = ""

for char in text:
    if char not in punctuation:
        filtered_text += char

# Count total characters for reference
total_chars = len(filtered_text)

# Extract words for potential future analysis
words = filtered_text.split()
word_count = len(words)

# Find number of unique characters (case-insensitive)
unique_chars = len(set([c.lower() for c in filtered_text]))

# Calculate the average word length for comparison
avg_word_length = sum(len(word) for word in words) / word_count

print(f"Result: {unique_chars}")