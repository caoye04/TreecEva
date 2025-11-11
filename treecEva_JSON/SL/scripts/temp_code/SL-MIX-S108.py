import math

coral_alpha_initial = 150
coral_beta_initial = 120
growth_alpha = 0.05
growth_beta = 0.07
time_years = 5
threshold = 20

population_alpha = coral_alpha_initial * math.exp(growth_alpha * time_years)
population_beta = coral_beta_initial * math.exp(growth_beta * time_years)
difference = abs(population_alpha - population_beta)
normalized_difference = math.log(difference) if difference > threshold else difference

print(f"Result: {normalized_difference}")