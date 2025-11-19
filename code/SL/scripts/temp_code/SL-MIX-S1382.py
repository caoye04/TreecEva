states = {
    'idle': {'A': 'beverage', 'B': 'snack'},
    'beverage': {'1': ('selected', 2.5), '2': ('selected', 3.0)},
    'snack': {'1': ('selected', 1.5), '2': ('selected', 2.0)},
    'selected': {}
}

current_state = 'idle'
final_cost = 0
combo_codes = frozenset(['AB1', 'BA2'])
inputs = ['A', '1', 'B', '2']
entry_sequence = ''

for idx, inp in enumerate(inputs):
    if current_state == 'selected':
        current_state = 'idle'
    
    if current_state in states and inp in states[current_state]:
        entry_sequence += inp
        transition = states[current_state][inp]
        if isinstance(transition, tuple):
            current_state, price = transition
            final_cost += price
            
            # Early return check
            if entry_sequence in combo_codes:
                final_cost *= 0.9  # 10% discount
                break
        else:
            current_state = transition
    else:
        # Invalid input resets sequence but not cost
        entry_sequence = ''

# Apply loyalty discount if conditions met
loyalty_members = {'VIP123', 'VIP456'}
customer_id = 'VIP123'
is_loyalty_member = customer_id in loyalty_members
has_min_spent = final_cost >= 5.0

if is_loyalty_member and has_min_spent:
    final_cost -= 1.0

print(f"Result: {final_cost}")