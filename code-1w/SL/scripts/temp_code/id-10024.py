from collections import defaultdict, Counter

# Simulate a distributed sensor network with node health monitoring
def analyze_sensor_cluster(nodes):
    node_metrics = defaultdict(list)
    temp_readings = []
    error_flags = []

    for idx, data in enumerate(nodes):
        raw_value = data['temp'] * 1.8 + 32  # Convert to Fahrenheit (unused red herring)
        normalized = data['temp'] / max(1, data['humidity'])
        node_metrics[data['zone']].append(normalized)

        if data['errors'] > 0:
            error_flags.append(idx)

        temp_readings.append(data['temp'])

    # Misleading statistical summary (not used in final result)
    error_summary = dict(Counter([nodes[i]['zone'] for i in error_flags]))
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0

    # Secondary processing: efficiency per zone
    zone_efficiency = {}
    for zone, values in node_metrics.items():
        peak = max(values)
        trough = min(values)
        efficiency = (peak - trough) / (peak + 1)  # Avoid division by zero
        zone_efficiency[zone] = round(efficiency, 4)

    # Simulated load balancing weights (distractor computation)
    total_zones = len(zone_efficiency)
    balance_weights = [abs(1/total_zones - v) for v in zone_efficiency.values()]
    average_weight = sum(balance_weights) / len(balance_weights) if balance_weights else 0.0

    # Core calculation chain
    cluster_load = sum(temp_readings) % 97  # Modular arithmetic key step
    stability_score = len(error_flags) * avg_temp  # Unused but plausible distraction

    def calculate_thermal_metric(load, factor):
        # Complex but focused metric
        base = load * 13
        shift = 0
        for i in range(2, 5):
            if load % i == 0:
                shift += i * 2
        result = (base + shift) / (factor + 1)
        return int(result)  # Deterministic integer output

    efficiency_factor = sum(zone_efficiency.values()) * 100
    efficiency_factor = max(10, int(efficiency_factor))  # Ensure minimum factor

    # Key execution point
    thermal_capacity = calculate_thermal_metric(cluster_load, efficiency_factor)

    # Dead code path - never executed (deliberate interference)
    if False:
        fallback = 0
        for z in node_metrics:
            fallback += len(node_metrics[z])
        thermal_capacity = fallback

    # Final output
    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Input data - fixed sensor readings for deterministic execution
sensor_network = [
    {'temp': 22, 'humidity': 45, 'zone': 'A', 'errors': 1},
    {'temp': 25, 'humidity': 60, 'zone': 'A', 'errors': 0},
    {'temp': 19, 'humidity': 55, 'zone': 'B', 'errors': 0},
    {'temp': 30, 'humidity': 40, 'zone': 'B', 'errors': 2},
    {'temp': 27, 'humidity': 65, 'zone': 'C', 'errors': 0},
    {'temp': 20, 'humidity': 35, 'zone': 'C', 'errors': 1},
    {'temp': 24, 'humidity': 50, 'zone': 'D', 'errors': 0}
]

# Execute main logic
result = analyze_sensor_cluster(sensor_network)