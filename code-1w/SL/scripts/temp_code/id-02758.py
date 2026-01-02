def main():
    # Sensor data simulation with noise filtering
    raw_readings = [105, 98, 112, 101, 95, 108, 115, 99]
    baseline = 100
    adjustment_factor = 0.9
    filtered_data = []
    temp_offset = 0

    for val in raw_readings:
        deviation = val - baseline
        if abs(deviation) > 15:
            corrected = baseline + deviation * adjustment_factor
        else:
            corrected = val
        filtered_data.append(int(corrected))
        temp_offset += deviation // 10  # Tracking minor thermal drift (distractor)

    # Data aggregation and outlier suppression
    aggregated = 0
    suppression_count = 0
    for i in range(len(filtered_data)):
        if i > 0 and abs(filtered_data[i] - filtered_data[i-1]) > 12:
            filtered_data[i] = (filtered_data[i] + filtered_data[i-1]) // 2
            suppression_count += 1
        aggregated += filtered_data[i]

    # Simulated calibration curve using lambda (relevant)
    threshold_func = lambda x: x > 102

    # Secondary metric tracking (mostly irrelevant)
    stability_log = []
    rolling_avg = 0
    for i in range(len(filtered_data)):
        rolling_avg = (rolling_avg * 2 + filtered_data[i]) // 3
        stability_log.append(abs(rolling_avg - filtered_data[i]))

    avg_stability = sum(stability_log) / len(stability_log) if stability_log else 0

    # Core processing function
    def process_metrics(log, threshold_fn):
        high_readings = list(filter(threshold_fn, log))
        low_readings = [x for x in log if not threshold_fn(x)]
        
        # Compute weighted contributions
        high_weight = len(high_readings) * 1.5 if high_readings else 0
        low_weight = len(low_readings) * 0.8 if low_readings else 0
        
        # Efficiency formula with bitwise influence (XOR of counts)
        count_xor = len(high_readings) ^ len(low_readings)
        efficiency_modifier = (count_xor % 4) * 0.1
        
        # Final efficiency score calculation
        efficiency_score = (high_weight - low_weight) + efficiency_modifier
        
        # Distractor variables below
        diagnostic_flag = False
        if len(high_readings) > len(low_readings):
            diagnostic_flag = True
        system_health = (len(log) ^ suppression_count) & 7  # Unused metric
        
        return efficiency_score  # Critical output

    # Execute core logic
    final_output = process_metrics(filtered_data, threshold_func)
    
    # Print result as required
    print(f"Result: {final_output}")

if __name__ == "__main__":
    main()