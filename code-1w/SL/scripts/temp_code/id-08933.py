import math

# Simulated sensor data processing pipeline for environmental monitoring station
def analyze_temperature_readings(raw_readings):
    filtered = [x for x in raw_readings if -50 <= x <= 60]
    avg_temp = sum(filtered) / len(filtered) if filtered else 0
    temp_anomalies = [t for t in filtered if abs(t - avg_temp) > 10]
    return avg_temp, len(temp_anomalies)


def compute_humidity_index(readings):
    index = 0
    for r in readings:
        if r > 80:
            index += 2.1
        elif r > 60:
            index += 1.3
    return round(index * 1.7, 4)

# Irrelevant helper - decoy function dealing with unrelated domain (pressure)
def calculate_pressure_trend(data):
    if not data:
        return 0
    trend = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend += 0.5
        elif data[i] < data[i-1]:
            trend -= 0.3
    return trend * 10  # Scaled arbitrarily

# Unused complex transformation - red herring
def transform_coordinates(latitudes, longitudes):
    transformed = []
    for lat, lon in zip(latitudes, longitudes):
        x = lat * math.cos(lon)
        y = lat * math.sin(lon)
        transformed.append((x, y))
    magnitude = sum(math.sqrt(tx**2 + ty**2) for tx, ty in transformed)
    return magnitude

# Core evaluation logic
def evaluate_air_quality(pollutant_levels):
    score = 0
    for level in pollutant_levels:
        if level < 50:
            score += 10
        elif level < 100:
            score += 7
        elif level < 200:
            score += 4
        else:
            score += 1
    return score

# Misleading intermediate calculation - looks important but unused
def assess_wind_pattern(velocities):
    high_wind_events = 0
    total_energy = 0.0
    for v in velocities:
        if v > 15:
            high_wind_events += 1
        total_energy += 0.5 * 1.225 * (v ** 3)  # Kinetic energy formula
    return {'events': high_wind_events, 'energy': total_energy}

# Key computation chain
def aggregate_performance(metrics, weights):
    weighted_sum = 0.0
    max_possible = 0.0
    for m, w in zip(metrics, weights):
        weighted_sum += m * w
        max_possible += 10 * w  # Max metric score is 10
    efficiency_ratio = weighted_sum / max_possible if max_possible != 0 else 0
    penalty = 0.0
    
    # Additional adjustment based on consistency
    if len(metrics) > 1:
        variance = sum((m - sum(metrics)/len(metrics))**2 for m in metrics) / len(metrics)
        if variance > 4:
            penalty = 0.15
    
    final_normalized = (efficiency_ratio - penalty) * 100
    return int(round(final_normalized))

# Distractor: unused data structure definitions
class SensorNode:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.calibration_offset = 0.0

nodes = [SensorNode(i, t) for i, t in enumerate(['temp', 'humid', 'air', 'pressure'])]

# Simulated input data
raw_temperatures = [23, 25, 24, -120, 26, 28, 27, 999, 29, 30, -45, 22]
avg_temp, anomaly_count = analyze_temperature_readings(raw_temperatures)
humidity_readings = [45, 67, 82, 76, 54, 90, 88]
humidity_index = compute_humidity_index(humidity_readings)

# Unused pressure simulation - dead path
dummy_pressure_data = [1013, 1015, 1010, 1008, 1012]
pressure_trend = calculate_pressure_trend(dummy_pressure_data)

# Air quality assessment
pollutants = [45, 88, 156, 73]
air_quality_score = evaluate_air_quality(pollutants)

# Wind data - calculated but ultimately irrelevant to final result
wind_speeds = [8, 12, 16, 14, 18, 9]
wind_assessment = assess_wind_pattern(wind_speeds)

# Satellite coordinates - complete red herring
lats = [40.1, 40.3, 40.2, 40.5]
lons = [-74.3, -74.2, -74.5, -74.1]
coord_magnitude = transform_coordinates(lats, lons)

# Main metrics and weights for performance aggregation
sensor_metrics = [
    min(int(avg_temp), 10),           # Temperature stability score
    int(humidity_index % 10),          # Humidity impact score
    air_quality_score // 10,           # Normalized air quality
    anomaly_count                      # Penalty factor from anomalies
]

weights = [0.3, 0.2, 0.4, 0.1]

# Critical execution point
final_score = aggregate_performance(sensor_metrics, weights)

# Output result
print(f"Result: {final_score}")