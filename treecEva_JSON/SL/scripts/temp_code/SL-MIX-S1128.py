import math
from collections import defaultdict

class TransactionLogProcessor:
    def __init__(self, log_data):
        self.log_data = log_data
        self.transaction_values = []
    
    def __enter__(self):
        # Tokenize log data and extract transaction values
        for line in self.log_data.split('\n'):
            if line.strip():
                tokens = line.split('|')
                value_token = tokens[2] if len(tokens) > 2 else '0'
                try:
                    value = float(value_token.strip())
                    self.transaction_values.append(value)
                except ValueError:
                    pass
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def calculate_volatility(values):
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / (len(values) - 1)
    return math.sqrt(variance)

def risk_adjusted_return(returns, volatility):
    return returns / (1 + volatility) if volatility > 0 else returns

# Simulated transaction log data
log_content = """TXN001|BUY|1250.75|AAPL
TXN002|SELL|875.50|GOOGL
TXN003|BUY|2100.00|MSFT
TXN004|DIVIDEND|50.25|AAPL
TXN005|SELL|1750.30|AMZN
TXN006|FEE|-15.75|BROKERAGE
TXN007|BUY|950.80|TSLA"""

base_return = 0.0
volatility_factor = 0.0
adjusted_return = 0.0

with TransactionLogProcessor(log_content) as processor:
    # Calculate base return as net sum of transactions
    base_return = sum(processor.transaction_values)
    
    # Calculate volatility of positive transactions only
    positive_transactions = [v for v in processor.transaction_values if v > 0]
    volatility_factor = calculate_volatility(positive_transactions)
    
    # Apply risk adjustment
    adjusted_return = risk_adjusted_return(base_return, volatility_factor)
    
    # Apply additional adjustment based on transaction count
    transaction_bonus = 0.02 if len(processor.transaction_values) > 5 else 0.0
    adjusted_return = adjusted_return * (1 + transaction_bonus) if transaction_bonus > 0 else adjusted_return

# Final adjustment using ternary operator
adjusted_return = adjusted_return if adjusted_return > 0 else abs(adjusted_return) * 0.5

print(f"Result: {adjusted_return}")