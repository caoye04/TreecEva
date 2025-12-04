# Sales data analysis for quarterly performance report

product_categories = {
    'A101': 'electronics',
    'B205': 'furniture',
    'C309': 'electronics',
    'D412': 'kitchenware',
    'E518': 'furniture',
    'F623': 'electronics'
}

# Sales data: product_id and sales amount
sales_data = [
    ('A101', 1200),
    ('B205', 890),
    ('C309', 1450),
    ('D412', 650),
    ('E518', 920),
    ('F623', 1380)
]

# Performance thresholds for bonus calculation
low_threshold = 500
high_threshold = 1000
bonus_multiplier = 1.5

# Calculate average sales per category
category_totals = {}
category_counts = {}
for product_id, sales in sales_data:
    category = product_categories[product_id]
    category_totals[category] = category_totals.get(category, 0) + sales
    category_counts[category] = category_counts.get(category, 0) + 1

average_by_category = {cat: total/category_counts[cat] 
                      for cat, total in category_totals.items()}

# Identify target category with highest average sales
target_category = max(average_by_category.items(), key=lambda x: x[1])[0]

# Apply discount to non-target categories (not used in final calculation)
discounted_sales = [(product_id, sales * 0.9 if product_categories[product_id] != target_category else sales)
                    for product_id, sales in sales_data]

# Potential bonus pool calculation (not used in final calculation)
potential_bonus = sum(sales for _, sales in sales_data if sales > high_threshold) * bonus_multiplier

# Filter sales from target category that exceed low threshold
filtered_sales = [(product_id, sales) for product_id, sales in sales_data 
                 if product_categories[product_id] == target_category 
                 and sales > low_threshold]

# Calculate total qualifying sales
total_qualifying_sales = sum(sales for product_id, sales in filtered_sales)

# Apply seasonal adjustment factor (not used in final calculation)
seasonal_factor = 1.2
adjusted_total = total_qualifying_sales * seasonal_factor

print(f"Target result: {total_qualifying_sales}")
