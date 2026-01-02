from collections import defaultdict, Counter

# Simulated sensor fusion module for environmental monitoring
def collect_sensor_data():
    raw_streams = {
        'temp': [23.5, 24.1, 22.9, 25.0, 26.3, 24.8, 23.7, 22.5],
        'humidity': [45, 47, 50, 55, 60, 62, 65, 70],
        'co2': [400, 410, 425, 440, 460, 480, 500, 520],
        'pressure': [1013, 1012, 1014, 1015, 1013, 1010, 1008, 1007]
    }
    timestamps = [1623456000 + i*300 for i in range(8)]
    return raw_streams, timestamps

# Irrelevant calibration function (dead code path)
def calibrate_sensors(data):
    adjustment_factors = {'temp': 1.02, 'humidity': 0.98, 'co2': 1.01}
    calibrated = {}
    for sensor, readings in data.items():
        if sensor in adjustment_factors:
            calibrated[sensor] = [r * adjustment_factors[sensor] for r in readings]
        else:
            calibrated[sensor] = readings[:]
    return calibrated

# Distractor: unused noise reduction filter
def apply_kalman_filter(readings):
    if len(readings) < 2:
        return readings
    filtered = [readings[0]]
    for i in range(1, len(readings)):
        pred = filtered[-1]
        residual = readings[i] - pred
        kalman_gain = 0.3
        corrected = pred + kalman_gain * residual
        filtered.append(corrected)
    return filtered

# Real processing pipeline
def detect_anomalies(stream):
    mean_val = sum(stream) / len(stream)
    variance = sum((x - mean_val) ** 2 for x in stream) / len(stream)
    std_dev = variance ** 0.5
    outliers = [i for i, x in enumerate(stream) if abs(x - mean_val) > 2 * std_dev]
    return outliers, mean_val

def slice_stable_period(data, anomalies):
    # Find longest consecutive segment without anomalies
    if not anomalies:
        return data
    breaks = sorted(anomalies)
    segments = []
    start = 0
    for pos in breaks:
        if pos > start:
            segments.append(data[start:pos])
        start = pos + 1
    segments.append(data[start:])
    return max(segments, key=len) if segments else data[:1]

def compute_entropy(readings):
    count = Counter(readings)
    total = len(readings)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 4)

# Main analysis workflow
def process_readings(data, thresholds):
    diagnostics = defaultdict(float)
    
    # Process each sensor stream
    for sensor, readings in data.items():
        # Compute basic stats
        avg = sum(readings) / len(readings)
        peak = max(readings)
        base = min(readings)
        
        # Apply dynamic threshold logic
        if sensor in thresholds:
            crit_low, crit_high = thresholds[sensor]
            severity = 0
            
            for val in readings:
                if val < crit_low:
                    severity += (crit_low - val) * 0.1
                elif val > crit_high:
                    severity += (val - crit_high) * 0.1
            
            diagnostics[f'{sensor}_risk'] = round(severity, 3)
        
        # Hidden signal extraction via slicing pattern
        window_size = 4
        if len(readings) >= window_size:
            # Extract mid-segment (distractor: not used in final result)
            mid_start = len(readings) // 2 - 2
            mid_window = readings[mid_start:mid_start + window_size]
            
            # Actual key computation: alternating pattern detection
            alt_score = 0
            for i in range(1, len(readings)):
                if (readings[i] - readings[i-1]) * ((-1)**i) > 0:
                    alt_score += 1
            diagnostics[f'{sensor}_stability'] = alt_score
        
        # Bit manipulation red herring
        bit_encoded = 0
        for val in readings[:3]:
            shifted = int(abs(val) * 10) & 0xFF
            bit_encoded ^= shifted
            bit_encoded = (bit_encoded << 1) | (bit_encoded >> 7)
        diagnostics[f'{sensor}_hash'] = bit_encoded % 1000
    
    # Critical calculation: weighted diagnostic index
    weights = {'temp_risk': 0.3, 'humidity_risk': 0.25, 'co2_risk': 0.35, 'pressure_risk': 0.1}
    final_index = 0
    for metric, weight in weights.items():
        if metric in diagnostics:
            final_index += diagnostics[metric] * weight
    
    # Normalize to clinical scale (0-100)
    final_index = min(final_index * 10, 100)
    
    # Inject decoy intermediate
    phantom_score = sum(diagnostics.values()) * 0.01
    
    # Final output (only this matters)
    return round(final_index, 4)

# Configuration map with misleading entries
def generate_threshold_map():
    config = defaultdict(lambda: (0, float('inf')))
    config.update({
        'temp': (22.0, 25.5),
        'humidity': (30, 65),
        'co2': (350, 500),
        'pressure': (1000, 1020)
    })
    # Add irrelevant safety modes
    config['safety_mode_A'] = (1, 1)
    config['safety_mode_B'] = (2, 2)
    return config

# Entry point with controlled execution flow
def main():
    # Collect data
    raw_data, times = collect_sensor_data()
    
    # Simulate preprocessing steps
    anomaly_report = {}
    cleaned_data = {}
    for sensor, readings in raw_data.items():
        anomalies, mean_val = detect_anomalies(readings)
        anomaly_report[sensor] = len(anomalies)
        stable_segment = slice_stable_period(readings, anomalies)
        cleaned_data[sensor] = stable_segment
    
    # Distractor: entropy analysis (not used)
    entropies = {s: compute_entropy(r) for s, r in raw_data.items()}
    
    # Filter data to relevant period (key step)
    filtered_data = {}
    for sensor, readings in cleaned_data.items():
        if len(readings) > 4:
            # Use first half as per protocol
            filtered_data[sensor] = readings[:len(readings)//2]
        else:
            filtered_data[sensor] = readings
    
    # Generate threshold configuration
    threshold_map = generate_threshold_map()
    
    # Execute critical statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()