import math

class PacketNode:
    def __init__(self, seq_num, size):
        self.seq_num = seq_num
        self.size = size
        self.next = None
        self.prev = None

class CircularPacketBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
    
    def add_packet(self, seq_num, size):
        new_node = PacketNode(seq_num, size)
        if self.size == 0:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            if self.size == self.capacity:
                # Remove the oldest packet (tail)
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                self.size += 1
        if self.size < self.capacity:
            self.size += 1

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

# Initialize buffer with capacity 10
packet_buffer = CircularPacketBuffer(10)

# Process 15 packets
seq_start = 100
size_start = 512
for i in range(15):
    seq_num = seq_start + i
    size = (size_start + i * 64) % 1024 or 1024  # Ensures size wraps at 1024 and is never 0
    packet_buffer.add_packet(seq_num, size)

# Calculate sum of sizes for packets with perfect square sequence numbers
target_sum = 0
current = packet_buffer.head
for _ in range(packet_buffer.size):
    if is_perfect_square(current.seq_num):
        target_sum += current.size
    current = current.next

print(f"Result: {target_sum}")