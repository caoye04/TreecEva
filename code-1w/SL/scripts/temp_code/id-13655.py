def calculate_remaining_capacity(grid_zones, occupied):
    total_capacity = 0
    for zone in grid_zones:
        if zone not in occupied:
            total_capacity += len(zone)
    return total_capacity

# System configuration
grid_layout = ['ABCD', 'EFGH', 'IJKL', 'MNOP']
reserved = {'EFGH', 'MNOP'}

# Irrelevant auxiliary variable (minor distraction)
backup_zones = grid_layout[1:3]

# Key computation
available_zones = [z for z in grid_layout if z not in reserved]
final_capacity = calculate_remaining_capacity(available_zones, reserved)

# Output result
print(f"Result: {final_capacity}")