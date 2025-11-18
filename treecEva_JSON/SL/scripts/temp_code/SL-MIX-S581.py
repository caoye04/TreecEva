from collections import defaultdict

# Daily sales record
pastry_sales = {
    'croissant': 15,
    'muffin': 8,
    'danish': 12,
    'scone': 5
}

# Pricing and discount rules
price_per_croissant = 3.50
discount_threshold = 10
discount_rate = 0.10  # 10% off

# Calculate croissant revenue with potential discount
quantity_sold = pastry_sales['croissant']
croissant_revenue = quantity_sold * price_per_croissant if quantity_sold <= discount_threshold else \
                    quantity_sold * price_per_croissant * (1 - discount_rate)

print(f'Result: {croissant_revenue}')