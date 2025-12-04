# Calculate the quarterly revenue from product sales across different regions

# Sales data by product and region
sales_data = {
    'ProductA': {'North': 1200, 'South': 950, 'East': 1400, 'West': 1100},
    'ProductB': {'North': 800, 'South': 700, 'East': 950, 'West': 850},
    'ProductC': {'North': 1500, 'South': 1300, 'East': 1100, 'West': 1400}
}

# Quarterly growth rates for market analysis (not needed for revenue calculation)
growth_rates = {
    'North': 0.05,
    'South': 0.03,
    'East': 0.07,
    'West': 0.04
}

# Product discount tiers
discount_tiers = {
    'ProductA': 0.1,  # 10% discount
    'ProductB': 0.15, # 15% discount
    'ProductC': 0.05  # 5% discount
}

# Calculate potential growth (not used in final calculation)
potential_growth = {}
for region, rate in growth_rates.items():
    potential = sum(sales_data[product][region] for product in sales_data) * rate
    potential_growth[region] = round(potential, 2)

# Apply seasonal modifier to each region (not relevant to the task)
seasonal_modifier = 1.12
for region in growth_rates:
    adjusted_growth = growth_rates[region] * seasonal_modifier
    growth_rates[region] = round(adjusted_growth, 3)

# Filter sales by region and apply discounts
target_regions = ['North', 'East']
filtered_sales = {}

for product, regions in sales_data.items():
    for region, amount in regions.items():
        if region in target_regions:
            # Apply discount to the sales amount
            discounted_amount = amount * (1 - discount_tiers[product])
            key = f"{product}_{region}"
            filtered_sales[key] = discounted_amount

# Calculate the total discounted revenue from target regions
total_revenue = sum(filtered_sales.values())

# Calculate average sales per region (not needed for the result)
avg_per_region = {}
for region in sales_data['ProductA'].keys():
    region_total = sum(sales_data[product][region] for product in sales_data)
    avg_per_region[region] = region_total / len(sales_data)

print(f"Result: {total_revenue}")