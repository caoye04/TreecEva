from collections import defaultdict

# Simulate a ranking system for a coding contest with weighted scoring
participants = ['Alice', 'Bob', 'Charlie', 'Diana']
raw_scores = [85, 92, 78, 96]
penalties = [5, 10, 0, 8]

# Apply penalties to raw scores
adjusted_scores = [max(0, raw - pen) for raw, pen in zip(raw_scores, penalties)]

# Normalize scores to 0-100 scale using min-max normalization
min_score, max_score = min(adjusted_scores), max(adjusted_scores)
normalized_scores = [(s - min_score) / (max_score - min_score) * 100 for s in adjusted_scores] if max_score > min_score else [100] * len(adjusted_scores)

# Assign rankings based on normalized scores
rankings = defaultdict(int)
for idx, score in enumerate(normalized_scores):
    rankings[participants[idx]] = score

# Misleading: irrelevant computation on reversed list
reversed_ranks = sorted(normalized_scores, reverse=True)
temp_sum = sum(reversed_ranks[i] * (i + 1) for i in range(len(reversed_ranks)))  # distractor

# Weight assignment using lambda for dynamic adjustment
steepness = 1.5
weight_function = lambda rank: round(1 + (1 / (rank + 1)) ** steepness, 3)
weights = [weight_function(i) for i in range(len(participants))]

# Shuffled order for confusion (not aligned with original)
sorted_participants = sorted(participants)
sorted_rankings = [rankings[p] for p in sorted_participants]

# Extra distraction: unused data structure
stats_summary = {
    'average_normalized': sum(normalized_scores) / len(normalized_scores),
    'top_scorer': participants[normalized_scores.index(max(normalized_scores))],
    'total_penalty': sum(penalties),
    'adjusted_variance': sum((x - sum(adjusted_scores)/len(adjusted_scores))**2 for x in adjusted_scores) / len(adjusted_scores)
}

# Core logic: calculate weighted score using original alignment
def calculate_weighted_score(ranking_dict, weight_list):
    total = 0.0
    for i, participant in enumerate(participants):  # maintain original order
        total += ranking_dict[participant] * weight_list[i]
    return total

# Execute main calculation
final_score = calculate_weighted_score(rankings, weights)

# Print result as required
print(f"Result: {final_score}")