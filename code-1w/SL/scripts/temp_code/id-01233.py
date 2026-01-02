from collections import defaultdict

# System efficiency map by sector
efficiency_map = defaultdict(float)
efficiency_map['hydro'] = 0.88
efficiency_map['solar'] = 0.91
efficiency_map['wind'] = 0.85
efficiency_map['geothermal'] = 0.96

# Raw installed capacities (in MW)
systems = [
    {'name': 'delta_hydro_1', 'type': 'hydro', 'capacity': 240},
    {'name': 'desert_solar_3', 'type': 'solar', 'capacity': 500},
    {'name': 'coastal_wind_2', 'type': 'wind', 'capacity': 380},
    {'name': 'valley_geothermal_1', 'type': 'geothermal', 'capacity': 120},
    {'name': 'plains_wind_5', 'type': 'wind', 'capacity': 420}
]

# Filter systems with capacity > 300 MW and calculate effective output
efficient_systems = [s for s in systems if s['capacity'] > 300]
filtered_types = [s['type'] for s in efficient_systems]

# Calculate adjusted capacity using efficiency
adjusted_capacities = []
for system in efficient_systems:
    adjusted = system['capacity'] * efficiency_map[system['type']]
    adjusted_capacities.append(adjusted)

# Final aggregation step
total_capacity = sum(capacity for capacity in adjusted_capacities)
print(f"Result: {total_capacity}")