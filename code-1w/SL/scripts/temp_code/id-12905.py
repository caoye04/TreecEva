system_status = "active"
base_load = 420
peak_multiplier = 1.6
operational_load = base_load * peak_multiplier
backup_capacity = 700
diagnostic_mode = False

# Key statement
energy_threshold = min(operational_load, backup_capacity) if system_status == "active" else max(operational_load, backup_capacity)

# Irrelevant diagnostic log
if diagnostic_mode:
    print("Running system diagnostics...")

print(f"Result: {energy_threshold}")