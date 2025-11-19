import statistics

def calculate_portfolio_adjustment(daily_changes):
    volatility_window = []
    portfolio_adjustment = 0
    weight_factor = 1.5
    
    for idx, change in enumerate(daily_changes):
        # Update rolling window
        volatility_window.append(abs(change))
        if len(volatility_window) > 3:
            volatility_window.pop(0)
        
        # Calculate current volatility (mean of absolute changes)
        current_volatility = statistics.mean(volatility_window) if volatility_window else 0
        
        # Greedy adjustment based on volatility thresholds
        if current_volatility > 2.0 and len(volatility_window) == 3:
            adjustment = round(weight_factor * max(volatility_window), 2)
            portfolio_adjustment += adjustment
        elif current_volatility <= 2.0 and current_volatility > 0:
            adjustment = round(weight_factor * min(volatility_window), 2)
            portfolio_adjustment -= adjustment
        
        # Short-circuit evaluation for emergency exit condition
        if change < -5.0 and current_volatility > 3.0:
            portfolio_adjustment *= 2 if portfolio_adjustment > 0 else 1
    
    return portfolio_adjustment

# Market data representing daily percentage changes
market_data = [1.2, -2.5, 3.1, -4.2, 2.8, -1.9, 5.5, -3.3, 0.7]
portfolio_adjustment = calculate_portfolio_adjustment(market_data)
print(f"Result: {portfolio_adjustment}")