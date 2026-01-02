def process_temperature_readings():
    # Simulated sensor data: (timestamp, temp_celsius, humidity)
    raw_data = [
        (1623456000, 23.5, 45), (1623456060, 24.1, 47), (1623456120, 22.8, 50),
        (1623456180, 25.3, 44), (1623456240, 26.0, 46), (1623456300, 24.8, 49)
    ]

    # Extract hour from timestamp and convert to readable time (irrelevant for result)
    def get_hour(ts):
        return (ts // 3600) % 24

    hourly_labels = [get_hour(row[0]) for row in raw_data]

    # Normalize temperatures to Fahrenheit for a parallel logging system (distractor)
    fahrenheit_temps = [(t * 9/5) + 32 for t in [row[1] for row in raw_data]]

    # Filter readings where temperature exceeds 24°C and humidity is below 48%
    filtered_data = [entry for entry in raw_data if entry[1] > 24.0 and entry[2] < 48]

    # Extract and sum only the temperatures from filtered entries
    filtered_sum = sum(map(lambda x: x[1], filtered_data))

    # Additional unrelated transformation (distractor)
    humidity_dict = {i: raw_data[i][2] for i in range(len(raw_data))}
    avg_humidity = sum(humidity_dict.values()) / len(humidity_dict)

    # Output target result
    print(f"Result: {filtered_sum}")

process_temperature_readings()