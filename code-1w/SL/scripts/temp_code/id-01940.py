def calculate_performance(base, data):
    adjusted = list(map(lambda x: (x - base) ** 2, filter(lambda x: x > base * 0.8, data)))
    if len(adjusted) == 0:
        return base
    trend = sum(1 for i in range(1, len(adjusted)) if adjusted[i] > adjusted[i-1])
    smooth_factor = 0.9 if trend > len(adjusted) // 2 else 1.1
    return round(sum(adjusted) * smooth_factor / len(adjusted), 3)

baseline = 42.5
readings = [38.1, 45.3, 47.8, 40.2, 52.0, 55.6, 39.8]
system_status = "active"  # irrelevant status flag
timestamp_log = [1680001200, 1680001260, 1680001320]  # unused timestamp data

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")