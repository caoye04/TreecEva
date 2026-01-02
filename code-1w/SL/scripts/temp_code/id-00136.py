import math
from collections import namedtuple

# Define drone movement states
DroneState = namedtuple('DroneState', ['position', 'velocity'])

def distance(z1, z2):
    return abs(z1 - z2)

def update_position(state, move):
    new_pos = state.position + move
    return DroneState(new_pos, move)

# Movement sequences for three drones (complex numbers representing x+yj coordinates)
drone_sequences = [
    [1+2j, 3+1j, -1-2j, 2-1j],
    [2+1j, 1+3j, -2-1j, 1-2j],
    [1+1j, 2+2j, -1-1j, 3-1j]
]

# Initialize drone states
states = [DroneState(0+0j, 0+0j) for _ in range(3)]

detected_convergence_events = 0
convergence_threshold = 1.5
max_steps = max(len(seq) for seq in drone_sequences)

for step in range(max_steps):
    positions = []
    for i in range(3):
        if step < len(drone_sequences[i]):
            states[i] = update_position(states[i], drone_sequences[i][step])
        positions.append(states[i].position)
    
    # Check pairwise distances
    distances = [distance(positions[i], positions[j]) 
                 for i in range(3) for j in range(i+1, 3)]
    
    # Statistical check: mean distance < threshold and max distance < 2*threshold
    if len(distances) > 0:
        mean_dist = sum(distances) / len(distances)
        max_dist = max(distances)
        if mean_dist < convergence_threshold and max_dist < 2 * convergence_threshold:
            detected_convergence_events += 1

print(f"Result: {detected_convergence_events}")