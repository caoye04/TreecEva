import math
from functools import reduce
from itertools import combinations

def transform_segment(segment_value, position):
    shifted = segment_value << (position % 4)
    masked = shifted & 0xFF
    return masked ^ (position * 7)

def compute_checksum(components):
    powered = [int(math.pow(x, 1.5)) for x in components if x > 0]
    logged = [int(math.log(y, 2)) for y in powered if y > 1]
    return reduce(lambda a, b: a ^ b, logged, 0)

data_segments = [12, 7, 23, 4, 19, 8, 15]
transformed_data = []

for idx, segment in enumerate(data_segments):
    if segment > 10 and idx < len(data_segments) - 1:
        transformed_value = transform_segment(segment, idx)
        transformed_data.append(transformed_value)
    elif segment <= 10 or len(str(segment)) == 1:
        transformed_data.append(segment ^ idx)

checksum = compute_checksum(transformed_data)
verification_components = list(combinations(transformed_data, 2))
aggregate_hash = 0

for pair in verification_components:
    product = pair[0] * pair[1]
    if product > 100 and product < 1000:
        aggregate_hash += product & 0x7F
    else:
        aggregate_hash += (product >> 2) ^ checksum

verification_code = (aggregate_hash >> 3) ^ checksum
print(f"Result: {verification_code}")