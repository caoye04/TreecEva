from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring with noise filtering
data = [15, 24, 30, 18, 45, 27, 33]
weights = [0.1, 0.2, 0.15, 0.05, 0.3, 0.1, 0.1]

# Irrelevant auxiliary data (distractor)
log_entries = ['OK', 'WARN', 'OK', 'ERROR', 'OK', 'OK', 'FATAL']
status_count = defaultdict(int)
for entry in log_entries:
    status_count[entry] += 1

# Noise filter: exclude values above threshold (semi-relevant preprocessing)
filtered_data = [x for x in data if x <= 40]
missing_count = len(data) - len(filtered_data)
fill_value = sum(filtered_data) // len(filtered_data) if filtered_data else 0

# Reconstruct data with imputation (only affects one element)
reconstructed = []
for val in data:
    if val > 40:
        reconstructed.append(fill_value)
    else:
        reconstructed.append(val)

# Weighted score calculation
weighted_sum = sum(reconstructed[i] * weights[i] for i in range(len(reconstructed)))

# Auxiliary computation: normalize weights if they don't sum to 1 (red herring)
weight_sum = sum(weights)
normalized_weights = [w / weight_sum for w in weights]
# But we use original weights, so normalization has no effect

# Secondary metric: variance of reconstructed data (unused)
mean_val = sum(reconstructed) / len(reconstructed)
variance = sum((x - mean_val) ** 2 for x in reconstructed) / len(reconstructed)

# Conditional adjustment based on data completeness
adjustment_factor = 1.0
if missing_count == 0:
    adjustment_factor = 1.1
else:
    adjustment_factor = 0.95

# Final score computation
base_score = weighted_sum * 10
final_score = int(base_score * adjustment_factor)

# Extraneous string processing (dead code path)
summary_label = "Complete" if not any(x > 40 for x in data) else "Partial"
label_lower = summary_label.lower()
sliced_label = label_lower[1:-1]
joined_chars = "-".join(sliced_label)

# Output result
print(f"Result: {final_score}")