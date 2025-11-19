class DeliveryNode:
    def __init__(self, location_id, priority_base):
        self.location_id = location_id
        self.priority_base = priority_base
        self.next = None

def calculate_adjusted_priority(node, modifier_map, depth=0):
    if not node or depth > 3:
        return 0
    base_value = node.priority_base
    modifier = modifier_map.get(node.location_id, 1)
    adjusted = (base_value << 1) ^ modifier
    if adjusted % 3 == 0:
        return adjusted + calculate_adjusted_priority(node.next, modifier_map, depth + 1)
    else:
        return adjusted - (calculate_adjusted_priority(node.next, modifier_map, depth + 1) >> 1)

delivery_zones = {
    'ZONE_A': 5,
    'ZONE_B': 12,
    'ZONE_C': 8,
    'ZONE_D': 15
}

modifier_lookup = {k: v for k, v in zip(delivery_zones.keys(), [2, 7, 3, 11])}
combined_map = {**delivery_zones, **modifier_lookup}

head = DeliveryNode('ZONE_A', delivery_zones['ZONE_A'])
head.next = DeliveryNode('ZONE_B', delivery_zones['ZONE_B'])
head.next.next = DeliveryNode('ZONE_C', delivery_zones['ZONE_C'])
head.next.next.next = DeliveryNode('ZONE_D', delivery_zones['ZONE_D'])

route_combinations = [
    [head, head.next],
    [head.next, head.next.next],
    [head, head.next.next.next]
]

priority_accumulator = 0
for pair in route_combinations:
    segment_priority = 0
    for node in pair:
        temp_modifier = combined_map[node.location_id] & 0b1111
        segment_priority ^= (node.priority_base | temp_modifier)
    if segment_priority > 20:
        priority_accumulator += segment_priority
    else:
        priority_accumulator -= (segment_priority >> 1)

optimized_score = calculate_adjusted_priority(head, modifier_lookup)
final_priority_score = priority_accumulator + (optimized_score & 0xFF)
print(f"Result: {final_priority_score}")