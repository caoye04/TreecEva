temperature = 37.5
hours_operating = 8
is_active = True
device_load = 120  # irrelevant variable (minimal interference)
base_rate = 0.8     # irrelevant variable

# Key computation with conditional expression
energy_threshold = temperature * (is_active if hours_operating > 5 else 0.5)

# Additional logic to justify execution flow without adding noise
if energy_threshold > 30:
    energy_threshold = energy_threshold // 2 + base_rate

print(f"Result: {energy_threshold}")