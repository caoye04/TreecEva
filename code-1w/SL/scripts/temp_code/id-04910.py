def main():
    # Simulate sensor readings from a chemical plant
    raw_readings = [23.5, 18.9, 25.1, 20.3, 27.8, 19.4, 22.7]
    calibration_offsets = [0.5, -0.3, 0.8, -0.6, 1.1, -0.2, 0.4]

    # Apply calibration using lambda and zip
    calibrated_readings = list(map(lambda x: x[0] + x[1], zip(raw_readings, calibration_offsets)))

    # Misleading transformation - not used in final result
    transformed_readings = [r ** 0.5 * 1.05 for r in raw_readings]
    avg_transformed = sum(transformed_readings) / len(transformed_readings)

    # Filter valid readings above threshold
    threshold = 20.0
    filtered_readings = [val for val in calibrated_readings if val >= threshold]

    # Compute rolling average (distraction)
    window_size = 2
    rolling_averages = [sum(calibrated_readings[i:i+window_size]) / window_size 
                         for i in range(len(calibrated_readings) - window_size + 1)]

    # Normalize data (semi-relevant, but only sum matters later)
    normalized = [round((x - min(filtered_readings)) / 
                        (max(filtered_readings) - min(filtered_readings)) * 100) 
                  for x in filtered_readings]

    # Prepare data packets with metadata
    timestamps = list(range(len(filtered_readings)))
    data_packets = []
    for idx, (val, ts) in enumerate(zip(filtered_readings, timestamps)):
        packet = {
            'id': idx,
            'value': val,
            'normalized': normalized[idx],
            'timestamp': ts,
            'status': 'OK' if val > 22 else 'LOW'
        }
        data_packets.append(packet)
    
    # Extract only values marked as 'OK' status
    processed_data = [p['value'] for p in data_packets if p['status'] == 'OK']

    # Critical function call
    net_flow = calculate_net_flow(processed_data)
    
    # Print result for evaluation
    print(f"Result: {net_flow}")


def calculate_net_flow(data):
    if not data:
        return 0
    base = sum(data)
    adjustment = len(data) * 0.5
    # Simulate minor loss due to evaporation
    adjusted_flow = base - adjustment
    return int(adjusted_flow)

if __name__ == '__main__':
    main()