def calculate_efficiency(speeds, tol):
    filtered = [s for s in speeds if abs(s - 70) <= tol]
    avg = sum(filtered) / len(filtered) if filtered else 0
    return round(avg * 0.85, 2)

speed_readings = [65, 70, 72, 68, 80, 75, 69]
tolerance = 5
baseline = 60
energy_threshold = 0

def update_system():
    global energy_threshold
    energy_threshold = calculate_efficiency(speed_readings, tolerance)

# Simulate system calibration
update_system()
print(f"Target result: {energy_threshold}")