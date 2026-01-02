from itertools import accumulate

def find_balance(masses, forces):
    # Calculate torque at each position (mass * index)
    torques = [m * i for i, m in enumerate(masses)]
    net_force = sum(forces)
    
    # Cumulative sum of torques from left and right
    left_torque = list(accumulate(torques))
    right_torque = list(accumulate(reversed(torques)))[::-1]
    
    # Find equilibrium: where left and right cumulative torques are equal
    equilibrium_index = -1
    for i in range(len(left_torque)):
        if left_torque[i] == right_torque[i]:
            equilibrium_index = i
            break
    
    # Irrelevant distraction: calculate unused kinetic energy estimate
    velocity_estimate = 0.5
    kinetic_energy = sum(0.5 * m * velocity_estimate**2 for m in masses)  # Not used
    
    return equilibrium_index

# System weights and applied forces
total_masses = [2, 3, 1, 4, 2]
applied_forces = [1, -1, 0, 1, -1]

# Compute equilibrium point
equilibrium_point = find_balance(total_masses, applied_forces)

print(f"Result: {equilibrium_point}")