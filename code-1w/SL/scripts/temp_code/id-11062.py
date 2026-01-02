from itertools import accumulate

def find_balance(masses, forces):
    # Calculate torque at each position
    torques = [m * f for m, f in zip(masses, forces)]
    
    # Compute cumulative torque from left and right
    left_accum = list(accumulate(torques))
    right_accum = list(accumulate(reversed(torques)))
    right_accum.reverse()
    
    # Find equilibrium point where left and right torque are balanced
    for i in range(len(torques)):
        left_torque = left_accum[i]
        right_torque = right_accum[i]
        if abs(left_torque - right_torque) < 1e-3:
            return i + 1
    return -1

# System parameters
weights = [2.0, 3.0, 1.5, 4.0, 2.5]
torques = [1.0, -1.0, 2.0, -2.5, 1.5]

# Irrelevant distraction: unused sensor calibration
sensor_offset = 0.05
baseline_readings = [sensor_offset * w for w in weights]

# Key computation
equilibrium_point = find_balance(weights, torques)

# Output result
print(f"Result: {equilibrium_point}")