from itertools import accumulate

def find_balance(masses, lever_arms):
    # Calculate torques (force * distance)
    torques = [m * a for m, a in zip(masses, lever_arms)]
    
    # Compute cumulative torque from left
    left_accum = list(accumulate(torques))
    
    # Total system torque
    total_torque = sum(torques)
    
    # Find the first point where cumulative torque >= half of total
    threshold = total_torque / 2.0
    equilibrium_index = None
    for i, acc in enumerate(left_accum):
        if acc >= threshold:
            equilibrium_index = i
            break
    
    # Some irrelevant auxiliary calculations (minimal distraction)
    avg_mass = sum(masses) / len(masses)
    peak_torque = max(torques)
    
    return equilibrium_index

# Physical system parameters
weights = [10, 20, 15, 25, 30]
moments = [1, 2, 3, 4, 5]

# Key computation
equilibrium_point = find_balance(weights, moments)

# Output result
print(f"Result: {equilibrium_point}")