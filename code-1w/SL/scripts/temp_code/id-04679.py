def calculate_net_torque():
    positions = [1, 2, 3, 4, 5]
    masses = [10, 20, 30, 40, 50]
    gravity = 9.8
    
    # Calculate forces at each position (mass * gravity)
    forces = [m * gravity for m in masses]
    
    # Split forces into left and right of center (position 3)
    pivot_index = 2  # corresponds to position 3
    forces_left = [f * (pivot_index - i) for i, f in enumerate(forces[:pivot_index])]
    forces_right = [f * (i - pivot_index) for i, f in enumerate(range(len(positions))) if i > pivot_index]
    
    # Key computation step
    equilibrium_point = sum(forces_left) - sum(forces_right)
    
    # Irrelevant auxiliary calculation (minimal distraction)
    max_force = max(forces)
    total_momentum = sum([f * p for f, p in zip(forces, positions)])
    
    print(f"Result: {equilibrium_point}")

calculate_net_torque()