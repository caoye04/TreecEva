import re
from functools import reduce
from collections import Counter

def ip_to_int(ip_str):
    parts = list(map(int, ip_str.split('.')))
    return reduce(lambda acc, octet: (acc << 8) + octet, parts, 0)

def count_ones(n):
    return bin(n).count('1')

log_entry = "Security alert from IP 192.168.1.10 at 2023-07-15T14:30:22Z"
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
match = re.search(ip_pattern, log_entry)

if match and all(0 <= int(x) <= 255 for x in match.group().split('.')):
    ip_address = match.group()
    ip_integer = ip_to_int(ip_address)
    masked_ip = ip_integer & 0xFFFF0000
    bit_count = count_ones(masked_ip)
    
    # Short-circuit evaluation in conditional assignment
    is_even = bit_count % 2 == 0
    adjusted_count = bit_count // 2 if is_even else (bit_count - 1) // 2
    
    # Additional check for private IP ranges
    first_octet = int(ip_address.split('.')[0])
    is_private = first_octet == 10 or first_octet == 172 and 16 <= int(ip_address.split('.')[1]) <= 31 or first_octet == 192 and int(ip_address.split('.')[1]) == 168
    
    # Final score calculation with conditional modifier
    final_score = adjusted_count + (10 if is_private else 0)
else:
    final_score = -1

print(f"Result: {final_score}")