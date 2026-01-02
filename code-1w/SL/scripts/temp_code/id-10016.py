import itertools

# Simulate sensor data with noise and valid readings
data_stream = [15, -3, 9, 0, 12, -7, 4, 8, 11, -1, 6]
noise_filter_threshold = 5
amplitude_correction = 1.5

# Step 1: Filter out low-amplitude noise
filtered_data = [x for x in data_stream if abs(x) > noise_filter_threshold]

# Irrelevant transformation (distractor)
doubled_values = [x * 2 for x in data_stream if x > 0]

# Step 2: Apply amplitude correction using lambda
correct_signal = lambda val: val * amplitude_correction
adjusted_data = list(map(correct_signal, filtered_data))

# Step 3: Detect rising edges (current > previous)
edge_indices = []
for i in range(1, len(adjusted_data)):
    if adjusted_data[i] > adjusted_data[i-1]:
        edge_indices.append(i)

# Misleading statistical computation (semi-relevant but unused)
avg_adjusted = sum(adjusted_data) / len(adjusted_data) if adjusted_data else 0
trend_score = len([e for e in edge_indices if adjusted_data[e] > avg_adjusted])

# Step 4: Compress data using run-length encoding idea (conceptual distraction)
rle_encoded = []
for key, group in itertools.groupby(sorted(adjusted_data, reverse=True)):
    rle_encoded.append((key, len(list(group))))

# Step 5: Compute signal quality metric based on edge distribution
if edge_indices:
    max_gap = max(edge_indices[i] - edge_indices[i-1] for i in range(1, len(edge_indices)))
else:
    max_gap = 0

# Step 6: Process signals through final nonlinear transformation
intermediate_sum = sum(itertools.chain(
    (x for x in adjusted_data if x > 10), 
    (x/2 for x in adjusted_data if x <= 10)
))

# Final processing function
def process_signals(data):
    base = sum(data)
    penalty = 0
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            penalty += 1
    return int(base - penalty * 1.5)

# Key assignment statement
final_output = process_signals(filtered_data)

print(f"Result: {final_output}")