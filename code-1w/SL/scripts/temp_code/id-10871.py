def analyze_sentiment(char):
    return 1 if char in 'aeiou' else -1

# Simulate user feedback sequence from a customer survey tool
customer_inputs = ['satisfied', 'good service', 'needs improvement', 'excellent', 'poor']
feedback_sequence = ''.join([word.replace(' ', '').lower() for word in customer_inputs])

# Irrelevant preprocessing: count consonants (not used in final logic)
consonant_count = sum(1 for c in feedback_sequence if c.isalpha() and c not in 'aeiou')

# Distractor function: computes average length but not used
def avg_word_length(words):
    return sum(len(w) for w in words) / len(words) if words else 0

mean_length = avg_word_length(customer_inputs)  # Dead computation

# Core sentiment scoring using lambda and enumerate
sentiment_shifts = []
sentiment_baseline = 50

for i, char in enumerate(feedback_sequence):
    modifier = (i % 5) // 2  # Position-based weight
    sentiment_shifts.append(analyze_sentiment(char) * (modifier + 1))

# Use zip to pair shifts with mirrored values for symmetry analysis (only partial use)
symmetry_pairs = list(zip(sentiment_shifts, reversed(sentiment_shifts)))
energy_levels = [abs(a + b) for a, b in symmetry_pairs][::2]  # Every other pair

# Secondary distraction: compute entropy-like measure (unused)
from math import log2
if energy_levels:
    total_energy = sum(energy_levels)
    entropy = sum((e / total_energy) * log2(e / total_energy + 1e-9) for e in energy_levels)

# Actual performance evaluation using lambda over filtered shifts
valid_shifts = [x for x in sentiment_shifts if x != 0]
evaluate_performance = lambda seq: sum(valid_shifts) + len(seq) // 10

final_score = evaluate_performance(feedback_sequence)

# Print result as required
print(f"Target result: {final_score}")