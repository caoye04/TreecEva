from collections import defaultdict

day = 20
pie_sales = {'apple': 15, 'cherry': 8, 'blueberry': 12, 'pumpkin': 5}
adjusted_sales = defaultdict(int)

is_weekend = (day % 7 == 0) or (day % 7 == 6)

if is_weekend:
    for pie_type, quantity in pie_sales.items():
        if quantity > 10:
            adjusted_sales[pie_type] = quantity * 2
        else:
            adjusted_sales[pie_type] = quantity
else:
    adjusted_sales = pie_sales

final_pie_count = sum(adjusted_sales.values())
print(f"Result: {final_pie_count}")