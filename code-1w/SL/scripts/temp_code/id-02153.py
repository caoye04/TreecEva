import math

# Simulated sensor fusion system for environmental monitoring
sensor_stream = [
    (1, 18.7, 45.2, 1013.25), (2, 19.1, 44.8, 1012.90),
    (3, 18.9, 46.1, 1013.10), (4, 19.6, 45.5, 1013.40),
    (5, 18.4, 47.0, 1012.80), (6, 18.2, 48.3, 1012.50),
    (7, 19.8, 44.0, 1013.60), (8, 20.1, 43.7, 1013.80)
]

# Irrelevant calibration data (distractor)
calibration_matrix = [[0.98, 1.02], [1.01, 0.99]]
offset_map = {'temp': 0.3, 'humidity': -1.2}
reference_epoch = 1672531200

# Data filters (some are decoys)
def filter_outliers(data):
    return [d for d in data if 18.0 <= d[1] <= 20.0]

def normalize_timestamps(data):
    return [(ref + idx, *vals[1:]) for idx, (ref, *vals) in enumerate(data)]

def filter_data(stream):
    # Only this function is actually used
    filtered = [s for s in stream if s[3] > 1013.0]
    return filtered

# Unused transformation chains (dead code paths)
transform_pipeline = lambda x: x ** 2
post_processor = lambda readings: [r[:3] for r in readings if r[2] < 46]

# Core processing with distractors
def analyze_trend(readings):
    temps = [r[1] for r in readings]
    diffs = [temps[i+1] - temps[i] for i in range(len(temps)-1)]
    return sum(diffs) / len(diffs) if diffs else 0.0

def compute_stability_index(readings):
    humidities = [r[2] for r in readings]
    mean_hum = sum(humidities) / len(humidities)
    variance = sum((h - mean_hum) ** 2 for h in humidities) / len(humidities)
    return math.sqrt(variance)

def process_readings(filtered_readings):
    # Real computation path
    trend = analyze_trend(filtered_readings)
    stability = compute_stability_index(filtered_readings)
    
    # Decoy calculations (misleading intermediate values)
    dummy_score = sum(r[1] * r[2] for r in filtered_readings) / 100
    penalty_factor = len([r for r in filtered_readings if r[1] > 19.5])
    adjustment = (penalty_factor * 0.1) if penalty_factor > 2 else 0
    
    # Actual answer formation
    raw_diagnostic = (trend * 1000) + (stability * 100)
    final_diagnostic = int(raw_diagnostic - adjustment * 50)
    
    # More red herrings
    audit_log = {'processed_count': len(filtered_readings), 'adjusted': bool(adjustment)}
    temp_bandwidth = max(r[1] for r in filtered_readings) - min(r[1] for r in filtered_readings)
    
    return final_diagnostic

# Unused functional composition (distractor)
data_flow = lambda x: process_readings(filter_data(x))

# Critical execution point
final_diagnostic = process_readings(filter_data(sensor_stream))

# Print result as required
print(f"Result: {final_diagnostic}")