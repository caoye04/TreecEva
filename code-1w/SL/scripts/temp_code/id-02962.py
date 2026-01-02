def calculate_performance(base, data):
    adjustment_factor = 1.5
    temp_offset = 0.8
    cumulative = 0
    peak_detected = False
    
    for i, reading in enumerate(data):
        normalized = (reading - base) * adjustment_factor
        
        if normalized > 10 and not peak_detected:
            peak_detected = True
            spike_correction = 2.1
        elif peak_detected:
            normalized -= temp_offset

        # Irrelevant computation - distractor
        shadow_value = (i + 1) * 0.05
        derived_metric = normalized ** 0.5 if normalized > 0 else 0
        
        cumulative += normalized if normalized < 15 else 14.9

    # Dead code path - rarely executed but looks important
    if len(data) > 100:
        cumulative *= 1.1

    stability_check = cumulative / len(data) if data else 0

    # Final decision using conditional expression
    final_adjustment = 1.2 if peak_detected else 0.9
    
    return int(cumulative * final_adjustment)

# Simulated sensor readings
baseline = 72.3
readings = [75.1, 78.3, 85.6, 79.2, 88.7, 73.0, 69.4, 82.5]

# Auxiliary variables - irrelevant to final result
diagnostic_log = []
max_reading = max(readings) if readings else 0
min_reading = min(readings) if readings else 0

# Key execution point
final_score = calculate_performance(baseline, readings)

print(f"Result: {final_score}")