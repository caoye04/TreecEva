def convert_and_adjust(temperatures, limit):
    celsius_list = [round((f - 32) * 5 / 9, 2) for f in temperatures]
    temp_dict = {i: c for i, c in enumerate(celsius_list)}
    above_limit = {k: v for k, v in temp_dict.items() if v > limit}
    adjustment = 1.5
    adjusted_temps = [v + adjustment for v in above_limit.values()]
    if len(adjusted_temps) == 0:
        return 0
    avg_temp = sum(adjusted_temps) / len(adjusted_temps)
    final_temperature = round(avg_temp, 2)
    return final_temperature

# Input data
fahrenheit_readings = [68, 77, 86, 95, 104]
threshold = 25
final_temperature = convert_and_adjust(fahrenheit_readings, threshold)
print(f"Result: {final_temperature}")