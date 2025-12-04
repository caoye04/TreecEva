import itertools

# Analyzing word patterns in a text corpus
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
filter_chars = ['a', 'e', 'i']

# Calculate average word length for reference
avg_length = sum(len(word) for word in words) / len(words)
print(f"Average length: {avg_length}")

# Extract words containing vowels for analysis
vowel_words = [word for word in words if any(vowel in word for vowel in 'aeiou')]

# Generate all possible word pairs for co-occurrence analysis
all_pairs = list(itertools.combinations(words, 2))

# Track word frequency for weighted scoring
char_freq = {}
for word in words:
    for char in word:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

# Calculate a relevance score based on shared characters
relevance_threshold = 1.5
shared_chars = []

for word1, word2 in all_pairs:
    # Find characters present in both words
    common = set(word1).intersection(set(word2))
    if len(common) > 0:
        shared_chars.append((word1, word2, common))

# Filter pairs based on specific criteria
filtered_pairs = []
for word1, word2 in all_pairs:
    # Skip pairs with the same starting character (distractor condition)
    if word1[0] == word2[0]:
        continue
        
    # Calculate combined length
    total_length = len(word1) + len(word2)
    
    # Only include pairs where at least one word contains a filter character
    has_filter_char = any(fc in word1 or fc in word2 for fc in filter_chars)
    
    # Include pairs meeting our criteria
    if has_filter_char and total_length > 9:
        filtered_pairs.append((word1, word2))

# Count unique valid combinations
valid_combinations = len(set(filtered_pairs))
print(f"Result: {valid_combinations}")