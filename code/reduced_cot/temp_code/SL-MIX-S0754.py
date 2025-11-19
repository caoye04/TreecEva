import re
from collections import deque
from functools import reduce

def process_packet_headers(packet_stream):
    # Count HTTP-like patterns in packet headers
    http_patterns = sum(1 for pkt in packet_stream if re.search(r'HTTP/\d\.\d', pkt))
    return http_patterns

def calculate_token_rate(base_rate, pattern_count):
    # Adjust token rate based on detected patterns
    return base_rate + (pattern_count * 3)

def simulate_network_traffic():
    # Packet queue implementation using deque
    packet_queue = deque([
        "GET /api/v1/data HTTP/1.1\r\nHost: example.com",
        "POST /upload HTTP/1.1\r\nContent-Length: 1024",
        "SSH-2.0-OpenSSH_7.9\r\nKEXINIT",
        "GET /index.html HTTP/1.0\r\nUser-Agent: Mozilla",
        "TCP Flags: SYN ACK\r\nSequence: 12345"
    ])
    
    # Initialize system parameters
    token_bucket_capacity = 20
    current_tokens = 15
    base_generation_rate = 5
    congestion_window = 8
    
    # Process packets and adjust token rate
    processed_packets = []
    while packet_queue and len(processed_packets) < 3:
        current_packet = packet_queue.popleft()
        processed_packets.append(current_packet)
    
    # Apply functional programming to analyze packet headers
    http_pattern_count = process_packet_headers(processed_packets)
    adjusted_rate = calculate_token_rate(base_generation_rate, http_pattern_count)
    
    # Update congestion window based on token availability
    tokens_needed = reduce(lambda acc, _: acc + 2, range(congestion_window), 0)
    
    if tokens_needed <= current_tokens:
        congestion_window = congestion_window + (adjusted_rate // 2)
    else:
        congestion_window = max(1, congestion_window - (tokens_needed - current_tokens))
    
    return congestion_window

# Execute simulation
final_congestion_window = simulate_network_traffic()
print(f"Result: {final_congestion_window}")