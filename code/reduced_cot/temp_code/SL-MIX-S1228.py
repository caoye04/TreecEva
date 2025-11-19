from math import sqrt
from itertools import combinations

def compute_variance(data):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** 2 for x in data) / len(data)

def rarity_weight(species_count, total_species):
    return 1 + (total_species - species_count) / total_species

def adjust_score(raw_score, stats):
    mean, var = stats
    if var == 0:
        return raw_score
    return (raw_score - mean) / sqrt(var)

# Species observations in different zones
zones_observations = {
    'montane': [12, 15, 9, 11],
    'riparian': [20, 18, 22],
    'desert': [5, 7, 6, 8, 5]
}

# Calculate base scores using combinatorial species interactions
base_scores = {}
for zone, counts in zones_observations.items():
    interaction_score = 0
    total_species = len(counts)
    for combo in combinations(counts, 2):
        interaction_score += sum(combo) * rarity_weight(min(combo), total_species)
    base_scores[zone] = interaction_score

# Normalize scores using statistical measures
all_base_scores = list(base_scores.values())
score_stats = (sum(all_base_scores)/len(all_base_scores), compute_variance(all_base_scores))

normalized_scores = {zone: adjust_score(score, score_stats) for zone, score in base_scores.items()}

# Apply final adjustment using a lambda function
final_adjustment = lambda x: round(x * 1.25 + 10, 2)
montane_diversity_index = final_adjustment(normalized_scores['montane'])

print(f"Result: {montane_diversity_index}")