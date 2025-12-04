def calculate_tax(amount, rate=0.08):
    """Calculate tax for a given amount."""
    return amount * rate

# Product sales data with region, product, and units sold
data = [
    {"region": "North", "product": "Widget", "units": 120, "price": 45.99},
    {"region": "South", "product": "Gadget", "units": 85, "price": 65.50},
    {"region": "East", "product": "Widget", "units": 95, "price": 47.25},
    {"region": "West", "product": "Gadget", "units": 110, "price": 62.75},
    {"region": "North", "product": "Tool", "units": 65, "price": 32.99},
    {"region": "South", "product": "Widget", "units": 75, "price": 46.50}
]

# Filter data for analysis
product_filter = lambda item: item["product"] in ["Widget", "Gadget"]
filtered_data = list(filter(product_filter, data))

# Process inventory statistics
inventory_count = sum(item["units"] for item in data)
average_price = sum(item["price"] for item in data) / len(data)

# Calculate shipping costs (not used in final result)
shipping_rates = {"North": 12.50, "South": 10.75, "East": 14.25, "West": 15.99}
total_shipping = sum(shipping_rates[item["region"]] for item in filtered_data)

def calculate_performance(sales_data):
    # Calculate revenue
    widget_sales = sum(item["units"] * item["price"] 
                     for item in sales_data if item["product"] == "Widget")
    
    # Calculate tax for tracking (not used in final calculation)
    tax_amount = calculate_tax(widget_sales, 0.095)
    
    # Calculate performance metric
    widget_count = sum(1 for item in sales_data if item["product"] == "Widget")
    gadget_revenue = sum(item["units"] * item["price"]
                       for item in sales_data if item["product"] == "Gadget")
    
    # Calculate discount factor (not used in final result)
    discount_factor = 0.85 if widget_count > 2 else 0.9
    
    # Return performance metric
    return round((widget_sales / widget_count) - (gadget_revenue / 1000), 2)

# Analyze market trends (not directly used)
market_growth = {"Widget": 0.12, "Gadget": 0.08, "Tool": 0.05}
projected_growth = sum(market_growth.get(item["product"], 0) * item["units"] 
                      for item in filtered_data)

# Calculate performance metric
sales_performance = calculate_performance(filtered_data)

# Display results
print(f"Inventory count: {inventory_count}")
print(f"Average price: ${average_price:.2f}")
print(f"Total shipping: ${total_shipping:.2f}")
print(f"Projected growth: {projected_growth:.2f}")
print(f"Result: {sales_performance}")