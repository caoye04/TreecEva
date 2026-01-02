from itertools import accumulate

def find_balance(masses, forces):
    moments = [m * f for m, f in zip(masses, forces)]
    total_moment = sum(moments)
    total_mass = sum(masses)
    
    if total_mass == 0:
        return 0
    
    center_of_mass = total_moment / total_mass
    
    # Calculate cumulative moment from left
    cum_moments = list(accumulate(moments))
    
    # Find first position where cumulative moment exceeds half total
    for i, cm in enumerate(cum_moments):
        if cm >= total_moment / 2:
            return i + 1  # Position index (1-based)
    
    return len(moments)

# System weights and applied torques
weights = [10, 20, 30, 40]
torques = [1, 2, 1, 3]

# Irrelevant distraction variable (minimal interference)
dummy_calc = sum([x**2 for x in weights]) / len(weights)

equilibrium_point = find_balance(weights, torques)
print(f"Result: {equilibrium_point}")