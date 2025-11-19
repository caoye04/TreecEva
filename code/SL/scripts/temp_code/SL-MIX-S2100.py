import math

device_ids = [0x1A3F, 0x2B5E, 0x3C7D, 0x4D9C]
transformed_ids = []
base_key = 0

for idx, dev_id in enumerate(device_ids):
    stage_one = dev_id ^ (dev_id << 2)
    stage_two = stage_one & 0xFFFF
    transformed_ids.append(stage_two)
    base_key |= (stage_two >> idx)

id_set = frozenset(transformed_ids)
composite_map = {k: math.log2(k) if k > 0 else 0 for k in id_set}

aggregate = sum(composite_map.values())
scaling_factor = int(math.exp(aggregate % 3))

final_key = (base_key * scaling_factor) & 0xFF
print(f"Result: {final_key}")