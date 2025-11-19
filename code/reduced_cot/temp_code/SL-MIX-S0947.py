import math

def calculate_zone_modifier(zone_id):
    modifiers = {1: 7, 2: 11, 3: 13, 4: 17, 5: 19}
    return modifiers.get(zone_id, 23)

def process_package(weight, zone):
    if weight <= 0:
        return 0
    log_component = int(math.log2(weight)) if weight > 1 else 0
    zone_factor = calculate_zone_modifier(zone)
    return (log_component * zone_factor) % 32

package_manifest = [
    {'weight': 8, 'zone': 2},
    {'weight': 16, 'zone': 4},
    {'weight': 3, 'zone': 1},
    {'weight': 32, 'zone': 3}
]

routing_key = 0
for package in package_manifest:
    weight = package['weight']
    zone = package['zone']
    
    if weight > 10:
        temp_key = process_package(weight, zone)
        routing_key = (routing_key + temp_key) % 256
        if routing_key > 100:
            break
    else:
        temp_key = process_package(weight*2, zone+1)
        routing_key = (routing_key ^ temp_key) & 0xFF

print(f"Result: {routing_key}")