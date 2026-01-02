from collections import defaultdict

# Simulate sensor data streams with timestamped readings
def generate_sensor_stream(base, noise, length):
    return [base + (i % 5) - noise + (i // 10) for i in range(length)]

# Analyze temporal trends in data flow
def compute_trend(data):
    trend_sum = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_sum += 1
        elif data[i] < data[i-1]:
            trend_sum -= 1
    return trend_sum

# Calculate equilibrium score based on deviation from threshold
def calculate_equilibrium(data, limit):
    total_deviation = 0
    spike_count = 0
    suppression_factor = 0.95
    
    # Irrelevant helper calculation (distractor)
    avg = sum(data) / len(data) if data else 0
    temp_offset = (avg * 0.05) - 2
    
    for val in data:
        if val > limit:
            excess = val - limit
            total_deviation += excess * suppression_factor
            spike_count += 1
        elif val < limit * 0.5:  # Deep drop penalty
            total_deviation += (limit * 0.5 - val) * 0.5
    
    # Secondary adjustment using spike frequency
    adjustment = spike_count * 0.7 if spike_count > 5 else spike_count * 0.3
    final_score = total_deviation - adjustment
    
    # Dead code path (never executed under current logic)
    if final_score < -100:
        final_score = -100  # Clamp lower bound (unreachable here)
    
    return int(final_score)

# Main execution
if __name__ == "__main__":
    # Generate multi-source data flows
    stream_a = generate_sensor_stream(base=18, noise=3, length=15)
    stream_b = generate_sensor_stream(base=22, noise=5, length=15)
    
    # Combine streams with overlap weighting
    flow_data = []
    for i in range(len(stream_a)):
        combined = (stream_a[i] * 0.6) + (stream_b[i] * 0.4)
        flow_data.append(combined)
    
    # Apply moving average filter (slicing operation)
    smoothed_flow = []
    window_size = 3
    for i in range(len(flow_data)):
        start = max(0, i - window_size + 1)
        segment = flow_data[start:i+1]
        smoothed_flow.append(sum(segment) / len(segment))
    
    # Misleading intermediate analysis (distractor)
    histogram = defaultdict(int)
    for val in smoothed_flow:
        bucket = int(val // 5)
        histogram[bucket] += 1
    
    # Unused statistical measures (dead variables)
    variance_proxy = sum((x - sum(smoothed_flow)/len(smoothed_flow))**2 for x in smoothed_flow) / len(smoothed_flow)
    entropy_approx = 0.0
    for count in histogram.values():
        if count > 0:
            p = count / len(smoothed_flow)
            entropy_approx -= p * p  # Not real entropy, just looks complex

    # Key control variable
    threshold = 20
    
    # Critical computation point
    equilibrium_score = calculate_equilibrium(smoothed_flow, threshold)
    
    # Print result as required
    print(f"Result: {equilibrium_score}")