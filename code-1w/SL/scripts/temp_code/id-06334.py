def process_turbine_data(rpm_readings, temp_offsets):
    baseline = 127
    adjustment_factor = 0.89
    cumulative_drift = 0
    efficiency_log = []
    
    for i, (rpm, temp) in enumerate(zip(rpm_readings, temp_offsets)):
        if i % 2 == 0:
            adjusted_rpm = rpm * adjustment_factor
        else:
            adjusted_rpm = rpm + temp
        
        power_estimate = (adjusted_rpm // 10) * (baseline - temp)
        efficiency_score = power_estimate / (baseline + i)
        
        if efficiency_score > 100:
            efficiency_score = 100
        
        efficiency_log.append(round(efficiency_score, 2))

    # Irrelevant data transformation
    temp_set = set(temp_offsets)
    rpm_set = set(rpm_readings)
    drift_values = [abs(a - b) for a, b in zip(rpm_readings, rpm_readings[1:])]
    avg_drift = sum(drift_values) / len(drift_values) if drift_values else 0

    # Distractor: unused function
    def analyze_vibration(data):
        return sum(x ** 0.5 for x in data if x > 50)
    
    # Distractor variables
    calibration_offset = sum(temp_offsets) * 0.01
    stability_index = len(efficiency_log) - avg_drift

    def calculate_thermal_rating(log):
        base_rating = 0
        for idx, score in enumerate(log):
            if idx == 0:
                base_rating += score * 1.1
            elif idx % 3 == 0:
                base_rating += score * 0.7
            else:
                base_rating += score * 0.9
        return int(base_rating // 1.5)

    thermal_capacity = calculate_thermal_rating(efficiency_log)
    return thermal_capacity

# Input data
readings = [850, 910, 870, 930, 890]
temps = [25, 28, 26, 29, 27]

result = process_turbine_data(readings, temps)
print(f"Result: {result}")