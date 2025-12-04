from collections import Counter

# Weather monitoring station data
daily_temps = [23, 25, 22, 27, 26, 24, 28, 25]
humidity_levels = [65, 70, 75, 60, 55, 68, 50, 62]

# Calculate average temperature
total_temp = sum(daily_temps)
day_count = len(daily_temps)
avg_temp = total_temp / day_count

# Find number of days with temperature above average
filtered_count = len([temp for temp in daily_temps if temp > avg_temp])

# Find most common humidity level
humidity_counter = Counter(humidity_levels)
most_common_humidity = humidity_counter.most_common(1)[0][0]

# Some additional analysis
for i, (temp, humidity) in enumerate(zip(daily_temps, humidity_levels)):
    if temp > 25 and humidity < 60:
        comfort_index = temp - humidity * 0.1
    else:
        comfort_index = temp - humidity * 0.05

print(f"Result: {filtered_count}")