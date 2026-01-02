def evaluate_performance(log, thresh):
    # Irrelevant preprocessing: reverse and slice
    reversed_entries = log[::-1]
    summary = {}
    temp_values = []

    for entry in log:
        category = entry['cat']
        value = entry['val']
        confidence = entry.get('conf', 1.0)

        # Distractor: complex confidence-weighted sum (not used)
        weighted = value * confidence
        temp_values.append(weighted)

        if category not in summary:
            summary[category] = {'count': 0, 'total': 0}
        summary[category]['count'] += 1
        summary[category]['total'] += value

    # Real logic begins: find high-confidence entries above threshold
    filtered = [e for e in log if e['val'] > thresh]
    adjusted_total = 0

    for item in filtered:
        raw_val = item['val']
        # Apply diminishing returns using modular arithmetic
        if raw_val > 20:
            adjusted = (raw_val % 17) + 3
        else:
            adjusted = raw_val + 2
        adjusted_total += adjusted

    # Another distraction: string-based status check (semi-relevant)
    status_flags = []
    for e in log:
        flag_str = f"{e['cat']}{e['val']}"
        if 'urgent' in flag_str:
            status_flags.append('alert')
        elif str(e['val']) in flag_str:
            status_flags.append('normal')

    # Core result depends only on adjusted_total and number of categories
    unique_categories = len(summary)
    base_score = adjusted_total * 2
    final_score = base_score - unique_categories

    # Dead code path (never reached in normal execution)
    if False:
        fallback = sum(temp_values) // (len(temp_values) or 1)
        final_score = fallback

    return final_score

# Main execution
feedback_log = [
    {'cat': 'ux', 'val': 25, 'conf': 0.9},
    {'cat': 'api', 'val': 18, 'conf': 1.0},
    {'cat': 'db', 'val': 30, 'conf': 0.8},
    {'cat': 'ux', 'val': 12, 'conf': 1.0},
    {'cat': 'security', 'val': 22, 'conf': 0.95}
]
threshold = 20
final_score = evaluate_performance(feedback_log, threshold)
print(f"Result: {final_score}")