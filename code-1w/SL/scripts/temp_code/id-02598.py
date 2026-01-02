import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_readings = {
        'temp': [23.5, 24.1, 22.7, 25.3, 26.0],
        'humidity': [45, 48, 50, 44, 52],
        'co2': [420, 435, 460, 410, 480],
        'pm25': [12, 15, 11, 18, 20],
        'pressure': [1013, 1015, 1012, 1016, 1014]
    }
    return raw_readings

# Irrelevant calibration function (dead code path)
def calibrate_sensors(device_id):
    adjustments = {}
    for i in range(3):
        for j in range(3):
            adjustments[f'sensor_{i}{j}'] = (i * j + 2) % 7
    return adjustments

# Distractor: Unused data transformation
def transform_coordinates(latitudes, longitudes):
    transformed = []
    for lat in latitudes:
        for lon in longitudes:
            if lat > 0:
                x = lat * math.cos(lon)
                y = lat * math.sin(lon)
                transformed.append((x, y))
    return transformed

# Real processing begins here
def filter_outliers(data_list, tolerance=1.5):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data_list if abs(x - mean_val) <= tolerance * std_dev]
    return filtered

# Another red herring: GPS spoofing check (never called)
def validate_signal_integrity(timestamps):
    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    expected_interval = 1.0
    drift = sum(abs(interval - expected_interval) for interval in intervals)
    return drift < 0.5

# Real function: Normalize and aggregate readings
def process_environmental_data(raw_data):
    processed = {}
    for sensor_type, readings in raw_data.items():
        clean_readings = filter_outliers(readings)
        avg_reading = sum(clean_readings) / len(clean_readings)
        processed[sensor_type] = round(avg_reading, 2)
    
    # Inject irrelevant intermediate calculation
    temp = processed['temp']
    humidity = processed['humidity']
    heat_index = temp + 0.5 * humidity  # Not used later
    
    # Decoy dictionary entry
    processed['diagnostic_flag'] = int(heat_index) % 11
    
    return processed

# Misleading state tracker (used nowhere)
class SystemState:
    def __init__(self):
        self.status = 'OK'
        self.error_log = []
        self.uptime = 1274
    
    def update_status(self, new_status):
        self.status = new_status
        self.error_log.append(new_status)

# Core analysis logic
def analyze_readings(data, thresholds):
    risk_score = 0
    active_alerts = []
    
    # Spurious local computation
    baseline = sum(data.values()) / len(data)
    fluctuation = max(data.values()) - min(data.values())
    pseudo_entropy = -sum((v / baseline) * math.log(v / baseline) for v in data.values() if v > 0)
    
    # Actual decision logic
    for param, value in data.items():
        if param in thresholds:
            limit_low, limit_high = thresholds[param]
            if value < limit_low:
                deviation = (limit_low - value) / limit_low
                risk_score += int(deviation * 100)
                active_alerts.append(f'{param}_low')
            elif value > limit_high:
                deviation = (value - limit_high) / limit_high
                risk_score += int(deviation * 100)
                active_alerts.append(f'{param}_high')
    
    # Distractor: unused composite metric
    alert_severity = len(active_alerts) * risk_score
    if alert_severity > 100:
        fallback_code = hash(''.join(active_alerts)) % 1000
    else:
        fallback_code = 0
    
    # Final result derived from actual logic
    final_risk = (risk_score * 3) + len(active_alerts)
    return final_risk

# Entry point
if __name__ == '__main__':
    # Setup phase with multiple distractions
    device_state = {'active': True, 'mode': 'auto', 'battery': 87}
    calibration_data = calibrate_sensors('DEV-X7')  # Dead code call
    
    # Real workflow
    raw_data = collect_sensor_data()
    processed_data = process_environmental_data(raw_data)
    
    # Threshold map for environmental parameters
    threshold_map = {
        'temp': (22.0, 25.0),
        'humidity': (40, 50),
        'co2': (400, 450),
        'pm25': (10, 15),
        'pressure': (1000, 1020)
    }
    
    # Unused coordinate transformation
    lats = [34.05, 36.11, 38.56]
    lons = [-118.25, -120.12, -121.11]
    spatial_data = transform_coordinates(lats, lons)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output the target result
    print(f"Target result: {final_diagnostic}")