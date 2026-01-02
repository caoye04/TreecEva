temperatures_celsius = [23, 18, 31, 27, 15, 35, 20]

temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

above_average = [t for t in temperatures_fahrenheit if t > sum(temperatures_fahrenheit) / len(temperatures_fahrenheit)]

divisible_by_five = {int(t) for t in above_average if int(t) % 5 == 0}

indices_of_high_heat = [i for i, t in enumerate(temperatures_celsius) if t >= 30]

zipped_data = list(zip(indices_of_high_heat, [temperatures_celsius[i] for i in indices_of_high_heat]))

sliced_temps = temperatures_celsius[1:6:2]

adjusted_temps = [t + 2 for t in sliced_temps]

filtered_data = [t for t in adjusted_temps if t in divisible_by_five]

filtered_sum = sum(filtered_data)

Result: filtered_sum