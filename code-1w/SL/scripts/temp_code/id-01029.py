def calculate_remaining_capacity(nodes, threshold):
    active_loads = [load for _, load in nodes if load > threshold]
    normalized = [round(load * 0.85) for load in active_loads]
    
    # Irrelevant distraction: metadata collection (minimal interference)
    node_names = [name for name, _ in nodes]
    total_nodes = len(node_names)
    
    if len(normalized) == 0:
        return 0
    
    avg_load = sum(normalized) / len(normalized)
    peak = max(normalized)
    efficiency_factor = 0.9 if avg_load > 40 else 1.0
    
    # Key computation with integer division and conditional logic
    base_capacity = 1000
    used_capacity = (avg_load * len(normalized)) // 1  # integer division as control point
    remaining = base_capacity - used_capacity
    final_capacity = int(remaining * efficiency_factor)
    
    # Unrelated side calculation (low interference)
    zipped_data = list(zip(node_names, [len(str(x)) for x in normalized]))
    unused_sum = sum(len(item[0]) for item in zipped_data)
    
    return final_capacity

# Setup input data using enumerate and set operations (required python features)
raw_usage = [35, 60, 20, 80, 45]
indexed_nodes = list(enumerate(raw_usage))
storage_nodes = [(f'node_{i}', usage) for i, usage in indexed_nodes]

# Use set to filter out duplicate thresholds (though none here, demonstrates concept)
distinct_thresholds = set([30])
usage_threshold = min(distinct_thresholds)

# Execute main logic
def main():
    result = calculate_remaining_capacity(storage_nodes, usage_threshold)
    print(f"Target result: {result}")

main()