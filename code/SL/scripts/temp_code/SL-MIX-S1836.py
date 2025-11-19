from collections import namedtuple
import statistics

# Define a named tuple for daily sales
BakerySales = namedtuple('BakerySales', ['croissants', 'baguettes', 'muffins'])

# Weekly sales data
weekly_sales = [
    BakerySales(croissants=25, baguettes=15, muffins=30),
    BakerySales(croissants=30, baguettes=20, muffins=25),
    BakerySales(croissants=20, baguettes=10, muffins=35),
    BakerySales(croissants=35, baguettes=25, muffins=20),
    BakerySales(croissants=28, baguettes=18, muffins=32),
    BakerySales(croissants=22, baguettes=12, muffins=28),
    BakerySales(croissants=30, baguettes=22, muffins=26)
]

# Extract croissant sales for the week
croissant_sales = [day.croissants for day in weekly_sales]

# Calculate average croissant sales
average_croissant_sales = statistics.mean(croissant_sales)

print(f'Result: {average_croissant_sales}')