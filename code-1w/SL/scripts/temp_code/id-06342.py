def analyze_storage_efficiency(inventory):
    efficiency_map = {}
    total_items = 0
    for section, items in inventory.items():
        if len(section) % 2 == 0:
            scale_factor = 1.5
        else:
            scale_factor = 0.8
        processed = int(len(items) * scale_factor)
        efficiency_map[section] = processed
        total_items += len(items)
    return efficiency_map, total_items


def track_movement_log(log_entries):
    movement_count = 0
    phantom_events = 0  # distractor: not used later
    for event in log_entries:
        action = event['type']
        if action == 'inbound':
            movement_count += event['qty']
        elif action == 'outbound':
            movement_count -= event['qty']
        else:
            phantom_events += 1  # red herring
    adjusted_count = movement_count + 10  # irrelevant adjustment
    return adjusted_count  # not used in final result

def calculate_remaining_capacity(state, threshold):
    temp_buffer = []
    over_threshold = 0
    debug_sum = 0  # semi-relevant but not final
    
    for zone, data in state.items():
        occupancy = data['current']
        max_cap = data['max']
        utilization = occupancy / max_cap
        
        # distraction: complex condition with partial use
        if utilization > 0.9:
            status = 'critical'
        elif utilization > 0.7:
            status = 'high'
        else:
            status = 'normal'
            
        if occupancy > threshold:
            over_threshold += 1
        
        # unnecessary transformation
        normalized = int((occupancy / max_cap) * 100)
        debug_sum += normalized
        
        temp_buffer.append(normalized)
    
    # core logic hidden among distractions
    capacity_left = 0
    for zone, data in state.items():
        capacity_left += (data['max'] - data['current'])
    
    # inject meaningless sort
    temp_buffer.sort(reverse=True)
    
    # final answer based on actual remaining capacity
    return capacity_left

# Main execution
if __name__ == '__main__':
    warehouse_state = {
        'A1': {'max': 100, 'current': 45},
        'B2': {'max': 200, 'current': 150},
        'C3': {'max': 50, 'current': 30},
        'D4': {'max': 300, 'current': 220}
    }

    logistics_log = [
        {'type': 'inbound', 'qty': 20},
        {'type': 'outbound', 'qty': 5},
        {'type': 'inbound', 'qty': 10}
    ]

    # Irrelevant preprocessing
    efficiency_stats, total_stock = analyze_storage_efficiency(warehouse_state)
    movement_audit = track_movement_log(logistics_log)

    # Key computation
    final_capacity = calculate_remaining_capacity(warehouse_state, threshold=15)

    print(f"Result: {final_capacity}")