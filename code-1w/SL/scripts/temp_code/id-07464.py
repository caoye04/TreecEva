def process_leaderboard(entries):
    filtered = [e for e in entries if e['score'] > 50]
    sorted_entries = sorted(filtered, key=lambda x: (-x['score'], x['name']))
    return sorted_entries

rankings = [
    {'name': 'Alice', 'score': 85, 'level': 5},
    {'name': 'Bob', 'score': 90, 'level': 4},
    {'name': 'Charlie', 'score': 70, 'level': 6},
    {'name': 'Diana', 'score': 45, 'level': 3},
    {'name': 'Eve', 'score': 95, 'level': 7}
]

base_points = 10
bonus_multiplier = 1.5
penalty_factor = 0.8

# Irrelevant tracking variables (distractors)
current_streak = 0
total_penalties_applied = 0
historical_max = 0

# Preprocessing with list comprehension and filtering
cleaned_rankings = process_leaderboard(rankings)

# Intermediate scoring calculations (some used, some not)
raw_scores = [player['score'] * base_points for player in cleaned_rankings]
level_bonuses = {p['name']: p['level'] * 2 for p in rankings}  # Computed but only partially used

# Simulate performance drift detection (dead logic path)
for idx, entry in enumerate(cleaned_rankings):
    if idx > 0 and entry['score'] < cleaned_rankings[idx-1]['score']:
        current_streak += 1
    else:
        total_penalties_applied += 1  # Incremented but not used

# Calculate group statistics (semi-relevant)
high_performers = {p['name'] for p in cleaned_rankings if p['score'] >= 85}
mid_performers = {p['name'] for p in rankings if 50 <= p['score'] < 85}
all_names = set(level_bonuses.keys())
eligible_bonus_recipients = high_performers.intersection(all_names)

# Actual score computation chain
aggregate_base = sum(raw_scores)
dynamic_adjustment = len(eligible_bonus_recipients) * 5

# Accumulate final score through multiple steps
interim_score = aggregate_base + dynamic_adjustment

# Apply conditional level bonus only to top-ranked player
if cleaned_rankings:
    top_player = cleaned_rankings[0]['name']
    if top_player in level_bonuses:
        interim_score += level_bonuses[top_player]

# Unused complexity: historical max tracking
for s in raw_scores:
    if s > historical_max:
        historical_max = s

# Final calculation point
final_score = calculate_final_score(rankings, base_points)

# Supporting function definition
def calculate_final_score(ranks, base):
    valid = [r for r in ranks if r['score'] > 50]
    total = sum([r['score'] * base for r in valid])
    bonus_eligible = len([r for r in valid if r['score'] >= 85])
    return total + bonus_eligible * 10

print(f"Result: {final_score}")