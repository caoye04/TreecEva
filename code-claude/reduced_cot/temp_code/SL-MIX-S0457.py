# Weather data analysis for a week
import statistics

# Raw temperature readings (Celsius) collected over 7 days
temperature_readings = [22.5, 23.1, 19.8, 25.3, 22.0, 21.4, 24.7]

# Quality control: flag any readings that seem suspicious
noise_threshold = 2.5
mean_temp = statistics.mean(temperature_readings)

# Find outliers for reporting purposes
potential_outliers = [temp for temp in temperature_readings if abs(temp - mean_temp) > noise_threshold]
print(f"Potential outliers: {potential_outliers}")

# Process the main data
humidity_values = [78, 82, 65, 45, 67, 72, 70]
weather_conditions = ['Cloudy', 'Rainy', 'Sunny', 'Sunny', 'Partly Cloudy', 'Rainy', 'Sunny']

# Calculate rainfall effect (not used in final calculation, just for reporting)
rainfall_effect = sum(5 if condition == 'Rainy' else 0 for condition in weather_conditions)

# Data normalization factor (distraction)
normalization_factor = 0.1 * statistics.stdev(temperature_readings)

# Filter temperatures by specific criteria
sunny_temps = [temperature_readings[i] for i in range(len(temperature_readings)) 
               if weather_conditions[i] == 'Sunny']

# Another filter - temperatures with humidity below 70% (relevant to final answer)
filtered_temperatures = [temperature_readings[i] for i in range(len(temperature_readings)) 
                         if humidity_values[i] < 70]

# Calculate the temperature range for filtered data
final_temperature = max(filtered_temperatures) - min(filtered_temperatures)

# Calculate average temperature (distraction)
average_filtered_temp = sum(filtered_temperatures) / len(filtered_temperatures)

# Apply normalization (distraction)
normalized_range = final_temperature / normalization_factor

print(f"Result: {final_temperature}")