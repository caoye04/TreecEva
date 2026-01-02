def calculate_thermal_output(energy, efficiency):
    base_output = energy * efficiency
    adjustment_factor = 1.0 if energy > 500 else 0.85
    peak_load = 42  # legacy threshold, not used in current calc
    degradation_rate = 0.03
    
    for cycle in range(3):
        base_output -= base_output * degradation_rate
    
    # Red herring computation: simulates auxiliary system
    aux_power = 0
    for hour in range(1, 8):
        aux_power += (hour ** 2) / 100  # irrelevant to main result
    
    final_output = base_output * adjustment_factor
    
    # Distractor block: emergency override logic (never triggered here)
    override_threshold = 999
    if energy > override_threshold:
        final_output = 0
    
    return final_output

# System initialization parameters
temperature_profile = [23.5, 24.1, 22.7, 25.3]
efficiency_factor = 0.92
energy_reserves = 760
system_status = "nominal"

# Ancillary diagnostic array (unused in calculation)
diagnostic_codes = [0x1A, 0x2B, 0x3C]
error_counter = 0
for code in diagnostic_codes:
    if code % 2 == 0:
        error_counter += 1

# Core physics model execution
target_flux = sum(temperature_profile) * 15.5  # red herring value
effective_yield = energy_reserves * 0.77  # intermediate check

# Key statement
thermal_capacity = calculate_thermal_output(energy_reserves, efficiency_factor)

# Final output reporting
print(f"Result: {thermal_capacity}")