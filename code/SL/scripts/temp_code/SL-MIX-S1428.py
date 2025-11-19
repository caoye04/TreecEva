from collections import defaultdict
from statistics import mean

temperatures = [22, 25, 19, 27, 24, 30, 21, 26, 23, 28]
overall_avg = mean(temperatures)
above_avg_temps = [t for t in temperatures if t > overall_avg]
above_avg_mean = mean(above_avg_temps)
print(f"Result: {above_avg_mean}")