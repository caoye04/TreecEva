def process_results(data, limit):
    # Irrelevant pre-processing (distractor)
    temp_stats = {'count': 0, 'sum': 0}
    for item in data:
        temp_stats['count'] += 1
        temp_stats['sum'] += len(item['name'])

    # Actual logic begins: extract active users and compute weighted metric
    active_users = list(filter(lambda x: x['active'], data))
    base_value = sum(ord(name[0]) for name in [u['name'] for u in active_users])

    # String manipulation with case conversion and character counting (semi-relevant)
    uppercase_count = sum(1 for u in active_users for c in u['name'] if c.isupper())
    adjusted_value = base_value + (uppercase_count * 10)

    # Conditional logic with comparison and logical operations
    bonus = 25 if len(active_users) >= limit and all(len(u['name']) > 3 for u in active_users) else 0

    # Dictionary-based scoring rules
    score_rules = {
        'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1
    }
    rule_multiplier = sum(score_rules.get(u['name'][0], 0) for u in active_users)

    # Final computation (key step)
    final_score = adjusted_value + bonus + rule_multiplier

    # Dead code path (irrelevant)
    if False:
        fallback = [x for x in range(100) if x % 11 == 0]
        final_score -= sum(fallback)

    return final_score

# Input data
user_data = [
    {'name': 'Alice', 'active': True},
    {'name': 'Bob', 'active': False},
    {'name': 'Charlie', 'active': True},
    {'name': 'David', 'active': True},
    {'name': 'Eve', 'active': False}
]
threshold = 3

# Execute main logic
final_score = process_results(user_data, threshold)
print(f"Result: {final_score}")