def calculate_system_capacity():
    base_load = 850
    redundancy_ratio = 1.2
    peak_multiplier = 0.9
    system_age = 3

    # Compute adjusted base capacity considering redundancy and aging
    adjusted_base = int(base_load * redundancy_ratio)
    
    # Efficiency degrades over time; after age 2, it drops to 0.85
    efficiency_factor = 0.85 if system_age > 2 else 1.0

    # System passes status check if name validation succeeds
    system_name = "Node_Γ42"
    status_check = system_name.startswith("Node_") and system_name[5:].isalnum()

    # Final capacity depends on conditional logic and integer division
    final_capacity = adjusted_base // efficiency_factor if status_check else 0
    
    # Irrelevant utility (minimal distraction)
    temp_warning = "Overheat" in ["Normal", "Standby", "Overheat"]

    print(f"Result: {final_capacity}")

    return final_capacity

result = calculate_system_capacity()