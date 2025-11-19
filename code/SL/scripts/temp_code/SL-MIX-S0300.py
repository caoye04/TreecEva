from collections import defaultdict
sales_data = ['bread:12,croissant:15', 'bread:20,croissant:18', 'bread:8,croissant:10', 'bread:25,croissant:30']
excess_days = 0
for day in sales_data:
    items = day.split(',')
    bread_sales = int(items[0].split(':')[1])
    croissant_sales = int(items[1].split(':')[1])
    if croissant_sales > bread_sales:
        excess_days += 1
print(f'Result: {excess_days}')