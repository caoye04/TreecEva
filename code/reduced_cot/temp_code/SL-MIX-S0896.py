import base64

def process_packet_segment(segment):
    # Dynamic programming approach to calculate segment threat weight
    dp = [0] * (len(segment) + 1)
    for i in range(1, len(segment) + 1):
        dp[i] = dp[i-1] + (ord(segment[i-1]) % 16)
    return dp[len(segment)]

def decode_and_transform(packet_data):
    # Divide and conquer approach to split packet
    if len(packet_data) <= 2:
        return process_packet_segment(packet_data)
    mid = len(packet_data) // 2
    left_result = decode_and_transform(packet_data[:mid])
    right_result = decode_and_transform(packet_data[mid:])
    return left_result + right_result

# Context manager for packet analysis
class PacketAnalyzer:
    def __init__(self):
        self.normalized_packets = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_packet(self, raw_packet):
        # String transformation and encoding/decoding
        decoded = base64.b64decode(raw_packet).hex()
        transformed = ''.join([chr(int(decoded[i:i+2], 16)) for i in range(0, len(decoded), 2)])
        self.normalized_packets.append(transformed)

# Main processing pipeline
packet_sequence = ['SGVsbG8=', 'V29ybGQ=', 'UHl0aG9u']
threat_score = 0

with PacketAnalyzer() as analyzer:
    # List comprehension to process all packets
    [analyzer.add_packet(p) for p in packet_sequence]
    
    # Lambda function for calculating weighted threat score
    calculate_weight = lambda pkt: decode_and_transform(pkt) * len(pkt)
    
    # Generator expression to compute scores
    scores = (calculate_weight(packet) for packet in analyzer.normalized_packets)
    
    # Aggregate threat score
    for score in scores:
        threat_score += score

print(f"Result: {threat_score}")