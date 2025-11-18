from dataclasses import dataclass
from typing import Dict

def process_sales():
    @dataclass
    class VendingMachine:
        inventory: Dict[str, int]
        prices: Dict[str, float]
        revenue: float = 0.0
        
        def sell(self, item: str, quantity: int):
            if self.inventory.get(item, 0) >= quantity:
                self.inventory[item] -= quantity
                self.revenue += self.prices[item] * quantity
            else:
                raise ValueError(f"Not enough {item} in stock")
    
    # Initialize vending machine with inventory and prices
    vm = VendingMachine(
        inventory={'soda': 20, 'chips': 15, 'candy': 30},
        prices={'soda': 1.50, 'chips': 1.00, 'candy': 0.75}
    )
    
    # Sales log: list of (item, quantity) tuples
    sales_log = [
        ('soda', 3),
        ('chips', 5),
        ('candy', 8),
        ('soda', 2),
        ('chips', 3)
    ]
    
    # Process each sale
    for item, qty in sales_log:
        with open('temp_log.txt', 'a') as f:
            f.write(f'Selling {qty} of {item}\n')
        vm.sell(item, qty)
    
    # Calculate bonus revenue from high-demand items
    bonus = sum(
        map(lambda x: x * 0.1 if x > 2 else 0, 
            [vm.prices['soda'], vm.prices['chips'], vm.prices['candy']])
    )
    
    # Add bonus to total revenue
    total_revenue = vm.revenue + bonus
    
    return total_revenue

# Execute the sales processing
final_revenue = process_sales()
print(f'Result: {final_revenue}')