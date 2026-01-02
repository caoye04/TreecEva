import itertools

def analyze_trends(values):
    trends = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trends.append(1)
        elif values[i] < values[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

# Simulate performance metrics over time
time_series_data = [120, 135, 130, 140, 142, 138, 150]
raw_trends = analyze_trends(time_series_data)

def generate_pairs(lst):
    return list(itertools.combinations(lst, 2))

# Generate all possible pairs of trend changes (distraction)
pairwise_trends = generate_pairs(raw_trends)

# Rank data based on thresholds
rank_data = {}
for idx, val in enumerate(time_series_data):
    if val >= 140:
        rank_data[f'entry_{idx}'] = 3
    elif val >= 130:
        rank_data[f'entry_{idx}'] = 2
    else:
        rank_data[f'entry_{idx}'] = 1

# Misleading intermediate calculation (dead path)
aggregate_deviation = 0
baseline = sum(time_series_data) / len(time_series_data)
for val in time_series_data:
    aggregate_deviation += abs(val - baseline)

# Bonus logic with red herring variables
count_high_performers = sum(1 for v in rank_data.values() if v == 3)
bonus_multiplier = 1.0
if count_high_performers > 2:
    bonus_multiplier = 1.25
elif count_high_performers == 2:
    bonus_multiplier = 1.15
else:
    bonus_multiplier = 1.05  # unused due to override below

# Override based on pattern (this is the real one)
if raw_trends[-1] == 1 and time_series_data[-1] > time_series_data[0]:
    bonus_multiplier = 1.3

# Auxiliary dictionary processing (semi-relevant)
adjusted_ranks = {k: v * 10 for k, v in rank_data.items()}
scale_factor = len([v for v in adjusted_ranks.values() if v > 20])

# Final score computation
total_base = sum(rank_data.values())
final_score = total_base * bonus_multiplier

# Print result as required
print(f"Target result: {final_score}")