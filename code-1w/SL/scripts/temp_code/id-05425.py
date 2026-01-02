def analyze_performance(records):
    base_multiplier = 1.5
    bonus_factor = 0.2
    penalty_rate = 0.1
    temp_offset = 5  # unused in final logic
    scaling_constant = 10

    weighted_total = 0
    count = 0
    penalties_applied = 0

    for record in records:
        raw_score = record['score']
        effort_level = record['effort']
        attendance = record['attendance']

        if attendance < 75:
            raw_score *= (1 - penalty_rate)
            penalties_applied += 1

        effort_bonus = effort_level * bonus_factor
        adjusted = raw_score + effort_bonus

        if adjusted > 95:
            adjusted = 95  # cap score

        weighted_total += adjusted * base_multiplier
        count += 1

    average = weighted_total / count if count else 0

    # Irrelevant transformation
    outlier_check = list(filter(lambda x: x > 90, [r['score'] for r in records]))
    adjustment_shift = len(outlier_check) * 0.05

    # Unused calculation chain
    hypothetical_max = count * 95 * base_multiplier + adjustment_shift
    debug_ratio = weighted_total / hypothetical_max if hypothetical_max else 0

    return average


def process_results(results, threshold):
    result_log = []
    passing = 0
    total_adjustment = 0

    for res in results:
        if res >= threshold:
            result_log.append(True)
            passing += 1
        else:
            result_log.append(False)

        # Apply diminishing returns on high scores
        if res > 80:
            excess = res - 80
            normalized_excess = excess * 0.5  # half credit beyond 80
            total_adjustment += normalized_excess

    # Simulated calibration
    calibration_curve = lambda x: x * 1.1 if x < 70 else x * 0.95
    calibrated_passing = sum([calibration_curve(p) for p in results if p >= threshold])

    # Final score incorporates adjustment but not calibration curve output
    final_raw = sum(results) + total_adjustment
    adjustment_weight = 0.07
    final_score = final_raw * (1 + adjustment_weight * (passing / len(results) if results else 0))

    # Dead code branch — never executed due to prior logic
    if False and len(results) == 0:
        final_score = 0

    return int(final_score)

# Main execution
assessments = [
    {'score': 88, 'effort': 4, 'attendance': 90},
    {'score': 76, 'effort': 5, 'attendance': 60},
    {'score': 94, 'effort': 3, 'attendance': 95},
    {'score': 82, 'effort': 4, 'attendance': 80},
    {'score': 70, 'effort': 2, 'attendance': 70}
]

passing_threshold = 80

# Key processing step
performance_data = [analyze_performance([a]) for a in assessments]
final_score = process_results(performance_data, passing_threshold)

print(f"Target result: {final_score}")