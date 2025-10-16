import math
from collections import defaultdict

temperature_readings = [20, 25, 30, 15, 10, 35, 40, 5, 0, 45]
adjustment_factors = [0.9, 0.95, 1.05, 1.1, 0.85, 1.15, 1.2, 0.8, 0.75, 1.25]
correction_thresholds = [2, 3, 1, 4, 2, 5, 3, 1, 2, 6]

stability_tracker = defaultdict(int)
base_temp = 25
simulation_cycles = 3
final_stability_index = 0

for cycle in range(simulation_cycles):
    for i, (temp, factor, threshold) in enumerate(zip(temperature_readings, adjustment_factors, correction_thresholds)):
        adjusted_temp = temp * factor
        exponential_factor = math.exp(-0.1 * i)
        modulated_temp = adjusted_temp * exponential_factor
        
        if modulated_temp > base_temp and threshold % 2 == 0:
            corrected_temp = modulated_temp - (threshold * math.log(modulated_temp))
        elif modulated_temp <= base_temp or threshold % 3 == 0:
            corrected_temp = modulated_temp + (threshold * math.sqrt(modulated_temp))
        else:
            corrected_temp = modulated_temp
            
        stability_score = int(corrected_temp) % 7
        stability_tracker[stability_score] += 1
        
        if stability_tracker[stability_score] >= 3 and (cycle * i) % 5 == 0:
            final_stability_index = stability_score ** 2 + int(math.log(factor * 10))
            break
    else:
        continue
    break

print(f"Result: {final_stability_index}")