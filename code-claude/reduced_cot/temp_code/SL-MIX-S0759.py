# City temperature analysis program
temperature_data = {
    'New York': 28,
    'Los Angeles': 32,
    'Chicago': 26,
    'Houston': 35,
    'Phoenix': 40,
    'Philadelphia': 30,
    'San Antonio': 37,
    'San Diego': 29
}

# Filter settings
min_temp = 30
max_temp = 38
excluded_cities = {'Phoenix', 'Dallas'}

# Process data
warm_cities = {city for city, temp in temperature_data.items() if temp >= min_temp}
all_cities = set(temperature_data.keys())
cool_cities = all_cities - warm_cities

# Find cities meeting criteria
qualified_cities = warm_cities - excluded_cities

# Count valid entries
valid_count = len(qualified_cities)

# Display results
print(f"Warm cities: {warm_cities}")
print(f"Qualified cities: {qualified_cities}")
print(f"Result: {valid_count}")