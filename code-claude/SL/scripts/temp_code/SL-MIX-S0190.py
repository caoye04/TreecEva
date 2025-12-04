# Calculate optimal price for a product based on market analysis

def calculate_market_factor(competitors):
    # Calculate market factor based on competitor prices
    market_weight = sum(price for price in competitors if price > 0)
    seasonal_adjustment = 0.85 if sum(competitors) % 2 == 0 else 1.15
    return market_weight * seasonal_adjustment / len(competitors)

# Competitor prices from market research
competitor_prices = [42, 39, 45, 38, 41]

# Historical sales data [units_sold, price]
sales_history = [(120, 40), (95, 45), (150, 38), (110, 42), (105, 43)]

# Calculate average profit margin
total_profit = sum((price - 25) * units for units, price in sales_history)
total_units = sum(units for units, _ in sales_history)
average_profit_per_unit = total_profit / total_units

# Customer satisfaction scores (1-10) at different price points
satisfaction_data = {38: 9.2, 40: 8.7, 42: 7.9, 44: 7.1, 46: 6.5}

# Calculate weighted price based on sales history
weighted_price = sum(price * units for units, price in sales_history) / total_units

# Potential pricing options
potential_prices = [price for price in range(38, 47, 2)]

# Calculate market factor
market_factor = calculate_market_factor(competitor_prices)

# Analyze each potential price
price_analysis = []
for price in potential_prices:
    # Calculate expected demand
    base_demand = 100 + (40 - price) * 5
    
    # Calculate satisfaction impact (not directly used in final calculation)
    satisfaction_score = satisfaction_data.get(price, 7.0)
    customer_loyalty = satisfaction_score / 10 * 100
    
    # Calculate competitor pressure
    lower_priced_competitors = len([p for p in competitor_prices if p < price])
    competitor_pressure = lower_priced_competitors * 2.5
    
    # Adjusted demand calculation
    adjusted_demand = base_demand - competitor_pressure
    
    # Calculate expected revenue
    expected_revenue = price * adjusted_demand
    
    # Calculate expected profit
    production_cost = 25
    expected_profit = (price - production_cost) * adjusted_demand
    
    # Add to analysis with market factor adjustment
    price_analysis.append(expected_profit * market_factor / 100)

# Find the price that maximizes profit
optimal_price = max(price_analysis)

# Apply seasonal adjustment (doesn't affect optimal_price)
seasonal_demand = [demand * 1.2 for demand in [base_demand, adjusted_demand]]

print(f"Target result: {optimal_price}")