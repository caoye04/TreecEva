from collections import defaultdict

# Simulate sensor readings over time with some noise
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 26.0, 23.2]
humidity_readings = [45, 47, 50, 44, 55, 48, 52, 46]

# Irrelevant auxiliary data (distractor)
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1011, 1014, 1016]  # Not used
altitude_data = [50, 52, 51, 55, 53, 54, 56, 58]  # Dead code path

# State tracking for anomalies (partially relevant)
anomaly_count = 0
recent_alerts = []

# Preprocess: detect temperature fluctuations above threshold
temp_changes = [abs(temperature_readings[i] - temperature_readings[i-1]) for i in range(1, len(temperature_readings))]
threshold_exceeded = [change > 1.0 for change in temp_changes]

# Count anomalies using defaultdict (relevant)
sensor_anomalies = defaultdict(int)
sensor_anomalies['temp'] = sum(threshold_exceeded)
sensor_anomalies['humidity_spike'] = len([h for h in humidity_readings if h > 50])

# Misleading computation: complex but unused pressure trend analysis (distractor)
pressure_trend = 0
for i in range(1, len(pressure_readings)):
    if pressure_readings[i] > pressure_readings[i-1]:
        pressure_trend += 1
    elif pressure_readings[i] < pressure_readings[i-1]:
        pressure_trend -= 1

# Simulate conditional alert logic with short-circuiting (relevant)
high_risk_condition = (
    sensor_anomalies['temp'] > 2 and 
    sensor_anomalies['humidity_spike'] > 1 or 
    False  # Hardcoded false to simulate fallback
)

if high_risk_condition:
    recent_alerts.append('CRITICAL')
else:
    recent_alerts.append('MONITORING')

# Data transformation: normalize temperature for scoring (relevant)
mean_temp = sum(temperature_readings) / len(temperature_readings)
normalized_deviation = [abs(t - mean_temp) for t in temperature_readings]
avg_deviation = sum(normalized_deviation) / len(normalized_deviation)

def calculate_performance_rating():
    base_score = 100
    
    # Apply deductions based on anomaly levels
    temp_penalty = sensor_anomalies['temp'] * 3
    humidity_penalty = sensor_anomalies['humidity_spike'] * 2
    
    # Red herring: unused function-local variables (distractor)
    debug_trace = []
    internal_counter = 0
    for i in range(5):
        internal_counter += i ** 2
        debug_trace.append(f"step_{i}")
    
    # Real scoring logic
    score = base_score - temp_penalty - humidity_penalty
    
    # Bonus if deviation is low (conditional)
    if avg_deviation < 1.0:
        score += 10
    
    # Final adjustment based on control flow outcome
    if 'CRITICAL' in recent_alerts:
        score -= 15
    else:
        score -= 5
        
    return score

# Execute main logic
final_score = calculate_performance_rating()

# Print result as required
print(f"Result: {final_score}")