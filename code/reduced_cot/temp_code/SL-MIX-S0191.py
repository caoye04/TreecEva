warehouse_data = {
    'zone_A': 150,
    'zone_B': 85,
    'zone_C': 210,
    'zone_D': 45
}
priority_zones = ['zone_C', 'zone_A', 'zone_D']
adjustment_factor = 25
final_quantity = warehouse_data[priority_zones[1]] - adjustment_factor
print(f"Result: {final_quantity}")