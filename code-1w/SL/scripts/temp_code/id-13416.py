def calculate_network_capacity(speeds, redundancy):
    base_total = sum(speeds)
    adjusted_total = base_total * (1.0 - 0.1 * (redundancy - 1)) if redundancy > 1 else base_total
    stability_bonus = 50 if adjusted_total > 800 and redundancy >= 2 else 0
    return adjusted_total + stability_bonus

# Network configuration parameters
link_speeds = [100, 200, 150, 300]
redundancy_factor = 2
temp_offset = 0.0  # Irrelevant variable for minimal interference
final_capacity = calculate_network_capacity(link_speeds, redundancy_factor)
print(f"Target result: {final_capacity}")