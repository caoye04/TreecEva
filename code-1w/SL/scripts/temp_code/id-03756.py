def analyze_utilization(patterns):
    total_load = 0
    peak_moment = 0
    for seq in patterns:
        segment_sum = sum(seq)
        if segment_sum > peak_moment:
            peak_moment = segment_sum
        total_load += segment_sum
    return total_load, peak_moment

# Simulate system resource allocation across time slices
def calculate_remaining_capacity(units, threshold):
    base_allocation = 1000
    adjustment_factor = 0.85
    temp_buffer = []
    
    for u in units:
        if u > threshold:
            temp_buffer.append(u * adjustment_factor)
        else:
            temp_buffer.append(u)
    
    processed = temp_buffer[::2]  # Slice every other element for downsampling
    aggregated = sum(processed)
    
    # Irrelevant computation: tracking index patterns (distractor)
    index_tracker = []
    for i, val in enumerate(processed):
        if val % 2 == 0:
            index_tracker.append(i * 1.5)
    
    # Actual capacity logic
    overhead = len(processed) * 5
    final_capacity = base_allocation - aggregated - overhead
    
    # Dead code path (misleading)
    if len(index_tracker) > 100:
        final_capacity += sum(index_tracker)
        
    return final_capacity

# Main execution
workload_segments = [
    [12, 15, 23, 8],
    [45, 18, 9, 31],
    [7, 41, 29, 14],
    [36, 22, 10, 5]
]

# Extract key unit values using slicing from flattened data
flattened_units = [val for segment in workload_segments for val in segment]
selected_units = flattened_units[1:-1]  # Exclude first and last

threshold = 20

# Perform utilization analysis (irrelevant to final answer but adds distraction)
analysis_result = analyze_utilization(workload_segments)

# Key statement
final_capacity = calculate_remaining_capacity(selected_units, threshold)

print(f"Result: {final_capacity}")