def main():
    # Simulate sensor data processing with performance scoring
    raw_readings = [145, 203, 98, 176, 255]
    baseline = 100
    adjustment_factor = 1.2

    # Irrelevant transformation (distractor)
    adjusted_readings = [round((x - baseline) * adjustment_factor) for x in raw_readings]
    outlier_threshold = 150
    filtered_data = [x for x in adjusted_readings if x < outlier_threshold]

    # Normalization logic (semi-relevant)
    max_val = max(raw_readings)
    normalized_data = [(x / max_val) for x in raw_readings]

    # Weighting scheme using dictionary and lambda (core concept)
    metric_config = {
        'precision': 0.4,
        'stability': 0.3,
        'sensitivity': 0.2,
        'response_time': 0.1
    }
    
    # Lambda used for dynamic scaling (required python feature)
    scaler = lambda x, w: x ** w
    scaled_metrics = {k: scaler(normalized_data[i % len(normalized_data)], v) 
                      for i, (k, v) in enumerate(metric_config.items())}

    # Secondary distractor: unused computation on strings (string method)
    status_messages = [f'Reading_{i}_OK' for i in range(len(raw_readings))]
    padded_msgs = [msg.ljust(20, '.') for msg in status_messages]
    checksum = sum([len(msg.replace('.', '')) for msg in padded_msgs])  # Not used later

    # Weight vector extraction (required dict operation)
    metric_weights = list(scaled_metrics.values())

    # Core evaluation function
    def evaluate_performance(weights, data):
        cumulative = 0.0
        temp_buffer = []
        for i, val in enumerate(data):
            # Nested logic with interdependent steps
            if i % 2 == 0:
                intermediate = val * weights[i % len(weights)]
                temp_buffer.append(intermediate)
                cumulative += intermediate * 0.9
            else:
                backup_calc = val ** weights[i % len(weights)]
                temp_buffer.append(backup_calc)
                cumulative += backup_calc * 0.85

        # Additional distraction: bitwise op with no impact
        flag = len(temp_buffer) & 1
        debug_flag = flag << 2  # Dead code path

        # Final aggregation
        final_component = sum(temp_buffer) * 0.95
        return int(cumulative + final_component)

    final_score = evaluate_performance(metric_weights, normalized_data)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()