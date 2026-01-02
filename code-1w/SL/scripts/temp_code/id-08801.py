def analyze_surplus(region_data, thresholds):
    surplus = []
    temp_aggregate = 0
    for r in region_data:
        temp_aggregate += sum(r) * 0.1
        if sum(r) > thresholds['upper']:
            surplus.append(sum(r) - thresholds['upper'])
    return surplus


def analyze_deficit(region_data, thresholds):
    deficit = []
    for r in region_data:
        total = sum(r)
        if total < thresholds['lower']:
            deficit.append(thresholds['lower'] - total)
    return deficit


def filter_critical_areas(surplus_regions, deficit_regions):
    # Simulated critical area filtering using set operations
    surplus_set = {i for i, val in enumerate(surplus_regions)}
    deficit_set = {i for i, val in enumerate(deficit_regions)}
    overlap = surplus_set & deficit_set  # Empty in practice, but adds cognitive load
    return list(surplus_set - overlap), list(deficit_set - overlap)


def optimize_distribution(surplus_indices, deficit_indices):
    # Dummy transformation to increase complexity
    adjusted_surplus = [idx * 2 + 1 for idx in surplus_indices]
    adjusted_deficit = [idx * 3 + 2 for idx in deficit_indices]
    
    # Irrelevant accumulation
    dummy_sum = 0
    for x in adjusted_surplus:
        for y in adjusted_deficit:
            dummy_sum += (x - y) ** 2

    # Core logic: weighted sum of index positions
    base_score = sum(adjusted_surplus) * 1.5 - sum(adjusted_deficit) * 0.8
    
    # Additional red herring: unused helper calculation
    magnitude_check = max(base_score, 0) if len(adjusted_surplus) > len(adjusted_deficit) else min(base_score, 0)

    # Final meaningful computation
    scaling_factor = len(surplus_indices) - len(deficit_indices)
    if scaling_factor == 0:
        scaling_factor = 1
    
    intermediate_result = base_score / scaling_factor
    final_capacity = round(intermediate_result + 10.5, 2)
    
    return final_capacity


# Main execution block
region_data = [
    [12, 15, 10],
    [8, 6, 7],
    [20, 22, 18],
    [5, 4, 3],
    [17, 16, 19]
]

thresholds = {
    'upper': 45,
    'lower': 15
}

# Step 1: Identify surplus and deficit regions
surplus_regions = analyze_surplus(region_data, thresholds)
deficit_regions = analyze_deficit(region_data, thresholds)

# Step 2: Extract indices of relevant regions (distractor: full sets not used)
filtered_surplus, filtered_deficit = filter_critical_areas(surplus_regions, deficit_regions)

# Step 3: Compute optimization metric based on index patterns
excess_regions = filtered_surplus
constrained_zones = filtered_deficit
final_capacity = optimize_distribution(excess_regions, constrained_zones)

# Output result
print(f"Result: {final_capacity}")