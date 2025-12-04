import itertools

# Weather monitoring system for a week
daily_temperatures = [23, 25, 22, 25, 27, 23, 21]
humidity_values = [45, 50, 55, 48, 40, 52, 60]

# Analysis parameters
min_temp = 22
max_temp = 26
preferred_humidity = 50

# Count days with good temperature range
warm_days = sum(1 for temp in daily_temperatures if temp > 24)
cool_days = len([temp for temp in daily_temperatures if temp < 23])

# Find unique temperature values within the comfortable range
unique_count = len(set([temp for temp in daily_temperatures if min_temp <= temp <= max_temp]))

# Calculate average humidity for days with temperatures in range
matching_humidity = [hum for temp, hum in zip(daily_temperatures, humidity_values) if min_temp <= temp <= max_temp]
avg_humidity = sum(matching_humidity) / len(matching_humidity) if matching_humidity else 0

# Determine if humidity meets preferences on comfortable temperature days
ideal_days = sum(1 for temp, hum in zip(daily_temperatures, humidity_values) 
                if min_temp <= temp <= max_temp and abs(hum - preferred_humidity) <= 5)

print(f"Result: {unique_count}")