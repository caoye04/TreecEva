from collections import deque

packet_queues = {
    'switch_A': deque([10, 25, 30]),
    'switch_B': deque([15, 20, 35]),
    'switch_C': deque([5, 40, 45])
}

priority_flags = {10, 15, 20, 25}
frozen_blacklist = frozenset([30, 35])

maintenance_summary = 0

for switch_id, queue in packet_queues.items():
    temp_stack = []
    while queue:
        packet = queue.popleft()
        if packet in frozen_blacklist:
            continue
        is_high_priority = packet in priority_flags
        temp_stack.append(packet * 2 if is_high_priority else packet + 1)
    
    while temp_stack:
        processed_packet = temp_stack.pop()
        maintenance_summary += processed_packet if processed_packet % 2 == 0 else processed_packet - 1

print(f'Result: {maintenance_summary}')