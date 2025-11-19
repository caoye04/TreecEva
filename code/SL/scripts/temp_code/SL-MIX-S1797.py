from functools import reduce

def process_transaction(coins, product_price):
    states = ['START', 'VALIDATING', 'CALCULATING', 'DISPENSING', 'COMPLETE']
    current_state = 0
    valid_coins = {5, 10, 25}
    total_inserted = 0
    
    # State machine processing
    while current_state < len(states) - 1:
        if states[current_state] == 'START':
            current_state += 1
        elif states[current_state] == 'VALIDATING':
            # Validate coins using functional approach
            validated_coins = list(filter(lambda x: x in valid_coins, coins))
            current_state += 1
        elif states[current_state] == 'CALCULATING':
            # Calculate total using reduce
            total_inserted = reduce(lambda acc, coin: acc + coin, validated_coins, 0)
            current_state += 1
        elif states[current_state] == 'DISPENSING':
            # Compare and calculate change
            if total_inserted >= product_price:
                final_change = total_inserted - product_price
            else:
                final_change = -1  # Insufficient funds
            current_state += 1
        else:  # COMPLETE state
            break
    
    return final_change

# Transaction details
inserted_coins = [5, 10, 25, 25]
product_cost = 60

# Process transaction
final_change = process_transaction(inserted_coins, product_cost)
print(f'Result: {final_change}')