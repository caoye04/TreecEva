def calculate_efficiency(rpm, temp):
    base_efficiency = 0.85
    if rpm > 3000:
        efficiency_loss = 0.05 if temp > 80 else 0.02
    else:
        efficiency_loss = 0.01 if temp > 90 else 0.0
    return base_efficiency - efficiency_loss

# System parameters
rpm = 3200
temp = 85
load_factor = 1.2

# Critical computation
energy_output = calculate_efficiency(rpm, temp) * load_factor

# Output result
print(f"Result: {energy_output}")