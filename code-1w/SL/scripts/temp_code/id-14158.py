def calculate_performance(base, data):
    adjusted_values = []
    offset = len(data) // 2
    threshold = base * 0.75

    for val in data:
        if isinstance(val, str) and val.isdigit():
            num = int(val)
        elif isinstance(val, (int, float)):
            num = val
        else:
            continue
        
        if num < threshold:
            continue
        
        adjusted = num - base
        adjusted_values.append(adjusted)
        
        if len(adjusted_values) >= 4:
            break
    
    if not adjusted_values:
        return 0
        
    result = sum(adjusted_values) / len(adjusted_values)
    return round(result, 3)

baseline = 85
readings = ["90", 87, "xyz", 88, 92, "86", 95]
system_status = "active"
version = "2.1.0"

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")