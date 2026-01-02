def calculate_final_score(scores, importance_weights):
    normalized = [(s / 100) for s in scores]
    weighted = map(lambda x, w: x * w, normalized, importance_weights)
    return round(sum(weighted) * 100)

# Irrelevant auxiliary data
timestamp_log = [162345, 162346, 162347]
user_status = 'active'

raw_scores = [88, 92, 76, 85]
weights = [0.2, 0.3, 0.15, 0.35]

# Calculation of final composite score
final_score = calculate_final_score(raw_scores, weights)

print(f"Result: {final_score}")