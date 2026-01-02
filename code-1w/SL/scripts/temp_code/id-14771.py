def analyze_signal_strength(signal_data):
    # Irrelevant helper: computes average signal but not used in final result
    total = 0
    count = 0
    for entry in signal_data:
        if entry > 0:
            total += entry
            count += 1
    return total / count if count else 0

def validate_slice_integrity(slice_list):
    # Distractor function: checks for negative values but not crucial
    for s in slice_list:
        if s < 0:
            return False
    return True

def calculate_remaining_capacity(slices, loads):
    # Core logic with slicing and conditional reductions
    base_capacity = 1000
    threshold = 50
    adjustment_factor = 0.9
    
    # Misleading pre-processing
    filtered_slices = slices[1:-1]  # Remove first and last (distractor use)
    temp_sum = sum(filtered_slices) * 0.1  # Used nowhere important
    
    active_load = 0
    overload_penalty = 0
    
    for i, load in enumerate(loads):
        if i % 2 == 0 and load > threshold:
            active_load += load
        if load > 80:
            overload_penalty += 10
    
    # Key slicing operation: analyze mid-section of loads
    mid_loads = loads[2:6]
    surge_count = 0
    for load in mid_loads:
        if load > 75:
            surge_count += 1
    
    # Real impact on capacity
    capacity_reduction = active_load * 1.5 + surge_count * 5
    final_capacity = base_capacity - capacity_reduction - overload_penalty
    
    # Dead code branch (never executed due to data)
    if len(slices) > 100:
        final_capacity *= adjustment_factor  # Not triggered
    
    return int(final_capacity)

# Simulated 5G network data
network_slices = [10, 25, 30, 45, 20, 50, 35]
signal_readings = [88, 76, 92, 65, 81, 77, 89]
user_loads = [40, 55, 70, 85, 90, 60, 45]

# Irrelevant calls adding cognitive load
avg_signal = analyze_signal_strength(signal_readings)
is_valid = validate_slice_integrity(network_slices)

# Critical execution point
final_capacity = calculate_remaining_capacity(network_slices, user_loads)

print(f"Result: {final_capacity}")