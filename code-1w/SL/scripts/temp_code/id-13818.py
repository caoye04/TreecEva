from itertools import accumulate

# Simulate mechanical load distribution across a beam
def calculate_load_balance():
    positions = [1, 2, 3, 4, 5]
    weights = [10, 20, 30, 40, 50]
    pivot = 3

    # Calculate moments on left and right sides of pivot
    forces_left = [w for p, w in zip(positions, weights) if p < pivot]
    forces_right = [w for p, w in zip(positions, weights) if p > pivot]

    # Moment arm effect roughly modeled as weight * (distance from pivot)
    moment_left = [w * (pivot - p) for p, w in zip(positions, weights) if p < pivot]
    moment_right = [w * (p - pivot) for p, w in zip(positions, weights) if p > pivot]

    total_moment_left = sum(moment_left)
    total_moment_right = sum(moment_right)

    # Equilibrium metric: imbalance in force sums (not moments)
    equilibrium_point = sum(forces_left) - sum(forces_right)

    # Additional analysis (irrelevant to answer but adds minor context)
    trend = list(accumulate(weights))
    stability_index = total_moment_left - total_moment_right

    return equilibrium_point

result = calculate_load_balance()
print(f"Result: {result}")