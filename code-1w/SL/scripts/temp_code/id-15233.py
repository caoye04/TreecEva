def calculate_harvest(layout, factor):
    # Irrelevant preprocessing: normalize layout (does nothing since all are positive)
    normalized = [[max(1, cell) for cell in row] for row in layout]

    # Distractor: unused environmental modifiers
    env_modifiers = list(map(lambda x: x * 0.9 + 0.1, [0.5, 0.7, 0.6, 0.8]))
    saturation_index = sum(env_modifiers) / len(env_modifiers)

    # Real computation begins: count valid growth zones
    zones = 0
    total_growth = 0.0
    for i in range(len(normalized)):
        for j in range(len(normalized[i])):
            if normalized[i][j] >= 3:
                zones += 1
                total_growth += normalized[i][j] * factor

    # Misleading secondary calculation (dead-end)
    hypothetical_yield = zones * 10 if saturation_index > 0.5 else 0
    adjustment = hypothetical_yield * 0.15

    # Actual core logic: apply decay based on zone density
    density_ratio = zones / (len(layout) * len(layout[0])) if zones > 0 else 0
    decay_factor = 1 - (density_ratio * 0.3)

    # Final yield depends only on total_growth and decay_factor
    final_yield = total_growth * decay_factor

    # Unrelated string processing (distractor)
    status_log = "Harvest complete".upper().replace(" ", "_")
    log_length = len(status_log)
    return final_yield

# Define orchard layout (1=young tree, 3=mature, 5=prime)
orchard_layout = [
    [1, 5, 3],
    [2, 4, 1],
    [3, 3, 5]
]
growth_factor = 2.5

# Unused helper function (red herring)
def predict_rainfall():
    return sum([i * 0.2 for i in range(5)])

# State tracking with irrelevant counters
iteration_count = 0
update_history = []

final_yield = calculate_harvest(orchard_layout, growth_factor)
print(f"Result: {final_yield}")