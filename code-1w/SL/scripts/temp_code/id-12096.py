from collections import defaultdict
from itertools import cycle

# Simulate a data integrity tracker for a packet transmission system
packet_stream = [17, 23, 19, 31, 29, 41, 37]
error_flags = [False, True, False, False, True, False, False]
prime_base = 97
twist_factor = 13

# Auxiliary tracking structures
diagnostic_log = defaultdict(int)
flag_cycle = cycle([1, 0, 1])

# Primary computation variables
checksum = 0
accumulated_shift = 0
rolling_mask = 5
supplementary_sum = 0

for idx, (value, flag) in enumerate(zip(packet_stream, error_flags)):
    # Irrelevant diagnostic logging (distractor)
    diagnostic_log['processed'] += 1
    if flag:
        diagnostic_log['errors'] += 1
        accumulated_shift ^= idx * twist_factor

    # Core logic with interference from masking operations
    temp_value = value ^ rolling_mask
    rolling_mask = (rolling_mask * 3) % prime_base

    # Conditional manipulation based on cycle (semi-relevant)
    if next(flag_cycle):
        temp_value = (temp_value + twist_factor) % prime_base

    # Key statement: update checksum with current value
    checksum = (checksum + temp_value) % prime_base

    # Dead code path - never affects result (distractor)
    if idx > 100:
        supplementary_sum += value

    # Additional irrelevant accumulation
    supplementary_sum += idx & value

# Final unrelated transformation (does not alter checksum)
final_flag_state = sum(diagnostic_log.values()) % 2

print(f"Result: {checksum}")