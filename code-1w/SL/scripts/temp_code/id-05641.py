temperature = 24.5
hours_operating = 10
is_active = True
diagnostics_mode = False
base_calibration = 1.05

# Key computation with conditional expression
energy_threshold = temperature * (is_active if hours_operating > 8 else 0.5)

# Irrelevant diagnostic adjustment (distractor)
diagnostic_energy = base_calibration * 2 if diagnostics_mode else 0

Result: energy_threshold