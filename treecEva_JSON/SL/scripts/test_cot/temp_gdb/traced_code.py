import statistics

def celsius_converter(temp, unit):
    if unit == 'F':
        return (temp - 32) * 5/9
    elif unit == 'K':
        return temp - 273.15
    return temp

def outlier_filter(temps):
    if len(temps) < 2:
        return temps
    mean_temp = statistics.mean(temps)
    print(f'[TRACE] Line 13: mean_temp = {mean_temp}')
    stdev_temp = statistics.stdev(temps) if len(temps) > 1 else 0
    print(f'[TRACE] Line 14: stdev_temp = {stdev_temp}')
    return [t for t in temps if abs(t - mean_temp) <= 2 * stdev_temp]

# Sensor data: (temperature, unit)
sensor_readings = [
print(f'[TRACE] Line 18: sensor_readings = {sensor_readings}')
    (25, 'C'),
    (77, 'F'),
    (298.15, 'K'),
    (30, 'C'),
    (86, 'F'),
    (310, 'K'),
    (22, 'C'),
    (68, 'F')
]

# Normalize all temperatures to Celsius
normalized_temps = [celsius_converter(temp, unit) for temp, unit in sensor_readings]
print(f'[TRACE] Line 30: normalized_temps = {normalized_temps}')

# Filter outliers
filtered_temps = outlier_filter(normalized_temps)
print(f'[TRACE] Line 33: filtered_temps = {filtered_temps}')

# Compute reliability score as weighted average
weights = [0.1, 0.15, 0.2, 0.25, 0.3] * ((len(filtered_temps) // 5) + 1)
print(f'[TRACE] Line 36: weights = {weights}')
weights = weights[:len(filtered_temps)]
print(f'[TRACE] Line 37: weights = {weights}')

weighted_sum = sum(temp * weight for temp, weight in zip(filtered_temps, weights))
print(f'[TRACE] Line 39: weighted_sum = {weighted_sum}')
weight_sum = sum(weights)
print(f'[TRACE] Line 40: weight_sum = {weight_sum}')

final_reliability_score = weighted_sum / weight_sum if weight_sum != 0 else 0
print(f'[TRACE] Line 42: final_reliability_score = {final_reliability_score}')

print(f"Result: {round(final_reliability_score, 2)}")