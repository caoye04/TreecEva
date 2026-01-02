def analyze_pattern(sequence):
    if not sequence:
        return 0
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def useless_transform(data):
    temp = [x * 2 + 1 for x in data]
    shifted = [temp[-i] for i in range(1, len(temp)+1)]
    return [z // 2 for z in shifted]

# Unused constant (red herring)
MAX_THRESHOLD = 98765

# Simulated sensor readings (some relevant, some not)
sensor_a = [3, 1, 4, 1, 5, 9, 2]
sensor_b = [2, 7, 1, 8, 2, 8, 1]
sensor_c = [1, 6, 1, 8, 0, 3, 3]

# Distractor: complex but unused transformation chain
transformed = list(map(lambda x: x ** 0.5, filter(lambda y: y > 2, sensor_a)))
aggregated = [sum(pair) for pair in zip(sensor_a, sensor_b)]
differences = [b - a for a, b in zip(aggregated, sensor_c)]

# Real metric computation begins here
base_metrics = [
    sum(sensor_a),
    max(sensor_b) - min(sensor_b),
    analyze_pattern(sensor_c),
    len([x for x in aggregated if x > 5])
]

# Weight vector for scoring (critical)
weights = [0.2, 0.5, 0.1, 0.2]

# Another decoy function that is defined but never used
def compute_entropy(vals):
    from math import log
    total = sum(vals)
    probs = [v / total for v in vals if v > 0]
    return -sum(p * log(p) for p in probs)

# Misleading intermediate calculation (dead path)
temp_score = 0
for idx, val in enumerate(base_metrics):
    if idx % 2 == 0:
        temp_score += val * 0.1  # Not part of final logic

# Key data structure: enumerated weighted terms
weighted_terms = []
for i, (metric, weight) in enumerate(zip(base_metrics, weights)):
    contribution = metric * weight
    weighted_terms.append(contribution)

# Final evaluation using lambda-based reduction
evaluate_performance = lambda mets, wts: sum(m * w for m, w in zip(mets, wts))

# Critical assignment point
final_score = evaluate_performance(base_metrics, weights)

# Additional noise: unused tuple unpacking
data_snapshot = (sensor_a[:2], sensor_b[1:3], sensor_c[-2:])
prev, curr, last = data_snapshot

# Output must be printed exactly once
print(f"Result: {final_score}")