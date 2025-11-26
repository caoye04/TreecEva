from collections import Counter

def calculate_capacity(active_nodes, max_bandwidth=100):
    # Distractor: unused parameter and misleading calculation
    unused_temp = active_nodes * 2 + max_bandwidth // 3
    return active_nodes * max_bandwidth

def validate_nodes(node_list):
    # Misleading validation that doesn't affect main logic
    if len(node_list) > 10:
        return False  # Dead code path
    return sum(node_list) % 2 == 0

def final_calculation(primary, backup):
    # Core logic with multiple steps and distractions
    base_capacity = calculate_capacity(primary)
    
    # Irrelevant intermediate calculation
    misleading_sum = primary + backup * 2 - (backup // 3)
    
    # Actual relevant calculation with conditional expression
    adjusted_capacity = (base_capacity // 2) if primary > backup else (base_capacity * 3 // 4)
    
    # More distractions
    node_status = [primary, backup, misleading_sum]
    status_count = Counter(node_status)
    
    # Final calculation with bitwise operations
    final_value = adjusted_capacity ^ (backup & 0xFF)
    return final_value

# Main execution with irrelevant variables
primary_nodes = 7
backup_nodes = 5
redundancy_factor = 3  # Unused variable
system_load = 85  # Misleading constant

# Irrelevant validation that doesn't affect result
node_list = [primary_nodes, backup_nodes]
validation_result = validate_nodes(node_list)

# The key execution point
network_throughput = final_calculation(primary_nodes, backup_nodes)

# Print the target result
print(f"Target result: {network_throughput}")