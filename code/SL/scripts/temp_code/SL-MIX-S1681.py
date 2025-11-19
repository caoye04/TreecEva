from itertools import combinations

# Poetic analysis system
phoneme_endings = ['AT', 'AN', 'OP', 'OT', 'IN', 'IM']

# Lambda to check if two phonemes create a rhyme (same ending)
create_rhyme = lambda p1, p2: p1[-1] == p2[-1]

# Calculate all possible phoneme pair combinations
phoneme_pairs = list(combinations(phoneme_endings, 2))

# Count unique rhyming combinations using set for automatic deduplication
rhyming_combinations = {pair for pair in phoneme_pairs if create_rhyme(pair[0], pair[1])}

# Poetic diversity score is the count of unique rhyming combinations
poetic_diversity_score = len(rhyming_combinations)

print(f"Result: {poetic_diversity_score}")