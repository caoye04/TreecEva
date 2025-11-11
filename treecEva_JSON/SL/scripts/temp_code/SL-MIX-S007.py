from functools import reduce

temperature_anomalies = [1.2, -0.5, 0.3, 2.1, -1.0, 0.8, 1.5, -0.2]
positive_anomalies = list(filter(lambda x: x > 0, temperature_anomalies))
total_warming_impact = reduce(lambda acc, val: acc + val, positive_anomalies, 0)
print(f"Result: {total_warming_impact}")