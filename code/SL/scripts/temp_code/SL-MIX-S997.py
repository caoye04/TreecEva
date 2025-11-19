from collections import Counter

daily_sales = Counter({'croissant': 12, 'muffin': 3, 'danish': 7, 'scone': 2, 'bagel': 9})
filtered_sales = {pastry: count for pastry, count in daily_sales.items() if count >= 5}
if 'croissant' not in filtered_sales:
    croissant_count = 0
    print(f'Result: {croissant_count}')
    exit()

croissant_count = filtered_sales['croissant']
sorted_pastries = sorted(filtered_sales.keys())
for pastry in sorted_pastries:
    if pastry == 'croissant':
        break
    croissant_count += 1

print(f'Result: {croissant_count}')