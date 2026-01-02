from itertools import combinations

def analyze_performance(scores, threshold=50):
    above_threshold = [s for s in scores if s > threshold]
    normalized = [round(s / max(scores) * 100, 2) for s in scores]
    return above_threshold, normalized

def calculate_entropy(data):
    # Irrelevant function for distraction
    from math import log
    total = sum(data)
    entropy = sum(-(x/total) * log(x/total) for x in data if x > 0)
    return round(entropy, 4)

def process_ranking(ranking_dict, multiplier):
    values = list(ranking_dict.values())
    sorted_vals = sorted(values, reverse=True)
    
    # Apply position-based weighting
    weighted_sum = 0
    for i, val in enumerate(sorted_vals):
        weight = 0.9 ** i  # Exponential decay
        weighted_sum += val * weight
    
    # Dummy logic for distraction
    temp_results = []
    for pair in combinations(sorted_vals, 2):
        diff = abs(pair[0] - pair[1])
        if diff % 2 == 0:
            temp_results.append(diff * 0.1)
    
    # Actual computation path
    base_score = sum(sorted_vals[:3])  # Top 3 values
    adjustment = len([v for v in values if v < 40]) * -2  # Penalty
    raw_score = base_score + adjustment
    final_score = int(raw_score * multiplier)
    
    # Unused intermediate variables (distractors)
    avg_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    peak_gap = sorted_vals[0] - sorted_vals[-1] if sorted_vals else 0
    
    return final_score

# Main execution block
scores_list = [85, 72, 90, 45, 68, 33, 95]
data_summary = {i: val for i, val in enumerate(scores_list)}
ratings = {'A': 85, 'B': 72, 'C': 90, 'D': 45, 'E': 68, 'F': 33, 'G': 95}
rankings = ratings.copy()

# Unused transformations (distractors)
indexed_data = list(enumerate(scores_list))
paired_data = list(zip(scores_list[:-1], scores_list[1:]))
doubled_scores = [s * 2 for s in scores_list if s < 70]

# Calculate some irrelevant metrics
_, normalized_scores = analyze_performance(scores_list)
entropy_value = calculate_entropy(scores_list)

total_normalized = sum(normalized_scores)
effective_count = len([x for x in doubled_scores if x > 50])

bonus_multiplier = 1.4
final_score = process_ranking(rankings, bonus_multiplier)
print(f"Result: {final_score}")