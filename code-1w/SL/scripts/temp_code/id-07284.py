from collections import defaultdict

# Simulate document-term analysis with positional scoring
text = "the quick brown fox jumps over the lazy dog and the brown cat jumps too"
words = text.split()

# Track first occurrence and frequency
first_occurrence = {}
frequency_count = defaultdict(int)
position_sum = defaultdict(int)

for idx, word in enumerate(words):
    frequency_count[word] += 1
    position_sum[word] += idx
    if word not in first_occurrence:
        first_occurrence[word] = idx

# Misleading distraction: secondary analysis on letter counts
letter_frequency = defaultdict(int)
for word in words:
    for char in word:
        letter_frequency[char] += 1

# Compute vowel density per word (irrelevant but plausible)
vowel_density = {}
for word in set(words):
    vowels = sum(1 for c in word if c in 'aeiou')
    vowel_density[word] = round(vowels / len(word), 3) if len(word) > 0 else 0

# Focus back on relevance: weight by inverse frequency and position
relevance_scores = {}
max_freq = max(frequency_count.values())
for word, freq in frequency_count.items():
    inv_freq = (1 / freq)
    avg_position = position_sum[word] / freq
    # Normalize average position to 0-1 scale
    norm_position = avg_position / (len(words) - 1)
    relevance_scores[word] = inv_freq * (1 - norm_position)

# Build relevance count vector for unique words in order of appearance
unique_words = list(dict.fromkeys(words))
relevance_counts = [round(relevance_scores[word], 4) for word in unique_words]

# Position-based weights: earlier positions more important
position_weights = [round((len(unique_words) - i) / len(unique_words), 3) for i in range(len(unique_words))]

# Dead code path: alternative weighting (never used)
if len(unique_words) > 20:
    position_weights = [w * 1.5 for w in position_weights]
elif len(unique_words) > 10:
    temp_weights = [w ** 2 for w in position_weights]  # unused
else:
    scaling_factor = 0.8
    smoothed_weights = [w * scaling_factor for w in position_weights]  # defined but unused

# Introduce noise variables
normalization_constant = sum(position_weights)
dummy_shift = sum(1 for w in vowel_density.values() if w > 0.3)
phantom_score = sum(letter_frequency.values()) / 26

# Core computation: weighted average of relevance by position importance
def calculate_weighted_average(values, weights):
    if not values or not weights or len(values) != len(weights):
        return 0.0
    total_weight = 0.0
    weighted_sum = 0.0
    for v, w in zip(values, weights):
        weighted_sum += v * w
        total_weight += w
    return round(weighted_sum / total_weight, 4) if total_weight != 0 else 0.0

# Final score calculation
temp_result = calculate_weighted_average(relevance_counts, position_weights)
scaling_offset = len(first_occurrence.get('the', 0).to_bytes(1, 'big')) if 'the' in first_occurrence else 0  # red herring
final_score = int(round(temp_result * 1000 + scaling_offset))

print(f"Result: {final_score}")