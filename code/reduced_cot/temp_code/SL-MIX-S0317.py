def compute_modular_sum(values):
    # Helper function with some irrelevant calculations
    temp_sum = sum(values)
    unused_mod = temp_sum % 7  # Unused calculation
    shifted = temp_sum << 2  # Distractor operation
    return temp_sum

# Initialize data structures with mixed operations
student_ids = [101, 102, 103, 104, 105]
exam_scores = [88, 92, 76, 85, 94]
attendance_weights = [0.9, 0.85, 0.95, 0.88, 0.92]

# Irrelevant processing that doesn't affect final result
bonus_points = [5, 3, 7, 4, 6]
adjusted_bonus = [x * 1.1 for x in bonus_points]  # Unused calculation

# Main computation chain
processed_values = []
for i, (score, weight) in enumerate(zip(exam_scores, attendance_weights)):
    if i % 2 == 0:
        processed = (score * weight) // 2
    else:
        processed = (score * weight) + 10
    processed_values.append(processed)

# More distractions
prime_check = 17  # Used in final calculation
composite_check = 23  # Unused distractor

# Sorting operations
sorted_scores = sorted(exam_scores, reverse=True)
redundant_sorted = sorted(student_ids)  # Unused

# Dead code path - never executed
if len(student_ids) > 10:
    unused_result = compute_modular_sum(student_ids)
else:
    # Final computation - critical execution point
    final_score = (sorted_scores[1] + processed_values[2]) % prime_check

print(f"Result: {final_score}")