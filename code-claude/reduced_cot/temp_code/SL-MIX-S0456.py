# Text analysis for a book review website
words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']
min_length = 3
target_letter = 'l'

# Count words that meet review highlight criteria
prefix_words = [w for w in words if w.startswith(target_letter)]
total_words = len(words)
long_words = len([w for w in words if len(w) > min_length])

# Find words that are both long and start with the target letter
filtered_count = len([w for w in words if len(w) > min_length and w.startswith(target_letter)])

# Calculate percentage of filtered words
if total_words > 0:
    percentage = (filtered_count / total_words) * 100
else:
    percentage = 0

print(f"Result: {filtered_count}")