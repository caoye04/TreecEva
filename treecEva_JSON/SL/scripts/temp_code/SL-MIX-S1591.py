from collections import defaultdict
from functools import reduce

# Daily sales data: day -> {pastry: quantity}
daily_sales = [
    {'croissant': 20, 'muffin': 15, 'danish': 10},
    {'croissant': 25, 'muffin': 12, 'danish': 8},
    {'croissant': 18, 'muffin': 20, 'danish': 15},
    {'croissant': 22, 'muffin': 18, 'danish': 12},
    {'croissant': 30, 'muffin': 10, 'danish': 9},
    {'croissant': 27, 'muffin': 25, 'danish': 14},
    {'croissant': 24, 'muffin': 17, 'danish': 11}
]

# Extract croissant sales using map and filter
extract_croissants = lambda day_data: day_data['croissant']
croissant_sales = list(map(extract_croissants, daily_sales))

# Calculate total croissants sold using reduce
total_croissants = reduce(lambda x, y: x + y, croissant_sales)

# Calculate average
average_croissants = total_croissants // len(croissant_sales)

print(f'Result: {average_croissants}')