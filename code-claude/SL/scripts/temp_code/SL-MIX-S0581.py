from collections import Counter, defaultdict

def analyze_sales_trend(data):
    # Analyze historical sales data (distractor function)
    trend_factors = {}
    for month, sales in data.items():
        if sales > 100:
            trend_factors[month] = sales * 0.15
        else:
            trend_factors[month] = sales * 0.08
    return sum(trend_factors.values()) / len(trend_factors)

def calculate_shipping_costs(distance, weight):
    # Calculate shipping costs based on distance and weight (distractor function)
    base_cost = 10
    distance_factor = distance * 0.05
    weight_factor = weight * 0.2
    return base_cost + distance_factor + weight_factor

def get_prime_factors(n):
    # Get prime factors of a number (helper function used in calculation)
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def calculate_optimal_stock(sales_data, seasonal_factors):
    # Process sales data with seasonal adjustments
    monthly_totals = defaultdict(int)
    product_counts = Counter()
    
    # Process sales data (relevant calculation)
    for product, data in sales_data.items():
        product_counts[product] = data.get('quantity', 0)
        month = data.get('month', 1)
        monthly_totals[month] += data.get('quantity', 0)
    
    # Calculate base inventory needs (relevant calculation)
    avg_monthly_sales = sum(monthly_totals.values()) / max(1, len(monthly_totals))
    
    # Calculate safety stock based on prime factors (relevant calculation)
    safety_factor = len(get_prime_factors(int(avg_monthly_sales))) * 1.5
    
    # Process seasonal adjustments (relevant calculation)
    seasonal_adjustment = 0
    for season, factor in seasonal_factors.items():
        if season in ['summer', 'winter']:
            seasonal_adjustment += factor * 2
        else:
            seasonal_adjustment += factor
    
    # Calculate logistics efficiency (distractor calculation)
    logistics_efficiency = 0
    for i in range(1, 10):
        if i % 3 == 0:
            logistics_efficiency += i * 0.5
        elif i % 2 == 0:
            logistics_efficiency -= i * 0.2
    
    # Apply bit operations to product variance (distractor calculation)
    product_variance = 0
    for count in product_counts.values():
        product_variance += (count & 15) | 3
    
    # Calculate lead time factor (distractor calculation)
    lead_times = [5, 12, 8, 15, 7]
    lead_time_factor = sum(lead_times[i] for i in range(len(lead_times)) if i % 2 == 0)
    
    # Calculate final optimal inventory (key calculation)
    base_inventory = avg_monthly_sales * 1.2
    adjusted_inventory = base_inventory + (seasonal_adjustment / 2)
    optimal_inventory = int(adjusted_inventory * safety_factor)
    
    # More distractor calculations that don't affect the result
    market_volatility = [0.05, -0.02, 0.03, -0.01, 0.04]
    volatility_impact = sum(market_volatility) * 100
    
    return optimal_inventory

# Main execution
sales_data = {
    'product_a': {'quantity': 120, 'month': 3},
    'product_b': {'quantity': 85, 'month': 3},
    'product_c': {'quantity': 200, 'month': 5},
    'product_d': {'quantity': 45, 'month': 5},
    'product_e': {'quantity': 170, 'month': 8}
}

seasonal_factors = {
    'spring': 0.8,
    'summer': 1.2,
    'fall': 0.7,
    'winter': 1.5
}

# Calculate shipping for different scenarios (distractor)
shipping_costs = []
for i in range(5):
    distance = 100 + (i * 50)
    weight = 10 + (i * 5)
    shipping_costs.append(calculate_shipping_costs(distance, weight))

# Analyze sales trends (distractor)
monthly_sales = {1: 85, 3: 120, 5: 200, 8: 170, 10: 90, 12: 150}
trend_factor = analyze_sales_trend(monthly_sales)

# Calculate the optimal inventory level
optimal_inventory = calculate_optimal_stock(sales_data, seasonal_factors)

# Apply additional adjustments (distractor)
if trend_factor > 15:
    adjusted_inventory = optimal_inventory * 1.1
else:
    adjusted_inventory = optimal_inventory * 0.95

print(f"Trend factor: {trend_factor}")
print(f"Shipping costs: {shipping_costs}")
print(f"Result: {optimal_inventory}")