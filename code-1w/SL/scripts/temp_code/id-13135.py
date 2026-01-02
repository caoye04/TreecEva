def analyze_feedback(raw_logs):
    parsed_entries = []
    temp_sum = 0
    count_tracker = 0

    for log in raw_logs:
        if not log.strip():
            continue
        parts = log.split(',')
        category = parts[0].strip()
        rating = float(parts[1])
        timestamp = parts[2].strip()  # unused metadata (distractor)

        if category == "usability":
            temp_sum += rating
            count_tracker += 1
        elif category == "performance":
            temp_sum += rating * 1.1  # minor adjustment, affects average slightly
            count_tracker += 1

        parsed_entries.append((category, rating))

    avg_rating = temp_sum / count_tracker if count_tracker > 0 else 0
    return parsed_entries, avg_rating


def filter_critical_issues(parsed_data):
    issues = set()
    severity_weights = {'critical': 3, 'high': 2, 'medium': 1}
    weighted_total = 0

    for item in parsed_data:
        cat, val = item
        if val < 3.0:  # threshold for concern
            key = f"{cat}_{val:.1f}"
            issues.add(key)
            if 'performance' in cat:
                weighted_total += severity_weights.get('high', 0)
            elif 'usability' in cat:
                weighted_total += severity_weights.get('medium', 0)

    # Distractor computation: normalization with no downstream use
    normalized_weight = weighted_total / len(issues) if issues else 0
    _ = [normalized_weight * i for i in range(3)]  # dead computation

    return issues


def evaluate_performance(feedback_set, thresholds):
    base = len(feedback_set)
    adjustment = 0

    # Use of slicing and set operations (required python features)
    sorted_keys = sorted(list(feedback_set))[1:-1]  # exclude min and max keys by string order
    for key in sorted_keys:
        if 'performance' in key and '4.0' not in key:
            adjustment += 1.5

    # Logical combination with dictionary lookup
    lower_bound = thresholds['min_acceptable']
    upper_bound = thresholds['max_expected']
    range_span = upper_bound - lower_bound

    intermediate_calc = base * range_span + adjustment

    # Complex but ultimately unused distractor block
    stats_snapshot = {
        'entries': base,
        'span': range_span,
        'adjust': adjustment,
        'snapshot_id': hash(str(intermediate_calc)) % 1000
    }
    snapshot_mean = sum(stats_snapshot.values()) / len(stats_snapshot)  # irrelevant
    _ = round(snapshot_mean, 1)  # used nowhere

    final_score = int(intermediate_calc - 2)  # final deterministic result
    return final_score

# Main execution flow
raw_user_logs = [
    "usability,2.5,2023-08-01T10:00",
    "performance,3.8,2023-08-01T10:05",
    "usability,4.1,2023-08-01T10:10",
    "performance,2.9,2023-08-01T10:15",
    "usability,3.2,2023-08-01T10:20",
    "",  # empty line to test filtering
    "performance,4.5,2023-08-01T10:25"
]

benchmark_ranges = {
    'min_acceptable': 2.5,
    'max_expected': 4.2
}

parsed_feedback, average_rating = analyze_feedback(raw_user_logs)
feedback_set = filter_critical_issues(parsed_feedback)
final_score = evaluate_performance(feedback_set, benchmark_ranges)
print(f"Target result: {final_score}")