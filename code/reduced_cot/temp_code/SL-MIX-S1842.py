import math
from collections import Counter
temperature_deviations = [1.2, -0.5, 0.8, -1.0, 0.3]
exponential_values = [math.exp(temp) for temp in temperature_deviations]
mean_exponential = sum(exponential_values) / len(exponential_values)
normalized_temperature_index = math.log(mean_exponential)
print(f'Result: {normalized_temperature_index}')