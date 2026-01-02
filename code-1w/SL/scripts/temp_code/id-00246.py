from collections import defaultdict

# Simulate daily power grid load balance across regions
energy_production = [120, 150, 130, 160, 140]
energy_demand = [135, 145, 140, 150, 155]

deficit_tracker = defaultdict(int)

for day in range(len(energy_production)):
    surplus = energy_production[day] - energy_demand[day]
    if surplus < 0:
        deficit_tracker[f'day_{day+1}'] = abs(surplus)

# Aggregate total energy deficit over the period
total_deficit = sum(deficit_tracker.values())
print(f'Target result: {total_deficit}')