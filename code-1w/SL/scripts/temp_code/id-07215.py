operational_mode = True
standby_reserve = 150
efficiency_factor = 0.85
base_capacity = 950
system_load = (base_capacity + standby_reserve) * 0.6

# Determine active status based on threshold check
threshold = 500
system_active = system_load > threshold

# Compute final load only if system is active
final_load = system_load * efficiency_factor if system_active else 0

# Additional unrelated monitoring variables (minimal interference)
current_phase = 3
voltage_stability = 0.97

Result: final_load