from itertools import compress

# Agricultural yield data: (yield_per_acre, acres_planted)
harvest_data = [(12, 30), (8, 45), (15, 20), (10, 50)]

# Environmental factors that affect viability (simulated as binary mask)
effective_yield = [True, False, True, True]

# Apply filter to only include viable yields
filtered_data = list(compress(harvest_data, effective_yield))

# Calculate total harvest: sum of (yield_per_acre * acres_planted)
total_harvest = sum(map(lambda x: x[0] * x[1], harvest_data))

# Irrelevant auxiliary calculation (distractor)
avg_yield = sum(x[0] for x in harvest_data) / len(harvest_data)

# Output result
print(f"Target result: {total_harvest}")