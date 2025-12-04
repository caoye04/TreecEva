# Inventory optimization system for a warehouse
# Calculates optimal weight distribution based on product metrics

products = {
    'A': {'weight': 3.5, 'volume': 2.1, 'priority': 8},
    'B': {'weight': 1.2, 'volume': 0.8, 'priority': 5},
    'C': {'weight': 5.0, 'volume': 4.2, 'priority': 9},
    'D': {'weight': 2.8, 'volume': 3.0, 'priority': 6},
    'E': {'weight': 4.1, 'volume': 2.7, 'priority': 7}
}

# Calculate volume efficiency score
volume_scores = []
for product_id, details in products.items():
    ratio = details['weight'] / details['volume'] if details['volume'] > 0 else 0
    volume_scores.append(ratio)

# Track the highest priority products
high_priority = [p for p, d in products.items() if d['priority'] > 6]

# Calculate alternate metrics (not directly used in final calculation)
alternate_metric = sum(d['volume'] * d['priority'] for d in products.values()) / len(products)
density_factor = max(volume_scores) - min(volume_scores)

# Process only products with priority over threshold
threshold = 6
valid_products = {k: v for k, v in products.items() if v['priority'] > threshold}

# Apply weighting coefficients
coefficients = {'weight': 2.5, 'priority': 1.8, 'unused': 0.7}
total_coefficient = coefficients['weight'] + coefficients['priority']

# Calculate weighted values
weighted_values = []
for product, details in valid_products.items():
    # Calculate the weighted value for each product
    value = details['weight'] * coefficients['weight'] + details['priority'] * coefficients['priority']
    weighted_values.append(value)

# This is our target calculation
optimal_weight = sum(weighted_values) / total_coefficient

# Additional processing (not affecting the result)
historical_data = [optimal_weight * 0.95, optimal_weight * 1.05, optimal_weight * 0.97]
trend_indicator = sum(historical_data) / len(historical_data)

print(f"Result: {optimal_weight}")