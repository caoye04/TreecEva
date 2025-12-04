# Text analysis of common and rare words in sample documents

doc1 = "the quick brown fox jumps over the lazy dog"
doc2 = "pack my box with five dozen liquor jugs"
doc3 = "how vexingly quick daft zebras jump"

# Extract all words from documents
doc1_words = set(doc1.split())
doc2_words = set(doc2.split())
doc3_words = set(doc3.split())

# Calculate frequency metrics
total_words = doc1_words.union(doc2_words).union(doc3_words)
word_count = len(total_words)
max_word_length = max(len(word) for word in total_words)

# Find words that appear in at least 2 documents
common_words = (doc1_words.intersection(doc2_words) | 
               doc1_words.intersection(doc3_words) | 
               doc2_words.intersection(doc3_words))

# Create a set of words with unusual letter patterns
unusual_letter_words = set()
for word in total_words:
    if 'q' in word or 'z' in word or 'x' in word:
        unusual_letter_words.add(word)
    elif len(word) > 5 and 'j' in word:
        unusual_letter_words.add(word)

# Analysis of character distribution
vowel_counts = {}
for word in total_words:
    vowel_count = sum(1 for char in word if char.lower() in 'aeiou')
    vowel_counts[word] = vowel_count

# Calculate average vowels per word
average_vowels = sum(vowel_counts.values()) / len(vowel_counts)

# Words with above average vowel count
vowel_rich_words = {word for word, count in vowel_counts.items() if count > average_vowels}

# Words that appear in exactly one document
rare_words = total_words - common_words

# Words that are both rare and have unusual letters
special_words = rare_words.intersection(unusual_letter_words)
special_count = len(special_words)

# Calculate the overlap between common words and rare words
unique_elements = len(common_words.intersection(rare_words))

# Additional metrics that don't affect the final result
average_word_length = sum(len(word) for word in total_words) / word_count
long_words = {word for word in total_words if len(word) > 4}
long_word_ratio = len(long_words) / word_count

print(f"Result: {unique_elements}")