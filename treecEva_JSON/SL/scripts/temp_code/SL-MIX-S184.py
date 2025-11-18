import heapq

class TelemetryPacket:
    def __init__(self, timestamp, sensor_id):
        self.timestamp = timestamp
        self.sensor_id = sensor_id
    
    def priority(self):
        # Priority encoding formula
        return (self.timestamp * 3 + self.sensor_id * 2) % 100

# Initialize empty heap
packet_heap = []

# Process 5 sensor packets
packets = [
    TelemetryPacket(1623456789, 12),
    TelemetryPacket(1623456790, 8),
    TelemetryPacket(1623456791, 15),
    TelemetryPacket(1623456792, 3),
    TelemetryPacket(1623456793, 21)
]

for pkt in packets:
    priority_value = pkt.priority()
    heapq.heappush(packet_heap, priority_value)

# After all insertions, what is the root value?
root_priority = packet_heap[0]
print(f"Result: {root_priority}")