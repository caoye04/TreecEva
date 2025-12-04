def calculate_price_index(prices, weights):
    # Calculate weighted average of prices
    total_weighted_price = sum(p * w for p, w in zip(prices, weights))
    total_weight = sum(weights)
    return total_weighted_price / total_weight if total_weight > 0 else 0

# Market data for different product categories
product_categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home']
product_prices = [450, 65, 30, 25, 120]

# Historical price changes (not directly used in calculation)
historical_changes = [0.05, -0.02, 0.08, 0.01, 0.03]

# Store inventory counts (distraction)
inventory_levels = [120, 350, 800, 250, 175]

# Calculate inventory value (distraction)
inventory_value = [p * i for p, i in zip(product_prices, inventory_levels)]
total_inventory = sum(inventory_value)

# Generate importance weights based on price range
max_price = max(product_prices)
min_price = min(product_prices)
price_range = max_price - min_price

# Calculate normalized weights (higher price = higher weight)
raw_weights = [(p - min_price) / price_range for p in product_prices]

# Apply seasonal adjustment factors (distraction)
seasonal_factors = [1.2, 0.9, 1.1, 0.8, 1.0]
adjusted_weights = [w * s for w, s in zip(raw_weights, seasonal_factors)]

# Filter products with prices above average
average_price = sum(product_prices) / len(product_prices)
expensive_indices = [i for i, p in enumerate(product_prices) if p > average_price]

# Extract filtered prices and weights
filtered_prices = [product_prices[i] for i in expensive_indices]
filtered_weights = [raw_weights[i] for i in expensive_indices]

# Calculate market penetration (distraction)
market_share = [0.15, 0.22, 0.35, 0.08, 0.20]
weighted_share = sum(s * w for s, w in zip(market_share, raw_weights))

# Calculate final price index
price_index = calculate_price_index(product_prices, filtered_weights)

print(f"Result: {price_index}")