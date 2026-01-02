from itertools import accumulate

def calculate_torque(sequence):
    return [i * val for i, val in enumerate(sequence)]

def find_balance(masses, forces):
    weights = [m * 9.8 for m in masses]
    moments = calculate_torque([f * 1.5 for f in forces])
    net_force = sum(weights)
    net_moment = sum(moments)
    
    # Compute running sum of moments to find equilibrium index
    cum_moments = list(accumulate(moments))
    
    # Find first index where cumulative moment exceeds half total
    threshold = net_moment / 2
    equilibrium_index = next((i for i, cm in enumerate(cum_moments) if cm >= threshold), len(cum_moments))
    
    adjustment_factor = 0.75
    equilibrium_point = equilibrium_index + adjustment_factor
    
    # Irrelevant auxiliary variable (minimal distraction)
    dummy_result = sum(w ** 0.5 for w in weights if w > 10)
    
    return equilibrium_point

# Input data
masses = [2, 5, 3, 8, 1]
forces = [4, 7, 6, 9, 2]

# Key execution point
equilibrium_point = find_balance(masses, forces)

print(f"Result: {equilibrium_point}")