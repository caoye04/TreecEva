import itertools

def is_valid_word(word):
    # Valid words have at least 3 characters and contain more vowels than consonants
    vowels = 'aeiou'
    vowel_count = sum(1 for char in word.lower() if char in vowels)
    consonant_count = len(word) - vowel_count
    return len(word) >= 3 and vowel_count > consonant_count

# Sample text from a document on plant species
text = "Aloe Vera is a medicinal plant. Eucalyptus and Oak are trees. Rose, Daisy, and Lily are beautiful flowers."

# Process the text by removing punctuation and splitting into words
punctuation = '.,:;!?'
processed_text = ''.join(char if char not in punctuation else ' ' for char in text)
lower_text = processed_text.lower()

# Split into words and apply some transformations
words = lower_text.split()

# Create pairs of words (not used in final calculation)
word_pairs = list(itertools.combinations(words, 2))
pair_count = len(word_pairs)

# Calculate average word length (not used in final calculation)
avg_length = sum(len(word) for word in words) / len(words)
rounded_avg = round(avg_length, 2)

# Apply a filter to get unique words
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Process words by removing common words
common_words = ['is', 'are', 'and', 'the', 'a']
processed_words = [word for word in unique_words if len(word) > 1]

# Calculate number of valid words according to our criteria
valid_count = sum(1 for word in processed_words if is_valid_word(word))

# Additional calculations (not affecting the result)
max_word_length = max(len(word) for word in processed_words)
min_word_length = min(len(word) for word in processed_words)
length_difference = max_word_length - min_word_length

print(f"Result: {valid_count}")