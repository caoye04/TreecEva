import itertools

# Simulate environmental stress response in a crop yield model
def compute_resilience_index(values):
    base_score = sum(v ** 0.5 for v in values if v > 0)
    penalty = 0
    for v in values:
        if v < 5:
            penalty += 1.5
    return base_score - penalty

# Misleading helper function (partially dead code path)
def calculate_redunant_metric(data):
    flat = list(itertools.chain.from_iterable(data))
    nonzero = [x for x in flat if x != 0]
    if len(nonzero) == 0:
        return 0
    geometric_mean = (sum(x * x for x in nonzero) / len(nonzero)) ** 0.5
    return round(geometric_mean, 3)

# Core logic for stress exposure aggregation
def aggregate_exposure(regions, stressors):
    exposure_matrix = [[0] * len(stressors[0]) for _ in range(len(regions))]
    
    # Initialize with baseline stress levels
    for i, region in enumerate(regions):
        for j, stress_row in enumerate(stressors):
            if j < len(stress_row):
                exposure_matrix[i][j] = stress_row[j] + len(region) % 4
    
    # Apply spatial decay adjustment (irrelevant for final result but plausible)
    for i in range(len(exposure_matrix)):
        for j in range(len(exposure_matrix[i])):
            adjustment = (i + 1) * 0.1 if j % 2 == 0 else 0.05 * (j + 1)
            exposure_matrix[i][j] += adjustment  # Semi-relevant but not used directly
    
    # Normalize per row using L1 norm (distractor computation)
    for i, row in enumerate(exposure_matrix):
        total = sum(abs(x) for x in row)
        if total > 0:
            normalized = [x / total for x in row]
            exposure_matrix[i] = [round(x, 4) for x in normalized]
    
    return exposure_matrix

# Main yield prediction based on filtered stress exposure
def harvest_results(matrix, threshold):
    filtered_values = []
    temp_aggregate = 0
    
    for i, row in enumerate(matrix):
        # Use string method to simulate zone labeling
        zone_tag = f"Z{i+1}".zfill(2)
        zone_digit_sum = sum(int(c) for c in zone_tag if c.isdigit())
        
        for j, val in enumerate(row):
            # Critical filtering condition
            if abs(val) > threshold:
                temp_aggregate += val * (j + 1)
                if zone_digit_sum % 2 == 1:
                    filtered_values.append(val * 1.1)  # Minor transformation
                else:
                    filtered_values.append(val)
    
    # Secondary processing using itertools
    paired = list(itertools.combinations(filtered_values, 2))
    bonus = 0
    for p in paired:
        if p[0] * p[1] > 0:  # same sign
            bonus += 0.25

    # Final computation
    base_yield = sum(filtered_values)
    resilience = compute_resilience_index(filtered_values)
    final_yield = int(base_yield + resilience + bonus)
    
    # Irrelevant sorting operation (dead end)
    sorted_doubled = sorted([x * 2 for x in filtered_values], reverse=True)
    temp_checksum = sum(1 for _ in itertools.groupby(sorted_doubled))
    
    return final_yield

# Input data setup
regions = ['alpha', 'beta', 'gamma', 'delta']
stressors = [
    [3.0, -1.5, 4.2],
    [2.1, 0.0, -3.3],
    [-2.8, 5.5, 1.9],
    [0.4, -4.1, 3.7]
]
stressor_threshold = 2.0

# Generate exposure matrix
exposure_matrix = aggregate_exposure(regions, stressors)

# Compute final yield (key statement)
final_yield = harvest_results(exposure_matrix, stressor_threshold)

print(f"Result: {final_yield}")