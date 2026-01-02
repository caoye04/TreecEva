def calculate_system_capacity(base_load, maintenance_mode, peak_demand):
    adjusted_base = base_load * 0.9 if maintenance_mode else base_load * 1.1
    demand_surged = peak_demand > 85
    growth_factor = 0.2 if demand_surged and not maintenance_mode else 0.05
    final_capacity = adjusted_base * (1 + growth_factor if demand_surged else 0.5)
    
    # Irrelevant tracking variables (minimal interference)
    status_log = "Normal" if not maintenance_mode else "Maintenance"
    peak_level = "High" if peak_demand > 70 else "Low"
    
    return final_capacity

result = calculate_system_capacity(800, False, 90)
print(f"Target result: {result}")