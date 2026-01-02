from collections import defaultdict, Counter

# Simulated sensor data ingestion and diagnostic pipeline
def ingest_sensor_data():
    raw_streams = {
        'temp': [23.4, 24.1, 25.0, 22.8, 26.3, 27.1, 25.8, 24.7],
        'pressure': [1013, 1009, 1015, 1020, 1018, 1012, 1014, 1016],
        'vibration': [3, 5, 8, 42, 6, 7, 4, 9],  # anomaly at index 3
        'humidity': [45, 47, 50, 52, 48, 55, 53, 49]
    }
    return raw_streams

# Misleading auxiliary function (dead path)
def analyze_frequency_spectrum(data):
    total_power = 0
    for x in data:
        if x > 40:
            total_power += x ** 2
    spectral_index = total_power / (len(data) + 1)
    return spectral_index  # never used

# Irrelevant transformation chain
def transform_coordinates(x, y):
    lat = (x * 111.32) % 180
    lon = (y * 98.76) % 90
    dist = (lat**2 + lon**2) ** 0.5
    return round(dist, 3)

def generate_checksum(sequence):
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val * (i + 1)) % 256
    return chk

# Real processing begins here
def filter_outliers(streams):
    cleaned = defaultdict(list)
    anomalies_detected = 0
    for sensor, readings in streams.items():
        avg = sum(readings) / len(readings)
        for val in readings:
            if abs(val - avg) < 1.8 * avg:  # relaxed threshold
                cleaned[sensor].append(val)
            else:
                anomalies_detected += 1
    # Inject decoy statistic
    stability_score = (100 - anomalies_detected * 3.5) if anomalies_detected else 100
    return dict(cleaned)

# Another red herring: unused statistical model
def fit_linear_model(x_vals, y_vals):
    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(a*b for a,b in zip(x_vals, y_vals))
    sum_xx = sum(x**2 for x in x_vals)
    denominator = n * sum_xx - sum_x ** 2
    if denominator == 0:
        return 0.0, 0.0
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n
    return round(slope, 4), round(intercept, 4)

# Core logic disguised among noise
def compute_health_factor(metrics):
    base = 1.0
    adjustment = 0.0
    for metric, values in metrics.items():
        count = len(values)
        total = sum(values)
        if metric == 'temp':
            base *= (total / count) / 25.0
        elif metric == 'pressure':
            base *= 1.0
        elif metric == 'vibration':
            avg_vibe = total / count
            adjustment -= 0.15 if avg_vibe > 6 else 0.0
        elif metric == 'humidity':
            humidity_ratio = total / (count * 50)
            adjustment += 0.05 if 0.9 <= humidity_ratio <= 1.1 else -0.05
    return round(base + adjustment, 4)

# Critical function with embedded distractions
def process_readings(data, thresholds):
    # Unused threshold application (decoy)
    flagged = []
    for sensor, vals in data.items():
        limit = thresholds.get(sensor, float('inf'))
        for v in vals:
            if v > limit:
                flagged.append(v)
    # Real computation hidden below distractions
    stats = {}
    for k, v in data.items():
        c = Counter(v)
        mode_val = c.most_common(1)[0][0]
        stats[k] = {
            'mean': sum(v)/len(v),
            'mode': mode_val,
            'range': max(v) - min(v)
        }
    # Actual answer derivation
    primary = stats['temp']['mean']
    secondary = stats['pressure']['range']
    tertiary = len(data['vibration'])
    
    # Decoy calculation (looks important but unused)
    composite_risk = (primary * 0.6) + (secondary * 0.3) + (tertiary * 0.1)
    
    # The real result
    result = int((primary - 20) * 100) + secondary + (tertiary * 2)
    
    # Multiple assignments to obscure flow
    final_status, final_code, final_diagnostic = 'OK', 200, result
    
    # Dead code block with misleading prints
    if False:
        debug_val = transform_coordinates(primary, secondary)
        print(f'Debug coordinate: {debug_val}')
    
    return final_diagnostic

# Main execution with setup
if __name__ == '__main__':
    # Initialize threshold map (partially used)
    threshold_map = {
        'temp': 30.0,
        'pressure': 1030,
        'vibration': 40,      # catches anomaly
        'humidity': 80
    }
    
    # Generate fake spatial grid (irrelevant)
    coordinates = [(i, j) for i in range(3) for j in range(3)]
    checksums = []
    for x, y in coordinates:
        cs = generate_checksum([x*10 + y, y*10 + x])
        checksums.append(cs)
    
    # Real pipeline starts
    raw_data = ingest_sensor_data()
    filtered_data = filter_outliers(raw_data)
    
    # Call that produces the answer
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")