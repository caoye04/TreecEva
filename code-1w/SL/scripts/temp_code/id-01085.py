from itertools import combinations

# Simulate sensor data with noise and valid readings
data = [12, 15, 10, 18, 22, 8]
noise_floor = 5
weight_map = {0: 1.1, 1: 0.9, 2: 1.0, 3: 1.2, 4: 0.8, 5: 1.3}
weights = list(weight_map.values())

# Irrelevant transformation: generate all pairs above threshold (distraction)
pairs_above_threshold = []
for pair in combinations(data, 2):
    if sum(pair) > 30:
        pairs_above_threshold.append(pair)

# Misleading accumulator: computes average deviation but unused later
total_deviation = 0
for i in range(len(data)):
    total_deviation += abs(data[i] - 12)
avg_deviation = total_deviation / len(data)

# Auxiliary function with red herring parameters
def apply_correction(values, factor=1.0, invert=False):
    multiplier = -factor if invert else factor
    return [v * multiplier for v in values]

# Corrective scaling (not actually used in final path)
corrected_data = apply_correction(data, factor=0.95, invert=False)

# Core logic disguised among distractions
def calculate_weighted_sum(vals, wts):
    return sum(v * w for v, w in zip(vals, wts))

# Secondary scoring using filtered high-value sensors (semi-relevant)
high_sensitivity_sum = 0
for i, val in enumerate(data):
    if val > 15:
        high_sensitivity_sum += val * weights[i]

# Another distraction: simulate calibration offset that's never applied
calibration_sequence = [0.1 * i for i in range(len(data))]
baseline_adjustment = sum(calibration_sequence)

# Real computation hidden in lambda and conditional override
use_enhanced = len(pairs_above_threshold) > 2
scoring_rule = lambda x, y: calculate_weighted_sum(x, y) if use_enhanced else sum(x)

# Final score depends on actual condition
def calculate_final_score(vals, wts):
    base_score = scoring_rule(vals, wts)
    penalty = 0
    # Apply penalty if any value exceeds 20
    for v in vals:
        if v > 20:
            penalty += 5
    adjusted_score = base_score - penalty
    
    # Dead code branch: never executed due to fixed flag
    debug_mode = False
    if debug_mode:
        print("Debug:", base_score, penalty)
    
    return adjusted_score

# Execution point of interest
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")