def calculate_remaining_capacity(nodes, failed):
    active_nodes = nodes - failed
    base_capacity_per_node = 120
    redundancy_factor = 0.85
    total_capacity = len(active_nodes) * base_capacity_per_node * redundancy_factor
    return int(total_capacity)

# System configuration
all_nodes = set(range(1, 11))
unresponsive = {3, 7, 9}
decommissioned = {1, 10}

failed_during_audit = unresponsive.union(decommissioned)
storage_nodes = sorted(list(all_nodes))
failed_nodes = list(failed_during_audit)

# Case conversion for log normalization (irrelevant to calculation but part of workflow)
log_status = "ERROR"
normalized_log = log_status.lower() if log_status else "info"

initial_estimate = 960
adjustment_factor = 0.95

# Main computation
final_capacity = calculate_remaining_capacity(storage_nodes, failed_nodes)
print(f"Result: {final_capacity}")