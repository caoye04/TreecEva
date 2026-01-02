def calculate_final_score(data, limit):
    # Preprocessing: filter and transform data
    processed = [x * 2 for x in data if x > 0]
    shifted_data = [x >> 1 for x in processed]  # Bitwise shift as transformation

    # Irrelevant intermediate computation (distractor)
    temp_sum = sum([x ** 2 for x in processed])
    normalization_factor = max(processed) // 4 if processed else 1
    adjusted = [x / normalization_factor for x in processed[:5]]  # Only used locally

    # Core logic: count how many exceed the limit after transformation
    valid_entries = set()
    for val in shifted_data:
        if val > limit:
            valid_entries.add(val)
        elif val == limit:
            break  # Early termination on equality

    # Secondary filtering using slicing
    sliced_valid = list(valid_entries)[::-1][:]  # Reverse and copy (redundant but realistic)

    # Scoring logic
    base_score = len(valid_entries)
    bonus = 0
    for i, v in enumerate(sliced_valid):
        if i % 2 == 0 and v % 3 == 0:
            bonus += 1

    final_score = base_score * 10 + bonus

    # More distractions: unused variables and dead-end logic
    outlier_count = 0
    for x in processed:
        if x > 100:
            outlier_count += 1
    scaling_ratio = outlier_count / len(processed) if processed else 0

    return final_score

# Main execution
raw_data = [3, 7, -2, 12, 5, 14, 8, 0, 9]
threshold = 6
initial_total = sum(raw_data)  # Distractor variable
buffer_copy = raw_data[::]  # Full slice copy - not used later
flag_state = False
for x in buffer_copy:
    if x < 0:
        flag_state = True

result = calculate_final_score(raw_data, threshold)
final_score = result
print(f"Target result: {final_score}")