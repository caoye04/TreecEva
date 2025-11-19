class VendingMachine:
    def __init__(self):
        self.inventory = {'cola': 5, 'chips': 3, 'candy': 8}
        self.prices = {'cola': 125, 'chips': 100, 'candy': 75}
        self.denominations = [100, 25, 10, 5]
        self.total_revenue = 0
        
    def process_payment(self, item, payment):
        if item in self.inventory and self.inventory[item] > 0 and payment >= self.prices[item]:
            self.inventory[item] -= 1
            change_due = payment - self.prices[item]
            self.total_revenue += self.prices[item]
            
            # Greedy algorithm for making change
            change_breakdown = {}
            for denom in self.denominations:
                count = change_due // denom
                if count > 0:
                    change_breakdown[denom] = count
                    change_due -= count * denom
            
            return True
        return False

# State machine for transaction processing
transaction_states = [
    ('cola', 200),
    ('chips', 100),
    ('candy', 100),
    ('cola', 150),
    ('invalid_item', 100),
    ('candy', 50),
    ('chips', 125)
]

vm = VendingMachine()
for item, payment in transaction_states:
    vm.process_payment(item, payment)

# Additional revenue calculation using lambda
bonus_func = lambda sales: sales * 0.1 if sales > 500 else sales * 0.05
bonus_revenue = bonus_func(vm.total_revenue)

# Context manager for logging final revenue
class RevenueLogger:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def get_final_revenue(self, base, bonus):
        return base + bonus

with RevenueLogger() as logger:
    final_revenue = logger.get_final_revenue(vm.total_revenue, bonus_revenue)

print(f"Result: {final_revenue}")