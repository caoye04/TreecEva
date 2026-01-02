from itertools import combinations

def analyze_interactions(elements):
    interaction_scores = []
    for pair in combinations(elements, 2):
        a, b = pair
        score = (a * b) / (a + b) if (a + b) != 0 else 0
        interaction_scores.append(score)
    return interaction_scores

def compute_aggregate(data):
    raw_scores = analyze_interactions(data)
    adjusted_scores = [round(s, 3) for s in raw_scores]
    total = sum(adjusted_scores)
    return total

# Experimental dataset representing sensor sensitivity values
data_set = [8, 12, 16, 4]

# Irrelevant auxiliary variable (minor distraction, intervention level 4)
baseline_reference = 3.14159

# Compute final metric
total_harmonic_score = compute_aggregate(data_set)

# Output result as required
print(f"Result: {total_harmonic_score}")