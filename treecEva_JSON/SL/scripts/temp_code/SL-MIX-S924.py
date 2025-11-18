from collections import defaultdict
import bisect

def calculate_restock_priority(slot_id, current_stock, max_capacity, popularity):
    base_priority = (max_capacity - current_stock) * popularity
    return base_priority + (slot_id % 3)  # Add cyclic bonus

class VendingMachine:
    def __init__(self):
        self.inventory = defaultdict(lambda: {'stock': 0, 'capacity': 10, 'popularity': 0})
        self.restock_queue = []
        self.optimization_score = 0
    
    def add_item(self, slot_id, initial_stock, capacity, popularity):
        self.inventory[slot_id]['stock'] = initial_stock
        self.inventory[slot_id]['capacity'] = capacity
        self.inventory[slot_id]['popularity'] = popularity
        priority = calculate_restock_priority(slot_id, initial_stock, capacity, popularity)
        bisect.insort(self.restock_queue, (-priority, slot_id))  # Max-heap simulation
    
    def process_restock_events(self, events):
        dp_table = [0] * (len(events) + 1)
        
        for i, (event_type, slot_id, quantity) in enumerate(events):
            if event_type == 'RESTOCK':
                item = self.inventory[slot_id]
                item['stock'] = min(item['stock'] + quantity, item['capacity'])
                
                # Update optimization score with dynamic programming
                restock_impact = quantity * item['popularity']
                dp_table[i+1] = max(dp_table[i], dp_table[i-1] if i > 0 else 0) + restock_impact
                
                # Apply state transition penalty
                if item['stock'] >= item['capacity'] * 0.9:
                    self.optimization_score += dp_table[i+1] // 2
                else:
                    self.optimization_score += dp_table[i+1]
            elif event_type == 'DISPENSE':
                item = self.inventory[slot_id]
                item['stock'] = max(0, item['stock'] - quantity)
                # No change to optimization score for dispensing
                dp_table[i+1] = dp_table[i]
        
        return self.optimization_score

# Initialize vending machine
vm = VendingMachine()

# Add items to inventory
vm.add_item(101, 3, 15, 8)   # Slot 101: Candy Bars
vm.add_item(205, 7, 20, 5)   # Slot 205: Chips
vm.add_item(309, 12, 12, 10) # Slot 309: Soda (already full)
vm.add_item(412, 0, 10, 7)   # Slot 412: Cookies (empty)

# Process restocking events
restock_events = [
    ('RESTOCK', 101, 5),   # Restock candy bars
    ('DISPENSE', 205, 3),  # Dispense chips
    ('RESTOCK', 412, 8),   # Restock cookies
    ('RESTOCK', 101, 4),   # Additional candy bar restock
    ('DISPENSE', 412, 2),  # Dispense some cookies
    ('RESTOCK', 205, 10)   # Restock chips
]

optimization_score = vm.process_restock_events(restock_events)
print(f"Result: {optimization_score}")