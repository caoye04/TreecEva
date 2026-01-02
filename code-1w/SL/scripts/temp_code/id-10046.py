from itertools import accumulate

def balance_finder(values):
    total = sum(values)
    running = 0
    for i, value in enumerate(values):
        if running == total - running - value:
            return i
        running += value
    return -1

# Environmental monitoring simulation
population_levels = [15, 7, 8, 20, 10]
baseline = [x * 0.5 for x in population_levels]
offset = sum(baseline[::2])  # Irrelevant distractor: slicing but not used in final logic
smoothed = [round(x, 1) for x in baseline]  # Another red herring

equilibrium_point = balance_finder(population_levels)
print(f"Result: {equilibrium_point}")