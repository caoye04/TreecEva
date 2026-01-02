temperatures = [23.5, 19.0, 27.3, 31.2, 25.8]

# Calculate average temperature
total = sum(temperatures)
avg_temp = total / len(temperatures)

# Determine season flag using string method
season_data = 'SUMMER_SOLSTICE'
is_summer = season_data.lower().startswith('summer')

# Apply conditional adjustment based on outlier presence
has_outlier = any(temp > 30 for temp in temperatures)
adjusted_avg = avg_temp + 5 if has_outlier else avg_temp - 2

# Final adjustment based on season
final_temperature = adjusted_avg + (2 if is_summer else -1)

print(f"Result: {final_temperature}")