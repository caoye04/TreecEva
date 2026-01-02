from collections import defaultdict, Counter

def analyze_feedback(patterns):
    # Irrelevant helper: counts character frequency in feedback strings
    char_freq = defaultdict(int)
    for p in patterns:
        for c in p.lower():
            char_freq[c] += 1
    return dict(char_freq)

def validate_entry(record):
    # Semi-relevant validation logic (used later)
    if not record.get('active'):
        return False
    if record['attempts'] > 5:
        return False
    return True

def process_metrics(entries):
    stats = defaultdict(float)
    total_weight = 0.0
    valid_count = 0

    # Distractor loop: computes average length (not used in final result)
    lengths = [len(entry['name']) for entry in entries]
    avg_length = sum(lengths) / len(lengths) if lengths else 0

    for entry in entries:
        if validate_entry(entry):
            effort = entry['attempts'] * 0.7 + entry['success_rate'] * 1.3
            stats[entry['category']] += effort
            total_weight += effort
            valid_count += 1

    normalized = {k: v / total_weight for k, v in stats.items()} if total_weight else {}
    return normalized, valid_count

def evaluate_performance(feedback_set, benchmark_data):
    # Core logic begins
    feedback_codes = set(feedback_set)
    temp_mapping = {i: val * 1.1 for i, val in enumerate(benchmark_data)}  # unused transformation

    # Relevant aggregation
    category_totals = defaultdict(int)
    for item in benchmark_data:
        key = item % 4
        category_totals[key] += item * 2

    # Conditional computation based on set intersection
    flag_code = len(feedback_codes & {3, 5, 7, 11})
    adjustment_factor = 1.5 if flag_code > 1 else 0.8

    intermediate_sum = sum(category_totals.values())
    adjusted_sum = intermediate_sum * adjustment_factor

    # Red herring: string processing with no impact
    labels = ['alpha', 'beta', 'gamma']
    label_caps = [lbl.upper() for lbl in labels]
    label_hash = sum(ord(c) for c in ''.join(label_caps)) % 17

    # Final computation chain
    base_score = adjusted_sum // 4
    bonus = len(feedback_codes) * 3
    penalty = sum(1 for x in feedback_codes if x < 0) * 5
    final_score = int(base_score + bonus - penalty)

    return final_score

# Main execution context
feedback_set = [2, 3, 5, -1, 8, 11]
benchmark_data = [12, 15, 7, 4, 9, 13]

# Dead code path: never called but looks relevant
historical_logs = [{'version': 'v1', 'status': 'archived'}]

# Key statement
final_score = evaluate_performance(feedback_set, benchmark_data)

print(f"Result: {final_score}")