from collections import defaultdict

def calculate_network_load(matrix, efficiency):
    load_counter = defaultdict(float)
    for i, row in enumerate(matrix):
        for j, data_rate in enumerate(row):
            if data_rate > 0 and (i + j) % 2 == 0:
                key = f"node_{min(i, j)}"
                load_counter[key] += data_rate * efficiency.get((i, j), 0.5)
    return sum(load_counter.values()) + len(load_counter)

def monitor_system_health(log_entries):
    error_count = 0
    for entry in log_entries:
        if "ERROR" in entry:
            error_count += 1
    return error_count > 5

data_buffer = [0.1, 0.4, 0.8]
transmission_matrix = [
    [10, 0, 30],
    [0, 25, 0],
    [15, 0, 20]
]
efficiency_map = {
    (0, 0): 0.9,
    (0, 2): 0.75,
    (1, 1): 0.8,
    (2, 0): 0.65,
    (2, 2): 0.7
}

total_load = calculate_network_load(transmission_matrix, efficiency_map)

# Simulate health check with dummy logs
logs = ["INFO: startup", "DEBUG: retrying", "ERROR: timeout"]
health_alert = monitor_system_health(logs)

print(f"Result: {total_load}")