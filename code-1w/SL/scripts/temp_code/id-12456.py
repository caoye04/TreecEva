def process_entries(entries):
    processed = []
    temp_sum = 0
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            temp_sum += sum(entry)
        processed.append(sum(entry) * (i + 1))
    scaling_factor = 1.5 if temp_sum > 10 else 1.0
    return processed, scaling_factor

entries = [(2, 3), (5, 1), (4, 4), (3, 2)]
weights = [0.2, 0.3, 0.1, 0.4]

# Irrelevant transformation (distractor)
transformed_data = [tuple(x * 0.9 for x in e) for e in entries]
noise_level = sum(sum(t) for t in transformed_data)

processed_values, factor = process_entries(entries)

# Additional unrelated computation (dead code path)
def unused_helper(arr):
    total = 0
    for a in arr:
        total += len(str(a))
    return total

# Real calculation begins here
adjusted_values = [val * factor for val in processed_values]

# Simulate normalization step (partially relevant but not used directly)
normalized = [x / max(adjusted_values) for x in adjusted_values]

# Actual weighted sum logic
weighted_sum = sum(w * v for w, v in zip(weights, adjusted_values))

# Secondary adjustment based on index parity (relevant)
correction = 0
for idx, val in enumerate(processed_values):
    if idx % 2 == 1:
        correction += val * 0.1

intermediate_result = weighted_sum + correction

# Final score calculation using correct logic chain
final_score = int(intermediate_result + 0.5)  # Round to nearest integer

print(f"Result: {final_score}")