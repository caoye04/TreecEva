def process_temperature_data(temp_list):
    # Filter temperatures above freezing and convert to Fahrenheit
    above_freezing = [t for t in temp_list if t > 0]
    
    # Distractor: calculate average (not used in final result)
    avg_temp = sum(above_freezing) / len(above_freezing) if above_freezing else 0
    
    # Convert to Fahrenheit using lambda
    to_fahrenheit = lambda c: (c * 9/5) + 32
    fahrenheit_temps = list(map(to_fahrenheit, above_freezing))
    
    # Apply temperature adjustment based on range
    adjusted_temps = []
    for temp in fahrenheit_temps:
        if temp < 50:
            adjusted_temps.append(temp + 5)  # Cold weather boost
        elif temp > 80:
            adjusted_temps.append(temp - 3)  # Hot weather reduction
        else:
            adjusted_temps.append(temp + 2)  # Moderate adjustment
    
    # Final temperature is the last adjusted value
    final_temperature = adjusted_temps[-1] if adjusted_temps else 0
    
    # Distractor: calculate temperature range (not used)
    temp_range = max(fahrenheit_temps) - min(fahrenheit_temps) if fahrenheit_temps else 0
    
    print(f"Result: {final_temperature}")
    return final_temperature

# Input temperatures in Celsius
temperatures = [-5, 15, 8, 25, -2, 12, 18]

# Process the data
temperature_check = process_temperature_data(temperatures)