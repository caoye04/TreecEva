import math
initial_bacteria_count = 50
growth_hours = 3
final_population = initial_bacteria_count * (2 ** growth_hours)
log_population = math.log(final_population)
print(f'Result: {log_population}')