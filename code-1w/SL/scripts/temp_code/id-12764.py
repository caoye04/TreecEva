import itertools

def analyze_performance(metrics):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.25, 0.15]
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    return weighted_sum

# Simulate system health check (distractor function)
def check_health(temps):
    avg_temp = sum(temps) / len(temps)
    if avg_temp > 75:
        status = "overheating"
    else:
        status = "stable"
    # This function is never called
    return status

# Main computation block
base_values = [88, 92, 76, 85, 94]
adjustment_factor = 1.05

# Irrelevant transformation (dead code path)
doubled = [x * 2 for x in base_values if x > 80]

# Real processing begins
normalized = [x * adjustment_factor for x in base_values]
efficiency_ratings = [min(x, 100) for x in normalized]
score_vector = analyze_performance(efficiency_ratings)

# Bonus logic with distractors
bonus_pool = 0
for val in efficiency_ratings:
    if val >= 90:
        bonus_pool += 5
    elif val >= 85:
        bonus_pool += 2  # Misleading: not used later

# Unused dictionary operation (interference)
status_map = {i: ('high' if v >= 90 else 'normal') for i, v in enumerate(efficiency_ratings)}
unused_combinations = list(itertools.combinations([1, 2, 3], 2))

# Core logic masked by noise
rank_data = sorted(efficiency_ratings, reverse=True)[:4]  # Top 4
penalty = len([x for x in efficiency_ratings if x < 80]) * 3

# Another red herring: complex but unused calculation
aggregate = sum([a * b for a, b in zip(rank_data, [4, 3, 2, 1])])

bonus_multiplier = 1 + (bonus_pool / 100)

# Key statement
final_score = calculate_final_score(rank_data, bonus_multiplier)

# Helper function defined after use (adds cognitive load)
def calculate_final_score(ranks, mult):
    base = sum(ranks)
    adjusted = base * mult
    if adjusted > 300:
        adjusted -= penalty  # Uses penalty from outer scope (subtle!)
    return round(adjusted)

print(f"Result: {final_score}")