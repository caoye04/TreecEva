from collections import Counter

croissant_price = 2.50
muffin_price = 1.75
scone_price = 3.25

sales_count = Counter({
    'croissants': 48,
    'muffins': 32,
    'scones': 24
})

prices = {
    'croissants': croissant_price,
    'muffins': muffin_price,
    'scones': scone_price
}

total_revenue = sum(sales_count[item] * prices[item] for item in sales_count)

print(f"Result: {total_revenue}")