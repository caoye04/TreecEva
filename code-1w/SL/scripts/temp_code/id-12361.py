from collections import Counter

def analyze_traffic_patterns():
    # Simulated network packet sizes in bytes (realistic traffic data)
    packets = [64, 128, 64, 512, 128, 64, 1024, 128, 64, 512]
    
    # Count frequency of each packet size
    packet_freq = Counter(packets)
    
    # Calculate total inflow (sum of all packets)
    inflow = sum(packets)
    
    # Identify outlier packets (>500 bytes) and simulate retransmission overhead
    large_packets = [p for p in packets if p > 500]
    retransmission_overhead = len(large_packets) * 64
    
    # Total outflow includes original traffic + overhead
    base_outflow = inflow
    protocol_overhead = inflow * 0.1  # 10% protocol header overhead
    outflow = base_outflow + protocol_overhead + retransmission_overhead
    
    # Key computation: effective network throughput
    net_flow = inflow - outflow
    
    # Irrelevant string analysis (distractor at intervention level 5)
    status_msg = "Traffic analysis complete"
    capitalized = status_msg.upper()
    word_count = len(status_msg.split())
    
    return net_flow

result = analyze_traffic_patterns()
print(f"Result: {result}")