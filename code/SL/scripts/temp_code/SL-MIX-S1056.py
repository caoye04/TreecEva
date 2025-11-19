import re
from functools import reduce

# Encoded packets with custom base-64-like encoding
packets = ['AABBAABB', 'XYZXYZ', 'MNOPQRST', 'QRSTUVWX']
trusted_flags = [False, True, False, False]

def custom_decode(s):
    # Simple mapping for demonstration
    mapping = {chr(i): i-65 for i in range(65, 91)}  # A=0, B=1, ..., Z=25
    return [mapping.get(c, 0) for c in s]

# Greedy tracking of XOR values with dynamic programming for earliest indices
cumulative_xor = 0
earliest_indices = {0: -1}  # DP table: xor_value -> earliest index
earliest_zero_xor_index = -1

for idx, (packet, trusted) in enumerate(zip(packets, trusted_flags)):
    # Short-circuit evaluation: skip if trusted
    if trusted or not re.match(r'^[A-Z]+$', packet):
        continue
    
    # Decode packet
    decoded_bytes = custom_decode(packet)
    
    # Lambda to compute cumulative XOR using reduce
    cumulative_xor = reduce(lambda acc, b: acc ^ b, decoded_bytes, cumulative_xor)
    
    # Update DP table and check for zero XOR
    if cumulative_xor not in earliest_indices:
        earliest_indices[cumulative_xor] = idx
    elif cumulative_xor == 0:
        # Found a subsequence with XOR 0
        earliest_zero_xor_index = max(earliest_zero_xor_index, earliest_indices[cumulative_xor])

print(f"Result: {earliest_zero_xor_index}")