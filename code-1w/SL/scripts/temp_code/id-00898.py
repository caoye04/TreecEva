def calculate_threshold(data):
    total = sum(data)
    count = len(data)
    average = total / count
    
    # Determine baseline threshold using conditional expression
    threshold_score = average * 1.5 if average > 100 else average * 1.2
    
    return threshold_score

# Sensor readings in millivolts
readings = [85, 90, 110, 130, 95]

# Irrelevant variable (minimal distraction - intervention level 4)
dummy_offset = 5

threshold_score = calculate_threshold(readings)

Result: {threshold_score}