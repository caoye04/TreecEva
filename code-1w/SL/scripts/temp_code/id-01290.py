def analyze_metrics(data):
    base = sum(d['value'] for d in data)
    offset = len([d for d in data if d['flag']])
    bonus = 0
    penalty = 0

    temp_result = []
    for item in data:
        if item['value'] > 10:
            bonus += 2
        if item['value'] < 5:
            penalty += 1
        temp_result.append(item['value'] * 1.5)

    intermediate_total = sum(temp_result) // len(temp_result)
    adjustment = bonus - penalty

    # Distractor: irrelevant list processing
    ignored_list = [x for x in range(3)]
    cumulative = 0
    for i in ignored_list:
        cumulative += i ** 2  # This has no effect on output

    return base + adjustment


def compute_ranking(dataset):
    raw = analyze_metrics(dataset)
    modifiers = {'alpha': 1.1, 'beta': 0.9}
    weighted = raw * modifiers['alpha'] if raw > 20 else raw * modifiers['beta']

    status_flags = [entry['status'] for entry in dataset]
    active_count = sum(1 for s in status_flags if s == 'active')

    # Conditional expression usage (required Python feature)
    scaling_factor = 1.5 if active_count >= 2 else 0.8

    preliminary = int(weighted * scaling_factor)

    # Dead code path (distractor)
    extra_buffer = []
    for _ in range(2):
        extra_buffer.append('placeholder')  # Unused

    final_rank = preliminary + (5 if preliminary % 2 == 0 else -3)
    return final_rank

# Main data input
benchmark_data = [
    {'value': 12, 'flag': True, 'status': 'active'},
    {'value': 8, 'flag': False, 'status': 'inactive'},
    {'value': 15, 'flag': True, 'status': 'active'},
    {'value': 3, 'flag': True, 'status': 'pending'}
]

# Key computation
final_score = compute_ranking(benchmark_data)
print(f"Target result: {final_score}")