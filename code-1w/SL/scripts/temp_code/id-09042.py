system_age = 8
maintenance_cycles = 12
temperature_rating = 82
humidity_factor = 38
stability_index = True

# Irrelevant maintenance metric (distractor)
maintenance_efficiency = maintenance_cycles / (system_age + 1)

# Key logical evaluation with conditional expression
energy_threshold = temperature_rating > 75 and (humidity_factor < 40 or stability_index if system_age < 10 else False)

Result: energy_threshold