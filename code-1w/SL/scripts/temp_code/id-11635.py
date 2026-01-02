def calculate_storage(flow, limit):
    total = 0
    for value in flow:
        adjusted = value * 0.85 if value > limit else value * 0.65
        total += adjusted
    return int(total)

grid_flow = [120, 150, 90, 200, 175]
threshold = 140
temp_log = [f'Reading: {x}' for x in grid_flow]  # Irrelevant logging (distractor)
status_flag = True if sum(grid_flow) > 500 else False
energy_capacity = calculate_storage(grid_flow, threshold)
print(f'Target result: {energy_capacity}')