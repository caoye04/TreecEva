def calculate_threshold(data):
    filtered = [x for x in data if x > 50]
    averages = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    return max(averages) if averages else 0

# Sensor readings in microvolts
readings = [45, 60, 70, 55, 80, 30, 90, 85]
baseline = 50  # Ignore values below baseline
status_flag = True
energy_threshold = 0

if any(x > baseline for x in readings):
    energy_threshold = calculate_threshold(readings)

status_flag = False

print(f"Target result: {energy_threshold}")