from collections import defaultdict

# Simulate student category scores with default zero for missing entries
category_scores = defaultdict(int, math=85, science=90, literature=78, art=88)

# Apply difficulty scaling factors by category
scaling_factors = {"math": 1.2, "science": 1.1, "literature": 0.95, "art": 1.0}
scaled_values = []

for subject, base_score in category_scores.items():
    if subject in scaling_factors:
        adjusted = base_score * scaling_factors[subject]
        scaled_values.append(round(adjusted))

# Aggregate final score
total_score = sum(scaled_values)
print(f"Target result: {total_score}")