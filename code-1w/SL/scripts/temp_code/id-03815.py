temperature = 24.5
system_state = True
activation_factor = 1.8
is_active = activation_factor > 1.5
diagnostics = [102, 203, 405]
status_code = diagnostics[1] if system_state else diagnostics[0]
energy_threshold = temperature * (is_active if system_state else 0.5)
monitoring_active = status_code == 203

print(f"Result: {energy_threshold}")