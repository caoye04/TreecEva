def analyze_metrics(raw_values):
    normalized = [round(x / max(raw_values) * 100, 2) for x in raw_values]
    outliers = [x for x in normalized if x > 90]
    return normalized, len(outliers)

raw_data = [23, 45, 67, 89, 12, 34, 56, 78]
processed_data, anomaly_count = analyze_metrics(raw_data)

# Irrelevant computation block (distractor)
temp_stats = {}
duplicate_check = set()
for val in raw_data:
    temp_stats[val] = val ** 2 + 3 * val - 1
    if val in duplicate_check:
        break
    duplicate_check.add(val)

# Misleading transformation chain
shadow_copy = [x * 1.1 for x in processed_data if x < 70]
shadow_copy = [round(x, 1) for x in shadow_copy]

# Core logic disguised among side operations
efficiency_flags = [1 if x > 50 else 0 for x in processed_data]
activation_threshold = sum(efficiency_flags) >= 4

scaling_factor = 1.5 if activation_threshold else 0.8
adjusted_scores = [x * scaling_factor for x in processed_data]

# Secondary distractor: string-based encoding of numbers (unused)
encoded_ids = [str(int(x)).zfill(3) for x in adjusted_scores]
status_map = {i: ('high' if x > 75 else 'low') for i, x in enumerate(adjusted_scores)}

# Critical function with mixed concerns
def calculate_final_score(scores):
    base_total = sum(scores)
    penalty = 0
    for s in scores:
        if s < 40:
            penalty += 5
    bonus = 10 if len([s for s in scores if s > 80]) >= 2 else 0
    return int(base_total - penalty + bonus)

# Final computation point
final_score = calculate_final_score(adjusted_scores)
print(f"Result: {final_score}")