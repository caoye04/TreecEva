def process_sensor_readings(readings):
    base_offset = 1.5
    filtered = [r for r in readings if r > 0]
    total = sum(filtered)
    count = len(filtered)
    average = total / count if count else 0
    
    normalized = [round((x - average) * base_offset, 2) for x in filtered]
    
    status_flags = []
    for i, val in enumerate(normalized):
        if val < -1.0:
            status_flags.append('LOW')
        elif val > 1.0:
            status_flags.append('HIGH')
        else:
            status_flags.append('OK')
    
    uppercase_count = sum(1 for s in status_flags if s.isupper())
    flag_summary = [s.lower() for s in status_flags]

    def calculate_threshold(data, flags):
        adjustment = 0.1 * len([f for f in flags if f == 'high'])
        return int(sum(data) + adjustment)

    threshold_score = calculate_threshold(normalized, flag_summary)
    
    extra_metadata = {'source': 'sensor_v2', 'calibrated': True}
    temp_result = [n * 2 for n in normalized if n > 0]
    
    return threshold_score

readings_input = [3, -1, 4, 1, 5, -2, 9, 2, 6]
result = process_sensor_readings(readings_input)
print(f"Result: {result}")