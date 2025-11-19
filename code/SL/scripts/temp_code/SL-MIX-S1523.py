from collections import deque

def ip_to_int(ip):
    parts = ip.split('.')
    return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

def prefix_match(ip_int, prefix_int, prefix_len):
    mask = ~((1 << (32 - prefix_len)) - 1) & 0xffffffff
    return (ip_int & mask) == (prefix_int & mask)

# Packet source IPs in chronological order
packets = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.15",
    "172.16.0.1",
    "192.168.1.20",
    "10.0.0.45",
    "192.168.2.5"
]

# Suspicious IP prefixes stored in a stack (processed in LIFO order)
suspicious_prefixes = [
    ("192.168.1.0", 24),
    ("10.0.0.0", 16),
    ("172.16.0.0", 12)
]

# Convert prefixes to integer representations
prefix_stack = []
while suspicious_prefixes:
    ip, length = suspicious_prefixes.pop()
    prefix_stack.append((ip_to_int(ip), length))

# Process packets
flagged_status = []
for packet_ip in packets:
    packet_int = ip_to_int(packet_ip)
    is_flagged = False
    
    # Check against prefixes in the stack
    temp_storage = []
    while prefix_stack:
        prefix_int, prefix_len = prefix_stack.pop()
        temp_storage.append((prefix_int, prefix_len))
        if prefix_len >= 24 and prefix_match(packet_int, prefix_int, prefix_len):
            is_flagged = True
            break
    
    # Restore the stack
    while temp_storage:
        prefix_stack.append(temp_storage.pop())
    
    flagged_status.append(is_flagged)

# Dynamic programming to find maximum consecutive flags
dp = [0] * len(flagged_status)
if flagged_status[0]:
    dp[0] = 1
max_consecutive_flags = dp[0]

for i in range(1, len(flagged_status)):
    if flagged_status[i]:
        dp[i] = dp[i-1] + 1
        if dp[i] > max_consecutive_flags:
            max_consecutive_flags = dp[i]
    else:
        dp[i] = 0

print(f"Result: {max_consecutive_flags}")