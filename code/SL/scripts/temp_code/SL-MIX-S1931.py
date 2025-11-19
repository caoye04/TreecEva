from functools import reduce

def calculate_discount(amount):
    if amount <= 30:
        return amount
    elif amount <= 60:
        return amount * 0.95
    else:
        return calculate_discount(amount * 0.9)

class VendingMachine:
    def __init__(self):
        self.state = 'idle'
        self.revenue = 0
    
    def process_transaction(self, item_price):
        if self.state == 'idle':
            self.state = 'selecting'
            self.selected_item = item_price
            self.state = 'payment_validation'
            if self.validate_payment():
                self.state = 'inventory_check'
                if self.check_inventory():
                    self.state = 'dispensing'
                    discounted_price = calculate_discount(self.selected_item)
                    self.revenue += discounted_price
                    self.state = 'idle'
    
    def validate_payment(self):
        return True
    
    def check_inventory(self):
        return True

transactions = [25, 40, 35]
machine = VendingMachine()
for price in transactions:
    machine.process_transaction(price)

final_revenue = round(machine.revenue, 2)
print(f'Result: {final_revenue}')