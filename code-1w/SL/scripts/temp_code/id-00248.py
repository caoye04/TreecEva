def system_check(diagnostic_fn):
    sensor_readings = [3.2, 4.1, 5.7, 6.3, 4.9]
    baseline = sum(sensor_readings) / len(sensor_readings)
    energy_baseline = round(baseline, 1)
    status_codes = {1: 'OK', 0: 'FAILED'}
    # Irrelevant status mapping (minor distraction)
    current_status = status_codes.get(1, 'UNKNOWN')
    diagnostic_results = list(map(diagnostic_fn, sensor_readings))
    true_count = sum(diagnostic_results)
    energy_threshold = true_count * 10
    final_diagnostic = system_check(lambda x: x > energy_baseline * 1.5)
    return energy_threshold

result = system_check(lambda x: x > 4.5)
print(f"Result: {result}")