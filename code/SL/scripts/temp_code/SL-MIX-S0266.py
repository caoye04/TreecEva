import math
from collections import defaultdict

def calculate_zone_capacity(zone_id):
    return 50 + (zone_id * 15) % 100

def simulate_visitor_flow():
    zones = {i: {'capacity': calculate_zone_capacity(i), 'current': 0} for i in range(1, 6)}
    overflow_counter = 0
    visitor_patterns = [
        [1, 3, 2, 5],
        [2, 4, 1, 3],
        [3, 1, 4, 2],
        [4, 2, 5, 1],
        [5, 3, 1, 4]
    ]
    
    # Lambda to check if zone can accept more visitors
    is_available = lambda z: zones[z]['current'] < zones[z]['capacity']
    
    for cycle in range(10):
        for pattern in visitor_patterns:
            for zone in pattern:
                if is_available(zone):
                    zones[zone]['current'] += 1
                    break
                else:
                    continue
            else:
                # Visitor could not enter any preferred zone
                overflow_counter += 1
        
        # Reset every 3 cycles with modulo arithmetic
        if (cycle + 1) % 3 == 0:
            for zone_id in zones:
                reset_amount = zones[zone_id]['current'] // 2
                zones[zone_id]['current'] = zones[zone_id]['current'] - reset_amount
    
    return overflow_counter

# Main execution
final_overflow_count = simulate_visitor_flow()
print(f"Result: {final_overflow_count}")