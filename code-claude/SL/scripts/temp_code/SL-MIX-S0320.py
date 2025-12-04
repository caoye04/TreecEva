# Analyzing rainfall data from weather station readings
monthly_data = [45, 32, 67, 89, 102, 75, 43, 29, 51, 38, 62, 71]

# Set analysis parameters
station_id = 'WS-1092'
start_month = 3    # April (0-indexed)
end_month = 9      # October (0-indexed)

# Calculate statistics for annual report
max_rainfall = max(monthly_data)
min_rainfall = min(monthly_data)

# Extract data for growing season (April through September)
growing_season = monthly_data[start_month:end_month]

# Calculate total rainfall for the growing season
rainfall_total = sum(monthly_data[start_month:end_month])

# Calculate average monthly rainfall during growing season
average_monthly = rainfall_total / len(growing_season)

# Determine months with above average rainfall
above_average_count = len([m for m in growing_season if m > average_monthly])

print(f"Result: {rainfall_total}")