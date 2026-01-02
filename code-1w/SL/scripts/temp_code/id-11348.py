def calculate_remaining(capacities, usage_log):
    total_used = 0
    peak_usage = 0
    temp_buffer = []
    
    for hour, usage in enumerate(usage_log):
        if usage > 50:
            peak_usage += 1
        total_used += usage
        temp_buffer.append(usage * 0.1)  # Irrelevant smoothing

    efficiency_ratio = (total_used / len(usage_log)) / max(usage_log) if usage_log else 0
    
    adjusted_capacities = [c * (0.9 if i % 2 == 0 else 1.1) for i, c in enumerate(capacities)]
    
    aggregate = 0
    for val in adjusted_capacities:
        if val > 100:
            aggregate += val * 0.75
        else:
            aggregate += val * 0.5

    # Misleading intermediate calculation
    projected_waste = sum(temp_buffer) * (1 - efficiency_ratio)
    
    # Key logic: only the first and last capacity matter
    relevant_sum = capacities[0] + capacities[-1]
    usage_factor = total_used / 100.0
    
    final_capacity = int(relevant_sum - usage_factor)
    
    return final_capacity

# Simulated system capacity levels (in MW)
capacities = [120, 85, 95, 110, 130]

# Hourly energy consumption log over 5 hours (in MW)
usage_log = [45, 60, 75, 55, 80]

# Misleading auxiliary variables
dummy_matrix = [[i * j for j in range(3)] for i in range(3)]
scaling_factor = sum(dummy_matrix[0]) / 3  # Unused beyond this

final_capacity = calculate_remaining(capacities, usage_log)
print(f"Result: {final_capacity}")