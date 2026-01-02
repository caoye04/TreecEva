from itertools import combinations

# Simulate a multi-phase signal analysis with combinatorial filtering
raw_signals = [3, 5, 7, 11, 13]
filtered_pairs = list(combinations(raw_signals, 2))

# Irrelevant baseline calibration (distractor)
calibration_offset = sum([x % 2 for x in raw_signals])
bias_factor = len(raw_signals) - calibration_offset

# Signal interaction matrix generation (semi-relevant)
interaction_products = []
for pair in filtered_pairs:
    product = pair[0] * pair[1]
    if product % 4 == 0:
        interaction_products.append(product + bias_factor)
    else:
        interaction_products.append(product)

dynamic_weights = [p % 7 for p in interaction_products]

# Primary inertial accumulation (relevant)
inertial_contributions = []
for i, w in enumerate(dynamic_weights):
    if i % 3 == 0:
        inertial_contributions.append(w * 2)
    elif i % 5 == 0:
        inertial_contributions.append(w // 2)
    else:
        inertial_contributions.append(w)

inertial_sum = sum(inertial_contributions) // len(inertial_contributions)

# Oscillation potential via conditional expression chain (relevant)
base_amplitude = len(filtered_pairs)
amplitude_shift = base_amplitude if base_amplitude > 10 else 10
oscillation_potential = amplitude_shift * 2 + (15 if any(p > 100 for p in interaction_products) else 8)

# Red herring: unused recursive function
# def useless_recurse(n):  # Dead code path
#     return useless_recurse(n-1) if n > 0 else 0

# Key statement determining answer
# What is the value of equilibrium_score after this line?
equilibrium_score = max(inertial_sum, oscillation_potential) - min(inertial_sum, oscillation_potential)

# Print final result
print(f"Result: {equilibrium_score}")