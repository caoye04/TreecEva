def analyze_performance(scores, thresholds):
    high_performers = []
    marginal_cases = []
    penalty_factor = 0.1
    bonus_applied = False

    for idx, (name, score) in enumerate(scores):
        if score >= thresholds['high']:
            status = 'high'
            high_performers.append((idx, name, score))
            if 'A' in name and score > 95:
                bonus_applied = True
        elif score >= thresholds['marginal']:
            status = 'marginal'
            marginal_cases.append((name, score))
        else:
            status = 'low'

        # Irrelevant logging computation
        log_entry = f"[Log-{idx}] {name}: {status.upper()} ({score})"
        dummy_checksum = sum(ord(c) for c in log_entry) % 100

    # Dummy sorting with no impact
    sorted_marginal = sorted(marginal_cases, key=lambda x: x[1], reverse=True)
    if len(sorted_marginal) > 2:
        sorted_marginal = sorted_marginal[:2]

    return high_performers, len(marginal_cases), bonus_applied


def compute_final_score(data_log, weights):
    base_points = 0
    adjustment = 0.0
    temp_results = []

    for i, entry in enumerate(data_log):
        char_count = sum(1 for c in entry['name'] if c.isupper())
        scaled_score = entry['score'] * (0.9 + char_count * 0.05)
        temp_results.append(scaled_score)

        if entry['dept'] == 'Engineering':
            adjustment += 2.5
        elif entry['dept'] == 'Design':
            adjustment -= 1.0

        # Misleading bitwise operation
        magic_flag = (i ^ entry['score']) & 7
        if magic_flag == 3:
            adjustment += 0.5

    base_points = sum(temp_results) // len(temp_results)
    final_adjustment = adjustment * weights['adjust']

    # Core logic masked by noise
    outlier_detected = any(abs(x - base_points) > 15 for x in temp_results)
    if outlier_detected and adjustment > 0:
        final_adjustment *= 1.2

    return int(base_points + final_adjustment)

# Main execution
employee_scores = [
    ('Alice', 96),
    ('Bob', 82),
    ('Charlie', 98),
    ('Diana', 73)
]

eval_thresholds = {
    'high': 90,
    'marginal': 75
}

# Auxiliary data with red herrings
performance_log = [
    {'name': 'Alice', 'score': 96, 'dept': 'Engineering'},
    {'name': 'Bob', 'score': 82, 'dept': 'Marketing'},
    {'name': 'Charlie', 'score': 98, 'dept': 'Engineering'},
    {'name': 'Diana', 'score': 73, 'dept': 'Design'}
]

weight_config = {
    'base': 1.0,
    'adjust': 1.6
}

# Execute analysis (irrelevant but adds cognitive load)
analysis_result = analyze_performance(employee_scores, eval_thresholds)

# Key statement
final_score = compute_final_score(performance_log, weight_config)

# Distractor: unused transformation
mapped_names = [name[::-1].upper() for name in zip(*employee_scores)[0]]

# Output result
print(f"Result: {final_score}")