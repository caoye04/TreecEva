# Analyzing common words between two text samples

text_a = "The quick brown fox jumps over the lazy dog"
text_b = "A quick dog barks at the fox in the yard"

# Convert to lowercase for better comparison
text_a = text_a.lower()
text_b = text_b.lower()

# Split texts into words
words_a = text_a.split()
words_b = text_b.split()

# Words to exclude from analysis
stop_words = {'the', 'a', 'at', 'in'}

# Filter out stop words
filtered_words_a = [word for word in words_a if word not in stop_words]
filtered_words_b = [word for word in words_b if word not in stop_words]

# Find common words between the filtered texts
common_words = set(filtered_words_a) & set(filtered_words_b)

# Count total unique words across both texts
all_unique_words = set(filtered_words_a) | set(filtered_words_b)
total_unique = len(all_unique_words)

# Calculate the result
result = len(common_words)

print(f"Result: {result}")