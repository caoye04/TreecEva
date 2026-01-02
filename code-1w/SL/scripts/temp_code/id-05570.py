def analyze_efficiency(record):
    tokens = record.split('_')
    base = len(tokens[0])
    modifier = tokens[1].count('X') - tokens[1].count('N')
    efficiency = base * (1.5 if modifier > 0 else 0.8)
    return efficiency

record_id = 'PROC_XXNNX'
efficiency_rating = analyze_efficiency(record_id)

metrics = [85, 72, 91, 64]
bonus_multiplier = 1.2 if efficiency_rating > 3.0 else 1.0
temp_offset = sum([x % 10 for x in metrics])  # Distractor: not used later
duplicate_check = tuple(x for x in metrics if metrics.count(x) > 1)  # Dead code path

scaling_factor = 0.9
adjusted_metrics = [x * scaling_factor for x in metrics]
penalty = 0
for val in adjusted_metrics:
    if val < 70:
        penalty += 5

# Simulate data transformation
shifted = ''.join([chr(ord(c) + 1) for c in record_id.lower()])
reversed_shift = shifted[::-1]
unused_hash = hash(reversed_shift)  # Irrelevant computation

# Core logic with distractors
buffer = []
for i, m in enumerate(metrics):
    trend = 'up' if i > 0 and m > metrics[i-1] else 'down'
    buffer.append(trend)

growth_count = buffer.count('up')

final_score = process_performance(metrics, bonus_multiplier)

# Helper function defined after use (adds cognitive load)
def process_performance(data, multiplier):
    base_total = sum(data)
    quality_bonus = 10 if all(d >= 60 for d in data) else 0
    consistency = len(data) == len(set(data))  # Check duplicates
    consistency_penalty = -8 if not consistency else 0
    initial_calc = base_total + quality_bonus + consistency_penalty
    applied = int(initial_calc * multiplier)
    if applied > 300:
        applied = 300  # Cap score
    return applied

print(f"Result: {final_score}")