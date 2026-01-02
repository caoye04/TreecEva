def calculate_final_score(items, importance_weights):
    base_values = [ord(str(item)[-1]) for item in items]
    adjusted = []
    temp_offset = 0
    
    for i, val in enumerate(base_values):
        if i % 2 == 0:
            adjusted.append(val * importance_weights[i % len(importance_weights)])
        else:
            shifted = val << 1
            adjusted.append(shifted + 3)
    
    # Irrelevant computation block (distractor)
    outlier_count = 0
    running_avg = 0
    for x in adjusted:
        running_avg += x
    if len(adjusted) > 0:
        running_avg /= len(adjusted)
    for x in adjusted:
        if abs(x - running_avg) > 10:
            outlier_count += 1

    # Another distractor: unused transformation
    transformed = [x ^ 25 for x in base_values if x % 2 == 1]
    size_factor = len(transformed) if transformed else 1

    aggregate = sum(adjusted)
    penalty = 0
    for i in range(len(items)):
        if isinstance(items[i], str) and items[i].isupper():
            penalty += 2

    # Actual final score calculation
    final_score = (aggregate - penalty) // (size_factor if size_factor > 0 else 1)
    return final_score

# Main execution
raw_data = [107, 'ABC', 205, 'xyz', 309, 'TEST', 401]
weights = [3, 1, 4]
intermediate_flag = False
dummy_tracker = [0] * len(raw_data)

for idx, entry in enumerate(raw_data):
    if isinstance(entry, str):
        dummy_tracker[idx] = len(entry) * 2
    else:
        dummy_tracker[idx] = entry % 50

final_score = calculate_final_score(raw_data, weights)
print(f"Result: {final_score}")