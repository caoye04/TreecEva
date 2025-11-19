from collections import defaultdict, Counter
import statistics

def calculate_quality_score(freq_map):
    if not freq_map:
        return 0
    values = list(freq_map.values())
    return sum(v * v for v in values) / len(values)

def process_sequences(sequences):
    results = []
    for seq in sequences:
        freq = Counter(seq)
        score = calculate_quality_score(freq)
        results.append(score)
    return results

# Batch of DNA sequences
lab_sequences = [
    "ATCGATCG",
    "GGCCTTAA",
    "TTAGGCTA",
    "CCGGAATT",
    "AACCGGTT",
    "TTTTCCCC"
]

scores = process_sequences(lab_sequences)
mean_score = statistics.mean(scores)
variance_score = statistics.variance(scores) if len(scores) > 1 else 0

# Filtering logic with short-circuit evaluation
filtered_count = 0
for i in range(len(scores)):
    condition_a = scores[i] >= mean_score
    condition_b = variance_score > 10
    # Ternary operator and short-circuit evaluation
    increment = 1 if (condition_a and condition_b) or (scores[i] > (mean_score + variance_score)**0.5) else 0
    filtered_count += increment

print(f"Result: {filtered_count}")