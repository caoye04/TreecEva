def portfolio_calculations(holdings, prices, dividend_rate):
    # Calculate total market value
    market_value = sum(holdings[symbol] * prices[symbol] for symbol in holdings)
    
    # Calculate dividend income (distraction - not used in final result)
    dividend_income = sum(holdings[symbol] * prices[symbol] * dividend_rate for symbol in holdings)
    
    # Calculate weighted average price (distraction - calculated but not used)
    total_shares = sum(holdings.values())
    weighted_price = sum(holdings[symbol] * prices[symbol] for symbol in holdings) / total_shares
    
    # Calculate portfolio adjustments
    adjustment_factor = 0.85
    adjusted_value = market_value * adjustment_factor
    
    # Apply management fee
    management_fee = adjusted_value * 0.02
    
    # Final balance after fees
    final_balance = adjusted_value - management_fee
    return final_balance

# Portfolio data
holdings = {'AAPL': 50, 'GOOGL': 30, 'MSFT': 25}
market_prices = {'AAPL': 150.0, 'GOOGL': 2800.0, 'MSFT': 340.0}
dividend_yield = 0.015

# Execute the calculation
final_balance = portfolio_calculations(holdings, market_prices, dividend_yield)
print(f"Result: {final_balance}")