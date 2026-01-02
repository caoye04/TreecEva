def optimize_storage(sizes, ratings):
    base = sum([s * 0.85 for s in sizes])
    adjustment_factor = sum(map(lambda r: r['factor'], ratings))
    return int(base * adjustment_factor)

# System configuration parameters (some irrelevant)
max_load = 1200
voltage_stability = 0.93
units = [150, 200, 100, 300]
temp_monitoring_enabled = True

# Efficiency mapping with case-insensitive keys
efficiency_data = {
    'A': {'factor': 1.2},
    'b': {'factor': 0.8},
    'C': {'factor': 1.5}
}

# Normalize keys to uppercase for consistent access
efficiency_map = {k.upper(): v for k, v in efficiency_data.items()}

# Additional environmental constants (not used in main logic)
cooling_required = False
baseline_offset = 42

# Main computation
aggregate_size = sum(units)
scaled_capacity = aggregate_size * 0.75
final_capacity = optimize_storage(units, efficiency_map)

print(f"Result: {final_capacity}")