def calculate_safety_margin(data):
    avg = sum(data) / len(data)
    deviation = [abs(x - avg) for x in data]
    max_dev = max(deviation)
    return avg - (max_dev * 0.5) if avg > 100 else avg + (max_dev * 0.3)

readings = [95, 108, 99, 112, 101]
baseline = 100
adjustment_factor = 0.5
outlier_count = len([x for x in readings if x < 90 or x > 110])
energy_threshold = calculate_safety_margin(readings)
Result: energy_threshold