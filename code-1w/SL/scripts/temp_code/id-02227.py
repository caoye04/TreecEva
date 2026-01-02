def calculate_efficiency(rate, press):
    if rate <= 0:
        return 0.0
    base_efficiency = (rate * 0.8) + (press * 0.1)
    adjustment = 0.05 if rate > 50 else 0.02
    return base_efficiency - adjustment

flow_rate = 60
pressure = 25
calibration_factor = 1.05

# Preliminary system check (irrelevant to final result)
system_status = 'active' if flow_rate > 0 else 'inactive'
baseline = 10  # Used in other subsystems, not here

energy_output = calculate_efficiency(flow_rate, pressure) * calibration_factor

print(f"Result: {energy_output}")