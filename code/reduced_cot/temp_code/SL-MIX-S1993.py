from dataclasses import dataclass
from typing import List

@dataclass
class VendingItem:
    name: str
    quantity: int
    popularity_score: float

    def __lt__(self, other):
        return self.popularity_score < other.popularity_score

class VendingMachineState:
    RESTOCKING = 'RESTOCKING'
    AVAILABLE = 'AVAILABLE'
    MAINTENANCE = 'MAINTENANCE'

class VendingMachine:
    def __init__(self):
        self.state = VendingMachineState.AVAILABLE
        self.inventory: List[VendingItem] = []
        self.restock_operations = 0
    
    def add_items(self, items: List[VendingItem]):
        self.inventory.extend(items)
    
    def process_operations(self, operations: List[str]) -> int:
        restock_count = 0
        for op in operations:
            if op == 'RESTOCK' and self.state == VendingMachineState.AVAILABLE:
                self.state = VendingMachineState.RESTOCKING
                # Sort items by popularity (divide and conquer approach with merge sort via sorted())
                self.inventory = sorted(self.inventory, reverse=True)
                # Restock logic
                for i in range(len(self.inventory)):
                    item = self.inventory[i]
                    if item.quantity < 10:  # Threshold for restocking
                        old_quantity = item.quantity
                        item.quantity = min(20, item.quantity + 15)
                        if item.quantity != old_quantity:
                            restock_count += 1
                self.state = VendingMachineState.AVAILABLE
            elif op == 'MAINTENANCE':
                self.state = VendingMachineState.MAINTENANCE
                # During maintenance, we might reorder based on a different criterion
                self.inventory.sort(key=lambda x: x.name)
                self.state = VendingMachineState.AVAILABLE
        return restock_count

# Initialize vending machine
vm = VendingMachine()

# Add initial inventory
initial_inventory = [
    VendingItem('CHIPS', 3, 0.75),
    VendingItem('COOKIE', 12, 0.85),
    VendingItem('SODA', 8, 0.92),
    VendingItem('CANDY', 15, 0.65),
    VendingItem('NUTS', 2, 0.55)
]
vm.add_items(initial_inventory)

# Process operations
operations_log = ['RESTOCK', 'MAINTENANCE', 'RESTOCK']
final_restock_count = vm.process_operations(operations_log)

print(f'Result: {final_restock_count}')