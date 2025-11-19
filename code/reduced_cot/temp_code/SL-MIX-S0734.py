class VendingMachine:
    def __init__(self):
        self.state = 'idle'
        self.balance = 0
        self.accepted_payments = frozenset(['coin', 'card', 'mobile'])
        self.discount_calculator = lambda amount, discount: amount * (1 - discount)
    
    def process_payment(self, method, amount):
        if method in self.accepted_payments:
            if method == 'coin':
                self.balance += amount
                self.state = 'paid_coins'
            elif method == 'card' or method == 'mobile':
                # Apply 5% discount for card/mobile payments
                discounted = self.discount_calculator(amount, 0.05)
                self.balance += discounted
                self.state = 'paid_card' if method == 'card' else 'paid_mobile'
        else:
            self.state = 'error'
    
    def select_item(self, price):
        if self.state.startswith('paid') and self.balance >= price:
            self.balance -= price
            self.state = 'item_dispensed'
        elif self.state.startswith('paid') and self.balance < price:
            self.state = 'insufficient_funds'
        else:
            self.state = 'error'
    
    def refund(self):
        if self.state in ['paid_coins', 'paid_card', 'paid_mobile']:
            refunded = self.balance
            self.balance = 0
            self.state = 'refunded'
            return refunded
        return 0

# Initialize machine
vm = VendingMachine()

# Customer interaction sequence
payment_methods = ['coin', 'card', 'mobile', 'cash']
amounts = [100, 200, 150, 50]
item_prices = [90, 190]

for i in range(len(payment_methods)):
    vm.process_payment(payment_methods[i], amounts[i] if i < len(amounts) else 0)
    if i < len(item_prices):
        vm.select_item(item_prices[i])

# Refund any remaining balance
vm.refund()

# Add bonus for mobile payment users
if 'mobile' in payment_methods and vm.state == 'refunded':
    vm.balance += 10

final_balance = vm.balance
print(f"Result: {final_balance}")