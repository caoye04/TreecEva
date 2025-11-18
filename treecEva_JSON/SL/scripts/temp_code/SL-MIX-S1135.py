from functools import reduce
from collections import defaultdict

class CryptoDay:
    def __init__(self, day_id, price_change_pct, volume_ratio):
        self.day_id = day_id
        self.price_change_pct = price_change_pct
        self.volume_ratio = volume_ratio

days_data = [
    CryptoDay(1, 3.2, 1.1),
    CryptoDay(2, -6.1, 1.8),
    CryptoDay(3, 2.0, 2.5),
    CryptoDay(4, 4.5, 0.9),
    CryptoDay(5, -3.3, 1.2)
]

# Dynamic programming cache
memo = {}

def calculate_score(day):
    if day.day_id in memo:
        return memo[day.day_id]
    
    # Base score calculation
    base_score = abs(day.price_change_pct) * day.volume_ratio
    
    # Apply penalties
    penalty = 1.0
    if abs(day.price_change_pct) > 5.0 or day.volume_ratio >= 2.0:
        penalty = 0.5
    
    final_score = base_score * penalty
    memo[day.day_id] = final_score
    return final_score

scores = []
for day in days_data:
    scores.append(calculate_score(day))

# Adjust scores using nested loop processing
adjusted_scores = []
for i in range(len(scores)):
    adjustment = 1.0
    for j in range(i):
        if scores[j] > scores[i]:
            adjustment *= 0.95
    adjusted_scores.append(scores[i] * adjustment)

# Compute final volatility index using reduce
final_volatility_index = reduce(lambda x, y: x * y, adjusted_scores, 1.0)

print(f"Result: {round(final_volatility_index, 2)}")