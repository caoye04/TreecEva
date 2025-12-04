import itertools

def is_valid_pair(pair):
    # Check if the pair elements are compatible
    word1, word2 = pair
    # Valid pairs have the last character of word1 matching the first of word2
    return word1[-1] == word2[0]

# Available words for creating pairs
available_words = ['apple', 'egg', 'grape', 'elephant', 'tiger', 'rabbit']

# Generate all possible combinations of two words
all_combos = list(itertools.combinations(available_words, 2))

# Filter combinations where the words have different lengths
filtered_combos = [(w1, w2) for w1, w2 in all_combos if len(w1) != len(w2)]

# Count how many of these filtered combinations form valid pairs
valid_combinations = sum(1 for combo in filtered_combos if is_valid_pair(combo))

# Display results
print(f"Total combinations: {len(all_combos)}")
print(f"Filtered combinations: {len(filtered_combos)}")
print(f"Result: {valid_combinations}")