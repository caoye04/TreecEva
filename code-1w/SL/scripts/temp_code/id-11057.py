from itertools import compress

def calculate_equilibrium(pressures, flows):
    # Identify active channels where flow rate exceeds threshold
    threshold = 0.5
    active_mask = [f > threshold for f in flows]
    active_pressures = list(compress(pressures, active_mask))
    
    # Compute adjusted mean pressure only for active channels
    if active_pressures:
        avg_pressure = sum(active_pressures) / len(active_pressures)
        adjustment = len(active_pressures) * 0.1
        return avg_pressure + adjustment
    else:
        return 0.0

# Sensor readings from 6 monitoring points
pressures = [1.2, 2.4, 1.8, 3.0, 0.9, 2.1]
flow_rates = [0.3, 0.7, 0.6, 0.4, 0.2, 0.8]

# Calculate final system equilibrium pressure
equilibrium_pressure = calculate_equilibrium(pressures, flow_rates)
print(f'Result: {equilibrium_pressure}')