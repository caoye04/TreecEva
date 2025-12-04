# Calculate player scores in a tournament
def calculate_bonus(level):
    # Calculate bonus points based on player level
    bonus_factors = {1: 5, 2: 10, 3: 15, 4: 20}
    return bonus_factors.get(level, 0) * 0.5

# Player data: (name, base_score, level)
players = [
    ('Alice', 120, 3),
    ('Bob', 85, 2),
    ('Charlie', 150, 4),
    ('David', 95, 1)
]

# Tournament modifiers
round_multipliers = [1.0, 1.5, 0.8]
total_rounds = len(round_multipliers)
qualification_threshold = 100

# Track scores
raw_scores = {}
bonus_points = {}
final_scores = {}

# Process player scores
for i, (name, base_score, level) in enumerate(players):
    # Calculate raw score with round multipliers
    round_index = i % total_rounds
    multiplier = round_multipliers[round_index]
    raw_scores[name] = base_score * multiplier
    
    # Calculate bonus points
    bonus = calculate_bonus(level)
    bonus_points[name] = bonus
    
    # Apply penalty for low scores
    penalty = 10 if raw_scores[name] < qualification_threshold else 0
    
    # Calculate final score
    final_scores[name] = raw_scores[name] + bonus_points[name] - penalty

# Calculate average bonus (not used in final calculation)
avg_bonus = sum(bonus_points.values()) / len(bonus_points) if bonus_points else 0

# Process some additional stats (not affecting final scores)
max_raw = max(raw_scores.values())
min_raw = min(raw_scores.values())
range_raw = max_raw - min_raw

# Calculate total score
total_score = sum(final_scores.values())

# Display results
print(f"Raw scores: {raw_scores}")
print(f"Bonus points: {bonus_points}")
print(f"Final scores: {final_scores}")
print(f"Result: {total_score}")