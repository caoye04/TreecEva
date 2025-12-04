# Color mixing analysis program
primary_colors = ['red', 'blue', 'yellow', 'red']
secondary_colors = ['green', 'orange', 'purple', 'blue']

# Track some additional color properties
warm_colors = ['red', 'orange', 'yellow']
cool_colors = ['blue', 'green', 'purple']

# Count colors that appear in both primary and secondary lists
common_colors = len([color for color in primary_colors if color in secondary_colors])

# Determine unique elements that appear in exactly one of the sets
unique_elements = len(set(primary_colors).symmetric_difference(set(secondary_colors)))

# Calculate a weighted color metric based on warm vs cool colors
color_metric = sum(2 if color in warm_colors else 1 for color in primary_colors)

# Print the result of our unique elements calculation
print(f"Result: {unique_elements}")