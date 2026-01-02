def analyze_performance(records):
    base_multiplier = 1.5
    adjustment_factor = 0.8
    temp_results = []
    cumulative_shift = 0

    for i, (score, fault) in enumerate(records):
        if score <= 0:
            continue
        weighted_score = score * base_multiplier
        penalty_deduction = fault * adjustment_factor
        adjusted = weighted_score - penalty_deduction
        
        # Distractor: tracking index shifts that aren't used later
        cumulative_shift += i % 3
        temp_results.append(adjusted)

    # Irrelevant transformation
    shifted_data = [x + 2 for x in temp_results if x > 5]
    normalized = sum(shifted_data) / len(shifted_data) if shifted_data else 0

    return temp_results, normalized


def calculate_ranking(marks, fines):
    total_points = 0
    bonus_pool = 0
    tier_thresholds = [10, 25, 50]

    for idx, (val, fine) in zip(range(len(marks)), marks, fines):
        if val < 5:
            bonus_pool += 2
            continue

        raw_contribution = val - fine
        if raw_contribution > tier_thresholds[1]:
            raw_contribution *= 1.2
        elif raw_contribution > tier_thresholds[0]:
            raw_contribution *= 1.1

        total_points += raw_contribution

    # Dead code branch (never reached due to loop structure)
    if bonus_pool > 100:
        total_points += 10

    # Final adjustment based on non-trivial condition
    helper_offset = 5 if total_points % 7 == 0 else 3
    total_points -= helper_offset

    return int(total_points)

# Main execution block
raw_data = [(12, 2), (8, 1), (30, 4), (6, 0), (50, 10)]
points, penalties = [], []

for entry in raw_data:
    pts, pnl = entry
    points.append(pts)
    penalties.append(pnl)

# Perform analysis (distractor: returns unused intermediate)
analysis_trace, avg_normalized = analyze_performance(raw_data)

# Key computation step
final_score = calculate_ranking(points, penalties)

print(f"Result: {final_score}")