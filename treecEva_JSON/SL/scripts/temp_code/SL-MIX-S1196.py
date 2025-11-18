from functools import reduce
from collections import namedtuple

# Define a Stock data structure
Stock = namedtuple('Stock', ['ticker', 'return_rate', 'risk_factor'])

# Portfolio of stocks
portfolio = [
    Stock('AAPL', 0.05, 0.1),
    Stock('GOOGL', 0.07, 0.15),
    Stock('MSFT', 0.06, 0.12),
    Stock('AMZN', 0.08, 0.18)
]

def calculate_sharpe(stock):
    return stock.return_rate / stock.risk_factor if stock.risk_factor != 0 else 0

def greedy_portfolio_selection(stocks):
    # Sort stocks by Sharpe ratio in descending order
    sorted_stocks = sorted(stocks, key=calculate_sharpe, reverse=True)
    
    # Select top stocks using a greedy approach until total risk <= 0.3
    selected_stocks = []
    total_risk = 0.0
    
    for stock in sorted_stocks:
        temp_risk = total_risk + stock.risk_factor
        total_risk = temp_risk if temp_risk <= 0.3 else total_risk
        selected_stocks.append(stock) if temp_risk <= 0.3 else None
    
    # Calculate combined Sharpe ratio of selected stocks
    total_return = sum(s.return_rate for s in selected_stocks)
    total_risk = sum(s.risk_factor for s in selected_stocks)
    
    # Ternary operator to handle zero risk case
    return total_return / total_risk if total_risk > 0 else 0

# Compute optimal Sharpe ratio using greedy selection
optimal_sharpe_ratio = greedy_portfolio_selection(portfolio)
print(f'Result: {optimal_sharpe_ratio}')