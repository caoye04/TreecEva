def calculate_storage_efficiency():
    # Define disk zones: primary, backup, and spare
    primary_zones = {1, 2, 3, 4, 5}
    backup_zones = {4, 5, 6, 7}
    spare_zones = {8, 9, 10, 11}

    # Simulate current utilization
    active_tasks = [1, 3, 5]
    utilized_zones = set(active_tasks)  # Zones currently in use

    # Critical calculation: find optimal redundancy zone
    optimal_zone = primary_zones & backup_zones  # Overlapping for fault tolerance

    # Compute final available capacity by combining optimal and unused spares
    final_capacity = optimal_zone | (spare_zones - utilized_zones)

    # Diagnostic metric (irrelevant to final result but plausible)
    efficiency_ratio = len(final_capacity) / (len(primary_zones) + len(spare_zones))

    # Output target result
    print(f"Target result: {len(final_capacity)}")

calculate_storage_efficiency()