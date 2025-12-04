def portfolio_manager(transactions):
    # Distractor: irrelevant financial calculations
    market_volatility = 0.15
    risk_adjustment = 1.25
    commission_rate = 0.02
    
    # Main logic - tracking stock portfolio
    stock_prices = {'AAPL': 150, 'GOOGL': 2800, 'MSFT': 330, 'TSLA': 220}
    initial_positions = {'AAPL': 100, 'GOOGL': 50, 'MSFT': 75, 'TSLA': 200}
    
    # Red herring: unused calculations
    portfolio_value_initial = sum(stock_prices[sym] * qty for sym, qty in initial_positions.items())
    avg_price = portfolio_value_initial / sum(initial_positions.values())
    
    # Process transactions
    transaction_log = [('AAPL', 25, 'BUY'), ('GOOGL', 10, 'SELL'), ('MSFT', 30, 'BUY'), ('TSLA', 50, 'SELL')]
    current_positions = initial_positions.copy()
    cash_balance = 100000  # Starting cash
    
    # Misleading intermediate calculation
    total_commission_paid = len(transaction_log) * commission_rate * 1000
    
    for symbol, quantity, action in transaction_log:
        price = stock_prices[symbol]
        if action == 'BUY':
            cost = quantity * price
            cash_balance -= cost
            current_positions[symbol] += quantity
            # Dead code path
            if cash_balance < 0:
                print("Margin call!")
        elif action == 'SELL':
            proceeds = quantity * price
            cash_balance += proceeds
            current_positions[symbol] -= quantity
    
    # Final portfolio value calculation
    final_value = sum(stock_prices[sym] * qty for sym, qty in current_positions.items())
    final_balance = cash_balance + final_value
    
    # More distractions
    portfolio_return = (final_balance - 100000) / 100000
    risk_adjusted_return = portfolio_return * risk_adjustment
    
    print(f"Result: {final_balance}")
    return final_balance

# Execute the main function
transaction_log = [('AAPL', 25, 'BUY'), ('GOOGL', 10, 'SELL'), ('MSFT', 30, 'BUY'), ('TSLA', 50, 'SELL')]
final_balance = portfolio_manager(transaction_log)