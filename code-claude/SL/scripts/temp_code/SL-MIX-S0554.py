# Analysis of water quality classification thresholds

# Sample water quality measurements (turbidity in NTU)
samples = {
    'river_a': [2.4, 3.1, 1.8, 5.2, 4.7, 2.9],
    'river_b': [6.8, 7.3, 8.1, 5.9, 7.5, 6.2],
    'lake_x': [3.5, 4.2, 3.8, 2.7, 3.9, 4.1],
    'lake_y': [9.2, 8.7, 9.5, 10.1, 8.9, 9.8]
}

# Ground truth classifications (0 = clean, 1 = contaminated)
ground_truth = {
    'river_a': 0,
    'river_b': 1,
    'lake_x': 0,
    'lake_y': 1
}

# Calculate average turbidity for each water body
avg_turbidity = {}
median_values = {}

for location, measurements in samples.items():
    avg_turbidity[location] = sum(measurements) / len(measurements)
    # Calculate median (not used in final calculation)
    sorted_values = sorted(measurements)
    n = len(sorted_values)
    if n % 2 == 0:
        median_values[location] = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    else:
        median_values[location] = sorted_values[n//2]

# Generate potential threshold values from 0 to 12 with step 0.5
thresholds = [t/2 for t in range(0, 25)]

# Tracking error metrics
error_rates = []
false_positives = []
false_negatives = []

# Evaluate each threshold
for threshold in thresholds:
    errors = 0
    fp = 0
    fn = 0
    
    for location, avg in avg_turbidity.items():
        # Predict contamination if turbidity exceeds threshold
        predicted = 1 if avg > threshold else 0
        actual = ground_truth[location]
        
        if predicted != actual:
            errors += 1
            if predicted == 1 and actual == 0:
                fp += 1
            elif predicted == 0 and actual == 1:
                fn += 1
    
    error_rates.append(errors)
    false_positives.append(fp)
    false_negatives.append(fn)

# Find threshold with minimum error
min_error = min(error_rates)
min_error_indices = [i for i, error in enumerate(error_rates) if error == min_error]

# Among thresholds with minimum error, prefer the one with balanced FP and FN
if len(min_error_indices) > 1:
    best_balance = float('inf')
    min_error_idx = min_error_indices[0]  # Default to first if no better balance found
    
    for idx in min_error_indices:
        balance = abs(false_positives[idx] - false_negatives[idx])
        if balance < best_balance:
            best_balance = balance
            min_error_idx = idx
else:
    min_error_idx = min_error_indices[0]

# Calculate weighted error rate (not used in final answer)
weighted_error = min_error * 0.8 + (false_positives[min_error_idx] + false_negatives[min_error_idx]) * 0.2

# Find the optimal threshold
optimal_threshold = thresholds[min_error_idx]

# Apply a correction factor (not actually used)
correction = 0.05 if false_positives[min_error_idx] > false_negatives[min_error_idx] else -0.05
adjusted_threshold = optimal_threshold + correction

print(f"Result: {optimal_threshold}")