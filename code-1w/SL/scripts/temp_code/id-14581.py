def analyze_performance(records):
    base_multiplier = 1.5
    adjustment_factor = 0.9
    temp_results = []
    cumulative_offset = 0

    for idx, record in enumerate(records):
        raw_value = record['metric_a'] * base_multiplier
        if record['flag']:
            raw_value -= adjustment_factor * idx

        # Irrelevant transformation (distractor)
        transformed = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(record['tag'])])
        transformed_length = len(transformed)

        # Semi-relevant computation
        normalized = raw_value / (transformed_length + 1)
        temp_results.append(normalized)

        # Dead code path (distractor)
        if transformed_length > 100:
            cumulative_offset += len(record['tag'])

    return temp_results


def calculate_consistency(data):
    consistency_score = 0
    prev = data[0]
    for curr in data[1:]:
        if curr > prev:
            consistency_score += 1
        elif curr < prev:
            consistency_score -= 0.5
        prev = curr
    return max(consistency_score, 0)


def calculate_ranking(values, deductions):
    total_value = sum(values)
    penalty_reduction = 0

    # Modular arithmetic and conditional branching
    for i, val in enumerate(values):
        if i % 3 == 0:
            penalty_reduction += deductions[i % len(deductions)] % (i + 2)

    base_rank = total_value * 2.5
    adjusted_rank = base_rank - penalty_reduction * 1.75

    # Complex list comprehension with zip (required feature)
    zipped = list(zip(values, deductions * 2))
    bonus = sum([v * d for v, d in zipped if v > 10 and d < 3]) * 0.1

    # Final result influenced by multiple factors
    final_rank = adjusted_rank + bonus
    return int(final_rank)

# Main execution
records_data = [
    {'metric_a': 12, 'flag': True,  'tag': 'alpha'},
    {'metric_a': 15, 'flag': False, 'tag': 'beta'},
    {'metric_a': 18, 'flag': True,  'tag': 'gamma'},
    {'metric_a': 14, 'flag': True,  'tag': 'delta'},
    {'metric_a': 20, 'flag': False, 'tag': 'epsilon'}
]

points = analyze_performance(records_data)
penalties = [4, 2, 5, 3, 1]

# Tracking auxiliary values (distractors)
sum_of_points = sum(points)
dummy_shift = sum_of_points << 2
inverted_flags = [not r['flag'] for r in records_data]

# Key statement
final_score = calculate_ranking(points, penalties)

# Additional irrelevant computation (dead weight)
reversed_tags = [r['tag'][::-1] for r in records_data]
concatenated = ''.join(reversed_tags)
hash_approx = sum([ord(c) * (i + 1) for i, c in enumerate(concatenated)]) % 1000

print(f"Result: {final_score}")