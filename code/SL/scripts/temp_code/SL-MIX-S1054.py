from collections import defaultdict

# State definitions
IDLE, PROCESSING, RESTOCK_NEEDED = 0, 1, 2

def process_purchases():
    # Inventory tracking
    inventory = defaultdict(int, {'chips': 10, 'soda': 5, 'candy': 7})
    thresholds = {'chips': 3, 'soda': 2, 'candy': 4}
    
    # Purchase sequence
    purchases = [
        ('chips', 3),
        ('soda', 2),
        ('candy', 4),
        ('chips', 5)
    ]
    
    # System state
    state = IDLE
    restock_flag = False
    
    for item, quantity in purchases:
        state = PROCESSING
        inventory[item] -= quantity
        
        # Short-circuit evaluation for restock check
        if state == PROCESSING and inventory[item] < thresholds[item]:
            state = RESTOCK_NEEDED
            restock_flag = restock_flag or True
    
    return restock_flag

# Execute and get result
final_restock_flag = process_purchases()
print(f"Result: {int(final_restock_flag)}")