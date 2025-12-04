def calculate_profit(investments, price_changes):
    # Track potential investments for different currencies
    potential_gains = {'BTC': 0, 'ETH': 0, 'ADA': 0, 'XRP': 0}
    market_trends = [0.05, -0.02, 0.08, -0.03, 0.06]
    
    # Calculate market sentiment (unused in actual calculation)
    sentiment = sum(market_trends) / len(market_trends)
    
    # Process investment history and price changes
    total_investment = 0
    actual_returns = 0
    
    # Track investments by currency type (distractor)
    currency_distribution = {}
    for currency, amount in investments.items():
        currency_distribution[currency] = currency_distribution.get(currency, 0) + amount
        
    # Calculate potential ROI for each currency (distractor)
    for currency in potential_gains:
        potential_roi = (price_changes.get(currency, 0) - sentiment) * 100
        potential_gains[currency] = potential_roi
    
    # Calculate weighted average of price changes (distractor)
    weights = [0.3, 0.25, 0.2, 0.15, 0.1]
    weighted_changes = 0
    for i, currency in enumerate(['BTC', 'ETH', 'ADA', 'XRP', 'DOGE'][:len(weights)]):
        if currency in price_changes:
            weighted_changes += price_changes[currency] * weights[i]
    
    # Actually calculate profit
    for currency, amount in investments.items():
        if currency in price_changes:
            total_investment += amount
            actual_returns += amount * (1 + price_changes[currency])
    
    # Calculate risk-adjusted returns (distractor)
    risk_factors = {'BTC': 0.8, 'ETH': 0.7, 'ADA': 0.6, 'XRP': 0.9}
    risk_adjusted = 0
    for currency, factor in risk_factors.items():
        if currency in investments and currency in price_changes:
            risk_adjusted += investments[currency] * price_changes[currency] * factor
    
    # Return actual profit
    return round(actual_returns - total_investment, 2)

# Investment history: currency -> amount invested
investment_history = {
    'BTC': 1000,
    'ETH': 1500,
    'ADA': 800,
    'XRP': 400
}

# Recent price changes as decimal (1.0 = no change)
price_changes = {
    'BTC': 0.15,   # 15% increase
    'ETH': -0.05,  # 5% decrease
    'ADA': 0.20,   # 20% increase
    'DOGE': 0.30,  # 30% increase (distractor - not in our portfolio)
    'XRP': -0.10   # 10% decrease
}

# Calculate diversification score (distractor)
portfolio_sum = sum(investment_history.values())
diversification = sum((amt/portfolio_sum)**2 for amt in investment_history.values())
diversification_score = (1 - diversification) * 100

# Process some data with enumerate and zip (distractor)
currency_tiers = ['premium', 'standard', 'basic', 'risky']
tier_bonuses = [0.05, 0.03, 0.02, 0.01]

bonus_map = {}
for i, (tier, bonus) in enumerate(zip(currency_tiers, tier_bonuses)):
    bonus_map[tier] = bonus * (i + 1)

# Apply some conditional logic with slicing (distractor)
sorted_investments = sorted(investment_history.items(), key=lambda x: x[1], reverse=True)
top_currencies = [c for c, _ in sorted_investments[:2]]
if 'BTC' in top_currencies and 'ETH' in top_currencies:
    loyalty_bonus = 25
else:
    loyalty_bonus = 10

# Calculate profit
crypto_profit = calculate_profit(investment_history, price_changes)

# Apply some tuples and conditionals (distractor)
fee_structure = [(1000, 0.01), (2000, 0.008), (3000, 0.006), (5000, 0.004)]
fee_rate = 0.012  # default
for threshold, rate in fee_structure:
    if portfolio_sum >= threshold:
        fee_rate = rate

# Final adjustments (distractor)
if diversification_score > 70:
    adjusted_profit = crypto_profit * 1.02
else:
    adjusted_profit = crypto_profit

print(f"Result: {crypto_profit}")