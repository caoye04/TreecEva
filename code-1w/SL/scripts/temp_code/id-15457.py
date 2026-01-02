def monitor_system(readings):
    baseline = sum(readings) / len(readings)
    deviation = lambda x: abs(x - baseline)
    significant = [d for d in readings if deviation(d) > baseline * 0.1]
    energy_threshold = len(significant) if any(significant) else (2 * len(readings)) // 3
    return energy_threshold

energy_readings = (120, 124, 118, 135, 121, 119, 150)
final_diagnostic = monitor_system(energy_readings)
print(f"Result: {final_diagnostic}")