class VendingMachine:
    def __init__(self):
        self.inventory = {
            'chips': {'count': 5, 'value': 2},
            'candy': {'count': 2, 'value': 1},
            'soda': {'count': 8, 'value': 3},
            'nuts': {'count': 1, 'value': 4}
        }
        self.state = 'NORMAL'
        self.restock_quota = 15
        
    def update_state(self):
        if any(item['count'] == 0 for item in self.inventory.values()):
            self.state = 'OUT_OF_ORDER'
        elif any(item['count'] < 3 for item in self.inventory.values()):
            self.state = 'LOW_STOCK'
        else:
            self.state = 'NORMAL'
        
    def process_purchases(self, purchases):
        for item, quantity in purchases.items():
            if item in self.inventory and self.inventory[item]['count'] >= quantity:
                self.inventory[item]['count'] -= quantity
        self.update_state()
    
    def restock_greedy(self):
        # Greedy algorithm: prioritize items with lowest stock first
        items_sorted = sorted(self.inventory.items(), key=lambda x: x[1]['count'])
        restock_priority_score = 0
        remaining_quota = self.restock_quota
        
        for item_name, item_data in items_sorted:
            if remaining_quota <= 0:
                break
            needed = max(0, 10 - item_data['count'])  # Target stock level is 10
            restock_amount = min(needed, remaining_quota)
            
            if restock_amount > 0:
                self.inventory[item_name]['count'] += restock_amount
                restock_priority_score += restock_amount * item_data['value']
                remaining_quota -= restock_amount
        
        self.update_state()
        return restock_priority_score

# Execution sequence
vm = VendingMachine()
purchase_list = {'chips': 3, 'candy': 1, 'soda': 6, 'nuts': 1}
vm.process_purchases(purchase_list)

# Apply greedy restocking algorithm only if machine is not OUT_OF_ORDER
restock_priority_score = 0
if vm.state != 'OUT_OF_ORDER':
    restock_priority_score = vm.restock_greedy()

print(f'Result: {restock_priority_score}')