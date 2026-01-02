def analyze_system_load():
    # System resource monitoring simulation
    base_units = [120, 85, 95, 110, 75, 130, 90]
    thresholds = {"low": 80, "high": 115}
    
    # Historical usage patterns (simulated)
    usage_log = [88, 92, 77, 105, 68, 125, 83]
    temp_buffer = [x * 1.1 for x in usage_log]  # Simulated peak adjustments (not used directly)
    
    # Redundant capacity reserve calculation (distractor)
    reserve_pool = 0
    for val in base_units:
        if val > thresholds["high"]:
            reserve_pool += val * 0.1
    
    # Active load filtering and window analysis
    active_loads = []
    for i in range(len(usage_log)):
        if usage_log[i] > thresholds["low"]:
            active_loads.append(usage_log[i])
    
    # Slice recent high-usage events for diagnostic (semi-relevant)
    recent_spikes = active_loads[-3:]  # Last three high-usage periods
    spike_average = sum(recent_spikes) / len(recent_spikes) if recent_spikes else 0
    
    # Capacity degradation model (core logic)
    capacities = [base - 5 for base in base_units]  # Base operational capacity after overhead
    degraded_count = 0
    for i in range(len(capacities)):
        if capacities[i] < thresholds["low"]:
            degraded_count += 1
    
    # Simulated recovery buffer (distractor)
    recovery_buffer = [capacities[i] + 10 for i in range(len(capacities)) if i % 2 == 0]
    
    # Core function to compute remaining usable capacity
    def calculate_remaining(caps, log):
        total_available = sum(caps)
        total_used = sum(log)
        efficiency_ratio = 0.95
        if total_used > 0:
            efficiency_ratio = min(0.95, total_available / (total_used * 1.1))
        return int((total_available - total_used) * efficiency_ratio)

    final_capacity = calculate_remaining(capacities, usage_log)
    
    # Diagnostic print (irrelevant to result)
    diagnostics = f"Degraded Units: {degraded_count}, Spike Avg: {spike_average:.2f}"
    
    # Output target result
    print(f"Result: {final_capacity}")
    
    return final_capacity

result = analyze_system_load()