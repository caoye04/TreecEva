def analyze_resource_allocation():
    initial_stock = 850
    delivery_lag = 12
    consumption_rate = 18
    safety_margin = 45
    peak_demand = 95

    # Simulate daily resource depletion over delivery lag period
    projected_depletion = consumption_rate * delivery_lag
    current_inventory = initial_stock - projected_depletion

    # Set thresholds for alert levels
    min_threshold = 100
    warning_level = 200
    critical_level = 50

    # Calculate buffer allocations
    base_buffer = current_inventory * 0.1
    dynamic_buffer = (peak_demand - consumption_rate) * 2
    total_buffer = int(base_buffer + dynamic_buffer)

    # Track historical peaks (irrelevant to final result)
    past_peaks = [78, 92, 88, 95, 84]
    average_peak = sum(past_peaks) / len(past_peaks)
    peak_variance = sum((p - average_peak) ** 2 for p in past_peaks) / len(past_peaks)

    # Resource pools
    available_resources = current_inventory + total_buffer
    reserved_pool = 120

    # Red herring: unused function call
    def calculate_reorder_point(demand, lead_time, service_factor=1.2):
        return demand * lead_time * service_factor

    reorder_point = calculate_reorder_point(consumption_rate, delivery_lag)

    # Distractor: conditional that doesn't affect outcome
    if current_inventory < warning_level:
        alert_status = "YELLOW"
        contingency_release = 30
        available_resources += contingency_release  # This branch is not taken
    else:
        alert_status = "GREEN"
        contingency_release = 0

    # Core logic step
    final_capacity = max(available_resources - reserved_pool, min_threshold)

    # Additional noise variables
    efficiency_ratio = available_resources / initial_stock
    utilization_log = [efficiency_ratio * 0.95, efficiency_ratio * 1.02]

    print(f"Result: {final_capacity}")

analyze_resource_allocation()