def calculate_remaining_capacity(units, allocations):
    total_allocated = 0
    temp_buffer = []
    overflow_flags = set()
    
    for unit in units:
        if unit not in allocations:
            continue
        raw_value = allocations[unit]
        normalized = raw_value // 2
        if normalized > 100:
            overflow_flags.add(unit)
            normalized = 100
        elif normalized < 0:
            normalized = 0
        
        adjustment_factor = 1
        if unit.startswith('aux'):
            adjustment_factor = 0.5
        elif unit.startswith('crit'):
            adjustment_factor = 1.2
            
        applied = int(normalized * adjustment_factor)
        temp_buffer.append(applied)
        total_allocated += applied

    baseline_total = sum([allocations[k] for k in allocations if k in units])
    theoretical_max = len(units) * 100
    efficiency_ratio = total_allocated / theoretical_max if theoretical_max > 0 else 0
    
    # Irrelevant debugging path
    debug_snapshot = {
        'units_processed': len(temp_buffer),
        'peak_load': max(temp_buffer) if temp_buffer else 0,
        'timestamp': '2023-09-15'
    }
    
    # Unused intermediate calculation
    phantom_capacity = 0
    for i in range(len(temp_buffer)):
        phantom_capacity += (temp_buffer[i] ** 2) % 7
    
    final_capacity = theoretical_max - total_allocated
    
    # Dead code branch (never executed due to fixed condition)
    if False and 'debug' in debug_snapshot:
        print("Debug mode active: ", debug_snapshot['debug'])
        
    return final_capacity

# Main execution
unit_list = ['crit_core_a', 'aux_node_1', 'data_port_b', 'crit_core_b', 'aux_node_2']
allocation_table = {
    'crit_core_a': 180,
    'aux_node_1': 90,
    'data_port_b': 60,
    'crit_core_b': 210,
    'aux_node_2': 110,
    'logging_unit': 30  # Not in unit_list, so ignored
}

intermediate_sum = sum(allocation_table[k] % 15 for k in allocation_table)
dummy_set = {x % 4 for x in range(intermediate_sum)}  # Set operation distraction

final_capacity = calculate_remaining_capacity(unit_list, allocation_table)
print(f"Result: {final_capacity}")