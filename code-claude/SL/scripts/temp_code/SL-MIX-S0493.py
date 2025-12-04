# Product pricing analysis
product_data = "apple:2.5,banana:1.8,orange:3.2,grape:4.5,kiwi:2.0"

# Parse the product data
products = product_data.split(",")

# Extract prices from products
prices = [float(item.split(":")[1]) for item in products]

# Filter prices based on threshold
price_threshold = 2.2
filtered_prices = [price for price in prices if price > price_threshold]

# Calculate average of filtered prices
average_price = sum([price for price in filtered_prices]) / len(filtered_prices)

# Track price ranges for reporting
low_range = [p for p in prices if p < 2.0]
medium_range = [p for p in prices if 2.0 <= p <= 3.0]
high_range = [p for p in prices if p > 3.0]

print(f"Result: {average_price}")