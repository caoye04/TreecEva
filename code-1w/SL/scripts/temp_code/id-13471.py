from itertools import combinations

# Simulate sensor data calibration and weighted aggregation
raw_readings = [12.5, 8.3, 15.7, 23.1, 9.4, 11.0]
offsets = [0.2, -0.4, 0.1, 0.0, -0.3, 0.5]

# Apply offsets (distractor: not all are used)
calibrated = [raw_readings[i] + offsets[i] for i in range(len(raw_readings))]

# Irrelevant processing: generate all pairs above threshold
above_threshold_pairs = []
for pair in combinations(calibrated, 2):
    if sum(pair) > 20.0:
        above_threshold_pairs.append(pair)

# Weight assignment (some distraction here)
basic_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.2]
adjusted_weights = [w * 1.1 for w in basic_weights]  # Unused adjustment
weights = basic_weights  # Actual weights used

# Data transformation via filtering and scaling
filtered = [val for val in calibrated if val > 10.0]
scaled_filtered = [x * 1.05 for x in filtered]

# Another distractor: count how many original values are near multiples of 5
close_to_five_multiple = sum(1 for v in raw_readings if round(v % 5) < 0.7)

# Key data structure: results dictionary with intermediate stats
results = {
    'mean_base': sum(raw_readings) / len(raw_readings),
    'peak': max(calibrated),
    'active_count': len(filtered),
    'baseline': scaled_filtered[0] if scaled_filtered else 0
}

# Helper function with misleading parameters
def compute_aggregate(data, weights, method='weighted', normalize=True, dummy_flag=False):
    # Dummy logic that doesn't change outcome
    if dummy_flag:
        return -999
    
    aggregate = 0.0
    norm_factor = sum(weights) if normalize else 1.0
    
    # Only use a subset of weights corresponding to filtered data indices
    relevant_indices = [i for i, v in enumerate(calibrated) if v > 10.0]
    for i, idx in enumerate(relevant_indices):
        weight = weights[idx] / norm_factor
        reading = calibrated[idx] * 0.95  # Revert scaling, then reapply correct factor
        aggregate += weight * reading
    
    # Additional computation that doesn't affect result
    outlier_check = [x for x in data.values() if x > 20.0]
    consistency_score = len(outlier_check) * 0.1
    
    return aggregate + 0.0  # Neutral addition (distractor)

# Execute main computation
intermediate_total = sum(scaled_filtered)
dummy_call = compute_aggregate(results, weights, dummy_flag=True)  # Dead call
final_score = compute_aggregate(results, weights)

print(f"Result: {final_score}")