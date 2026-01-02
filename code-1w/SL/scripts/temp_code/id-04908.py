def analyze_data_stream(data, threshold=50):
    # Simulate sensor data analysis with noise filtering and trend detection
    filtered_data = [x for x in data if x > threshold]
    
    # Irrelevant transformation: scaling non-filtered values (dead computation)
    scaled_noise = [x * 0.1 for x in data if x <= threshold]
    average_noise = sum(scaled_noise) / len(scaled_noise) if scaled_noise else 0

    # Track trends: count rising pairs in filtered data
    rising_trends = 0
    for i in range(1, len(filtered_data)):
        if filtered_data[i] > filtered_data[i-1]:
            rising_trends += 1

    # Secondary metric: volatility index (semi-relevant)
    if len(filtered_data) > 1:
        volatility = (max(filtered_data) - min(filtered_data)) / len(filtered_data)
    else:
        volatility = 0

    # Distractor: unused health check flag
    system_health = 'OK' if len(filtered_data) > 3 else 'WARNING'

    # Core logic: performance score based on size, trends, and volatility
    base_score = len(filtered_data) * 10
    trend_bonus = rising_trends * 5
    risk_penalty = int(volatility * 2)

    # Final computation
    final_score = base_score + trend_bonus - risk_penalty

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data stream (simulated sensor readings)
data_stream = [45, 67, 58, 72, 74, 68, 80, 85, 42, 30, 90]

# Execute analysis
result = analyze_data_stream(data_stream)