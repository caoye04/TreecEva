def calculate_system_efficiency():
    voltage_levels = [110, 120, 130, 140, 150]
    current_draw = [2.1, 2.3, 2.0, 2.4, 2.2]
    
    efficiencies = []
    for i, volt in enumerate(voltage_levels):
        power_in = volt * current_draw[i]
        useful_output = power_in * 0.85  # Assume 85% base conversion
        adjusted_efficiency = useful_output / power_in * 100
        efficiencies.append(round(adjusted_efficiency, 2))
    
    total_avg = sum(efficiencies) / len(efficiencies)
    peak_efficiency = max(efficiencies)
    
    redundant_copy = efficiencies.copy()  # Minor distraction
    temp_sum = 0
    for val in redundant_copy:
        temp_sum += val
    
    return peak_efficiency

result = calculate_system_efficiency()
print(f"Result: {result}")