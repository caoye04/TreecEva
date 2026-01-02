def calculate_final_score(data, weight_map):
    base_offset = 17
    temp_buffer = [0] * len(data)
    scaling_factor = 0.85
    adjustment = 0

    # Linear search for specific condition to set adjustment
    found = False
    for i in range(len(data)):
        if data[i][1] == 'senior' and data[i][2] > 8:
            adjustment = 5
            found = True
            break

    if not found:
        adjustment = -3

    # Process rankings with enumerate and apply weights using zip
    total = 0
    count_valid = 0
    intermediate_products = []

    for idx, (name, level, score) in enumerate(data):
        norm_score = (score + base_offset) * scaling_factor
        category_bonus = 2 if level == 'senior' else 1
        
        # Irrelevant buffer operation (distractor)
        temp_buffer[idx] = norm_score * category_bonus
        
        weighted_val = norm_score * weight_map[idx] * category_bonus
        intermediate_products.append(weighted_val)

        if score >= 5:
            total += weighted_val
            count_valid += 1

    # Secondary loop with zip (semi-relevant: computes average but not used directly)
    averages = []
    for p, w in zip(intermediate_products, weight_map):
        if w > 0:
            averages.append(p / w)
    mean_estimate = sum(averages) / len(averages) if averages else 0

    # Final computation chain
    raw_result = total / count_valid if count_valid > 0 else 0
    penalty = 10 if mean_estimate < 50 else 0
    final_score = int(raw_result + adjustment - penalty)

    return final_result

# Main execution
weights = [0.5, 0.7, 1.0, 0.6]
rank_data = [
    ('alice', 'junior', 7),
    ('bob', 'senior', 9),
    ('carol', 'senior', 6),
    ('dave', 'junior', 8)
]

# Dead code path (distractor)
if len(rank_data) > 10:
    weights.extend([0.4] * (len(rank_data) - 10))

final_score = calculate_final_score(rank_data, weights)
print(f"Result: {final_score}")