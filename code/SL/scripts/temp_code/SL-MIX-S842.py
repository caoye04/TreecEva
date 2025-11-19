from collections import defaultdict

daily_sales_data = [
    {'bread': 10, 'cakes': 5, 'cookies': 20},
    {'bread': 15, 'cakes': 8, 'cookies': 25},
    {'bread': 12, 'cakes': 7, 'cookies': 30}
]

item_profits = {'bread': 2, 'cakes': 5, 'cookies': 1}
ledger = defaultdict(int)

for day in daily_sales_data:
    temp_ledger = ledger.copy()
    for item, count in day.items():
        ledger[item] = temp_ledger[item] + (count * item_profits[item])

total_accumulated_profit = sum(ledger.values())
print(f"Result: {total_accumulated_profit}")