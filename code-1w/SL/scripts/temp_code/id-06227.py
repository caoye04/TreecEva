def sensor_calibration(sequence):
    calibrated = []
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            calibrated.append(val * 1.1)
        elif i % 5 == 0:
            calibrated.append(val + 2.5)
        else:
            calibrated.append(val * 0.95)
    return [round(x, 2) for x in calibrated]


def generate_signature(data):
    sig = 0
    for i, x in enumerate(data):
        sig += (i + 1) * int(x)
    return sig % 1000  # Irrelevant checksum


def deprecated_filter(arr):
    # Dead code path - never used
    return [x for x in arr if x > 0]


def transform_coordinates(points):
    # Distractor function with misleading relevance
    transformed = []
    for x, y in zip(points[:-1], points[1:]):
        transformed.append((x * 2 + 1, y * 2 - 1))
    return transformed


def analyze_readings(data, config):
    result = 0
    status_flags = []
    
    for idx, reading in enumerate(data):
        threshold = config.get(f'chan_{idx % 4}', 100)
        adjusted = reading * (0.8 + (idx % 3) * 0.1)
        
        if adjusted > threshold:
            status_flags.append(1)
            result += int(adjusted // 10)
        elif adjusted < threshold * 0.5:
            status_flags.append(-1)
            result -= 5
        else:
            status_flags.append(0)
            
        # Red herring computation
        temp_offset = (idx * 7 + 43) % 19
        if temp_offset > 15:
            result += 1  # Misleading adjustment
    
    # Key logic: count how many flags are non-zero
    active_alerts = sum(1 for f in status_flags if f != 0)
    result += active_alerts * 3
    
    return result

# Main execution
if __name__ == '__main__':
    raw_input = [85, 92, 78, 96, 88, 73, 91, 84, 77, 89, 95]
    
    # Irrelevant coordinate data
    coords = [(1.2, 3.4), (2.3, 4.5), (3.4, 5.6)]
    geo_processed = transform_coordinates(coords)
    
    # Unused filter
    filtered_coords = deprecated_filter([1, -2, 3, -4, 5])
    
    # Calibration step (relevant)
    processed_data = sensor_calibration(raw_input)
    
    # Checksum (distractor)
    signature = generate_signature(processed_data)
    
    # Threshold configuration map (relevant)
    threshold_map = {
        'chan_0': 88,
        'chan_1': 85,
        'chan_2': 90,
        'chan_3': 95
    }
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")