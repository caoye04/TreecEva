from itertools import combinations

def analyze_pattern(sequence):
    # Irrelevant helper function analyzing character frequency (not used in final result)
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in sorted(freq.items())}

# Simulate sensor data preprocessing with noise filtering
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
noise_threshold = 2
filtered_data = [x for x in data_stream if x > noise_threshold]
sorted_data = sorted(filtered_data, reverse=True)

# Extract overlapping triplets and compute product sum (distractor computation)
triplet_products = []
for i in range(len(sorted_data) - 2):
    triplet_products.append(sorted_data[i] * sorted_data[i+1] * sorted_data[i+2])
running_total = sum(triplet_products[:4])  # Unused beyond this point

# Core processing: slice middle segment and apply transformations
working_slice = sorted_data[2:7]  # Take central elements
squared_values = [x**2 for x in working_slice]
delta_changes = [squared_values[i+1] - squared_values[i] for i in range(len(squared_values)-1)]
net_trend = sum(delta_changes)  # This contributes indirectly

# Bitwise manipulation layer (semi-relevant)
bit_encoded = 0
for val in working_slice:
    bit_encoded ^= (val & 7)  # Use only lower 3 bits

# Weight assignment using modular arithmetic (relevant)
base_weights = [net_trend % 3 + 1, len(working_slice), bit_encoded % 4]
expanded_weights = base_weights * 2  # Duplicate to match expected dimension
metric_weights = expanded_weights[:3]  # Trim back down

# Process data through transformation pipeline
processed_data = []
for i, val in enumerate(squared_values):
    shift = metric_weights[i % 3]
    adjusted = (val >> shift) + (i * (bit_encoded % 2))  # Right shift dominates
    processed_data.append(adjusted)

# Final evaluation function combining weighted metrics
def evaluate_performance(weights, data):
    weighted_sum = 0
    for w, d in zip(weights, data[:len(weights)]):
        weighted_sum += w * d
    
    # Additional logic to increase nesting depth
    if weighted_sum > 100:
        correction_factor = 0.9
    else:
        temp_sequence = [weighted_sum // 3, weighted_sum // 5]
        correction_factor = 1.0
    
    intermediate_result = int(weighted_sum * correction_factor)
    
    # Extra distraction: generate unused combination pairs
    if len(data) >= 4:
        _ = list(combinations(data[:4], 2))  # Computation has no effect
    
    return intermediate_result + (bit_encoded & 15)  # Final adjustment

final_score = evaluate_performance(metric_weights, processed_data)
print(f"Target result: {final_score}")