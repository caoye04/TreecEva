def analyze_text_patterns(text_data):
    char_frequency = {}
    for char in text_data:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    # Irrelevant computation: counts vowels but not used later
    vowel_count = sum(1 for c in char_frequency if c in 'aeiou')
    total_chars = sum(char_frequency.values())
    
    # Semi-relevant transformation: normalized frequencies (not directly used)
    normalized = {c: freq/total_chars for c, freq in char_frequency.items()}
    
    # Return top 3 most frequent characters
    sorted_chars = sorted(char_frequency.items(), key=lambda x: -x[1])
    return [item[0] for item in sorted_chars[:3]]


def compute_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 4)

# Main processing pipeline
text_sample = "Dynamic programming solves complex problems by breaking them down into simpler subproblems."

token_list = text_sample.split()
word_lengths = [len(word) for word in token_list if word.isalpha() or '-' not in word]
filtered_words = [word for word in token_list if len(word) > 2 and word[0].islower()]

# Distractor: unused list comprehension with slicing
reversed_short = [word[::-1] for word in token_list][:5]

# Key data structures
letter_grades = {'a': 90, 'b': 80, 'c': 70, 'd': 60, 'f': 0}
metrics = []
for i, word in enumerate(filtered_words):
    metric_val = (len(word) * (i+1)) % 7
    metrics.append(metric_val)

# Additional noise: dead code path with misleading name
if len(metrics) > 100:
    adjustment_factor = 0.9
else:
    adjustment_factor = 1.0  # never applied

# Weight assignment with slicing distraction
base_weights = list(range(1, 10))[2:6]  # takes [3,4,5,6]
weights = [w ** 0.5 for w in base_weights]

# Another red herring: set operation that computes nothing new
unique_lengths = set([len(w) for w in filtered_words])
length_distribution = sorted(list(unique_lengths))

# Real computation begins here
weighted_sum = 0
for i in range(min(len(metrics), len(weights))):
    weighted_sum += metrics[i] * weights[i]

normalization_constant = sum(weights[:len(metrics)])
if normalization_constant != 0:
    normalized_score = weighted_sum / normalization_constant
else:
    normalized_score = 0

# Final evaluation function
def evaluate_performance(mets, wgts):
    temp_results = []
    for a, b in zip(mets, wgts):
        temp_results.append(a * b * 0.1)
    intermediate_total = sum(temp_results)
    
    # Nested logic with short-circuiting (semi-relevant)
    bonus = 10 if len(mets) >= 4 and (intermediate_total > 5 or True and False) else 0
    
    # Core answer calculation
    base_value = intermediate_total * 100
    return int(base_value) + bonus

# Execute main logic
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")