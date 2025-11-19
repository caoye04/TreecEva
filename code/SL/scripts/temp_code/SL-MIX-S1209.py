from collections import namedtuple
from statistics import mean, variance

def calculate_weighted_deviation(temps, weights):
    weighted_temps = [t * w for t, w in zip(temps, weights)]
    return sum(weighted_temps) / sum(weights)

def process_station_data(readings):
    base_temp = 20.0
    anomalies = []
    
    # First processing stage - identify anomalies
    for i, temp in enumerate(readings):
        if abs(temp - base_temp) > 5.0:
            anomalies.append((i, temp))
    
    # Second processing stage - apply weighting based on position
    weights = [1.0 / (i + 1) for i in range(len(readings))]
    weighted_avg = calculate_weighted_deviation(readings, weights)
    
    # Third processing stage - categorize using switch-like logic
    category_scores = {
        'extreme': 0,
        'moderate': 0,
        'normal': 0
    }
    
    for idx, temp in anomalies:
        deviation = abs(temp - weighted_avg)
        if deviation > 10:
            category_scores['extreme'] += 1
        elif deviation > 5:
            category_scores['moderate'] += 1
        else:
            category_scores['normal'] += 1
    
    # Final calculation using statistical measures
    values = list(category_scores.values())
    if len(values) > 1 and variance(values) > 0:
        score = mean(values) * len(anomalies) / (variance(values) + 1)
    else:
        score = mean(values) * len(anomalies)
    
    return round(score, 2)

# Climate station data
station_readings = [
    18.5, 22.1, 35.2, 19.8, 15.4, 21.0, 45.7, 20.3, 17.9, 23.6,
    12.1, 25.8, 19.5, 31.2, 22.7, 16.9, 24.3, 38.9, 21.4, 14.6
]

# Data processing pipeline
StationMetrics = namedtuple('StationMetrics', ['anomaly_count', 'avg_temp', 'score'])
anomaly_count = len([t for t in station_readings if abs(t - 20.0) > 5.0])
avg_temp = mean(station_readings)

# Apply divide and conquer approach to process subsets
mid_point = len(station_readings) // 2
first_half_score = process_station_data(station_readings[:mid_point])
second_half_score = process_station_data(station_readings[mid_point:])

# Combine results using custom logic
if first_half_score > second_half_score:
    final_anomaly_score = first_half_score * 1.5 - second_half_score
elif second_half_score > first_half_score:
    final_anomaly_score = second_half_score * 1.5 - first_half_score
else:
    final_anomaly_score = (first_half_score + second_half_score) / 2

metrics = StationMetrics(anomaly_count, avg_temp, final_anomaly_score)
print(f"Result: {metrics.score}")