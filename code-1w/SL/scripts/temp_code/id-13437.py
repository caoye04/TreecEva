temperatures = [25.0, 30.0, 22.5, 35.0, 27.8]
pressures = [99.5, 101.2, 98.7, 103.3, 100.1]

temperature_map = {temp: idx for idx, temp in enumerate(temperatures)}
adjusted_pressures = {}
for i, temp in enumerate(temperatures):
    adjusted_pressure = pressures[i] * (1 + (temp - 25) / 100)
    adjusted_pressures[temp] = round(adjusted_pressure, 2)

sensor_ranks = []
for temp in sorted(temperature_map.keys(), reverse=True):
    sensor_ranks.append(temperature_map[temp])

sensor_rank = [sensor_ranks[i] for i in range(len(sensor_ranks)) if i % 2 == 0]

final_pressure = adjusted_pressures.get(sensor_rank[0], 0)
print(f"Result: {final_pressure}")