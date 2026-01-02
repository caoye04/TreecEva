from itertools import accumulate

# Simulate daily production output in a manufacturing plant over a week
base_output = [85, 90, 78, 92, 88, 95, 80]
decay_factor = 0.1

efficiency_boost = [1.1, 1.0, 1.2, 1.05, 1.15, 0.95, 1.0]

daily_output = []
for i in range(7):
    adjusted = int(base_output[i] * efficiency_boost[i])
    if i > 0:
        adjusted = int(adjusted * (1 - decay_factor))
    daily_output.append(adjusted)

# Apply cumulative maintenance impact on the last three days
maintenance_impact = [0.9, 0.85, 0.8]
for j in range(4, 7):
    daily_output[j] = int(daily_output[j] * maintenance_impact[j - 4])

# Compute peak capacity
peak_capacity = max(daily_output)

# Print result for evaluation
print(f"Result: {peak_capacity}")