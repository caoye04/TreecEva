def calculate_efficiency(input_power, loss_factor, efficiency_ratio):
    adjusted_loss = loss_factor if input_power > 50 else loss_factor * 0.5
    base_efficiency = input_power * efficiency_ratio
    return base_efficiency - adjusted_loss

# System parameters
capacitor_charge = 120
resistance_load = 8.5
energy_output = 0

for cycle in range(3):
    input_level = capacitor_charge / (cycle + 1)
    if input_level >= 60:
        energy_output += calculate_efficiency(input_level, resistance_load, 0.95)
    else:
        energy_output += input_level * 0.8

energy_output = int(energy_output)
print(f"Result: {energy_output}")