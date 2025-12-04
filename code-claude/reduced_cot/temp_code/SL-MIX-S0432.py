# Hiking Trip Planner
# Calculate the optimal number of days for a hiking trip based on trail conditions

def calculate_trip_duration(trails, weather_factor):
    base_durations = []
    adjusted_durations = []
    
    # Process trail information
    for trail_name, distance, elevation in trails:
        # Calculate base duration (days) using distance and elevation
        base_duration = (distance / 10) + (elevation / 500)
        base_durations.append(base_duration)
        
        # Apply weather adjustment
        adjusted_duration = base_duration * weather_factor
        adjusted_durations.append(round(adjusted_duration, 1))
    
    return base_durations, adjusted_durations

# Trail data: (name, distance in km, elevation gain in meters)
trail_options = [
    ("Eagle Ridge", 45, 1200),
    ("Mountain Pass", 35, 2000),
    ("Valley Route", 60, 800),
    ("Highland Trek", 50, 1500)
]

# Current weather conditions (1.0 = normal, >1.0 = worse conditions)
current_weather = 1.2
forecasted_weather = 0.9

# Calculate durations
base_durations, adjusted_durations = calculate_trip_duration(trail_options, current_weather)

# Sort the adjusted durations for analysis
sorted_durations = sorted(adjusted_durations)

# Filter trails that are too long or too short
max_allowed = 10
min_allowed = 4
filtered_durations = [d for d in sorted_durations if min_allowed <= d <= max_allowed]

# Additional calculations for route planning
total_distance = sum(trail[1] for trail in trail_options)
average_elevation = sum(trail[2] for trail in trail_options) / len(trail_options)

# Alternative duration calculation based on averages
backup_duration = round((total_distance / (len(trail_options) * 10)) + (average_elevation / 1000), 1)

# Determine the optimal trip duration
optimal_days = min(filtered_durations) if filtered_durations else backup_duration

print(f"Result: {optimal_days}")