from collections import defaultdict

# Simulate a coding competition ranking system with bonus logic
participants = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78, 96]
penalties = [10, 5, 15, 8]

# Irrelevant auxiliary data (distractor)
team_affiliations = defaultdict(lambda: 'Unknown', {
    'Alice': 'TeamA',
    'Bob': 'TeamB',
    'Charlie': 'TeamA',
    'Diana': 'TeamC'
})

# Compute base performance (relevant)
base_performance = {}
for i in range(len(participants)):
    base_performance[participants[i]] = scores[i] - penalties[i]

# Apply arbitrary difficulty scaling for different problems (semi-relevant)
difficulty_factors = {'easy': 1.1, 'medium': 1.25, 'hard': 1.4}
category_difficulty = 'medium'
scaled_scores = {}
for name in participants:
    scaled_scores[name] = base_performance[name] * difficulty_factors[category_difficulty]

# Dummy transformation (dead code path - distractor)
legacy_transform = lambda x: x * 0.95 if x > 90 else x * 1.02
transformed_legacy = {k: legacy_transform(v) for k, v in scaled_scores.items()}

# Ranking preparation (relevant)
rankings = []
for name in participants:
    # Add noise factor that gets later ignored (misleading computation)
    noise_adjusted = scaled_scores[name] + (hash(name) % 3)
    rankings.append((name, scaled_scores[name]))  # Only clean score used

# Sort by score descending (relevant)
rankings.sort(key=lambda x: x[1], reverse=True)

# Bonus rules based on rank position (relevant)
def calculate_bonus(index):
    if index == 0:
        return 1.5
    elif index == 1:
        return 1.3
    elif index == 2:
        return 1.1
    else:
        return 1.0  # No bonus for last place

# Apply bonus using rank order (relevant)
bonus_multiplier = []
for idx, (name, score) in enumerate(rankings):
    multiplier = calculate_bonus(idx)
    bonus_multiplier.append((name, multiplier))

# Secondary unused penalty track (distractor)
late_submission_penalty = defaultdict(int)
late_submission_penalty['Charlie'] = 0.9  # Not applied anywhere

# Final score calculation with bonus (key step)
def calculate_final_score(ranking_list, bonus_list):
    bonus_dict = {item[0]: item[1] for item in bonus_list}
    total = 0
    for name, raw_score in ranking_list:
        adjusted = raw_score * bonus_dict[name]
        # Round to nearest integer per competition rules
        total += round(adjusted)
    
    # Extra distraction: unused intermediate aggregation
    avg_before_rounding = sum([raw_score * bonus_dict[name] for name, raw_score in ranking_list]) / len(ranking_list)
    deviation_score = abs(avg_before_rounding - 90)  # Computed but unused
    
    return int(total)

final_score = calculate_final_score(rankings, bonus_multiplier)

# Print result as required
print(f"Target result: {final_score}")