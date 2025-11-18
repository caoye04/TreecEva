import collections
import functools

def base36_decode(s):
    return int(s, 36)

def process_deliveries(encoded_times):
    # Step 1: Decode all times from base-36
    decoded_times = list(map(base36_decode, encoded_times))
    
    # Step 2: Sort the decoded times
    sorted_times = sorted(decoded_times)
    
    # Step 3: Calculate delays using a functional approach
    delays = map(lambda t: max(0, t - 720), sorted_times)
    
    # Step 4: Sum all delays
    total_delay_minutes = functools.reduce(lambda a, b: a + b, delays, 0)
    
    return total_delay_minutes

# Encoded delivery times (base-36 strings)
encoded_delivery_schedule = ['1c0', 'k4', 'oa', '2s0', 'zm', '190', 'aa0']

total_delay_minutes = process_deliveries(encoded_delivery_schedule)
print(f"Result: {total_delay_minutes}")