import itertools

def encode_base36(num):
    if num == 0:
        return '0'
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while num > 0:
        result = chars[num % 36] + result
        num //= 36
    return result

def decode_base36(s):
    return int(s, 36)

# Production defect data for 3 batches
batch_defect_counts = [125, 87, 203]

# Apply quality adjustment factors using lambda
adjustment_factors = list(map(lambda x: x * 2 if x > 100 else x + 10, batch_defect_counts))

# Combine adjusted values using itertools accumulation
accumulated_defects = list(itertools.accumulate(adjustment_factors, lambda a, b: a + b))

# Final processing step - take last accumulated value and encode/decode cycle
encoded_value = encode_base36(accumulated_defects[-1])
final_defect_summary = decode_base36(encoded_value)

print(f"Result: {final_defect_summary}")