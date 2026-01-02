from collections import defaultdict

# Simulate sensor readings over time
def process_readings(data, filter_outliers=True):
    counts = defaultdict(int)
    for value in data:
        if filter_outliers and abs(value - 50) > 20:
            continue
        counts[value // 10] += 1

    mode = max(counts, key=counts.get) * 10

    def calculate_threshold(readings, m):
        base = sum(r for r in readings if r >= m) / len(readings)
        adjustment = 0.1 * (m - 40) if m > 45 else 0
        return base + adjustment

    energy_threshold = calculate_threshold(data, mode)
    
    # Irrelevant auxiliary variable (minimal distraction)
    status_flag = "NORMAL" if energy_threshold < 60 else "HIGH"
    
    return energy_threshold

sensor_data = [45, 52, 30, 60, 55, 25, 48, 58, 70, 49, 51]
result = process_readings(sensor_data)
print(f"Target result: {result}")