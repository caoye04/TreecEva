def calculate_remaining_capacity(nodes, failed):
    active_nodes = nodes - failed
    base_capacity_per_node = 12.5
    redundancy_factor = 0.8
    total_capacity = active_nodes * base_capacity_per_node * redundancy_factor
    
    # Conditional adjustment for small clusters
    capacity_adjustment = 2.5 if active_nodes <= 3 else 0.0
    total_capacity += capacity_adjustment
    
    return total_capacity

# System configuration
storage_nodes = 7
failed_nodes = 2
recovery_reserve = 5.0  # Irrelevant distractor variable

temp_log_entry = "System check: nominal"  # Distractor log

# Key computation
final_capacity = calculate_remaining_capacity(storage_nodes, failed_nodes)

print(f"Result: {final_capacity}")