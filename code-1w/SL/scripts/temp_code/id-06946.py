from itertools import combinations

def analyze_pattern(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

# Simulated sensor flow data with embedded patterns
turbulence_factors = [3, 1, 4, 1, 5, 9, 2, 6]
phase_shifters = [x % 4 for x in turbulence_factors]

# Irrelevant transformation (distractor)
transformed = [abs((x - 2) ** 2 - 1) for x in phase_shifters if x > 1]

# Generate all 3-element subsequences to detect micro-patterns
subsequences = list(combinations(turbulence_factors, 3))
micro_scores = []
for sub in subsequences:
    score = sub[0] + sub[1] * sub[2]
    if score > 10:
        micro_scores.append(score // 2)

# Dead code path (distractor)
if len(micro_scores) > 100:
    adjusted = [x * 0.9 for x in micro_scores]
else:
    adjusted = [x for x in micro_scores]  # No real adjustment

# Core logic masked by noise
flow_data = [x for x in enumerate(turbulence_factors) if x[1] % 2 == 1]
active_indices = [idx for idx, val in flow_data]

threshold = sum(phase_shifters) / len(phase_shifters)

# Secondary distraction: simulate calibration drift
calibration_log = []
for i in range(len(active_indices)):
    if i % 3 == 0:
        calibration_log.append(i * 0.5)

# Main calculation buried in context
def calculate_equilibrium(data, limit):
    base = 0
    for index, value in data:
        base += value * (index + 1)
    adjustment = 0
    for combo in combinations(active_indices, 2):
        i, j = combo
        adjustment += (j - i) % 3
    final = base - int(adjustment * limit)
    return final

# Key execution point
equilibrium_score = calculate_equilibrium(flow_data, threshold)

# Output result
print(f"Result: {equilibrium_score}")