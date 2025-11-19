import itertools

class PacketNode:
    def __init__(self, identifier, next_node=None):
        self.identifier = identifier
        self.next = next_node
        self.integrity_value = 0

def fibonacci_mod(n, mod):
    if n <= 1:
        return n % mod
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % mod
    return b

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Initialize packet chain
head = None
for i in range(5, 0, -1):
    head = PacketNode(i, head)

# Hash table for integrity tracking
integrity_map = {}
fib_base = 13
modulus = 1000

# Process packet identifiers from combinatorial generator
packet_ids = list(itertools.combinations(range(1, 8), 3))[:6]
processed_count = 0
node_ptr = head

while node_ptr and processed_count < len(packet_ids):
    pid_tuple = packet_ids[processed_count]
    xor_checksum = 0
    for val in pid_tuple:
        xor_checksum ^= val
    
    fib_index = (xor_checksum + node_ptr.identifier) % 10
    fib_value = fibonacci_mod(fib_index, modulus)
    
    gcd_result = compute_gcd(xor_checksum, fib_base)
    node_ptr.integrity_value = (fib_value * gcd_result) % modulus
    
    integrity_map[node_ptr.identifier] = node_ptr.integrity_value
    
    node_ptr = node_ptr.next
    processed_count += 1

final_integrity_sum = sum(integrity_map.values()) % 10000
print(f"Result: {final_integrity_sum}")