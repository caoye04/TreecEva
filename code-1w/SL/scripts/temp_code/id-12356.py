def calculate_efficiency(load_profile):
    base_capacity = 120
    peak_multiplier = 1.75
    efficiency_ratio = 0.88

    adjusted_load = sum([x * 1.2 for x in load_profile if x > 50])
    
    if adjusted_load > base_capacity:
        projected_yield = base_capacity * peak_multiplier
    else:
        projected_yield = adjusted_load * efficiency_ratio

    status_flags = { 'stable': projected_yield < 100, 'critical': False }
    status_flags['critical'] = not status_flags['stable']
    
    energy_threshold = int(projected_yield - 15)  # key assignment
    
    return energy_threshold

# Simulated network load readings
network_load = [45, 60, 75, 55]
energy_threshold = calculate_efficiency(network_load)
print(f"Result: {energy_threshold}")