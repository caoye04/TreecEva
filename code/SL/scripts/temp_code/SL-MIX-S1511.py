import math

def calculate_std(values):
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

temperature_sensors = [
    [23.5, 24.0, 23.8, 24.2, 30.1, 24.0],
    [22.0, 22.5, 25.0, 26.5, 27.0],
    [20.0, 20.5, 21.0, 20.8, 21.2, 21.5, 22.0]
]

processed_readings = []
total_processed = 0
threshold = 5.0
anomaly_detected = False

for sensor_id, readings in enumerate(temperature_sensors):
    if anomaly_detected:
        break
    prev_reading = None
    for reading in readings:
        if prev_reading is not None:
            diff = abs(reading - prev_reading)
            if diff > threshold:
                anomaly_detected = True
                break
        processed_readings.append(reading)
        total_processed += 1
        if len(processed_readings) >= 2:
            std_dev = calculate_std(processed_readings)
            threshold = 2 * std_dev if std_dev > 0 else threshold
        prev_reading = reading

print(f"Total readings processed before anomaly: {total_processed}")
