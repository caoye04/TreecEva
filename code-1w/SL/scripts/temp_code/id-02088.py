from itertools import combinations

def analyze_efficiency(levels):
    efficiency_scores = []
    for i in range(1, len(levels) + 1):
        for combo in combinations(levels, i):
            efficiency = sum(combo) / len(combo)
            efficiency_scores.append(efficiency)
    return max(efficiency_scores) if efficiency_scores else 0

def calculate_utilization_rate(config):
    total = 0
    for val in config:
        if val % 2 == 0:
            total += val * 1.5
        else:
            total += val * 0.8
    return total

def calculate_system_capacity(units):
    baseline = 0
    adjustments = []
    temp_buffer = []

    for unit in units:
        if unit.get('active'):
            baseline += unit['power']
            adjustments.append(unit['efficiency_factor'])
            temp_buffer.append(unit['buffer'])

    # Misleading computation - not used in final result
    avg_buffer = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    buffer_variance = sum((x - avg_buffer) ** 2 for x in temp_buffer)

    # Relevant transformation
    utilization_data = [x * 1.2 for x in adjustments if x > 0.5]
    normalized_adjustment = sum(utilization_data) * 0.75

    # Dummy string processing (irrelevant but adds cognitive load)
    status_log = "System units: " + ", ".join([f"U{i}" for i in range(len(units))])
    warning_flags = set(status_log.split())
    flag_count = len([w for w in warning_flags if 'U' in w and len(w) > 2])

    # Core logic step: apply adjustment to baseline
    adjusted_capacity = baseline * (1 + normalized_adjustment / 100)

    # Additional red herring: unused dictionary aggregation
    summary_stats = {
        'count': len(units),
        'active_units': len([u for u in units if u['active']]),
        'total_power': baseline,
        'phantom_metric': len(warning_flags.intersection({'System', 'units:', 'U0'}))
    }

    # Final capacity calculation - depends only on adjusted_capacity and fixed offset
    system_age_discount = 5  # Assumed constant
    final_capacity = int(adjusted_capacity - system_age_discount)

    return final_capacity

# Simulate sensor input data from hardware units
sensor_units = [
    {'power': 40, 'efficiency_factor': 0.65, 'buffer': 12, 'active': True},
    {'power': 35, 'efficiency_factor': 0.72, 'buffer': 10, 'active': True},
    {'power': 20, 'efficiency_factor': 0.45, 'buffer': 8, 'active': False},
    {'power': 50, 'efficiency_factor': 0.88, 'buffer': 15, 'active': True},
    {'power': 30, 'efficiency_factor': 0.55, 'buffer': 9, 'active': True}
]

# Irrelevant pre-processing (adds noise)
data_strings = ["node_{}".format(i).upper() for i in range(len(sensor_units))]
discovered_nodes = set(filter(lambda x: 'NODE' in x, data_strings))

# Trigger analysis chain
baseline_efficiency = analyze_efficiency([u['power'] for u in sensor_units if u['active']])
system_config = [u['power'] for u in sensor_units]
util_rate = calculate_utilization_rate(system_config)

# Key execution point
final_capacity = calculate_system_capacity(sensor_units)
print(f"Result: {final_capacity}")