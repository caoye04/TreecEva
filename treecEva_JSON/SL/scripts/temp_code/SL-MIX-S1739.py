from functools import reduce

def mod_transform(x, mod_base=257):
    return (x * 17 + 23) % mod_base

def combine_segments(segment_values):
    dp = [0] * (len(segment_values) + 1)
    dp[0] = 1
    for i in range(1, len(segment_values) + 1):
        dp[i] = (dp[i-1] * segment_values[i-1] + i) % 257
    return dp[len(segment_values)]

def process_sensor_data(readings):
    segment_size = 4
    segments = [readings[i:i+segment_size] for i in range(0, len(readings), segment_size)]
    transformed_segments = []
    for segment in segments:
        segment_sum = sum(segment)
        transformed_value = mod_transform(segment_sum)
        transformed_segments.append(transformed_value)
    return combine_segments(transformed_segments)

sensor_readings = [12, 45, 67, 89, 23, 56, 78, 90, 11, 34, 57, 79]
sync_checksum = process_sensor_data(sensor_readings)
print(f"Result: {sync_checksum}")