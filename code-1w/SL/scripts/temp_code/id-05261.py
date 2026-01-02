import math

# Simulated sensor fusion and diagnostic system with red herrings
def analyze_signal_strength(signal):
    # Irrelevant function - not used in main logic
    return sum([math.sin(x) * 0.5 for x in signal])

def deprecated_calibration(seq):
    # Dead code path - never called
    return [x * 1.05 for x in seq if x > 0]

def transform_coordinates(x, y, z):
    # Distractor function - looks important but unused
    radius = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / radius)
    return radius, theta, phi

def compute_entropy(data):
    # Misleading intermediate calculation
    total = sum(data)
    probs = [d / total for d in data if d > 0]
    return -sum(p * math.log(p) for p in probs)

def integrate_series(ser):
    # Unused integration logic (red herring)
    acc = 0
    integrated = []
    for val in ser:
        acc += val
        integrated.append(acc)
    return integrated

def detect_anomalies(stream):
    # Looks critical but only returns dummy metadata
    anomalies = []
    for i, val in enumerate(stream):
        if val < 0.1 * sum(stream) / len(stream):
            anomalies.append(i)
    return {'count': len(anomalies), 'indices': anomalies, 'flag': False}

def filter_noise(data, threshold=0.01):
    # Sounds relevant but not actually used
    return [x for x in data if abs(x) > threshold]

def main():
    # Real input data
    sensor_data = [3.2, 1.8, 4.5, 2.7, 3.6, 5.1, 2.9]
    
    # Decoy datasets (only one is real)
    dummy_set_a = [0.1, 0.3, 0.2, 0.4]
    dummy_set_b = [99, 88, 77]  # Distraction
    backup_data = sensor_data.copy()  # Looks like fallback, never used
    
    # Calibration parameters - most are distractions
    base_offset = 1.02
    gain_factor = 0.987
    temperature_drift = -0.003  # Unused
    pressure_comp = 0.0015      # Unused
    
    # Multiple matrix attempts - only one matters
    identity_matrix = [[1,0,0],[0,1,0],[0,0,1]]
    scaling_matrix = [[2,0],[0,2]]
    calibration_matrix = [
        [0.97, 0.02, 0.01],
        [0.03, 0.95, 0.02],
        [0.00, 0.03, 0.99]
    ]
    
    # Fake processing chains
    processed_chain_1 = [x * base_offset for x in sensor_data]
    smoothed_data = [processed_chain_1[i] + processed_chain_1[i-1] * 0.1 
                     for i in range(len(processed_chain_1))]
    normalized = [x / max(smoothed_data) for x in smoothed_data]  # Looks final, isn't
    
    # Real computation begins here (buried among noise)
    weighted_sum = 0.0
    for i, reading in enumerate(sensor_data):
        correction = 0.0
        for j in range(min(3, len(calibration_matrix))):
            if i < len(calibration_matrix[j]):
                correction += calibration_matrix[j][i] if i < len(calibration_matrix[j]) else 0
        adjusted = reading * (gain_factor + correction)
        weighted_sum += adjusted * (i + 1)  # Weight by position
    
    # Secondary validation using zip and enumerate (required python features)
    validation_pairs = list(zip(sensor_data, [1.1, 0.9, 1.2, 0.8, 1.0, 1.3, 0.7]))
    adjustment_score = 0
    for idx, (val, weight) in enumerate(validation_pairs):
        if idx % 2 == 0:
            adjustment_score += val * weight * 0.1
        else:
            adjustment_score -= val * weight * 0.05
    
    # Final diagnostic calculation
    raw_diagnostic = weighted_sum + adjustment_score
    stability_factor = math.cos(len(sensor_data) * 0.1)
    final_diagnostic = int(raw_diagnostic * stability_factor * 100) / 100.0
    
    # Red herring: complex-looking but unused structure
    diagnostic_report = {
        'entropy': compute_entropy(sensor_data),
        'anomaly_meta': detect_anomalies(sensor_data),
        'transformed_coords': transform_coordinates(1, 2, 3),
        'signal_quality': analyze_signal_strength(sensor_data),
        'integration_trace': integrate_series(sensor_data),
        'filtered': filter_noise(sensor_data),
        'timestamp': '2023-11-05',
        'version': '2.1.0'
    }
    
    # Only this line matters for answer
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()