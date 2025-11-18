import re
from collections import deque

def custom_decode(encoded_str):
    return ''.join(chr(ord(c) - 5) for c in encoded_str)

def extract_ips(text):
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(pattern, text)

# Encoded packets with priority tags
packets = [
    ('tag1', 'MTkyLjE2OC4xLjE='),  # 192.168.1.1
    ('tag2', 'MTAuMC4wLjE='),      # 10.0.0.1
    ('tag3', 'MTcyLjE2LjAuMQ==')   # 172.16.0.1
]

priority_stack = [3, 1, 2]  # Stack of packet priorities
timestamps_queue = deque([100, 200, 300])  # Processing timestamps
ip_scores = {'192.168.1.1': 10, '10.0.0.1': 20, '172.16.0.1': 30}

final_score = 0
while priority_stack and timestamps_queue:
    priority = priority_stack.pop()
    timestamp = timestamps_queue.popleft()
    tag, encoded_data = packets.pop(0)
    decoded_text = custom_decode(encoded_data)
    ips = extract_ips(decoded_text)
    if ips:
        ip = ips[0]
        if ip in ip_scores:
            score = ip_scores[ip] * priority + (timestamp % 10)
            final_score += score

print(f"Result: {final_score}")