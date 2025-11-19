import heapq
import re
from functools import reduce

def build_binary_tree(nodes):
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = {'timestamp': nodes[mid][0], 'hash': nodes[mid][1], 'left': None, 'right': None}
    root['left'] = build_binary_tree(nodes[:mid])
    root['right'] = build_binary_tree(nodes[mid+1:])
    return root

packet_data = [
    (100, 'a1b2c3d4'),
    (250, 'e5f6g7h8i9'),
    (180, 'j0k1l2m3'),
    (90, 'n4o5p6q7'),
    (300, 'r8s9t0u1v2'),
    (120, 'w3x4y5z6')
]

# Filter valid packets: hash must contain at least one digit and be alphanumeric
valid_packets = list(filter(lambda p: re.match(r'^[a-z0-9]+$', p[1]) and any(c.isdigit() for c in p[1]), packet_data))

# Sort by timestamp
valid_packets.sort(key=lambda x: x[0])

# Build binary tree from sorted packets
tree_root = build_binary_tree(valid_packets)

# Extract hashes and compute hash scores
hashes = [node[1] for node in valid_packets]
hash_scores = list(map(lambda h: sum(ord(c) for c in h), hashes))

# Process using max heap (negate values for max-heap behavior)
heap = [-score for score in hash_scores]
heapq.heapify(heap)

# Compute verification score
verification_score = 0
while len(heap) > 1:
    first = -heapq.heappop(heap)
    second = -heapq.heappop(heap)
    combined = first + second
    verification_score += combined
    heapq.heappush(heap, -combined)

print(f"Result: {verification_score}")