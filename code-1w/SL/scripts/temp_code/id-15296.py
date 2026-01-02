from itertools import cycle

def calculate_balance(forces, directions):
    weighted_forces = []
    direction_cycle = cycle(directions)
    
    for force in forces:
        direction = next(direction_cycle)
        adjusted_force = force * (-1 if direction == 'left' else 1)
        weighted_forces.append(adjusted_force)
    
    net_force = sum(weighted_forces)
    equilibrium_point = abs(net_force)
    
    # Irrelevant auxiliary computation (minor distraction, intervention level 5)
    temp_result = [f * 0.1 for f in forces]
    normalized_total = round(sum(temp_result), 2)
    
    return equilibrium_point

# Input data
forces = [15, 23, 18, 14]
directions = ['right', 'left', 'left', 'right']

# Key execution point
equilibrium_point = calculate_balance(forces, directions)
print(f"Result: {equilibrium_point}")