from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Product:
    code: str
    price: int
    quantity: int

def process_vending_requests(products: Dict[str, Product], requests: List[str]) -> int:
    # State machine states
    STATE_READY = 'ready'
    STATE_PROCESSING = 'processing'
    STATE_OUT_OF_STOCK = 'out_of_stock'
    
    state = STATE_READY
    total_revenue = 0
    
    for request in requests:
        # Ternary operator to determine if request is valid
        is_valid_request = True if len(request) == 3 and request.isalnum() else False
        
        if not is_valid_request:
            continue
            
        state = STATE_PROCESSING
        
        # Greedy algorithm: find cheapest available product with matching prefix
        candidates = [p for p in products.values() if p.code.startswith(request[0]) and p.quantity > 0]
        
        if not candidates:
            state = STATE_OUT_OF_STOCK
            continue
            
        # Select cheapest item (greedy approach)
        selected_product = min(candidates, key=lambda p: p.price)
        
        # Process purchase
        selected_product.quantity -= 1
        total_revenue += selected_product.price
        
        state = STATE_READY
    
    # Calculate remaining inventory value
    remaining_value = sum(p.price * p.quantity for p in products.values())
    return remaining_value

# Initialize inventory
inventory = {
    'A01': Product('A01', 150, 3),
    'A02': Product('A02', 200, 2),
    'B01': Product('B01', 75, 5),
    'B02': Product('B02', 120, 1),
    'C01': Product('C01', 90, 4),
    'C02': Product('C02', 250, 2)
}

# Process requests
purchase_requests = ['A00', 'B00', 'C00', 'A00', 'B00']

remaining_inventory_value = process_vending_requests(inventory, purchase_requests)
print(f'Result: {remaining_inventory_value}')