from itertools import compress

def calculate_stability_metric(data):
    base_levels = [d['temp'] * d['flow_rate'] for d in data]
    normalized = [val / sum(base_levels) * 100 for val in base_levels]
    stable_mask = [val > 15 for val in normalized]
    filtered = list(compress(normalized, stable_mask))
    adjustment_factor = sum(map(lambda x: x ** 0.5, filtered))
    return int(sum(filtered) - adjustment_factor)

# Irrelevant auxiliary data (mild distraction)
constants = {'gravity': 9.81, 'R': 8.314}
waste_data = [1, 1, 0, 0, 1]

# Relevant input data
thermal_data = [
    {'temp': 20, 'flow_rate': 3},
    {'temp': 35, 'flow_rate': 2},
    {'temp': 50, 'flow_rate': 4},
    {'temp': 15, 'flow_rate': 1}
]

pressure_index = calculate_stability_metric(thermal_data)
Result: pressure_index