def process_metrics(raw_data):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.95 for x in raw_data if x > 0]
    filtered = [x for x in raw_data if x % 2 == 1]  # Only odd values kept

    # Semi-relevant aggregation
    base_total = sum(filtered)
    penalty = len([x for x in raw_data if x < 10]) * 1.5

    return base_total - penalty


def evaluate_performance(entries, threshold_fn):
    # Helper lambda: determines if entry is significant
    is_important = lambda x: threshold_fn(x) and x > 5

    count_high = 0
    temp_log = []
    adjustment = 0.0

    # Misleading loop with side logging (not used later)
    for val in entries:
        if val > 20:
            temp_log.append(f"High: {val}")
        if val < 5:
            adjustment -= 0.2  # Minor cumulative effect, but irrelevant

    # Core logic nested in conditionals
    for val in entries:
        if is_important(val):
            if val > 15:
                count_high += 2
            else:
                count_high += 1

    # Another distractor: complex but unused calculation
    avg_orig = sum(entries) / len(entries) if entries else 0
    outlier_count = len([x for x in entries if x > avg_orig * 1.8])

    # Final score depends only on count_high and fixed offset
    result = count_high * 7 + 3

    return result

# Main execution
raw_input = [3, 7, 12, 18, 22, 4, 19, 6]
data_points = [x + 2 for x in raw_input]  # Transform: [5,9,14,20,24,6,21,8]

# Threshold function (lambda) - only values >= 14 pass
threshold_func = lambda x: x >= 14

interim_result = process_metrics(raw_input)  # Unused in final score
final_score = evaluate_performance(data_points, threshold_func)

# Print final answer as required
print(f"Target result: {final_score}")