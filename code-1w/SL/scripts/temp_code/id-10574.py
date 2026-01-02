from itertools import accumulate

# Sensor readings from two synchronized environmental monitoring stations
temperature_readings = [20, 22, 19, 24, 21]
humidity_readings = [45, 50, 60, 55, 40]

# Auxiliary data (not used in final computation - minimal interference)
pressure_readings = [1013, 1011, 1009, 1015, 1020]
dummy_flag = True

# Compute weighted harmony index between temperature and humidity trends
cumulative_temp = list(accumulate(temperature_readings))
weighted_sum = 0

for i, (temp, hum) in enumerate(zip(cumulative_temp, humidity_readings)):
    weight = i + 1  # Increasing weight for later observations
    weighted_sum += (temp / 10) * (hum / 5) * weight

# Final aggregation step
total_harmony = int(weighted_sum // len(temperature_readings))

Result: total_harmony