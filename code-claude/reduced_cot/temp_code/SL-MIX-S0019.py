from collections import defaultdict, Counter
import math

# Network packet processing simulator with priority calculation

def calculate_checksum(packet_data):
    # Misleading function that isn't actually used for final result
    checksum = 0
    for i, char in enumerate(packet_data):
        checksum += (ord(char) * (i + 1)) % 256
    return checksum % 256

# Packet data and priorities
packets = [
    {"id": "P1", "data": "HELLO", "priority": 3, "status": "active"},
    {"id": "P2", "data": "WORLD", "priority": 5, "status": "dropped"},
    {"id": "P3", "data": "TEST", "priority": 2, "status": "active"},
    {"id": "P4", "data": "PACKET", "priority": 4, "status": "active"},
    {"id": "P5", "data": "NETWORK", "priority": 1, "status": "active"}
]

# Network configuration parameters
network_load = 78  # Percent
latency = 25       # Milliseconds
jitter = 12        # Milliseconds variance
packet_loss = 0.05 # 5% packet loss

# Process active packets
active_packets = [p for p in packets if p["status"] == "active"]
character_counts = Counter()
for packet in active_packets:
    character_counts.update(packet["data"])

# Calculate character statistics (distractor)
vowels = "AEIOU"
vowel_count = sum(character_counts[v] for v in vowels)
consonant_count = sum(character_counts[c] for c in character_counts if c in "BCDFGHJKLMNPQRSTVWXYZ")

# Priority queue system
priority_queue = []
base_priority = 0

# Network congestion simulation
congestion_factor = 0
if network_load > 75:
    congestion_factor = math.log(network_load - 60, 2)  # Logarithmic scaling
elif network_load > 50:
    congestion_factor = (network_load - 50) / 10  # Linear scaling
    
# Priority adjustments based on various factors
for packet in active_packets:
    # Distractor calculations
    packet_size = len(packet["data"]) * 8  # bits
    transmission_time = packet_size / 100  # arbitrary time unit
    
    # Actual priority calculation
    adjusted_priority = packet["priority"]
    
    # Apply adjustments based on packet contents
    if 'E' in packet["data"]:
        adjusted_priority += 1
    if 'T' in packet["data"]:
        adjusted_priority += 2
    
    # This part looks important but is actually a distractor
    checksum = calculate_checksum(packet["data"])
    if checksum % 2 == 0:
        adjusted_priority = adjusted_priority * 1.25
    else:
        adjusted_priority = adjusted_priority * 0.8
    
    # More distractor calculations
    theoretical_max = adjusted_priority * (1 + packet_loss)
    weighted_average = (adjusted_priority + theoretical_max) / 2
    
    # Only add to queue if it's actually an active packet
    if packet["status"] == "active":
        priority_queue.append(int(adjusted_priority))

# Sorting the queue (in reverse order - highest priority first)
priority_queue.sort(reverse=True)

# Base priority is calculated based on network conditions
base_priority = int(congestion_factor * 2)

# This is the critical statement we're asking about
final_priority = priority_queue.pop() if priority_queue else base_priority

# More processing that happens after (distractors)
processed_packets = defaultdict(int)
for i, packet in enumerate(active_packets):
    processing_time = latency + ((-1)**i * (jitter/2))
    processed_packets[packet["id"]] = processing_time

# Final network statistics (more distractors)
total_packets = len(packets)
processed_ratio = len(active_packets) / total_packets
effective_throughput = processed_ratio * (100 - network_load) / 100

print(f"Result: {final_priority}")