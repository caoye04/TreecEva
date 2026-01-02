from itertools import accumulate

# Simulate a physics-based weight distribution problem across a beam
weights = [3, 7, 1, 6, 5, 4]
positions = list(range(1, len(weights) + 1))

# Compute torque contributions (weight * position)
torques = [w * p for w, p in zip(weights, positions)]

total_torque = sum(torques)
total_weight = sum(weights)

center_of_gravity = total_torque / total_weight

# Find split index where left and right segments balance approximately
left_segment = weights[:3]
right_segment = weights[3:]

# Calculate cumulative weight distribution on both sides
left_cumulative = list(accumulate(left_segment))
right_cumulative = list(accumulate(right_segment[::-1]))[::-1]

# Estimate balancing point using final accumulated values
balance_left = left_cumulative[-1] * 2
balance_right = right_cumulative[0] * 2 + 1  # Offset by 1 for asymmetry

equilibrium_point = balance_left == balance_right

# Irrelevant distraction: unused slicing operation
unused_slice = weights[1:4:2]

print(f"Result: {equilibrium_point}")