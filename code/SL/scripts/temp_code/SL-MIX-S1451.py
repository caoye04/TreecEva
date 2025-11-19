import math
from statistics import variance

def calculate_zone_safety(elevations):
    elev_variance = variance(elevations)
    return 100 - (elev_variance / 10)

terrain_data = [
    [120, 125, 130, 128, 122],
    [150, 155, 160, 158, 152],
    [90, 95, 100, 98, 92],
    [200, 205, 210, 208, 202]
]

# Step 1: Calculate safety scores using list comprehension and lambda
safety_scores = list(map(lambda sector: calculate_zone_safety(sector), terrain_data))

# Step 2: Filter sectors with safety score above threshold
safe_sectors = [(i, score) for i, score in enumerate(safety_scores) if score > 85]

# Step 3: Sort sectors by safety score descending
safe_sectors.sort(key=lambda x: x[1], reverse=True)

# Step 4: Geometric adjustment based on sector index (simulate distance from base)
adjusted_scores = [(index, score * math.cos(index * math.pi / len(safe_sectors))) for index, score in safe_sectors]

# Step 5: Find optimal zone with maximum adjusted score
optimal_zone_index, optimal_zone_score = max(adjusted_scores, key=lambda x: x[1])

print(f"Result: {round(optimal_zone_score, 2)}")