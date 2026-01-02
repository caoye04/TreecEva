def calculate_remaining_capacity(units, allocation_map):
    total_allocated = 0
    temp_buffer = []
    debug_trace = []

    for idx, unit in enumerate(units):
        if unit['status'] == 'active':
            unit_id = unit['id']
            base_load = unit['load']
            adjustment_factor = 1.0

            # Simulate some irrelevant intermediate calculations
            shadow_value = base_load * 0.15
            temp_buffer.append(shadow_value)

            if unit_id in allocation_map:
                alloc_list = allocation_map[unit_id]
                for i, alloc in enumerate(alloc_list):
                    multiplier = alloc['factor']
                    phase_offset = alloc.get('phase', 0)

                    # Real computation step
                    total_allocated += base_load * multiplier

                    # Irrelevant diagnostic logging
                    debug_trace.append(f"Unit {unit_id} phase {phase_offset} processed")

    # Additional distraction: unused aggregation
    buffer_sum = sum(temp_buffer) if temp_buffer else 0
    average_shadow = buffer_sum / len(temp_buffer) if temp_buffer else 0

    system_baseline = 1000
    reserved_margin = system_baseline * 0.1
    raw_capacity = system_baseline - total_allocated - reserved_margin

    scaling_modifier = 1.0
    if raw_capacity > 500:
        scaling_modifier = 1.05
    elif raw_capacity > 250:
        scaling_modifier = 1.02

    final_capacity = int(raw_capacity * scaling_modifier)

    # Dead code path - never executed under current logic
    if False:
        fallback = system_baseline - total_allocated
        final_capacity = int(fallback * 0.9)

    return final_capacity

# Setup input data
units = [
    {'id': 1, 'load': 80, 'status': 'active'},
    {'id': 2, 'load': 120, 'status': 'active'},
    {'id': 3, 'load': 60, 'status': 'inactive'},
    {'id': 4, 'load': 100, 'status': 'active'}
]

allocation_map = {
    1: [{'factor': 0.5}, {'factor': 0.1}],
    2: [{'factor': 0.3}],
    4: [{'factor': 0.4}, {'factor': 0.2}]
}

# Key execution point
final_capacity = calculate_remaining_capacity(units, allocation_map)
print(f"Result: {final_capacity}")