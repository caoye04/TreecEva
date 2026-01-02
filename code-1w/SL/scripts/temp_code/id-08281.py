def calculate_remaining_capacity(units, constraints):
    # Simulate resource allocation across distributed nodes
    total_resources = sum(unit['capacity'] for unit in units)
    reserved = 0
    utilized = 0
    
    # Track active and inactive units using set operations
    all_ids = {unit['id'] for unit in units}
    constrained_ids = {c['unit_id'] for c in constraints}
    available_units = all_ids - constrained_ids  # Units without constraints

    temp_sum = 0
    for i in range(len(units)):
        unit = units[i]
        unit_id = unit['id']
        cap = unit['capacity']
        
        # Misleading intermediate calculation (not used in final result)
        temp_sum += cap * (i + 1) % 7
        
        if unit_id in constrained_ids:
            constraint = next(c for c in constraints if c['unit_id'] == unit_id)
            if constraint['type'] == 'hard':
                reserved += cap * 0.5
            elif constraint['type'] == 'soft':
                reserved += cap * 0.2
        else:
            utilized += cap * 0.8

    # Dead code path - never executed under current logic
    fallback_mode = False
    if len(available_units) > 100:
        fallback_mode = True
        utilized = sum(u['capacity'] * 0.1 for u in units)

    # Auxiliary computation to increase cognitive load
    efficiency_ratio = (utilized / (total_resources + 1e-9)) * 100
    efficiency_ratio = round(efficiency_ratio, 2)

    # Core logic: remaining capacity is what's not reserved
    unreserved_capacity = total_resources - reserved
    
    # Final decision based on conditional expression
    final_capacity = unreserved_capacity if efficiency_ratio > 10 else total_resources * 0.5
    
    return final_capacity

# Define system units
units = [
    {'id': 1, 'capacity': 20},
    {'id': 2, 'capacity': 30},
    {'id': 3, 'capacity': 50},
    {'id': 4, 'capacity': 40},
    {'id': 5, 'capacity': 60}
]

# Define constraints
constraints = [
    {'unit_id': 1, 'type': 'hard'},
    {'unit_id': 3, 'type': 'soft'},
    {'unit_id': 5, 'type': 'hard'}
]

# Execute main logic
final_capacity = calculate_remaining_capacity(units, constraints)
print(f"Target result: {final_capacity}")