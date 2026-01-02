def process_temperatures(temps):
    temp_kelvin = []
    for t in temps:
        if t > -273.15:
            temp_kelvin.append(t + 273.15)
    
    # Irrelevant variable (minor distraction)
    avg_temp = sum(temp_kelvin) / len(temp_kelvin) if temp_kelvin else 0
    
    # Apply filter using lambda and string-based condition check
    threshold_str = '293.15'
    threshold = float(threshold_str)
    is_high_temp = lambda x: x >= threshold
    filtered_values = list(filter(is_high_temp, temp_kelvin))
    
    # Perform final summation
    filtered_sum = sum(filtered_values)
    return filtered_sum

# Input data
temperature_celsius = [-40, 0, 20, 25, 30, 50]

# Call function and print result
result = process_temperatures(temperature_celsius)
print(f"Target result: {result}")