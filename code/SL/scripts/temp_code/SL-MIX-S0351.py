from collections import defaultdict

daily_sales = [
    {'croissant': 15, 'muffin': 20, 'scone': 10},
    {'croissant': 12, 'muffin': 18, 'scone': 15},
    {'croissant': 10, 'muffin': 15, 'scone': 12},
    {'croissant': 18, 'muffin': 25, 'scone': 8},
    {'croissant': 20, 'muffin': 30, 'scone': 10},
    {'croissant': 8, 'muffin': 12, 'scone': 20},
    {'croissant': 22, 'muffin': 28, 'scone': 15}
]

prices = {'croissant': 2.50, 'muffin': 1.75, 'scone': 2.00}

total_revenue = 0.0
found_target_week = False

for day in daily_sales:
    if not found_target_week:
        croissant_muffin_total = day['croissant'] + day['muffin']
        if croissant_muffin_total > 100:
            found_target_week = True
            
    if found_target_week:
        for item, quantity in day.items():
            total_revenue += quantity * prices[item]

print(f"Result: {total_revenue}")