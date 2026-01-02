from itertools import compress

def process_sensor_data(readings):
    base = 1
    for val in readings:
        base ^= val  # XOR all values into base
    return base + len(readings)

# Simulated IoT sensor readings
raw_data = [12, 7, 3, 8, 15, 4, 9]
temperature_flags = [x > 6 for x in raw_data]

# Filter only high-intensity readings
filtered_reads = list(compress(raw_data, temperature_flags))

# Key computation step
result = process_sensor_data(filtered_reads)

print(f"Result: {result}")