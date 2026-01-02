from itertools import compress, count

def analyze_growth_pattern(data, limit):
    # Irrelevant transformation - distractor
    transformed = list(map(lambda x: (x[0], x[1] * 0.9 + 2.1), data))
    filtered = [v for v in transformed if v[1] > limit]
    return [v[0] for v in filtered]

def calculate_harvest_efficiency(areas, thresh):
    indices = count(0)
    indexed_areas = [(next(indices), area) for area in areas]

    # Distractor: unused smoothing operation
    smoothed = [a * 0.95 for a in areas]

    # Relevant logic: find areas above threshold
    valid_mask = [area >= thresh for area in areas]
    valid_areas = list(compress(areas, valid_mask))

    # Secondary filter based on index parity (only even-indexed valid areas)
    indexed_valid = [(i, a) for i, a in indexed_areas if a >= thresh and i % 2 == 0]
    final_values = [val for idx, val in indexed_valid]

    # Accumulation with adjustment
    base_yield = sum(final_values) * 1.1

    # Distractor: dead computation path
    if len(smoothed) > 100:
        peak = max(smoothed)
        normalized = [s / peak for s in smoothed]
    else:
        peak = None
        normalized = []

    # Final adjustment based on count
    adjustment_factor = 0.9 if len(final_values) > 3 else 1.0
    final_yield = base_yield * adjustment_factor

    return final_yield

# Main execution
area_data = [12.5, 14.0, 13.7, 16.2, 15.8, 10.3, 18.1, 17.9]
threshold = 15.0

# Unused statistical analysis - red herring
mean_area = sum(area_data) / len(area_data)
variance = sum((x - mean_area) ** 2 for x in area_data) / len(area_data)
std_dev = variance ** 0.5

# Identify growth clusters (not used in final result)
growth_trend = analyze_growth_pattern(list(enumerate(area_data)), threshold - 5)

dummy_filter = lambda x: x > mean_area
extra_calc = sum(filter(dummy_filter, area_data))

# Key statement
final_yield = calculate_harvest_efficiency(area_data, threshold)
print(f"Result: {final_yield}")