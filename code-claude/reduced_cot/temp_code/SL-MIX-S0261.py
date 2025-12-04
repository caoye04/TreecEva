import itertools

# Dataset of website traffic by hour (visits per hour)
hourly_traffic = [45, 67, 23, 12, 89, 102, 76, 83, 95, 120, 110, 88,
                 65, 72, 91, 84, 56, 75, 82, 93, 71, 48, 35, 29]

# Time periods for analysis
peak_hours = [8, 9, 10, 11, 19, 20, 21]
low_activity = [0, 1, 2, 3, 4, 22, 23]

# Extract traffic data for specific periods
morning_traffic = hourly_traffic[6:12]  # 6 AM to 11 AM
evening_traffic = hourly_traffic[17:22]  # 5 PM to 9 PM

# Calculate average traffic
avg_traffic = sum(hourly_traffic) / len(hourly_traffic)
median_value = sorted(hourly_traffic)[len(hourly_traffic) // 2]

# Find hours with traffic above threshold
threshold = avg_traffic * 1.2
high_traffic_hours = [i for i, traffic in enumerate(hourly_traffic) if traffic > threshold]

# Group consecutive high traffic hours
grouped_hours = []
current_group = []
for hour in high_traffic_hours:
    if not current_group or hour == current_group[-1] + 1:
        current_group.append(hour)
    else:
        if len(current_group) >= 2:  # Only keep groups of 2+ consecutive hours
            grouped_hours.append(current_group)
        current_group = [hour]
        
if current_group and len(current_group) >= 2:
    grouped_hours.append(current_group)

# Calculate traffic patterns
traffic_changes = [hourly_traffic[i+1] - hourly_traffic[i] for i in range(len(hourly_traffic)-1)]
positive_changes = [change for change in traffic_changes if change > 0]
max_increase = max(positive_changes) if positive_changes else 0

# Find periods with consistent growth
growth_periods = []
for i in range(len(hourly_traffic) - 3):
    if all(hourly_traffic[i+j] < hourly_traffic[i+j+1] for j in range(3)):
        growth_periods.append(i)

# Filter values based on multiple conditions
filtered_values = [traffic for i, traffic in enumerate(hourly_traffic) 
                 if (i in peak_hours and traffic > avg_traffic) or 
                    (i not in low_activity and traffic > median_value)]

# Calculate the sum of filtered values
filtered_sum = sum(filtered_values)

# Some additional calculations that don't affect the result
traffic_variance = sum((x - avg_traffic) ** 2 for x in hourly_traffic) / len(hourly_traffic)
daily_total = sum(hourly_traffic)
highest_hour = hourly_traffic.index(max(hourly_traffic))

print(f"Result: {filtered_sum}")