# Analyzing overlapping elements in environmental monitoring data

# Primary monitoring station data (temperature readings)
primary_data = [18, 22, 24, 21, 19, 30, 27, 24, 18, 12]

# Secondary monitoring station data (humidity readings)
secondary_data = [33, 27, 24, 18, 15, 12, 21, 30, 36, 39]

# Calculate mean values for reference
primary_mean = sum(primary_data) / len(primary_data)
secondary_mean = sum(secondary_data) / len(secondary_data)

# Find elements that are divisible by 2 in primary data and by 3 in secondary data
unique_elements = len(set(filter(lambda x: x % 2 == 0, primary_data)) & set(filter(lambda x: x % 3 == 0, secondary_data)))

# Create data tuples for future analysis
data_pairs = [(primary_data[i], secondary_data[i]) for i in range(min(len(primary_data), len(secondary_data)))]

print(f"Result: {unique_elements}")