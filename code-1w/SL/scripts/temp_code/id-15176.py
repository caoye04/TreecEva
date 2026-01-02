from collections import defaultdict

# Simulate word frequency analysis with scoring modifiers
text_block = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text_block.split()

# Count word frequencies using defaultdict
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1

# Define modifier rules based on word length
modifier_rules = lambda length: 1.5 if length > 4 else 0.8

# Apply modifiers to each word's count
modifiers = {word: modifier_rules(len(word)) for word in word_counts}

# Irrelevant distraction: unused variable (minimal interference)
dummy_sum = sum([len(w) for w in words])

# Calculate final score: sum of (count * modifier) for each unique word
calculate_total = lambda counts, mods: sum(counts[w] * mods[w] for w in counts)
final_score = calculate_total(word_counts, modifiers)

print(f"Result: {final_score}")