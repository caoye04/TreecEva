from collections import defaultdict

def process_vending_actions():
    # State definitions
    IDLE, SELECTING, CONFIRMING, DISPENSING = 0, 1, 2, 3
    
    # Item prices
    prices = {'SODA': 150, 'CHIPS': 100, 'CANDY': 75}
    
    # User action sequence: (action_type, value)
    actions = [
        ('INSERT_MONEY', 200),
        ('SELECT_ITEM', 'SODA'),
        ('CONFIRM', None),
        ('INSERT_MONEY', 50),
        ('SELECT_ITEM', 'CHIPS'),
        ('CANCEL', None),
        ('SELECT_ITEM', 'CANDY'),
        ('CONFIRM', None)
    ]
    
    # Initialize state and balance
    current_state = IDLE
    balance = 0
    selected_item = None
    final_balance = 0
    
    # State transition handler
    for action_type, value in actions:
        if current_state == IDLE:
            if action_type == 'INSERT_MONEY':
                balance += value
                current_state = SELECTING
        elif current_state == SELECTING:
            if action_type == 'SELECT_ITEM':
                selected_item = value
                current_state = CONFIRMING
        elif current_state == CONFIRMING:
            if action_type == 'CONFIRM':
                if balance >= prices[selected_item]:
                    balance -= prices[selected_item]
                    current_state = DISPENSING
                else:
                    current_state = IDLE
            elif action_type == 'CANCEL':
                current_state = IDLE
        elif current_state == DISPENSING:
            # Dispense item and return to IDLE
            current_state = IDLE
    
    final_balance = balance
    
    return final_balance

# Process actions and get final balance
final_balance = process_vending_actions()
print(f"Result: {final_balance}")