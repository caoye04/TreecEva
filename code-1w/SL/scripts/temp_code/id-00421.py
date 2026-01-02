def analyze_resource_allocation():
    # Simulate time-based resource availability over a 24-hour cycle
    peak_hours = set(range(8, 18))  # 8 AM to 5 PM
    maintenance_windows = {13, 14}  # Overlaps with peak
    buffer_periods = {7, 18}

    # Total available time slots (excluding maintenance)
    total_slots = set(range(24))
    unavailable = peak_hours.copy()
    unavailable.update(maintenance_windows)
    unavailable.update(buffer_periods)

    # Red herring: Calculate average utilization (not used in final result)
    hourly_demand = [0.1] * 24
    for h in peak_hours:
        hourly_demand[h] = 0.9
    avg_utilization = sum(hourly_demand) / len(hourly_demand)

    # Distractor: Simulate redundant backup calculation
    backup_coverage = set()
    for hour in range(24):
        if hour not in maintenance_windows:
            backup_coverage.add((hour + 1) % 24)
            backup_coverage.add((hour - 1) % 24)

    # Core logic: Identify non-peak, non-buffer slots
    candidate_off_peak = total_slots.difference(peak_hours)
    candidate_off_peak.difference_update(buffer_periods)

    # Introduce irrelevant transformation
    shifted_slots = { (h + 3) % 24 for h in candidate_off_peak }
    sorted_shifted = sorted(shifted_slots)

    # Another distraction: count transitions
    transition_count = 0
    for i in range(len(sorted_shifted) - 1):
        if sorted_shifted[i+1] - sorted_shifted[i] > 1:
            transition_count += 1

    # Main capacity analysis
    reserved_test_slots = {23, 0, 1}  # Special testing window
    candidate_off_peak.difference_update(reserved_test_slots)

    fallback_contingency = set(range(2, 5))
    available_slots = candidate_off_peak.union(fallback_contingency)

    # Key statement
    final_capacity = max(available_slots.difference(unavailable))

    # Print required output
    print(f"Result: {final_capacity}")

    # Additional red herring: compute unused capacity metrics
    unused_ratio = len(available_slots) / 24.0
    capacity_fragmentation = len([i for i in range(23) if (i in available_slots) != (i+1 in available_slots)])

    return final_capacity

analyze_resource_allocation()