# Function to analyze word frequency in text samples
def count_unique_words(text_sample):
    words = text_sample.lower().split()
    return {word: words.count(word) for word in set(words)}

# Sample text from different categories
science_sample = "stars planets gravity universe atoms molecules"
art_sample = "canvas paint colors brush artist gallery"
mixed_sample = "stars colors canvas gravity atoms artist"

# Count words in mixed sample
word_counts = count_unique_words(mixed_sample)

# Category-specific tags
science_tags = {"stars", "planets", "gravity", "universe", "atoms"}
art_tags = {"canvas", "paint", "colors", "brush", "artist"}

# Combined category tags
category_tags = science_tags | art_tags

# Find overlap between sample words and category tags
unique_elements = len(set(word_counts.keys()) & set(category_tags))
print(f"Result: {unique_elements}")