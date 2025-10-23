from collections import Counter

def simulate_vending_machine():
    state = 'idle'
    snack_counter = Counter()
    
    # Simulate purchases
    purchases = ['chips', 'candy', 'chips', 'soda', 'chips']
    
    for snack in purchases:
        if state == 'idle':
            state = 'selecting'
        if state == 'selecting':
            state = 'processing'
        if state == 'processing':
            state = 'dispensing'
        if state == 'dispensing':
            snack_counter[snack] += 1
            state = 'idle'
    
    return snack_counter['chips']

result = simulate_vending_machine()
print(f"Result: {result}")