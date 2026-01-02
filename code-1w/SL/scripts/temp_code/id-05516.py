from collections import defaultdict

# Simulated system benchmark data with multiple metrics
test_results = [
    {'module': 'cpu', 'score': 89, 'temp': 67, 'overclocked': False},
    {'module': 'gpu', 'score': 94, 'temp': 82, 'overclocked': True},
    {'module': 'ram', 'score': 76, 'temp': 45, 'overclocked': False},
    {'module': 'disk', 'score': 81, 'temp': 50, 'overclocked': False},
    {'module': 'network', 'score': 91, 'temp': 30, 'overclocked': True}
]

# Irrelevant temperature tracking (distractor)
temp_analysis = defaultdict(list)
for entry in test_results:
    temp_category = 'high' if entry['temp'] > 60 else 'normal'
    temp_analysis[temp_category].append(entry['module'])

# Misleading performance adjustment based on overclocking (semi-relevant but not used directly)
overclock_penalty = 0
boosted_modules = 0
for result in test_results:
    if result['overclocked']:
        overclock_penalty += 2
        boosted_modules += 1

# Core evaluation logic
base_scores = [entry['score'] for entry in test_results]
adjusted_scores = []
performance_tiers = {"A": 0, "B": 0, "C": 0}

for score in base_scores:
    if score >= 90:
        performance_tiers["A"] += 1
        adjusted_scores.append(score - 1)  # minor stability deduction
    elif score >= 80:
        performance_tiers["B"] += 1
        adjusted_scores.append(score)
    else:
        performance_tiers["C"] += 1
        adjusted_scores.append(score + 3)  # optimization bonus for low scores

# Secondary adjustment pass (nested logic)
highest_base = max(base_scores)
avg_adjusted = sum(adjusted_scores) / len(adjusted_scores)
bonus_eligible = sum(1 for s in adjusted_scores if s > 85)

scaling_factor = 1.0
if bonus_eligible >= 3:
    scaling_factor = 1.05
    if avg_adjusted > 82:
        scaling_factor += 0.02

# Simulate calibration offset (unused path - dead code)
calibration_data = [1.02, 0.99, 1.01, 1.00]
if len(calibration_data) > 5:  # never executes
    scaling_factor *= sum(calibration_data) / len(calibration_data)

# Final aggregation
total_impact = 0
tier_weights = {'A': 1.2, 'B': 1.0, 'C': 0.8}
for tier, count in performance_tiers.items():
    total_impact += count * tier_weights[tier]

# Compute final score
def calculate_performance(data):
    raw_sum = sum(adjusted_scores)
    tier_multiplier = total_impact / len(performance_tiers)
    preliminary = raw_sum * tier_multiplier
    return int(preliminary * scaling_factor)

final_score = calculate_performance(test_results)
print(f"Result: {final_score}")