from collections import defaultdict
from functools import reduce

def calculate_change(price, payment, discount):
    effective_price = price * (1 - discount)
    return payment - effective_price

class VendingMachine:
    def __init__(self):
        self.state = 'IDLE'
        self.transaction_log = []
        self.total_revenue = 0.0
    
    def process_transaction(self, item_price, coins_inserted, customer_tier):
        if self.state == 'IDLE':
            self.state = 'PROCESSING'
            # Discount based on customer tier
            discounts = {'bronze': 0.05, 'silver': 0.10, 'gold': 0.15}
            discount_rate = discounts.get(customer_tier, 0.0)
            
            # Calculate payment from coins
            coin_values = [0.01, 0.05, 0.10, 0.25]  # penny, nickel, dime, quarter
            payment = sum(c * v for c, v in zip(coins_inserted, coin_values))
            
            # Calculate change
            change = calculate_change(item_price, payment, discount_rate)
            
            # State transition based on change
            if change >= 0:
                self.state = 'DISPENSING'
                revenue = item_price * (1 - discount_rate)
                self.total_revenue += revenue
                self.transaction_log.append({
                    'price': item_price,
                    'payment': payment,
                    'change': change,
                    'revenue': revenue
                })
            else:
                self.state = 'INSUFFICIENT_FUNDS'
            
            # Reset to IDLE
            final_state = self.state
            self.state = 'IDLE'
            return final_state

# Initialize vending machine
vm = VendingMachine()

# Transaction data: (item_price, coins_inserted, customer_tier)
transactions = [
    (2.50, [0, 2, 1, 9], 'silver'),    # 2 nickels, 1 dime, 9 quarters
    (1.75, [0, 0, 5, 5], 'bronze'),    # 5 dimes, 5 quarters
    (3.00, [0, 1, 2, 10], 'gold'),     # 1 nickel, 2 dimes, 10 quarters
    (2.25, [0, 0, 7, 6], 'none'),      # 7 dimes, 6 quarters
    (1.50, [0, 3, 0, 5], 'silver')     # 3 nickels, 5 quarters
]

# Process all transactions
for t in transactions:
    vm.process_transaction(*t)

# Calculate final result using functional approach
revenue_components = [t['revenue'] for t in vm.transaction_log]
total_revenue = reduce(lambda x, y: x + y, revenue_components, 0.0)

print(f"Result: {total_revenue}")