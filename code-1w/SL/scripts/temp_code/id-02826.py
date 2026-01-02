from collections import Counter

def parse_log_entry(entry):
    parts = entry.strip().split('|')
    timestamp = parts[0]
    node_id = parts[1]
    data_size = int(parts[2])
    status = parts[3]
    return node_id, data_size, status

def calculate_packet_weight(data_size, is_error):
    if is_error:
        return data_size * 1.5
    return data_size

def calculate_network_load(transmission_logs):
    log_counter = Counter()
    weighted_load = 0

    for log in transmission_logs:
        node_id, data_size, status = parse_log_entry(log)
        is_error = status == "ERR"
        packet_weight = calculate_packet_weight(data_size, is_error)
        weighted_load += packet_weight
        log_counter[node_id] += 1

    base_load = weighted_load
    adjustment_factor = len(log_counter) * 0.1
    total_load = int(base_load + (base_load * adjustment_factor))
    return total_load

def monitor_system_health():
    system_status = "HEALTHY"
    cpu_usage = 0.68
    memory_usage = 0.45
    return system_status

# Simulated transmission logs
transmission_logs = [
    "2023-09-15T10:01:05|NODE_X|120|OK",
    "2023-09-15T10:02:17|NODE_Y|200|ERR",
    "2023-09-15T10:03:33|NODE_X|80|OK",
    "2023-09-15T10:04:19|NODE_Z|300|OK",
    "2023-09-15T10:05:11|NODE_Y|150|ERR"
]

# Key computation
result = calculate_network_load(transmission_logs)
total_load = result

# Auxiliary unrelated monitoring call
monitor_system_health()

print(f"Target result: {total_load}")