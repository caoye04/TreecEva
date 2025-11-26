from collections import defaultdict

def portfolio_calculation(trades, capital):
    # Irrelevant tracking variables
    total_trades = len(trades)
    trade_count = defaultdict(int)
    
    # Misleading intermediate calculations
    volume_sum = sum(abs(amt) for _, amt in trades)
    temp_multiplier = (volume_sum % 17) + 3
    
    # Dead code path
    if volume_sum > 10000:
        bonus = capital * 0.1  # Never executed
    
    # Main logic with distractions
    balance = capital
    for symbol, amount in trades:
        trade_count[symbol] += 1
        
        # Distractor operations
        symbol_hash = sum(ord(c) for c in symbol) % 13
        
        # Actual balance calculation
        if amount > 0:
            balance += amount * (1 - 0.02)  # 2% fee on buys
        else:
            balance += amount * (1 + 0.01)  # 1% fee on sells
        
        # More irrelevant computations
        balance_check = balance * (symbol_hash / 100.0)
    
    # Final adjustments with red herrings
    fee_adjustment = len([amt for _, amt in trades if amt > 0]) * 5
    final_balance = balance - fee_adjustment + (temp_multiplier % 7)
    
    # Unused lambda function
    calc_bonus = lambda x: x * 0.05
    
    # Print the target result
    print(f"Result: {final_balance}")
    return final_balance

# Transaction data
initial_capital = 10000
transactions = [
    ("AAPL", 1500),
    ("MSFT", -800),
    ("GOOGL", 1200),
    ("AAPL", -600),
    ("TSLA", 900)
]

# Execute the key statement
final_balance = portfolio_calculation(transactions, initial_capital)