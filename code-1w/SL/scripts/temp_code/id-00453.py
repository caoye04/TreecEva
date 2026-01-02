from itertools import compress

# System parameters for load distribution analysis
core_weights = [12, 18, 24, 30, 36]
efficiency_flags = [True, False, True, True, False]
scaling_factor = 1.5

# Apply scaling and generate adjusted weights using conditional logic
adjusted_weights = []
for weight in core_weights:
    if weight > 20:
        adjusted_weights.append(weight * scaling_factor)
    else:
        adjusted_weights.append(weight)

# Minor distraction: unused filter operation using itertools
valid_cores = list(compress(core_weights, efficiency_flags))
dropped_count = len(core_weights) - len(valid_cores)

# Critical computation step
total_load = sum(adjusted_weights)

# Print result for evaluation
print(f"Result: {total_load}")