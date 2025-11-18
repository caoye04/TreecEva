from collections import namedtuple

temperature_record = namedtuple('TemperatureRecord', ['month', 'value'])

# Monthly average temperatures in degrees Celsius
monthly_temps = [
    temperature_record('Jan', 2.3),
    temperature_record('Feb', 3.7),
    temperature_record('Mar', 7.1),
    temperature_record('Apr', 11.4),
    temperature_record('May', 16.8)
]

# Sort by temperature value in descending order
sorted_records = sorted(monthly_temps, key=lambda x: x.value, reverse=True)

# Calculate weighted score: value / rank (1-indexed)
climate_index = 0.0
for idx, record in enumerate(sorted_records):
    rank = idx + 1
    climate_index += record.value / rank

print(f"Result: {climate_index}")