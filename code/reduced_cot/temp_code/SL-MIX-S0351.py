import heapq
from collections import defaultdict

def calculate_packet_checksum(events):
    checksum_heap = []
    event_tracker = defaultdict(int)
    
    for i, event in enumerate(events):
        # Update tracker with XOR of event and its position
        event_tracker[i] = event ^ (i << 2)
        
        # Push negative value for max-heap behavior
        heapq.heappush(checksum_heap, -((event & 0xF) | ((i & 0x3) << 4)))
        
        # Every third event, adjust with XOR of heap top
        if (i + 1) % 3 == 0:
            top_val = -heapq.heappop(checksum_heap)
            adjustment = top_val ^ event_tracker[i-1]
            heapq.heappush(checksum_heap, -adjustment)
    
    # Final checksum calculation
    primary_checksum = 0
    while checksum_heap:
        val = -heapq.heappop(checksum_heap)
        primary_checksum ^= val
    
    # Apply final transformation
    final_integrity_checksum = (primary_checksum >> 1) & 0xFF
    return final_integrity_checksum

# Network events data
network_events = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81]
final_integrity_checksum = calculate_packet_checksum(network_events)
print(f"Result: {final_integrity_checksum}")