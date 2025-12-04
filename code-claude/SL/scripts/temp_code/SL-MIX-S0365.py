# Stock portfolio analysis

# Initial portfolio with stock symbols and (price, shares) tuples
portfolio = {
    'AAPL': (187.50, 15),
    'MSFT': (403.78, 8),
    'GOOGL': (174.12, 12),
    'AMZN': (178.75, 10),
    'NVDA': (950.02, 5)
}

# Historical performance metrics (not used in final calculation)
historical_data = {
    'AAPL': [0.12, 0.08, 0.15],  # Annual returns for past 3 years
    'MSFT': [0.25, 0.18, 0.22],
    'GOOGL': [0.10, 0.05, 0.08],
    'AMZN': [0.20, 0.15, 0.18],
    'NVDA': [0.45, 0.50, 0.60]
}

# Calculate average annual returns (distractor)
avg_returns = {stock: sum(returns)/len(returns) for stock, returns in historical_data.items()}

# Identify potential stocks to sell based on arbitrary criteria
low_performing = [stock for stock, avg in avg_returns.items() if avg < 0.15]

# Risk assessment (distractor)
risk_levels = {'AAPL': 'low', 'MSFT': 'medium', 'GOOGL': 'medium', 
               'AMZN': 'high', 'NVDA': 'high'}

# Sector diversification check (distractor)
sectors = {'AAPL': 'Tech', 'MSFT': 'Tech', 'GOOGL': 'Tech', 
          'AMZN': 'Consumer', 'NVDA': 'Tech'}
sector_count = {sector: list(sectors.values()).count(sector) for sector in set(sectors.values())}

# Stocks to exclude from valuation based on sector overexposure
excluded_stocks = ['GOOGL'] if sector_count['Tech'] > 3 else []

# Calculate total market value of portfolio excluding specified stocks
total_market_value = sum([price * shares for stock, (price, shares) in portfolio.items() if stock not in excluded_stocks])

# Calculate unrealized gains based on purchase prices (distractor)
purchase_prices = {'AAPL': 150.00, 'MSFT': 300.25, 'GOOGL': 150.50, 'AMZN': 140.30, 'NVDA': 500.75}
unrealized_gains = sum([(portfolio[stock][0] - purchase_prices[stock]) * portfolio[stock][1] 
                       for stock in portfolio if stock not in low_performing])

# Display results
print(f"Portfolio diversification: {sector_count}")
print(f"Low performing stocks: {low_performing}")
print(f"Result: {total_market_value}")