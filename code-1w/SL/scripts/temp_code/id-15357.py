def calculate_efficiency(rate, pressure):
    if rate <= 0:
        return 0.0
    base_efficiency = (rate * 0.8) + (pressure * 0.2)
    return base_efficiency if base_efficiency <= 1.0 else 1.0

flow_rate = 75
pressure = 90
calibration_factor = 1.5

# Some auxiliary monitoring variables (minimal interference)
system_status = "online"
temperature = 45  # Celsius, not used in calculation
diagnostic_log = [flow_rate, pressure]

# Key computational statement
energy_output = calculate_efficiency(flow_rate, pressure) * calibration_factor

# Additional post-processing step using list comprehension
efficiency_metrics = [x * energy_output for x in diagnostic_log if x > 80]

# Final result output
Result: energy_output