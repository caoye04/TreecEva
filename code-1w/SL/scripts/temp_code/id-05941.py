def analyze_performance(metrics):
    base_score = sum([m['value'] for m in metrics if m['active']])
    penalty = 0
    for m in metrics:
        if m['flagged'] and m['severity'] > 1:
            penalty += m['value'] * 0.1
    adjusted = base_score - penalty
    return adjusted

metrics_data = [
    {'value': 15, 'active': True, 'flagged': False, 'severity': 0},
    {'value': 25, 'active': True, 'flagged': True, 'severity': 2},
    {'value': 10, 'active': False, 'flagged': False, 'severity': 0},
    {'value': 30, 'active': True, 'flagged': True, 'severity': 1},
    {'value': 20, 'active': True, 'flagged': False, 'severity': 0}
]

rankings = [5, 3, 8, 1, 9, 4]
bonuses = [2, 7, 3, 8, 1]

# Distractor: Irrelevant list processing
temp_data = [x**2 for x in bonuses if x > 5]
sum_temp = sum(temp_data)

# Real computation begins
base_rank_score = sum(rankings) // len(rankings)
bonus_factor = len(list(filter(lambda x: x > 6, bonuses)))

# Simulated external adjustment (no effect on final result)
mock_adjustment = 0
for i in range(3):
    mock_adjustment += i * 2

# Core logic
raw_score = analyze_performance(metrics_data)
scaled_bonus = bonus_factor * 10

# Secondary distractor: unused calculation chain
phantom_chain = 1
for val in rankings:
    if val % 2 == 0:
        phantom_chain *= val
    if phantom_chain > 1000:  
        break

# Final computation
intermediate = base_rank_score + scaled_bonus
final_score = int(raw_score + intermediate)

# Output required format
print(f"Result: {final_score}")