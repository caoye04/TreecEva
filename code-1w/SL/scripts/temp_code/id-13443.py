from collections import defaultdict

# Simulate a physics-based balancing system
def calculate_torque(positions, masses):
    torque = 0
    for i in range(len(positions)):
        torque += masses[i] * positions[i]
    return torque

def find_equilibrium(masses, adjustments):
    positions = list(range(len(masses)))
    adjusted_masses = [masses[i] + adjustments[i] for i in range(len(masses))]
    total_mass = sum(adjusted_masses)
    if total_mass == 0:
        return 0
    center_of_mass = sum(adjusted_masses[i] * positions[i] for i in range(len(positions))) / total_mass
    return round(center_of_mass, 3)

# System parameters
weights = [10, -5, 8, -3]
adjustments = [2, 1, -2, 4]

# Apply lambda-based correction factor for calibration
calibrate = lambda x: x * 1.05

# Initialize diagnostic counter (distractor)
diagnostic_count = defaultdict(int)
diagnostic_count['initialized'] += 1

# Compute equilibrium point
equilibrium_point = find_equilibrium(weights, adjustments)
equilibrium_point = calibrate(equilibrium_point)
equilibrium_point = round(equilibrium_point, 3)

diagnostic_count['completed'] += 1

print(f"Result: {equilibrium_point}")