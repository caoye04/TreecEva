from itertools import groupby

# Simulate user feedback ratings from different regions
customer_feedback = [
    ('US', 4), ('US', 5), ('US', 3), ('US', 4),
    ('EU', 5), ('EU', 5), ('EU', 4),
    ('ASIA', 3), ('ASIA', 4), ('ASIA', 5), ('ASIA', 4),
    ('US', 5), ('EU', 3)
]

# Irrelevant transformation: convert to uppercase strings (distraction)
region_names_upper = [region.upper() for region, _ in customer_feedback]

# Misleading intermediate: count total entries but not used in final logic
total_entries = len(customer_feedback) + 10  # red herring

# Group feedback by region
sorted_feedback = sorted(customer_feedback, key=lambda x: x[0])
grouped_feedback = {key: list(map(lambda x: x[1], group)) for key, group in groupby(sorted_feedback, key=lambda x: x[0])}

# Compute average per region (semi-relevant, used in weighting)
region_averages = {}
for region, ratings in grouped_feedback.items():
    avg = sum(ratings) / len(ratings)
    region_averages[region] = round(avg, 2)

# Dead code path: unused function (adds interference)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Simulate weighting based on market size (distraction with extra computation)
market_weights = {'US': 1.2, 'EU': 1.0, 'ASIA': 0.9}
weighted_contributions = {}
for region, avg in region_averages.items():
    weighted_contributions[region] = avg * market_weights.get(region, 1.0)

# Dummy string processing (distractor)
prefixes = {"US": "NorthAmerica", "EU": "Europe", "ASIA": "AsiaPacific"}
full_names = [prefixes[r] for r in region_averages.keys() if r in prefixes]

# Core logic: create a flattened list of all ratings above regional average (actual signal)
flattened_ratings = [rating for group in grouped_feedback.values() for rating in group]
overall_mean = sum(flattened_ratings) / len(flattened_ratings)
above_avg_count = len([r for r in flattened_ratings if r > overall_mean])

# Feedback map includes summary stats (used in final step)
feedback_map = {
    'ratings': flattened_ratings,
    'count_above_avg': above_avg_count,
    'region_size': len(grouped_feedback),
    'baseline': 3.5
}

# Aggregate performance using non-linear adjustment (key computational step)
def aggregate_performance(feedback):
    base = sum(feedback['ratings']) / len(feedback['ratings'])
    bonus = feedback['count_above_avg'] * 0.1
    penalty = (feedback['region_size'] - 3) * 0.05  # neutral since 3 regions
    adjusted = base + bonus + penalty
    # Apply sigmoid-like compression for stability
    import math
    return round(5 * (1 / (1 + math.exp(-adjusted / 2))), 4)

# Execution point of interest
final_score = aggregate_performance(feedback_map)

print(f"Result: {final_score}")