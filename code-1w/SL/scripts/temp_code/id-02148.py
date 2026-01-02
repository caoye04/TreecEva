from itertools import compress

# Sensor readings from water quality monitoring stations
candidate_readings = [6.8, 7.2, 6.9, 7.5, 6.7, 7.0, 7.3, 6.6]
ph_trends = [0.1, -0.2, 0.3, 0.0, -0.1, 0.4, -0.3, 0.2]

# Determine stable pH levels (small trend variation) and acceptable range (6.7-7.4)
stable_conditions = [abs(trend) < 0.25 for trend in ph_trends]
acceptable_range = [(6.7 <= ph <= 7.4) for ph in candidate_readings]

# Only consider readings that meet both stability and range criteria
effective_mask = [stable and valid for stable, valid in zip(stable_conditions, acceptable_range)]
filtered_results = list(compress(candidate_readings, effective_mask))

# Calculate cumulative filtration score based on qualified readings
filtration_score = sum(filtered_results)
print(f"Result: {filtration_score}")