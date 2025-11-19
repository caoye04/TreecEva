from collections import Counter

morning_sales = Counter({'apple': 10, 'cherry': 7, 'blueberry': 5})
afternoon_sales = Counter({'apple': 8, 'cherry': 12, 'pumpkin': 3})

# Divide and conquer: combine sales data
total_pie_sales = sum((morning_sales + afternoon_sales).values())

print(f"Result: {total_pie_sales}")