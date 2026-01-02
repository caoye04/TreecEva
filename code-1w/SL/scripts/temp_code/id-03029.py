from collections import defaultdict

# Simulate sensor data flow with timestamped readings
def generate_flow_data():
    raw_readings = [12, 15, 10, 8, 23, 17, 14, 9, 20, 18]
    timestamps = list(range(10))
    return list(zip(timestamps, raw_readings))

# Analyze temporal patterns in data flow
def analyze_trend(readings):
    trend_counter = defaultdict(int)
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend_counter['up'] += 1
        elif readings[i] < readings[i-1]:
            trend_counter['down'] += 1
    return trend_counter

# Calculate system equilibrium based on deviation from threshold
def calculate_equilibrium(data, base_threshold):
    values = [v for t, v in data]
    
    # Irrelevant aggregation - distractor
    avg_val = sum(values) / len(values)
    peak = max(values)
    normalized_total = 0
    for v in values:
        if v > avg_val:
            normalized_total += (v - avg_val) ** 0.5
    
    # Core logic: count significant deviations
    deviation_count = 0
    rolling_sum = 0
    temp_buffer = []
    
    for val in values:
        rolling_sum += val
        temp_buffer.append(val)
        if len(temp_buffer) > 3:
            temp_buffer.pop(0)
        
        # Check deviation from threshold
        diff = abs(val - base_threshold)
        if diff > 5 and val > base_threshold:
            deviation_count += 1
    
    # Secondary condition: suppress overcounting
    if deviation_count > 3:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 1.0
    
    # Compute equilibrium score
    trend_analysis = analyze_trend(values)
    upward_pressure = trend_analysis['up']
    downward_pressure = trend_analysis['down']
    pressure_diff = upward_pressure - downward_pressure
    
    # Final score with adjustment
    raw_score = rolling_sum * 0.1 + pressure_diff * 2
    equilibrium_score = int(raw_score * adjustment_factor)  # Key assignment
    
    # Dead code branch - red herring
    if False:
        backup_score = sum(temp_buffer) - deviation_count
        equilibrium_score = backup_score
    
    return equilibrium_score

# Main execution
flow_data = generate_flow_data()
threshold = 12

# Extraneous computation - irrelevant to final result
duplicate_data = [x for x in flow_data if x[1] % 2 == 0]
even_timestamps = [t for t, v in duplicate_data]

# Key statement
equilibrium_score = calculate_equilibrium(flow_data, threshold)

# Output result
print(f"Result: {equilibrium_score}")