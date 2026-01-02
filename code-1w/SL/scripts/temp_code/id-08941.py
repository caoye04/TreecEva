def analyze_system_efficiency():
    base_temps = {20, 25, 30, 35, 40}
    adjustment_factors = {0.8, 1.0, 1.2, 1.4}
    temp_set = set()
    for t in base_temps:
        if t > 25:
            temp_set.add(t * 1.1)
    
    # Irrelevant computation: energy loss estimation (not used in final result)
    energy_loss = 0
    for i in range(3):
        energy_loss += i * 0.5
    energy_loss = round(energy_loss, 2)
    
    # Flow rate calculation with dummy branches
    volume = 150
    time_units = 3
    flow_rate = volume / time_units if time_units > 0 else 0
    
    # Red herring: pressure build-up simulation (dead-end logic)
    pressure = 0
    for step in range(5):
        pressure += step * 2
        if pressure > 20:
            pressure = 20
            break  # Early exit, but value unused
    
    # Conditional adjustment based on set membership
    scaling_factor = 1.0
    if 33.0 in temp_set:  # 33.0 comes from 30*1.1
        scaling_factor = 1.3
    elif 38.5 in temp_set:  # 38.5 from 35*1.1
        scaling_factor = 1.5

    def calculate_thermal_response(temps, flow):
        total = 0
        count = 0
        for t in temps:
            if t >= 33.0:
                total += t * flow
                count += 1
        average_effect = total / count if count > 0 else 0
        return int(average_effect * scaling_factor)  # Final integer conversion

    # Key execution point
    thermal_capacity = calculate_thermal_response(temp_set, flow_rate)
    
    # Dummy post-processing (irrelevant)
    diagnostics = []
    for val in sorted(temp_set):
        diagnostics.append(f"Temp: {val}")
    
    print(f"Result: {thermal_capacity}")

analyze_system_efficiency()