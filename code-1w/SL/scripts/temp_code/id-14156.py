def analyze_sensor_data():
    base_readings = [12, -5, 8, 19, -3, 0, 7]
    offset = 3
    adjusted_readings = [x + offset for x in base_readings]
    
    # Filter readings above threshold using slicing and condition
    threshold = 10
    filtered_readings = [val for val in adjusted_readings if val > threshold]
    
    # Efficiency calculation with modular arithmetic
    cycle_count = 7
    efficiency_index = (cycle_count % 4) or 1
    efficiency_factor = 0.85 ** efficiency_index
    
    # Key computation point
    energy_output = sum(filtered_readings) * efficiency_factor
    
    # Irrelevant distraction: logging unrelated status
    status_flags = {"active": True, "calibrated": False}
    temp = [i**2 for i in range(3)]  # Unused list comprehension
    
    print(f"Result: {energy_output}")

analyze_sensor_data()