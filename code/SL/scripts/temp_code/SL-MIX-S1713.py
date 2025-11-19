import math
from collections import defaultdict

def entropy_calculator(packet_data):
    if not packet_data:
        return 0
    frequency = defaultdict(int)
    for byte_val in packet_data:
        frequency[byte_val] += 1
    total_bytes = len(packet_data)
    entropy = 0.0
    for count in frequency.values():
        probability = count / total_bytes
        entropy -= probability * math.log2(probability)
    return entropy

class PacketAnalyzer:
    def __init__(self):
        self.state = 'IDLE'
        self.processed_packets = 0
        self.routing_table = {'LOW': 0, 'MED': 0, 'HIGH': 0}
    
    def analyze_packet(self, packet):
        entropy = entropy_calculator(packet)
        # State machine transition
        if self.state == 'IDLE':
            self.state = 'ANALYZING' if entropy > 2.0 else 'IDLE'
        elif self.state == 'ANALYZING':
            route = 'HIGH' if entropy > 4.0 else ('MED' if entropy > 2.0 else 'LOW')
            self.routing_table[route] += 1
            self.state = 'ROUTING'
        elif self.state == 'ROUTING':
            # Ternary-based filtering
            self.processed_packets += 1 if self.routing_table['HIGH'] > self.routing_table['LOW'] else 0
            self.state = 'IDLE'
        return self.state

# Packet data simulation
packets = [
    [120, 150, 200, 120],  # Low entropy
    [10, 20, 30, 40, 50, 60, 70, 80],  # Medium entropy
    [255, 0, 128, 64, 32, 16, 8, 4, 2, 1],  # High entropy
    [100, 100, 100, 200, 200, 200, 150, 150],  # Medium entropy
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # High entropy
]

analyzer = PacketAnalyzer()
for p in packets:
    analyzer.analyze_packet(p)

print(f"Result: {analyzer.processed_packets}")