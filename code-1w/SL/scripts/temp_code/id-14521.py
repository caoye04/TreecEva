def analyze_performance(record):
    if not record['attempts']:
        return 0
    avg = sum(record['attempts']) / len(record['attempts'])
    bonus = 1.0
    if avg < 5:
        bonus = 1.5
    elif avg < 8:
        bonus = 1.2
    return bonus

def validate_sequence(seq):
    count = 0
    for s in seq:
        if s.isdigit():
            count += int(s) % 3
    return count % 4 == 0

def calculate_efficiency(values):
    total_ops = 0
    temp_store = []
    for v in values:
        if v <= 0:
            continue
        steps = 0
        while v > 1:
            if v % 2 == 0:
                v //= 2
            else:
                v = 3 * v + 1
            steps += 1
        temp_store.append(steps)
    total_ops = sum(temp_store)
    efficiency = len(values) / (total_ops + 1)
    return efficiency if efficiency <= 1 else 1.0

def calculate_final_score(data, mod):
    base = data['base_value']
    multiplier = 1.0

    # Irrelevant tracking (distractor)
    history_log = {'entries': [], 'flags': set()}
    for k in mod:
        if k == 'speed' and mod[k] > 0.7:
            multiplier += 0.3
        elif k == 'accuracy' and mod[k] >= 0.9:
            multiplier += 0.4
        elif k == 'consistency' and mod[k] == 'high':
            multiplier += 0.2

    # Semi-relevant computation (only some branches matter)
    penalty = 0.0
    if data['errors'] > 5:
        penalty += 0.15
    if data['warnings'] and 'critical' in data['warnings']:
        penalty += 0.25

    # Core logic: combinatorics of valid patterns
    sequences = data.get('sequences', [])
    valid_count = 0
    for seq in sequences:
        cleaned = ''.join([c for c in seq if c.isalnum()])
        if validate_sequence(cleaned):
            valid_count += 1

    # Efficiency factor
    efficiency = calculate_efficiency(data['values'])

    # Performance bonus
    record_stats = {'attempts': data['attempts']}
    performance_bonus = analyze_performance(record_stats)

    # Final score calculation (this is the key line)
    final_score = (base * multiplier - penalty * 100) + (valid_count * 10)
    final_score += efficiency * 50
    final_score += performance_bonus * 20

    # Dead code path (irrelevant)
    if final_score < 0:
        final_score = 0
    return int(round(final_score))

# Input data setup
stats = {
    'base_value': 85,
    'errors': 3,
    'warnings': ['minor'],
    'sequences': ['a1b2c3', 'x7y8z9', 'p4q5r6', 'm1n2o3'],
    'values': [7, 2, 5, 10],
    'attempts': [6, 4, 7, 3, 5]
}

modifiers = {
    'speed': 0.85,
    'accuracy': 0.88,
    'consistency': 'medium',
    'reliability': 0.95
}

# Misleading intermediate calculations
phantom_total = 0
for i in range(5):
    phantom_total += i ** 3

buffer_data = {k: v * 2 for k, v in enumerate([1, 1, 2, 3, 5])}
unused_flag = any(x > 20 for x in buffer_data.values())

# Critical execution point
final_score = calculate_final_score(stats, modifiers)
print(f"Result: {final_score}")