import math

# Hydrogen ion concentrations in mol/L from seawater samples
cytoplasmic_fluid_samples = [1e-8, 7.94e-9, 1e-7, 3.16e-8, 5.01e-8]

# Calculate pH levels using list comprehension
oceanic_ph_readings = [-math.log10(concentration) for concentration in cytoplasmic_fluid_samples]

# Calculate average pH
average_pH = sum(oceanic_ph_readings) / len(oceanic_ph_readings)

print(f'Result: {round(average_pH, 2)}')