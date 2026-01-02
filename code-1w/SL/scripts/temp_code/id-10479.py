def calculate_system_efficiency(voltage, cells_per_module):
    total_cells = cells_per_module * 4
    base_threshold = 12
    system_active = voltage >= base_threshold
    auxiliary_power = 3.5
    active_modules = 2 if system_active else 1
    energy_capacity = total_cells // active_modules if system_active else 0
    diagnostic_code = 100 + (total_cells % 4)
    return energy_capacity

result = calculate_system_efficiency(15, 6)
print(f"Result: {result}")