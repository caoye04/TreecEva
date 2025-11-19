obstacle_map = {
    'A': frozenset(['rock', 'tree']),
    'B': frozenset(['bush', 'pond']),
    'C': frozenset(['fence', 'gate']),
    'D': frozenset(['stairs', 'ramp'])
}

sensor_readings = [
    frozenset(['rock', 'bush', 'fence']),
    frozenset(['tree', 'pond']),
    frozenset(['gate', 'ramp'])
]

# State machine transitions based on set intersections
transitions = {
    ('root', True): 'A',
    ('root', False): 'B',
    ('A', True): 'C',
    ('A', False): 'D',
    ('B', True): 'D',
    ('B', False): 'C'
}

# Confidence modifiers for each node
confidence_modifiers = {node: len(obstacles) for node, obstacles in obstacle_map.items()}

# Initialize state and confidence
current_state = 'root'
navigation_confidence = 0.0

# Traverse the tree for 3 levels
for level in range(3):
    if current_state == 'root':
        # At root, check intersection with any known obstacle
        detected = any(sensor_readings[level] & obstacles for obstacles in obstacle_map.values())
    else:
        # At other nodes, check intersection with specific obstacle set
        detected = bool(sensor_readings[level] & obstacle_map[current_state])
    
    # Update confidence
    if current_state != 'root':
        navigation_confidence += confidence_modifiers[current_state] * (1.5 if detected else 0.5)
    
    # Transition to next state
    current_state = transitions.get((current_state, detected), 'root')

print(f"Result: {navigation_confidence}")