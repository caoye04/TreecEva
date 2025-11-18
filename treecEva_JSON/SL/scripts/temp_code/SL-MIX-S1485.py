import math
from functools import reduce
from itertools import combinations

def encode_reading(value, mean_val, std_dev):
    normalized = (value - mean_val) / std_dev if std_dev != 0 else 0
    scaled = int(normalized * 1000)
    return scaled & 0xFFFF

def decode_reading(encoded_val):
    return (encoded_val >> 8) ^ (encoded_val & 0xFF)

sensor_readings = [23.5, 45.2, 12.8, 67.9, 34.1, 56.3, 78.0, 29.4]
mean_reading = sum(sensor_readings) / len(sensor_readings)
variance = sum((x - mean_reading) ** 2 for x in sensor_readings) / len(sensor_readings)
std_deviation = math.sqrt(variance)

encoded_values = [encode_reading(reading, mean_reading, std_deviation) for reading in sensor_readings]
bitwise_combinations = [a ^ b for a, b in combinations(encoded_values, 2)]
aggregated_code = reduce(lambda x, y: x | y, bitwise_combinations, 0)
decoded_signal_strength = decode_reading(aggregated_code)

print(f"Result: {decoded_signal_strength}")