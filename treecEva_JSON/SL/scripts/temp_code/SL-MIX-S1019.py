from collections import deque
import math

def calculate_exchange_profit(initial_balance, transaction_log):
    portfolio = initial_balance
    pending_trades = deque()
    reversed_trades = []
    
    # Process transaction log
    for entry in transaction_log:
        if entry['type'] == 'buy':
            cost = entry['amount'] * entry['rate']
            if portfolio >= cost:
                portfolio -= cost
                pending_trades.append(entry)
        elif entry['type'] == 'sell':
            if pending_trades and pending_trades[-1]['currency'] == entry['currency']:
                trade = pending_trades.pop()
                profit = entry['amount'] * entry['rate'] - trade['amount'] * trade['rate']
                portfolio += profit + trade['amount'] * trade['rate']
    
    # Reverse failed trades using stack
    while pending_trades:
        failed_trade = pending_trades.popleft()
        reversal_cost = failed_trade['amount'] * failed_trade['rate']
        if portfolio >= reversal_cost * 0.1:  # 10% penalty
            portfolio -= reversal_cost * 0.1
            reversed_trades.append(failed_trade)
    
    return portfolio

# Financial data
initial_funds = 10000
exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}

# Transaction log with complex calculations
transactions = [
    {'type': 'buy', 'currency': 'EUR', 'amount': 5000, 'rate': exchange_rates['EUR']},
    {'type': 'buy', 'currency': 'GBP', 'amount': 3000, 'rate': exchange_rates['GBP']},
    {'type': 'sell', 'currency': 'EUR', 'amount': 5000, 'rate': exchange_rates['EUR'] * 1.02},
    {'type': 'buy', 'currency': 'JPY', 'amount': 100000, 'rate': exchange_rates['JPY']},
    {'type': 'sell', 'currency': 'GBP', 'amount': 3000, 'rate': exchange_rates['GBP'] * 0.98}
]

# Calculate final portfolio value
final_portfolio_value = calculate_exchange_profit(initial_funds, transactions)
print(f"Result: {math.floor(final_portfolio_value)}")