from collections import defaultdict

# System resource simulation: tracking container capacity usage over time
def main():
    # Core data structures
    capacities = {
        'container_A': 250,
        'container_B': 300,
        'container_C': 180,
        'container_D': 400
    }

    # Historical usage log (timestamp -> [list of used amounts])
    usage_log = [
        [50, 30, 20],
        [40, 10, 60],
        [25, 35],
        [100, 50, 20, 30]
    ]

    # Distractor: Redundant tracking of peak usage per container (not used in final result)
    peak_tracker = defaultdict(int)
    for key, cap in capacities.items():
        peak_tracker[key] = cap * 0.9  # Simulated historical peak

    # Auxiliary function to compute efficiency ratio (distractor - not used directly)
    def compute_efficiency(usage_list):
        total_used = sum(usage_list)
        operations = len(usage_list)
        if operations == 0:
            return 0.0
        return round(total_used / operations, 3) if total_used > 50 else 0.1

    # Secondary distractor: simulate maintenance cycles that don't affect current calc
    maintenance_schedule = []
    for i in range(len(usage_log)):
        cycle = {"id": i, "required_downtime": len(usage_log[i]) * 2}
        maintenance_schedule.append(cycle)

    # Simulate background process that logs string-based status (uses string methods)
    status_messages = []
    for entry in usage_log:
        msg = f"Batch processed: {len(entry)} operations, total load: {sum(entry)}"
        msg = msg.replace('Batch', 'Cycle').upper()
        status_messages.append(msg)

    # Actual core logic disguised among distractors
    base_sum = sum(capacities.values())
    total_usage = 0
    temp_ratios = []

    for log in usage_log:
        batch_total = sum(log)
        total_usage += batch_total
        if batch_total > 0:
            temp_ratios.append(round(batch_total ** 0.5, 2))  # Intermediate stat, semi-relevant

    # Key transformation: scale total_usage by average root usage
    adjustment_factor = 1.0
    if temp_ratios:
        avg_root = sum(temp_ratios) / len(temp_ratios)
        adjustment_factor = max(0.5, min(1.5, avg_root / 10))

    adjusted_usage = int(total_usage * adjustment_factor)

    # Helper function that appears general but is only used once
    def calculate_remaining(container_map, log):
        raw_capacity = sum(container_map.values())
        usage_sum = sum([sum(entry) for entry in log])
        reserved = raw_capacity * 0.1  # 10% reserved space
        return raw_capacity - usage_sum - int(reserved)

    final_capacity = calculate_remaining(capacities, usage_log)

    # Dead code path - never executed but adds cognitive load
    debug_mode = False
    if debug_mode and final_capacity < 0:
        print("Error: Negative capacity detected")

    # Output required format
    print(f"Result: {final_capacity}")

if __name__ == "__main__":
    main()