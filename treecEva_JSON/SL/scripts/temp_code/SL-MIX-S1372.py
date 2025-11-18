from collections import defaultdict

def analyze_packets(packet_data):
    segments = [packet_data[i:i+4] for i in range(0, len(packet_data), 4)]
    scores = defaultdict(int)
    
    for idx, segment in enumerate(segments):
        if len(segment) < 4:
            continue
        transformed = ''.join(chr(ord(c) ^ 0x55) for c in segment)
        if any(c.isdigit() for c in transformed):
            scores[idx] += sum(ord(c) for c in transformed) % 10
        else:
            scores[idx] -= sum(ord(c) for c in segment) % 7
    
    total = 0
    for k, v in scores.items():
        if v > 0:
            total += v << 1
        else:
            total += v >> 1
    return total

network_data = "SECURITY_PACKET_HEADER_2023"
threat_score = analyze_packets(network_data)
print(f"Result: {threat_score}")