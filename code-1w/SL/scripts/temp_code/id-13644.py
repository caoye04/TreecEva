from collections import defaultdict

# Simulate sensor readings with some noise and redundancy
temperature_readings = [23, 24, 25, 23, 24, 26, 25, 24, 23, 27]
humidity_readings = [45, 46, 44, 45, 47, 46, 45, 48, 44, 45]

# Track frequency of readings (distractor: not directly used in final result)
freq_temp = defaultdict(int)
for temp in temperature_readings:
    freq_temp[temp] += 1

# Calculate moving average of temperature (semi-relevant, used for adjustment)
moving_avg_temp = 0
for i in range(1, len(temperature_readings) - 1):
    moving_avg_temp += (temperature_readings[i-1] + temperature_readings[i] + temperature_readings[i+1]) / 3

moving_avg_temp /= (len(temperature_readings) - 2)

# Misleading calculation: energy_equivalent (not used in final path)
energy_equivalent = 0
for h in humidity_readings:
    energy_equivalent += h ** 0.5
energy_equivalent = round(energy_equivalent, 2)

# Core logic: compute adjusted sum of unique temperatures
unique_temps = set(temperature_readings)
base_sum = sum(unique_temps)
offset = len(humidity_readings) % 4  # minor adjustment based on humidity array length
adjusted_sum = base_sum - offset

# Use enumerate to find first significant jump in temps (index > 0 where diff >= 2)
jump_index = -1
for i, (t1, t2) in enumerate(zip(temperature_readings, temperature_readings[1:])):
    if t2 - t1 >= 2:
        jump_index = i
        break

# Correction factor depends on whether a jump was found
correction_factor = 1.5 if jump_index != -1 else 0.8

# Final computation step
temp_product = 1
for t in temperature_readings[:3]:
    temp_product *= t

# Dummy list comprehension with no side effects
_ = [t * correction_factor for t in temperature_readings if t > moving_avg_temp]

# Key assignment: final_score depends on adjusted_sum and correction_factor
final_score = adjusted_sum * correction_factor

print(f"Result: {final_score}")