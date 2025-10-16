import math
from itertools import combinations

elevations = [120, 150, 130, 125, 140, 135]
n = len(elevations)
mean_elevation = sum(elevations) / n

# Calculate log-dampened squared differences
log_dampened_sum = sum(math.log10((x - mean_elevation)**2 + 1) for x in elevations)

# Compute base stability score
base_stability_score = log_dampened_sum ** (1/3)

# Count unique elevation pair differences exceeding 10 meters
elevation_pairs = list(combinations(elevations, 2))
significant_differences_count = sum(1 for a, b in elevation_pairs if abs(a - b) > 10)

# Apply correction factor if necessary
correction_factor = 0
if significant_differences_count > 5:
    correction_factor = 2 ** (significant_differences_count - 5)

# Final corrected stability score
final_stability_score = base_stability_score + correction_factor

print(f"Result: {round(final_stability_score)}")