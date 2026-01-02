from collections import defaultdict

# Simulated daily temperature readings for a week in multiple cities
temperatures = [
    ('NewYork', [68, 70, 72, 69, 74, 75, 73]),
    ('LosAngeles', [75, 76, 78, 77, 79, 80, 78]),
    ('Chicago', [60, 62, 65, 63, 64, 68, 66]),
    ('Houston', [78, 80, 82, 81, 83, 84, 82])
]

# Irrelevant placeholder for distraction (minimal interference)
pressure_data = defaultdict(lambda: 'N/A')
pressure_data['NewYork'] = 'High'

# Extract all temperatures and compute average across all readings
temp_list = []
for city, temps in temperatures:
    temp_list.extend(temps)

# Calculate average temperature
total_temp = sum(temp_list)
count = len(temp_list)
avg_temp = total_temp / count

# Final computation step
final_temperature = round(avg_temp, 2)

print(f"Result: {final_temperature}")