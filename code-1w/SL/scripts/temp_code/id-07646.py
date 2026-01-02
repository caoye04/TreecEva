from collections import defaultdict

def find_balance(forces, torques):
    net_force = sum(forces)
    net_torque = sum(torques)
    
    # Calculate equilibrium point assuming linear relationship
    if net_force != 0:
        equilibrium = net_torque / net_force
    else:
        equilibrium = 0
        
    return equilibrium

# Simulate mechanical load distribution
weights = [12, -5, 8, -15]
moments = [24, -15, 32, -30]

# Secondary calculation (irrelevant but plausible)
stats = defaultdict(int)
for w in weights:
    if w > 0:
        stats['positive'] += 1
    else:
        stats['negative'] += 1

# Key computation
result_vector = [a * b for a, b in zip(weights, moments)]
total_energy = sum(result_vector) // 2 if result_vector else 0

# Target assignment
equilibrium_point = find_balance(weights, moments)

print(f"Result: {equilibrium_point}")