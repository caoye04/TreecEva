def calculate_rating(data):
    # Preprocessing: Normalize and filter valid entries
    normalized = [x / max(data) if max(data) != 0 else 0 for x in data]
    filtered = [x for x in normalized if x > 0.1]

    # Irrelevant distraction: Unused transformation
    inverted = [round(1 - x, 3) for x in normalized]
    temp_sum = sum(inverted[:2]) * 0.5  # Not used later

    # Core logic begins
    high_engagement = list(filter(lambda x: x >= 0.5, filtered))
    medium_engagement = [x for x in filtered if 0.3 <= x < 0.5]

    # Distractor variables
    placeholder = len(inverted) + len(normalized) - len(filtered)
    dummy_calc = placeholder * 0.01 if placeholder > 0 else 0

    # Scoring mechanism
    score = 0
    score += len(high_engagement) * 10
    score += len(medium_engagement) * 5

    # Bonus logic with conditional expression
    bonus = 20 if all(x < 1.0 for x in normalized) and len(high_engagement) >= 2 else 10

    # Final adjustment based on distribution skew
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    adjustment = 7 if avg_val > 0.45 else 3

    final_score = score + bonus + adjustment

    return final_score

# Simulated user engagement metrics (in arbitrary units)
data_points = [85, 90, 45, 60, 20, 10, 75, 80]
engagement_data = [x for x in data_points if x >= 15]  # Remove very low values

# Additional irrelevant tracking
tracking_codes = ['A7', 'B9', 'C3']
code_map = {code: idx for idx, code in enumerate(tracking_codes)}
offset_value = sum(code_map.values())  # Dead-end computation

final_score = calculate_rating(engagement_data)
print(f"Result: {final_score}")