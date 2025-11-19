import re
from collections import deque

def calculate_exchange_fees(amount, tier):
    fees = {1: 0.02, 2: 0.015, 3: 0.01}
    return amount * fees.get(tier, 0.005)

class CurrencyPortfolio:
    def __init__(self):
        self.balances = {'USD': 10000, 'EUR': 5000, 'GBP': 3000}
        self.transaction_stack = []
        self.exchange_history = []
    
    def is_valid_currency(self, code):
        return bool(re.match(r'^[A-Z]{3}$', code))
    
    def execute_hedge_strategy(self):
        # Process transactions using greedy approach for cost minimization
        pending_transactions = [
            ('USD', 'EUR', 2000, 2),
            ('EUR', 'GBP', 1500, 1),
            ('GBP', 'USD', 1000, 3),
            ('USD', 'GBP', 3000, 2)
        ]
        
        # Stack-based transaction management
        for from_curr, to_curr, amount, tier in pending_transactions:
            if self.is_valid_currency(from_curr) and self.is_valid_currency(to_curr):
                fee = calculate_exchange_fees(amount, tier)
                net_amount = amount - fee
                self.transaction_stack.append((from_curr, to_curr, net_amount))
        
        # Dynamic programming approach for optimal conversion rates
        conversion_rates = {
            ('USD', 'EUR'): 0.85,
            ('EUR', 'GBP'): 0.88,
            ('GBP', 'USD'): 1.35,
            ('USD', 'GBP'): 0.75
        }
        
        # Process stack with optimized conversions
        while self.transaction_stack:
            from_curr, to_curr, net_amount = self.transaction_stack.pop()
            rate = conversion_rates.get((from_curr, to_curr), 1.0)
            converted_value = net_amount * rate
            
            # Update balances
            self.balances[from_curr] -= net_amount
            self.balances[to_curr] += converted_value
            self.exchange_history.append((from_curr, to_curr, net_amount, converted_value))
        
        # Apply final portfolio optimization using array operations
        currency_weights = [0.4, 0.35, 0.25]  # USD, EUR, GBP target weights
        current_total = sum(self.balances.values())
        target_values = [current_total * w for w in currency_weights]
        
        # Calculate adjustment needed for each currency
        adjustments = [
            target_values[i] - list(self.balances.values())[i] 
            for i in range(len(target_values))
        ]
        
        # Apply adjustments with greedy rebalancing
        for i, (currency, balance) in enumerate(self.balances.items()):
            self.balances[currency] += adjustments[i]
        
        return sum(self.balances.values())

# Execute the financial hedging strategy
portfolio = CurrencyPortfolio()
final_portfolio_value = portfolio.execute_hedge_strategy()
print(f"Result: {int(final_portfolio_value)}")