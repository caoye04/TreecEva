from collections import defaultdict

def compute_loyalty(transactions):
    state = 'idle'
    item_value = 0
    coins_inserted = 0
    loyalty_points = 0
    
    for action in transactions:
        if state == 'idle':
            if action == 1:  # select_item
                state = 'item_selected'
                item_value = 5
            elif action == 2:  # insert_coin
                coins_inserted += 1
        elif state == 'item_selected':
            if action == 2:  # insert_coin
                coins_inserted += 1
                if coins_inserted >= item_value:
                    state = 'ready_to_dispense'
            elif action == 3:  # cancel_purchase
                state = 'idle'
                coins_inserted = 0
        elif state == 'ready_to_dispense':
            if action == 1:  # select_item
                # Award loyalty points using bitwise formula
                loyalty_points += (item_value << 1) & (coins_inserted | 3)
                item_value = 5
                coins_inserted = 0
                state = 'item_selected'
            elif action == 2:  # insert_coin
                coins_inserted += 1
    
    # Finalize loyalty calculation
    if state == 'ready_to_dispense':
        loyalty_points += (item_value << 1) & (coins_inserted | 3)
    
    return loyalty_points

# Customer interaction sequence
# 1=select_item, 2=insert_coin, 3=cancel_purchase
interactions = [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2]

final_loyalty_score = compute_loyalty(interactions)  # <-- QUERY
print(f"Result: {final_loyalty_score}")