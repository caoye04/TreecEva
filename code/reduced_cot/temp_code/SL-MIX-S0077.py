from collections import defaultdict

def process_restock(restock_event, inventory, max_capacity):
    product, amount = restock_event
    current = inventory[product]
    inventory[product] = min(current + amount, max_capacity[product])
    return max_capacity[product] - inventory[product]

def update_state_machine(state, event_type):
    transitions = {
        'IDLE': {'RESTOCK': 'PROCESSING', 'SERVE': 'IDLE'},
        'PROCESSING': {'COMPLETE': 'IDLE', 'RESTOCK': 'PROCESSING'}
    }
    return transitions.get(state, {}).get(event_type, state)

# Initialize inventory system
inventory_levels = defaultdict(int)
max_product_capacity = {'SODA': 20, 'CHIPS': 15, 'CANDY': 25}
state_machine = 'IDLE'

# Restocking events
restocking_queue = [
    ('SODA', 8),
    ('CHIPS', 10),
    ('CANDY', 5),
    ('SODA', 7),
    ('CHIPS', 8)
]

# Process events with state machine control
remaining_capacity = 0
for event in restocking_queue:
    state_machine = update_state_machine(state_machine, 'RESTOCK')
    remaining_capacity += process_restock(event, inventory_levels, max_product_capacity) if state_machine == 'PROCESSING' else 0
    state_machine = update_state_machine(state_machine, 'COMPLETE')

# Final adjustment using ternary logic
remaining_capacity = remaining_capacity if remaining_capacity > 0 else sum(max_product_capacity.values()) - sum(inventory_levels.values())

print(f"Result: {remaining_capacity}")