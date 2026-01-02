from itertools import combinations

def analyze_phases(readings):
    phase_pairs = list(combinations(readings, 2))
    diff_map = {i: abs(a - b) for i, (a, b) in enumerate(phase_pairs)}
    return sum(diff_map.values())

# Simulated sensor data from three environmental zones
temp_z1 = [23.5, 24.1, 22.9, 25.0]
temp_z2 = [26.3, 25.8, 27.1, 26.0]
temp_z3 = [20.2, 21.5, 19.8, 22.0]

# Misleading auxiliary computation (dead-end analysis)
baseline_avg = (sum(temp_z1[:2]) + sum(temp_z2[:2])) / 6
offset_tracker = [round(x - baseline_avg, 2) for x in temp_z3]
proxy_metric = sum(offset_tracker) * 0.75  # Not used later

# Core grouping logic with distraction via redundant transforms
raw_groups = [temp_z1, temp_z2, temp_z3]
processed = [
    [round(val ** 0.5 * 2, 3) for val in group] for group in raw_groups
]  # transformed but not optimally meaningful

# Weight assignment with red herring tuple unpacking
weights_config = [(0.5, 'low'), (0.3, 'med'), (0.2, 'high')]
_, w1 = weights_config[0]
w2, _ = weights_config[1]
w3, label = weights_config[2]
scaling_factor = len(temp_z1) / 4  # Neutral factor, equals 1.0

# Distractor: unused permutation set
permutation_pool = list(itertools.permutations([w1, w2, w3], 2))
path_count = len(permutation_pool)

# Real weighting using lambda-based aggregation strategy
aggregation_rule = lambda data, weight: sum(x * weight for x in data)

# Secondary distraction: conditional branch that doesn't affect outcome
if proxy_metric < -5:
    adjustment = 10
else:
    adjustment = 0  # Always taken, but trivial

intermediate_scores = []
for idx, grp in enumerate(processed):
    base_score = aggregation_rule(grp, [w1, w2, w3][idx])
    adjusted_score = base_score + adjustment  # adjustment is zero
    intermediate_scores.append(round(adjusted_score, 4))

# Additional noise: enumeration over zipped irrelevant pairing
aux_sum = 0
for i, (orig, proc) in enumerate(zip(raw_groups, processed)):
    delta = sum(proc) - sum(orig)
    aux_sum += delta * (i + 1)

# Final tally combines actual scores with correct weights
def final_tally(groups, weights):
    raw_averages = [sum(g) / len(g) for g in groups]
    weighted_total = sum(avg * w for avg, w in zip(raw_averages, weights))
    penalty = analyze_phases([weighted_total])  # Triggers combination logic, returns 0
    return int(round(weighted_total - penalty))

# Critical execution point
equilibrium_score = final_tally(groups=raw_groups, weights=[w1, w2, w3])
print(f"Result: {equilibrium_score}")