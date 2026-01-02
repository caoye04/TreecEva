temperatures_celsius = [25, 30, 15, 20, 35]
offset = 273.15
scale_factor = len(temperatures_celsius) - 2
total_kelvin = 0
adjusted_sum = 0

for temp in temperatures_celsius:
    kelvin = temp + offset
    total_kelvin += kelvin

for i, temp in enumerate(temperatures_celsius):
    if i % 2 == 0:
        adjusted_sum += temp * 1.1
    else:
        adjusted_sum += temp * 0.95

# Apply conditional scaling based on data size
correction = 1.05 if len(temperatures_celsius) > 3 else 0.95
adjusted_sum *= correction

final_temperature = adjusted_sum / scale_factor if scale_factor else 0

print(f"Result: {final_temperature}")