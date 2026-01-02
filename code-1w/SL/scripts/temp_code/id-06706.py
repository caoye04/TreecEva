def calculate_harvest_efficiency(data_map):
    base_threshold = 15
    adjustment_factor = 0.85
    penalty_rate = 0.1
    surplus_tracker = []
    efficiency_bins = {0: 0, 1: 0, 2: 0}

    total_yield = 0
    temp_buffer = []

    for region_id, metrics in data_map.items():
        raw_output = metrics['output']
        labor_hours = metrics['labor']
        rainfall = metrics['rainfall']

        # Irrelevant computation - tracks unused pattern
        if raw_output > base_threshold:
            surplus_tracker.append(raw_output - base_threshold)

        # Core efficiency calculation
        base_efficiency = raw_output / (labor_hours + 1)
        
        # Conditional efficiency boost
        if rainfall > 100:
            base_efficiency *= 1.2
        elif rainfall < 40:
            base_efficiency *= 0.9

        # Dummy state tracking (not used later)
        bin_key = min(int(base_efficiency // 10), 2)
        efficiency_bins[bin_key] += 1

        # Only high-efficiency regions contribute
        if base_efficiency >= 8.0:
            total_yield += base_efficiency

        # Dead code path - never accessed due to logic
        if base_efficiency < 0:
            temp_buffer.append(-base_efficiency)

    # Misleading aggregation
    avg_surplus = sum(surplus_tracker) / len(surplus_tracker) if surplus_tracker else 0
    adjustment_delta = avg_surplus * penalty_rate  # Computed but unused

    # Final adjustment based on active logic
    final_yield = int(total_yield - adjustment_delta + 0.5)
    return final_yield

# Input data
region_data = {
    'north': {'output': 20, 'labor': 2, 'rainfall': 120},
    'south': {'output': 18, 'labor': 3, 'rainfall': 35},
    'east': {'output': 25, 'labor': 4, 'rainfall': 95},
    'west': {'output': 14, 'labor': 1, 'rainfall': 110},
    'central': {'output': 30, 'labor': 5, 'rainfall': 45}
}

# Execution point
final_yield = calculate_harvest_efficiency(region_data)
print(f"Result: {final_yield}")