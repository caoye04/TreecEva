def calculate_energy_profile():
    base_input = [350, 720, 1500, 3800, 7600]
    peak_loads = [400, 800, 1600, 4000, 8000]
    efficiency_factor = 4
    
    # Simulate filtered storage capacity using slice of high-yield elements
    active_range = slice(1, 4)
    total_storage = [peak_loads[i] - base_input[i] for i in range(len(base_input))]
    slice_index = 2
    energy_capacity = total_storage[slice_index] // efficiency_factor
    
    # Irrelevant diagnostic variable (minimal interference)
    debug_status = "normal"
    
    print(f"Result: {energy_capacity}")

calculate_energy_profile()