import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [18, 22, 14, 30, 25, 10, 8, 12]
    offset = 5
    adjusted = [x + offset for x in raw_readings]
    filtered = [x for x in adjusted if x > 15]  # Only significant readings
    return filtered

# Irrelevant auxiliary function – distractor
def compute_checksum(data):
    checksum = 0
    for x in data:
        checksum ^= x * 3
    return checksum % 1000

# Data transformation pipeline
def transform_signal(signal_data):
    amplified = [x * 2 for x in signal_data]
    inverted = [~x & 0xFF for x in amplified]  # Bitwise invert and mask
    return inverted

# Another red herring: environmental compensation (not used in final result)
def apply_env_compensation(data, temp_factor=1.05, pressure_adj=0.97):
    compensated = [int(x * temp_factor * pressure_adj) for x in data]
    norm_factor = sum(compensated) / len(compensated)
    return [x / norm_factor for x in compensated]

# Core pattern analyzer – actually used
def analyze_pattern(seq, settings):
    window_size = settings['window']
    threshold = settings['thresh']
    total_anomalies = 0
    
    # Generate sliding windows using itertools
    it = iter(seq)
    windows = list(itertools.zip_longest(*(itertools.islice(it, window_size),) * window_size))
    
    for win in windows:
        valid_points = [x for x in win if x is not None]
        if not valid_points:
            continue
        avg = sum(valid_points) / len(valid_points)
        for pt in valid_points:
            if abs(pt - avg) > threshold:
                total_anomalies += 1
    
    # Secondary logic branch – dead path (never reached due to prior logic)
    if len(seq) > 100:
        scaling = settings.get('scale', 1)
        total_anomalies *= scaling
    
    return int(total_anomalies * settings['weight'])

# Unused recursive counter – pure distraction
def count_segments(data, acc=0):
    if not data:
        return acc
    return count_segments(data[1:], acc + (data[0] % 4 == 0))

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect and adjust sensor data
    readings = collect_sensor_readings()  # Result: [23, 27, 35, 30, 15, 13, 17]
    
    # Step 2: Transform signal using bitwise logic
    transformed_data = transform_signal(readings)
    
    # Step 3: Compute irrelevant checksum
    chk = compute_checksum(transformed_data)
    
    # Step 4: Apply fake compensation (result unused)
    dummy_normalized = apply_env_compensation(transformed_data, 1.08, 0.94)
    
    # Step 5: Set configuration for analysis
    config = {
        'window': 3,
        'thresh': 50,
        'weight': 7
    }
    
    # Step 6: Analyze pattern in transformed data
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Distraction: recursive segment counting on wrong data
    _ = count_segments(readings)
    
    # Final output
    print(f"Result: {final_diagnostic}")