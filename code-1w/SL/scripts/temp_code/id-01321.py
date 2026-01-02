from collections import defaultdict

# Simulate student test scores across multiple subjects
student_scores = {
    'Alice': [85, 90, 78],
    'Bob': [76, 88, 92],
    'Charlie': [95, 82, 84]
}

# Irrelevant distractor: unused variable
unused_buffer = [0] * 10

# Subject weights for final calculation (math, science, language)
weights = [0.4, 0.4, 0.2]

weighted_averages = []
for name, scores in student_scores.items():
    avg = sum(scores[i] * weights[i] for i in range(len(scores)))
    weighted_averages.append(avg)

# Normalize averages to a 0-100 scale using min-max scaling
min_val = min(weighted_averages)
max_val = max(weighted_averages)
range_val = max_val - min_val

if range_val == 0:
    scaled_values = [100 for _ in weighted_averages]
else:
    scaled_values = [100 * (x - min_val) / range_val for x in weighted_averages]

total_score = sum(scaled_values)
print(f"Result: {total_score}")