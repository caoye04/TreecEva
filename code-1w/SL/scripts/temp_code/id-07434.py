from collections import defaultdict

def calculate_energy_balance(grid, limits):
    surplus = defaultdict(float)
    deficit = defaultdict(float)
    total_surplus = 0.0
    total_deficit = 0.0

    for region, flow in grid.items():
        if flow > limits[region]:
            surplus[region] = flow - limits[region]
            total_surplus += surplus[region]
        else:
            deficit[region] = limits[region] - flow
            total_deficit += deficit[region]

    adjustment_factor = 1.0 if total_surplus == 0 else total_surplus / len(grid)
    scaling_constant = 0.85  # Minor distraction

    return total_deficit * scaling_constant

# Energy flow data (MW)
grid_flow = {
    'north': 420.5,
    'south': 380.0,
    'east': 460.3,
    'west': 390.7
}

thresholds = {
    'north': 410.0,
    'south': 395.0,
    'east': 450.0,
    'west': 400.0
}

baseline_reference = 98.6  # Irrelevant constant for minor distraction

result_code = 200  # Status code, unrelated to computation

# Key execution point
total_deficit = calculate_energy_balance(grid_flow, thresholds)

print(f"Target result: {total_deficit}")