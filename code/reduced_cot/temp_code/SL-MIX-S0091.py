from collections import Counter

today_sales = Counter({'croissants': 45, 'muffins': 20, 'danish': 30})

# Check if bonus condition is met and calculate tomorrow's plan
bonus_condition = (sum(today_sales.values()) > 100) and (today_sales['croissants'] >= 2 * today_sales['muffins'])

planned_croissants = today_sales['croissants']
if bonus_condition:
    planned_croissants += 20

print(f'Target result: {planned_croissants}')