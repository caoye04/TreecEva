from collections import defaultdict
import heapq
import hashlib

def decode_packet_signature(encoded_sig):
    return bytes.fromhex(encoded_sig).decode('utf-8')

def compute_hash_signature(content):
    return int(hashlib.md5(content.encode()).hexdigest()[:8], 16)

def transform_score(score, operation_code):
    switch = {
        1: lambda x: x ^ 0xFF,
        2: lambda x: (x << 2) & 0xFFFF,
        3: lambda x: x | 0x0F,
        4: lambda x: x & ~0x70
    }
    return switch.get(operation_code, lambda x: x)(score)

packet_signatures = ['48656c6c6f', '576f726c64', '507974686f6e']
threat_indicators = defaultdict(int)
threat_heap = []

for i, sig in enumerate(packet_signatures):
    decoded = decode_packet_signature(sig)
    hash_sig = compute_hash_signature(decoded)
    threat_score = hash_sig % 1000
    
    for j in range(3):
        adjusted_score = threat_score + i * 10 + j
        if adjusted_score % 7 == 0:
            threat_indicators[decoded] += adjusted_score
        elif adjusted_score % 5 == 0:
            heapq.heappush(threat_heap, -adjusted_score)
        else:
            threat_indicators[decoded] -= adjusted_score // 2

aggregated_threat_level = 0
for key in threat_indicators:
    score = threat_indicators[key]
    operation = len(key) % 4 + 1
    transformed = transform_score(score, operation)
    aggregated_threat_level += transformed

while threat_heap:
    heap_value = -heapq.heappop(threat_heap)
    aggregated_threat_level ^= heap_value

print(f"Result: {aggregated_threat_level}")