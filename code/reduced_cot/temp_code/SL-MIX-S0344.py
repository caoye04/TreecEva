import math
import numpy as np
from functools import reduce

def log_normalize(values):
    return [math.log(x + 1) for x in values]

def exp_smooth(values, alpha=0.3):
    smoothed = []
    prev = values[0]
    for v in values:
        current = alpha * v + (1 - alpha) * prev
        smoothed.append(current)
        prev = current
    return smoothed

temperature_readings = [25.3, 26.1, 24.8, 27.5, 26.9, 25.0, 28.2, 27.1]
normalized_temps = log_normalize(temperature_readings)
smoothed_temps = exp_smooth(normalized_temps)
filtered_temps = list(filter(lambda x: x > math.log(26), smoothed_temps))

if len(filtered_temps) > 0:
    matrix_a = np.array([[len(filtered_temps), sum(filtered_temps)], 
                         [sum(filtered_temps), sum([x**2 for x in filtered_temps])]])
    eigenvals = np.linalg.eigvals(matrix_a)
    stability_index = round(reduce(lambda a, b: a + b, eigenvals), 4)
else:
    stability_index = 0

print(f"Result: {stability_index}")