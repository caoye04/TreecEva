# Weather data analysis to find regions exceeding temperature threshold

# Temperature data for different regions (Celsius)
temperatures = [23.5, 18.7, 30.2, 27.8, 16.4, 28.9, 31.5, 22.3]

# Region names
regions = ['North', 'Northwest', 'South', 'Southeast', 'West', 'East', 'Central', 'Coastal']

# Map regions to their temperature data
region_data = {regions[i]: temperatures[i] for i in range(len(regions))}

# Calculate average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Set threshold to be slightly above average
threshold = avg_temp + 2

# Select regions with rainfall above the threshold
rainfall = [45.2, 62.8, 12.5, 30.1, 80.3, 35.7, 25.6, 68.9]
wet_regions = [regions[i] for i in range(len(regions)) if rainfall[i] > 50]

# Count regions with temperature above threshold
valid_regions = sum(1 for region in regions if region_data[region] > threshold)

# Get the hottest regions (top 3)
hottest_regions = sorted(regions, key=lambda r: region_data[r], reverse=True)[:3]

# Print results for verification
print(f"Average temperature: {avg_temp:.2f}")
print(f"Threshold: {threshold:.2f}")
print(f"Valid regions: {valid_regions}")
print(f"Hottest regions: {hottest_regions}")