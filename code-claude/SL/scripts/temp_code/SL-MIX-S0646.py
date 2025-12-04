from collections import Counter

color_palette = ['blue', 'red', 'green', 'blue', 'yellow', 'blue', 'green', 'red', 'blue']
shades = ['light', 'dark', 'medium']

# Count occurrences of each color
color_counter = Counter(color_palette)

# Add some additional colors for testing
if len(color_palette) > 5:
    color_counter['purple'] = 1
    color_counter['orange'] = 2

# Find the most common color and its count
most_common_color = color_counter.most_common(1)[0][0]
dominant_color_count = color_counter.most_common(1)[0][1]

# Calculate average occurrences per color
avg_occurrences = sum(color_counter.values()) / len(color_counter)

# Determine if distribution is balanced
is_balanced = max(color_counter.values()) <= 2 * min(color_counter.values())

# Print the dominant color count
print(f"Result: {dominant_color_count}")