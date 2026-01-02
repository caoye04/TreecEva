from itertools import combinations

# Simulate a mechanical equilibrium calculation on a lever
def calculate_torque(position, force):
    return position * force

def find_balance(masses, moments):
    total_mass = sum(masses)
    total_moment = sum(moment for moment in moments)
    
    # Conditional expression to avoid division by zero
    center_of_gravity = total_moment / total_mass if total_mass != 0 else 0
    
    # Use lambda to filter potential pivot points near center
    valid_pivots = list(filter(lambda x: abs(x - center_of_gravity) < 5, range(-10, 11)))
    
    # Simple combinatorics: count symmetric pairs around center
    sym_pairs = list(combinations([p for p in valid_pivots if p < center_of_gravity], 2))
    adjustment = len(sym_pairs) * 0.5
    
    return center_of_gravity + adjustment

# Given input data
positions = [2, -3, 5, -1]
forces = [10, 15, 6, 20]
weights = [abs(f) for f in forces]
torques = [calculate_torque(p, f) for p, f in zip(positions, forces)]

equilibrium_point = find_balance(weights, torques)
print(f"Result: {equilibrium_point}")