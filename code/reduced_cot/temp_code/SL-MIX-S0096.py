from functools import reduce
from contextlib import contextmanager

class PortfolioManager:
    def __init__(self):
        self.portfolio_value = 1000.0
        self.risk_multiplier = 1.05
        self.transaction_log = []
    
    def apply_market_condition(self, condition_factor):
        self.portfolio_value *= condition_factor
        return self.portfolio_value
    
    def log_transaction(self, amount):
        self.transaction_log.append(amount)
    
    @contextmanager
    def risk_adjustment_context(self, risk_factor):
        old_multiplier = self.risk_multiplier
        self.risk_multiplier *= risk_factor
        try:
            yield
        finally:
            self.risk_multiplier = old_multiplier

# Initialize portfolio
portfolio = PortfolioManager()

# Market data hash table
market_conditions = {
    'bull': 1.12,
    'bear': 0.92,
    'neutral': 1.01
}

# Tokenized transaction rules
transaction_rules = "ADD:500.0;APPLY:bull;ADD:200.0;APPLY:risk_context_1.2;ADD:300.0"

# Parse and process transactions
tokens = transaction_rules.split(';')

for token in tokens:
    operation, value = token.split(':')
    if operation == 'ADD':
        adjustment = float(value)
        portfolio.portfolio_value += adjustment
        portfolio.log_transaction(adjustment)
    elif operation == 'APPLY':
        if value.startswith('risk_context_'):
            factor = float(value.split('_')[2])
            with portfolio.risk_adjustment_context(factor):
                portfolio.portfolio_value = portfolio.apply_market_condition(market_conditions['bull'])
        else:
            factor = market_conditions[value]
            portfolio.portfolio_value = portfolio.apply_market_condition(factor)

# Final adjustment with risk multiplier
final_portfolio_value = portfolio.portfolio_value * portfolio.risk_multiplier

print(f"Result: {final_portfolio_value}")