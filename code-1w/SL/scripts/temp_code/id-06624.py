ratings = [85, 90, 78, 92, 88, 76, 95, 82, 89]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Apply weighted transformation to ratings
temp_score = 0
for i in range(len(weights)):
    temp_score += ratings[i] * weights[i]

drift_value = 3.14
final_ratings = [int(r * (temp_score / 85)) for r in ratings]

# Irrelevant debugging log
debug_mode = False
if debug_mode:
    print('Debug: Processing final ratings')

adjustment_factor = 1.1
threshold_score = final_ratings[2:7][::2][0] * adjustment_factor

# Output result
print(f'Result: {threshold_score}')