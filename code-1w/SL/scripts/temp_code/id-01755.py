from collections import defaultdict

def calculate_energy_deficit(states):
    daily_supply = defaultdict(float)
    daily_demand = defaultdict(float)
    
    # Log energy supply and demand per day
    for day, readings in enumerate(states):
        for sensor_id, supply, demand in readings:
            daily_supply[day] += supply
            daily_demand[day] += demand
    
    # Calculate deficit for each day
    deficits = []
    for day in sorted(daily_supply.keys()):
        deficit = daily_demand[day] - daily_supply[day]
        if deficit > 0:
            deficits.append(deficit)
    
    total_deficit = sum(deficits)
    return total_deficit

# Simulated grid states: (sensor_id, energy_supply, energy_demand)
grid_states = [
    [('A1', 120.5, 130.0), ('B2', 80.0, 95.0)],
    [('A1', 140.0, 135.0), ('C3', 60.0, 70.0)],
    [('B2', 90.0, 85.0), ('C3', 65.0, 65.0)]
]

total_deficit = calculate_energy_deficit(grid_states)
print(f"Result: {total_deficit}")