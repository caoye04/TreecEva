def calculate_yield(growth_data, efficiency_rates):
    total_harvest = 0
    status_log = []
    
    for i, (base_yield, days) in enumerate(growth_data):
        growth_factor = 1.0
        
        # Apply daily growth rate based on efficiency schedule
        cycle_efficiency = efficiency_rates[i % len(efficiency_rates)]
        adjusted_yield = base_yield * (1 + cycle_efficiency)
        
        # Simulate incremental harvest per day
        daily_increment = adjusted_yield / max(days, 1)
        
        for _ in range(days):
            growth_factor *= (1 + cycle_efficiency / 10)
        
        final_output = int(daily_increment * days * growth_factor)
        total_harvest += final_output
        
        # Logging irrelevant to computation
        status_log.append(f'Cycle {i}: completed')
    
    # Dummy dictionary for equipment tracking (not used in calculation)
    equipment = {'sensor': True, 'irrigation': False}
    system_check = sum(1 for v in equipment.values() if v)  # Distractor: not used

    # Linear search for max base yield (distractor operation)
    max_base = 0
    for base, d in growth_data:
        if base > max_base:
            max_base = base
    peak_reference = max_base  # Unused in main logic

    return total_harvest

# Input data
growth_data = [(40, 5), (60, 4), (50, 6)]
efficiency_rates = [0.12, 0.15]

result = calculate_yield(growth_data, efficiency_rates)
print(f"Result: {result}")