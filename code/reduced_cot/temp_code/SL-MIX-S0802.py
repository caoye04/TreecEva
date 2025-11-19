from functools import reduce

def vending_machine_processor():
    # State machine states
    STATE_IDLE = 0
    STATE_PROCESSING = 1
    STATE_DISPENSING = 2
    
    # Inventory tracking
    inventory = {'cola': 5, 'chips': 3, 'candy': 0}
    prices = {'cola': 125, 'chips': 100, 'candy': 75}
    
    # Transaction processor with closure
    def create_transaction_handler():
        balance = 0
        selected_item = None
        
        def handle_payment(amount):
            nonlocal balance
            balance += amount
            return balance
        
        def select_item(item):
            nonlocal selected_item
            selected_item = item
            return inventory.get(item, 0) > 0 and prices.get(item, 0) <= balance
        
        def process_purchase():
            nonlocal balance, selected_item
            if selected_item and inventory[selected_item] > 0:
                cost = prices[selected_item]
                if balance >= cost:  # Short-circuit evaluation
                    inventory[selected_item] -= 1
                    change = balance - cost
                    balance = 0
                    selected_item = None
                    return change
            return 0
        
        return handle_payment, select_item, process_purchase
    
    # Create handler instance
    payment_handler, item_selector, purchase_processor = create_transaction_handler()
    
    # Transaction sequence
    transactions = [
        (100, 'cola'),    # Not enough money
        (50, None),       # Additional payment
        (25, 'cola'),     # Now can buy
        (200, 'chips'),   # Buy chips
        (100, 'candy'),   # Try to buy candy (out of stock)
        (50, 'cola'),     # Another cola purchase
    ]
    
    change_due = 0
    state = STATE_IDLE
    
    for amount, item in transactions:
        if state == STATE_IDLE and amount:
            payment_handler(amount)
            state = STATE_PROCESSING
        
        if state == STATE_PROCESSING and item:
            # Short-circuit evaluation in item selection
            if item_selector(item) and inventory[item] > 0:
                state = STATE_DISPENSING
            else:
                state = STATE_IDLE
        
        if state == STATE_DISPENSING:
            change_due += purchase_processor()
            state = STATE_IDLE
    
    # Final transaction
    payment_handler(300)
    if item_selector('cola') and inventory['cola'] > 0:  # Short-circuit evaluation
        change_due += purchase_processor()
    
    return change_due

# Execute and get result
final_change = vending_machine_processor()
print(f"Result: {final_change}")