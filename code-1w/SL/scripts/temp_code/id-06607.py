import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [56, 61, 59, 66, 70, 52, 48, 74]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1016, 1020, 1005]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B3', 'C9', 'D1', 'E8', 'F2', 'G5', 'H6']
lookup_matrix = [[i * j for j in range(1, 9)] for i in range(1, 9)]

# Configuration map with red herring entries
default_config = {
    'threshold': 25.0,
    'weighting': {'temp': 0.5, 'humidity': 0.3, 'pressure': 0.2},
    'active_filters': ['outlier', 'spike', 'drift'],
    'log_level': 'DEBUG',
    'max_history': 100,
    'deprecated_mode': True,
    'placeholder_value': None
}

# Misleading transformation chain (partially unused)
def legacy_transform(x):
    return (x ** 1.05) - 2  # Unused function - distractor
def deprecated_normalize(val_list):
    min_val, max_val = min(val_list), max(val_list)
    return [(v - min_val) / (max_val - min_val + 1e-8) for v in val_list]  # Not used

# Core preprocessing
transformed_data = []
for i in range(len(temperature_readings)):
    entry = {
        'idx': i,
        'temp_c': temperature_readings[i],
        'humidity_pct': humidity_readings[i],
        'pressure_hpa': pressure_readings[i],
        'heat_index': temperature_readings[i] + 0.5 * humidity_readings[i] / 100.0,
        'dew_point': temperature_readings[i] - ((100 - humidity_readings[i]) / 5.0)
    }
    transformed_data.append(entry)

# Distractor: complex but unused list comprehension
correlation_pairs = [
    (temperature_readings[i], humidity_readings[j]) 
    for i in range(len(temperature_readings)) 
    for j in range(i+1, len(humidity_readings))
    if abs(i - j) % 2 == 0
]

# Real processing functions
def detect_anomalies(data_chunk, threshold):
    anomalies = []
    for record in data_chunk:
        if record['temp_c'] > threshold:
            anomalies.append(record['idx'])
    return anomalies

def compute_stability_score(anomaly_list, total_count):
    if not anomaly_list:
        return 100.0
    penalty = sum([abs(anomaly_list[i] - anomaly_list[i-1]) for i in range(1, len(anomaly_list))])
    return round(100 - (len(anomaly_list) * 5) - (penalty * 0.5), 2)

def apply_weighted_average(data_chunk, weights):
    temp_avg = sum(d['temp_c'] for d in data_chunk) / len(data_chunk)
    hum_avg = sum(d['humidity_pct'] for d in data_chunk) / len(data_chunk)
    pres_avg = sum(d['pressure_hpa'] for d in data_chunk) / len(data_chunk)
    return (
        temp_avg * weights['temp'] + 
        hum_avg * weights['humidity'] + 
        pres_avg * weights['pressure']
    )

def process_metrics(dataset, config):
    # Extract configuration
    thresh = config['threshold']
    weights = config['weighting']
    
    # Step 1: Detect high-temp anomalies
    anomalous_indices = detect_anomalies(dataset, thresh)
    
    # Step 2: Compute system stability score
    stability = compute_stability_score(anomalous_indices, len(dataset))
    
    # Step 3: Calculate composite environmental index
    composite_index = apply_weighted_average(dataset, weights)
    
    # Step 4: Apply correction based on stability
    adjusted_index = composite_index * (stability / 100.0)
    
    # Step 5: Final diagnostic calculation
    base_diagnostic = int(round(adjusted_index * 100))
    
    # Apply bit manipulation for final obfuscation (real use)
    # Flip every other bit in lower 16 bits as checksum proxy
    masked = base_diagnostic & 0xFFFF
    flipped = 0
    for bit_pos in range(16):
        if masked & (1 << bit_pos):
            if bit_pos % 2 == 0:
                flipped |= (1 << bit_pos)
        else:
            if bit_pos % 2 == 1:
                flipped |= (1 << bit_pos)
    
    final_diagnostic = base_diagnostic ^ flipped  # Actual result
    
    # Dead code path - misleading
    if config.get('deprecated_mode'):
        fallback = 0
        for c in config.get('placeholder_value', 'X'):
            fallback += ord(c)
        final_diagnostic += fallback  # Never reached
    
    return final_diagnostic

# Main execution flow
config = default_config.copy()
config['threshold'] = 25.0  # Reaffirm threshold

# Execute key statement
final_diagnostic = process_metrics(transformed_data, config)

# Print result
print(f"Result: {final_diagnostic}")