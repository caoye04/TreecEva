def calculate_peak(segments, factor):
    total_flow = 0
    temp_buffer = []
    adjustment_log = []

    for seg in segments:
        raw_flow = seg[0] * seg[1]
        latency_penalty = seg[2] // 4
        adjusted_flow = raw_flow - latency_penalty
        
        if adjusted_flow > 0:
            temp_buffer.append(adjusted_flow)
    
    sliced_view = temp_buffer[1:-1] if len(temp_buffer) > 3 else temp_buffer
    
    base_sum = sum(sliced_view)
    
    multiplier = factor ** 2
    
    # Irrelevant computation: signal-to-noise simulation (dead path)
    noise_floor = 0
    for i in range(len(segments)):
        noise_floor += (i * 0.5) % 3
    avg_noise = noise_floor / len(segments) if segments else 0
    
    # Distractor: unused metric
    coherence_score = len(temp_buffer) - len(sliced_view)
    
    final_aggregate = base_sum * multiplier
    
    # Actual result calculation
    peak_bandwidth = int(final_aggregate % 97 + 13)
    
    return peak_bandwidth

# System configuration parameters
flow_segments = [
    [12, 8, 5],
    [15, 7, 8],
    [10, 9, 6],
    [14, 6, 10],
    [13, 5, 4]
]
efficiency_factor = 1.8

# Simulated calibration sequence (irrelevant to final answer)
calibration_steps = 0
for i in range(3):
    calibration_steps += (i + 1) * 2

# Main execution point
peak_bandwidth = calculate_peak(flow_segments, efficiency_factor)

print(f"Result: {peak_bandwidth}")