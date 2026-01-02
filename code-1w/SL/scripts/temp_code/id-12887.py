from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 'temp', 23.5), (101, 'humidity', 45), (102, 'temp', 24.1),
    (103, 'pressure', 1013), (104, 'humidity', 47), (105, 'temp', 22.9),
    (106, 'pressure', 1015), (107, 'temp', 25.0), (108, 'humidity', 44)
]

# Aggregate data by type using defaultdict
sensor_data = defaultdict(list)
for ts, s_type, value in timestamped_readings:
    sensor_data[s_type].append(value)

# Extract individual series
temps = sensor_data['temp']
humidities = sensor_data['humidity']
pressures = sensor_data['pressure']

# Misleading intermediate calculations (distractors)
avg_temp = sum(temps) / len(temps)
median_humidity = sorted(humidities)[len(humidities)//2]
total_pressure = sum(pressures)

# Normalized values (not used in final result)
norm_temps = [round((t - min(temps)) / (max(temps) - min(temps)), 3) for t in temps]

# Data transformation: detect rising trends in temperature
rising_trend_count = 0
for i in range(1, len(temps)):
    if temps[i] > temps[i-1]:
        rising_trend_count += 1

# Auxiliary function to compute stability index (semi-relevant)
def compute_stability(values):
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0.0

# Compute fluctuation scores (some used, some not)
temp_fluctuation = compute_stability(temps)
humidity_fluctuation = compute_stability(humidities)
pressure_fluctuation = compute_stability(pressures)

# Processed data structure (key input)
processed_data = {
    'count': len(temps),
    'base_score': int(avg_temp * 10),
    'bonus': rising_trend_count * 5,
    'penalty': int(temp_fluctuation * 2)
}

# Irrelevant helper function (dead code path)
def analyze_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) > threshold * std_dev]

# Another distracting computation
outlier_temps = analyze_outliers(temps)  # Not used later

# Core scoring logic
def calculate_final_score(data):
    score = data['base_score']
    score += data['bonus']
    score -= data['penalty']
    
    # Additional rule: cap score at 300
    if score > 300:
        score = 300
    
    # Extra distraction: unused adjustment
    adjustment_factor = 1.05
    temp_adjusted = score * adjustment_factor  # Computed but not used
    
    return score

# Final execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")