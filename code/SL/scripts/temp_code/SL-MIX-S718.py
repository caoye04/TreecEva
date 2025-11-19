import heapq
from functools import reduce

class PacketNode:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None
    
    def __lt__(self, other):
        return self.priority < other.priority

def analyze_flags(flags):
    # Check if SYN and FIN flags are both set (potential SYN flood)
    syn_fin = (flags & 0x02) and (flags & 0x01)
    # Check if URG flag is set without PSH
    urg_not_psh = (flags & 0x20) and not (flags & 0x08)
    return syn_fin or urg_not_psh

def process_packets(packet_stream):
    heap = []
    head = PacketNode(0, None)
    current = head
    threat_indicators = []
    
    for i, (priority, flags, payload_len) in enumerate(packet_stream):
        node = PacketNode(priority, (flags, payload_len))
        current.next = node
        current = node
        
        is_suspicious = analyze_flags(flags)
        
        match priority:
            case p if p < 10:
                if is_suspicious and payload_len > 1000:
                    heapq.heappush(heap, node)
                    threat_indicators.append(1)
                else:
                    threat_indicators.append(0)
            case p if 10 <= p < 50:
                if is_suspicious or payload_len > 500:
                    heapq.heappush(heap, node)
                    threat_indicators.append(2)
                else:
                    threat_indicators.append(0)
            case _:
                if is_suspicious and payload_len > 100:
                    heapq.heappush(heap, node)
                    threat_indicators.append(3)
                else:
                    threat_indicators.append(0)
    
    # Calculate base threat level from indicators
    base_threat = reduce(lambda x, y: x + y, threat_indicators, 0)
    
    # Adjust threat level based on heap analysis
    high_priority_count = 0
    while heap:
        packet = heapq.heappop(heap)
        if packet.priority < 20:
            high_priority_count += 1
    
    # Final threat calculation
    threat_level = (base_threat * 2) - high_priority_count
    return threat_level

# Simulated packet stream: (priority, flags, payload_length)
packets = [
    (5,  0x23, 1500),   # Suspicious flags (SYN+FIN+URG), high priority, large payload
    (15, 0x10, 600),    # PUSH flag, medium priority, medium payload
    (25, 0x20, 200),    # URG flag only, lower priority, small payload
    (8,  0x02, 1200),   # SYN flag, high priority, large payload
    (45, 0x00, 50),     # No flags, low priority, tiny payload
    (12, 0x21, 800),    # FIN+URG flags, medium priority, large payload
]

threat_level = process_packets(packets)
print(f"Result: {threat_level}")