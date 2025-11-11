import hashlib

def process_device_id(d_id):
    reversed_id = d_id[::-1]
    hashed = hashlib.md5(reversed_id.encode()).hexdigest()
    hex_sum = sum(ord(c) for c in hashed[:8])
    return (hex_sum * 3) % 17

device_pool = ['DEV001', 'SEN202', 'MON303', 'ALR404']
transformed_values = {d: process_device_id(d) for d in device_pool}

enhanced_pool = {k: v + (7 if k.startswith('D') else 13) for k, v in transformed_values.items()}
filtered_pool = dict(filter(lambda item: item[1] > 10, enhanced_pool.items()))

aggregated_score = sum(map(lambda x: x**2, filtered_pool.values())) % 23
validation_checksum = (aggregated_score * 5 + 7) % 19

print(f"Result: {validation_checksum}")