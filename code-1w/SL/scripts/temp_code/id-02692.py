from itertools import compress

def filter_anomalies(data, limit):
    """Identify readings above threshold."""
    anomalies = [x > limit for x in data]
    return list(compress(data, anomalies))

def process_readings(abnormal, base):
    """Calculate deviation score from baseline."""
    if not abnormal:
        return 0
    
    # Irrelevant intermediate calculation (distractor)
    squared_total = sum(x ** 2 for x in abnormal if x < 150)
    adjusted_base = base * 1.05 if len(abnormal) > 2 else base
    
    # Core logic: average deviation from base
    deviations = [abs(val - adjusted_base) for val in abnormal]
    avg_dev = sum(deviations) / len(deviations)
    
    # Extra distraction: unused smoothing logic
    smoothed = [deviations[i] * 0.9 + 0.1 * deviations[i-1] for i in range(1, len(deviations))] if deviations else []
    
    return avg_dev

# Simulated sensor input
sensor_data = [98, 102, 145, 160, 170, 89, 130, 180]
baseline = 100
threshold = 150

# Auxiliary variables (some irrelevant)
outlier_flags = [x >= max(sensor_data) * 0.95 for x in sensor_data]
duplicate_check = set(sensor_data)
data_count = len(sensor_data)
filtered_readings = filter_anomalies(sensor_data, threshold)

# Key computation with moderate interference
final_diagnostic = process_readings(filter_anomalies(sensor_data, threshold), baseline)

# Print result as required
print(f"Target result: {final_diagnostic}")