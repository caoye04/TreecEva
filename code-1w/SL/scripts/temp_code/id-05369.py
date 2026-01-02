from collections import defaultdict

# Simulate player ranking and performance analytics
def analyze_performance(scores):
    avg = sum(scores) / len(scores)
    variance = sum((x - avg) ** 2 for x in scores) / len(scores)
    return avg, variance

def get_rank_category(avg_score):
    if avg_score >= 90:
        return 'S'
    elif avg_score >= 80:
        return 'A'
    elif avg_score >= 70:
        return 'B'
    else:
        return 'C'

# Irrelevant helper: used for distraction
def compute_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Track player stats with dictionary operations
player_stats = {
    'player_1': [85, 92, 78, 88],
    'player_2': [95, 87, 90, 93],
    'player_3': [70, 75, 68, 72],
    'player_4': [60, 65, 58, 62]
}

rank_data = {}
bonus_map = defaultdict(int)
scaling_factor = 1.5

# Misleading intermediate calculations (dead computations)
fib_val = compute_fibonacci(10)  # Unused later
temp_result = [x**2 for x in range(5)]  # Distractor list comprehension
useless_sum = sum(temp_result) * scaling_factor  # Not used

for player, scores in player_stats.items():
    avg_score, var = analyze_performance(scores)
    category = get_rank_category(avg_score)
    
    # Assign rank weight based on category
    weight = 1
    if category == 'S':
        weight = 4
    elif category == 'A':
        weight = 3
    elif category == 'B':
        weight = 2
    else:
        weight = 1
        
    rank_data[player] = {
        'average': avg_score,
        'category': category,
        'weight': weight,
        'variance': var
    }
    
    # Bonus logic with distractors
    if avg_score > 85:
        bonus_map[player] += 10
    if var < 50:
        bonus_map[player] += 5  # Low variance = consistency bonus
    
    # Red herring: complex but unused computation
    adjusted_avg = avg_score * (1 + var / 100) ** 0.5  # Computed but not stored usefully

# Another irrelevant list comprehension
status_flags = [True if v['weight'] > 2 else False for v in rank_data.values()]
flag_summary = sum(1 for f in status_flags if f)  # Used nowhere

# Core calculation buried among distractions
def calculate_final_score(ranks, bonuses):
    total_weighted = 0
    total_bonus = 0
    
    # Real logic mixed with noise
    multiplier_shift = 0
    for p in ranks:
        base = ranks[p]['average']
        w = ranks[p]['weight']
        b = bonuses[p]
        
        # Actual contribution
        total_weighted += base * w
        total_bonus += b
        
        # Distractor: conditional that never triggers due to data
        if ranks[p]['category'] == 'X':
            multiplier_shift += 10
    
    # Final score formula
    raw_score = total_weighted + total_bonus * 100
    normalized = raw_score / len(ranks)
    return int(normalized)

# Critical execution point
final_score = calculate_final_score(rank_data, bonus_map)

# Print result as required
print(f"Result: {final_score}")