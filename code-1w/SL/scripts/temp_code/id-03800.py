def analyze_readings(sensor_log):
    clean_log = [entry.strip() for entry in sensor_log if entry.strip()]
    numeric_values = []
    for item in clean_log:
        if item.isdigit():
            numeric_values.append(int(item))
        elif item.startswith('-') and item[1:].isdigit():
            numeric_values.append(int(item))
    
    adjusted_values = [val * 2 + 1 for val in numeric_values]
    offset = 5
    threshold = max(adjusted_values) // 3
    processed_data = [val - offset for val in adjusted_values]
    filtered_sum = sum([x for x in processed_data if x > threshold])
    return filtered_sum

log_entries = ['10', ' -5 ', 'abc', '', '7', '  12  ', '3']
result = analyze_readings(log_entries)
print(f"Result: {result}")