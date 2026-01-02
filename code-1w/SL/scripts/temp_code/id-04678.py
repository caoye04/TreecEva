from itertools import zip_longest

def convert_and_adjust(temperatures, adjustment_factors):
    # Convert Celsius to Kelvin
    kelvin_vals = [temp + 273.15 for temp in temperatures]
    
    # Apply adjustment factors cyclically
    adjusted = []
    for k, factor in zip_longest(kelvin_vals, adjustment_factors, fillvalue=1.0):
        adjusted.append(k * factor)
    
    # Calculate mean and offset by smallest adjustment used
    mean_val = sum(adjusted) / len(adjusted)
    min_factor = min(adjustment_factors)
    final_temperature = mean_val - min_factor
    
    # Irrelevant auxiliary variable (minor distraction)
    status_flags = {i: 'processed' for i in range(len(temperatures))}
    
    return final_temperature

# Input data
temps = [0, 25, -10, 100]
factors = [1.1, 0.9, 1.0]

final_temperature = convert_and_adjust(temps, factors)
print(f"Result: {final_temperature}")