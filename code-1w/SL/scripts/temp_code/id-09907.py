def process_leaderboard(entries):
    # Irrelevant transformation: shuffles case and adds noise tags
    processed = []
    for entry in entries:
        name = entry['name'].upper()[::-1].replace('A', '@')
        score = entry['score'] * 1.1
        processed.append({'coded_name': name, 'adjusted_score': score})
    return processed

# Decoy function that looks important but is never used
def evaluate_tier(value, threshold=500):
    if value > threshold:
        return "Elite"
    elif value > 250:
        return "Advanced"
    else:
        return "Basic"

# Another red herring: complex bit manipulation with no impact
status_flags = 0b101010
masked_flags = status_flags & 0b111100 >> 2
inverted = ~masked_flags & 0b1111

# Real data structures
points = [85, 92, 78, 96, 88]
penalties = [5, 8, 3, 10, 6]

# Distractor: list of thresholds with unclear purpose
evaluation_caps = {
    'tier_A': 100,
    'tier_B': 85,
    'tier_C': 70
}

# Unused recursive attempt (dead code path)
def recursive_sum(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Dictionary operation: mapping student IDs to names (partially relevant)
student_map = {i+1: f'Student_{i}' for i in range(len(points))}

# Conditional expression embedded in comprehension (actual use)
corrected_points = [
    p - (2 if p % 5 == 0 else 0) for p in points  # Small correction for round scores
]

# Misleading intermediate: average before penalty application
preliminary_avg = sum(corrected_points) / len(corrected_points)

# Key logic chain begins here — real computation
adjusted_points = [p - penalties[i] for i, p in enumerate(corrected_points)]

# String-based filtering: only students whose fake ID contains 'd' (always true)
valid_names = [name for sid, name in student_map.items() if 'd' in name.lower()]
effective_count = len(valid_names)

# Real calculation hidden among noise
scaling_factor = 1.05 if len(adjusted_points) >= 5 else 1.0
boosted = [round(x * scaling_factor) for x in adjusted_points]

# Aggregation using min/max/average
high = max(boosted)
lows = min(boosted)
avg = sum(boosted) / len(boosted)

# Final ranking formula: combines high, low, and avg with weight
rank_weights = {'peak': 0.4, 'consistency': 0.3, 'baseline': 0.3}
weighted_rank = (
    rank_weights['peak'] * high +
    rank_weights['consistency'] * (high - lows) +
    rank_weights['baseline'] * avg
)

# Final score derived from weighted ranking
final_score = int(round(weighted_rank))

# Print result as required
print(f"Result: {final_score}")