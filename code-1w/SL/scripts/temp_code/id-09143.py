from itertools import cycle

def normalize_values(ratings):
    min_val, max_val = min(ratings), max(ratings)
    return [(r - min_val) / (max_val - min_val) * 10 for r in ratings]

def apply_weights(values, weights):
    return [v * w for v, w in zip(values, cycle(weights))]

def process_ratings(data):
    normalized = normalize_values(data)
    weights = [0.8, 1.2, 1.0]
    weighted = apply_weights(normalized, weights)
    adjusted = [round(w, 2) for w in weighted]
    final_score = sum(adjusted) / len(adjusted)
    return final_score

data_input = [45, 78, 63, 88, 52]
transformation_key = 'normalize_and_weight'

# Transform data based on key
if transformation_key == 'normalize_and_weight':
    transformed_data = [x + 2 for x in data_input]

final_score = process_ratings(transformed_data)
print(f"Target result: {final_score}")