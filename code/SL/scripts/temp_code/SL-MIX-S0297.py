from collections import Counter

# Inventory management system analysis
product_categories = ['electronics', 'clothing', 'home_goods', 'electronics', 'clothing', 'books']
category_counts = Counter(product_categories)

# Initial revenue calculations
base_prices = [450, 120, 85, 490, 130, 45]
quantities = [12, 25, 18, 15, 30, 40]

revenue_by_category = {}
total_revenue = 0

for i, (category, price) in enumerate(zip(product_categories, base_prices)):
    if category not in revenue_by_category:
        revenue_by_category[category] = 0
    revenue_by_category[category] += price * quantities[i]
    total_revenue += price * quantities[i]

# Operating costs (some are irrelevant distractions)
operating_costs = 2850
staff_salaries = 4200  # Not used in final calculation
marketing_expense = 1250
utilities = 850  # Not used in final calculation
depreciation = 650

# Inventory holding costs (distractor)
inventory_holding_cost = sum(quantities) * 3.5  # Not used

# Final balance calculation
final_balance = total_revenue - (operating_costs + marketing_expense + depreciation)

print(f"Target result: {final_balance}")