import itertools

# Sales data analysis for an e-commerce platform
sales_data = {
    'product_a': [120, 145, 132, 168],  # Units sold per quarter
    'product_b': [85, 97, 101, 113],
    'product_c': [63, 59, 68, 72]
}

# Cost and price information (in dollars)
costs = {'product_a': 15, 'product_b': 22, 'product_c': 9}
prices = {'product_a': 29.99, 'product_b': 44.50, 'product_c': 17.25}

# Marketing campaign effectiveness scores
campaign_scores = {'product_a': 0.8, 'product_b': 0.65, 'product_c': 0.9}

# Calculate potential combinations for bundle offers
bundle_options = list(itertools.combinations(sales_data.keys(), 2))
potential_bundles = len(bundle_options)

# Analyze quarterly growth rates
growth_rates = {}
for product, sales in sales_data.items():
    rates = []
    for i in range(1, len(sales)):
        rate = (sales[i] - sales[i-1]) / sales[i-1]
        rates.append(rate)
    growth_rates[product] = rates

# Calculate average growth rate per product
avg_growth = {}
for product, rates in growth_rates.items():
    avg_growth[product] = sum(rates) / len(rates)

# Track seasonal performance index
seasonal_index = {}
for product, sales in sales_data.items():
    max_quarter = sales.index(max(sales)) + 1
    min_quarter = sales.index(min(sales)) + 1
    seasonal_index[product] = (max_quarter, min_quarter)

# Calculate total annual sales per product
annual_sales = {product: sum(quarters) for product, quarters in sales_data.items()}

# Calculate revenue per product
revenue = {}
for product in sales_data.keys():
    revenue[product] = annual_sales[product] * prices[product]

# Calculate profit per product
profits = {}
for product in sales_data.keys():
    profits[product] = revenue[product] - (annual_sales[product] * costs[product])

# Apply marketing effectiveness adjustment (not used in final calculation)
adjusted_profits = {}
for product in profits:
    adjusted_profits[product] = profits[product] * campaign_scores[product]

# Calculate overall business metrics
total_revenue = sum(revenue.values())
total_cost = sum([annual_sales[p] * costs[p] for p in costs])
total_profit = sum(profits.values())

# Track profit margin and other KPIs
profit_margin = total_profit / total_revenue
best_product = max(profits, key=profits.get)
worst_product = min(profits, key=profits.get)

print(f"Result: {total_profit}")