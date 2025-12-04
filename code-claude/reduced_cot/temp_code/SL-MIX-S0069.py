# Text analysis for website content evaluation
raw_text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."
filter_words = {"and", "was", "the"}

# Process text: convert to lowercase and remove punctuation
processed_text = raw_text.lower()
for char in ".,!?;:":
    processed_text = processed_text.replace(char, "")

# Count total words for reference
total_words = len(processed_text.split())

# Calculate unique words (excluding filter words)
unique_words = len(set(processed_text.split()))
significant_words = len([word for word in set(processed_text.split()) if word not in filter_words])

# Calculate text diversity score
diversity_ratio = significant_words / total_words if total_words > 0 else 0

print(f"Result: {unique_words}")