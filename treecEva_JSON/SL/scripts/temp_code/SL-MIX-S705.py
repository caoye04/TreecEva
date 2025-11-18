from collections import defaultdict

class VendingMachine:
    def __init__(self):
        self.inventory = defaultdict(lambda: {'stock': 5, 'base_price': 0})
        self.total_revenue = 0
        self.state = 'READY'
    
    def set_pricing(self, item, price):
        self.inventory[item]['base_price'] = price
    
    def get_price(self, item):
        stock = self.inventory[item]['stock']
        base = self.inventory[item]['base_price']
        return int(base * 1.1) if stock < 3 else base
    
    def process_order(self, item, payment, change_denom):
        if self.state != 'READY':
            return False
        
        if self.inventory[item]['stock'] <= 0:
            return False
            
        price = self.get_price(item)
        if payment < price:
            return False
            
        change_needed = payment - price
        if change_needed == 0:
            self.inventory[item]['stock'] -= 1
            self.total_revenue += price
            return True
            
        # Greedy change making
        change_denom.sort(reverse=True)
        change_given = 0
        temp_denom = change_denom[:]
        
        for coin in change_denom:
            while change_needed >= coin and coin in temp_denom:
                change_needed -= coin
                temp_denom.remove(coin)
                change_given += coin
                if change_needed == 0:
                    break
            if change_needed == 0:
                break
                
        if change_needed != 0:
            return False  # Cannot make exact change
            
        # Transaction successful
        self.inventory[item]['stock'] -= 1
        self.total_revenue += price
        return True

vm = VendingMachine()
vm.set_pricing('SODA', 12)
vm.set_pricing('CHIPS', 8)
vm.set_pricing('CANDY', 5)

orders = [
    ('SODA', 12, [1]*12),
    ('CHIPS', 10, [5, 5]),
    ('CANDY', 5, []),
    ('SODA', 15, [5, 5, 5]),  # Should fail - cannot make change
    ('CHIPS', 8, [5, 1, 1, 1]),
    ('CANDY', 6, [5, 1]),
    ('SODA', 13, [10, 1, 1, 1])
]

for item, payment, change in orders:
    vm.process_order(item, payment, change)
    
# What is the total revenue after all transactions?
print(f"Result: {vm.total_revenue}")