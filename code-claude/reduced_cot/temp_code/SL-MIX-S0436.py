import itertools

# Analyzing overlapping customer preferences between two stores
store_a_preferences = {(2, 5), (1, 3), (4, 6), (2, 3), (5, 6), (1, 4)}
store_b_preferences = {(3, 5), (1, 3), (2, 6), (4, 5), (2, 3)}

# Track potential marketing strategies
marketing_budget = 5000
campaign_costs = [1200, 800, 1500, 950, 700]

# Process the preference data
flat_preferences_a = set()
for pair in store_a_preferences:
    flat_preferences_a.add(pair[0])
    flat_preferences_a.add(pair[1])

# Calculate some metrics (not all will be used)
unique_items = set(range(1, 8))  # Items 1-7 available
common_single_items = flat_preferences_a.intersection(set([1, 2, 3, 4, 5, 6]))

# Find pairs that appear in both stores' preferences
intersection_set = store_a_preferences.intersection(store_b_preferences)
unique_pairs = len(intersection_set)

# Some additional calculations that don't affect the result
total_pairs = len(store_a_preferences) + len(store_b_preferences)
distinct_pairs = len(store_a_preferences.union(store_b_preferences))

# Calculate potential campaign combinations
viable_campaigns = [i for i, cost in enumerate(campaign_costs) if cost < 1000]
viable_combinations = list(itertools.combinations(viable_campaigns, 2))

# Calculate remaining budget after essential campaigns
remaining_budget = marketing_budget - sum(campaign_costs[i] for i in [1, 4])

# Final result - how many preference pairs appear in both stores
print(f"Result: {unique_pairs}")