from collections import defaultdict
from itertools import groupby

# Simulate user engagement scores grouped by content category
def preprocess_ranks(raw_ranks):
    processed = []
    for k, g in groupby(raw_ranks, key=lambda x: x[0]):
        entries = list(g)
        avg_score = sum(e[1] for e in entries) / len(entries)
        processed.append((k, round(avg_score, 2)))
    return processed

def calculate_final_score(rank_data):
    score_map = defaultdict(int)
    for category, score in rank_data:
        score_map[category] += score * 2.5
    
    base_total = sum(score_map.values())
    bonus = len(score_map) * 1.5  # Bonus per unique category
    penalty = 0
    
    # Apply penalty if any category score exceeds 20
    for val in score_map.values():
        if val > 20:
            penalty += 2
    
    final_score = base_total + bonus - penalty
    return round(final_score, 3)

# Raw input data: (category, engagement_score)
raw_user_ranks = [
    ('news', 8.4), ('news', 7.6),
    ('sports', 9.1), ('sports', 8.9),
    ('tech', 9.5), ('tech', 8.7),
    ('lifestyle', 6.5)
]

# Irrelevant auxiliary variable (minimal distraction)
temp_log = "Processing complete"

processed_ranks = preprocess_ranks(sorted(raw_user_ranks))
final_score = calculate_final_score(processed_ranks)
print(f"Target result: {final_score}")