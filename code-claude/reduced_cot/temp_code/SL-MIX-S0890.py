text = "The quick brown fox jumps over the lazy dog"

# Convert to lowercase for processing
lowercase_text = text.lower()

# Remove punctuation if needed
clean_text = lowercase_text.replace('.', '').replace(',', '')

# Split into words
all_words = clean_text.split()

# Filter out common words
common_words = ['the', 'over']
filtered_words = [word for word in all_words if word not in common_words]

# Define minimum word length
min_length = 4

# Get words meeting the length requirement
valid_words = [word for word in filtered_words if len(word) >= min_length]

# Count vowels in each word (just for analysis)
vowel_counts = {word: sum(1 for char in word if char in 'aeiou') for word in valid_words}

print(f"Result: {len(valid_words)}")