def main():
    # Simulate sensor data from a thermal regulation system
    raw_readings = [23.4, 19.5, 27.3, 18.2, 24.1, 20.0, 26.8, 22.7]
    
    # Irrelevant transformation: normalize to percentage (not used in final logic)
    normalized = [(x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100 for x in raw_readings]
    
    # Filter out readings below threshold and convert to integer for processing
    valid_readings = [int(x) for x in raw_readings if x > 20.0]
    
    # Apply correction factor based on calibration drift (real impact)
    corrected_readings = list(map(lambda x: x * 1.02 + 0.8, valid_readings))
    
    # Misleading aggregation: computes average but isn't used
    temp_avg = sum(corrected_readings) / len(corrected_readings)
    spike_count = len([x for x in corrected_readings if x > 25.0])
    
    # Simulate time-series window segmentation
    segments = []
    for i in range(0, len(corrected_readings), 2):
        segment = corrected_readings[i:i+2]
        if len(segment) == 2:
            segments.append((segment[0] + segment[1]) / 2)
    
    # Dead code path: never executed due to condition
    backup_mode = False
    if len(segments) > 10:
        segments = [x * 0.9 for x in segments]
        backup_mode = True
    
    # Process data through filtering and amplification
    processed_data = list(map(lambda x: x ** 2 - 2 * x, segments))
    
    # Key function call that determines answer
    efficiency_score = calculate_efficiency(processed_data)
    
    # Red herring variable: looks important but unused
    diagnostic_flag = efficiency_score < 40 and spike_count > 1
    
    # Final output
    print(f"Result: {efficiency_score}")


def calculate_efficiency(data):
    # Efficiency formula: sum of square roots divided by number of elements
    import math
    if not data:
        return 0
    sqrt_sum = sum(math.sqrt(abs(x)) for x in data)
    return sqrt_sum / len(data)

main()