from itertools import compress

def calculate_final_score(values, importance):
    weighted = list(map(lambda x, w: x * w, values, importance))
    filtered = list(compress(weighted, [v > 5 for v in values]))
    return sum(filtered) // len(filtered) if filtered else 0

data = [3, 7, 9, 4, 12]
weights = [0.5, 1.2, 0.8, 1.0, 1.5]

# Intermediate calculations
total_base = sum(data)
scale_factor = len(weights)

# Key statement
calculate_final_score(data, weights)
threshold_score = calculate_final_score(data, weights)

print(f"Result: {threshold_score}")