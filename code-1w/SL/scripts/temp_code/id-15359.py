from itertools import combinations

# System calibration parameters
temperature_zones = [23, 19, 27, 21, 25]
efficiency_scores = []

# Simulate efficiency under different threshold conditions
for zone in temperature_zones:
    if zone < 20:
        score = 8.5
    elif zone >= 25:
        score = 6.2
    else:
        score = 9.1
    efficiency_scores.append(score)

# Pair zones with scores
efficiency_map = {zone: efficiency_scores[i] for i, zone in enumerate(temperature_zones)}

# Identify optimal operating zone based on efficiency
optimal_setting = max(efficiency_map, key=lambda x: efficiency_map[x])

# Irrelevant auxiliary calculation (minor distraction)
dummy_result = list(combinations([1, 2, 3], 2))

print(f"Result: {optimal_setting}")